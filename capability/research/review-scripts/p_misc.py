import json,pandas as pd,numpy as np,pickle,sys
C='/home/user/Claude-Model-Guide/.claude/worktrees/capability/capability/'
J=json.load(open(C+'output/capability_forecast.json'))
# 1. regressions within family: base rate
m=pd.read_csv(C+'data/models.csv'); c=m[(m.lab=='Anthropic')&m.family.isin(['opus','sonnet','haiku','fable'])&m.eci.notna()].sort_values('release_date')
d=c.groupby('family').eci.diff().dropna(); print('within-family successor steps n',len(d),'negative',(d<0).sum(),'min',d.min(), 'median',d.median())
for f,v in J['next_models']['families'].items(): print(f,'P(ECI>prev)',v['p_eci_above_previous_in_family'],'lo80',v['eci']['lo80'],'prev',v['previous_eci'])
# 2. frontier folds: pool_all vs others sign in backtest vs live
ff=pickle.load(open('ffolds.pkl','rb'))
A=[f for f in ff if f['which']=='anth' and f['h'] in (0.5,1.0)]
dd=[np.median(f['samples']['pool_all'])-np.median(f['samples']['lin_12']) for f in A]
print('backtest: pool_all median minus lin_12 median: mean',np.mean(dd).round(2),'share pool_all higher',np.mean(np.array(dd)>0).round(2))
by={}
for f in A: by.setdefault(round(f['t0'],2),[]).append(np.median(f['samples']['pool_all'])-np.median(f['samples']['lin_12']))
print({k:round(float(np.mean(v)),1) for k,v in by.items()})
cur=J['trend']['candidate_curves_anthropic']
for T in (2027.0,2027.5,2027.87):
    print('live',T,{k:round(float(np.interp(T,cur[k]['t'],cur[k]['median'])),1) for k in cur})
# 3. frontier 1y errors: std vs rmse
tab=[r for r in J['backtest']['frontier']['table'] if r['method']=='stacked' and r['horizon_years']==1.0]; print(tab)
print('sigma_w used',J['projection']['assumptions']['annual_random_walk_sd'])
# 4. open predictions inventory
op=pd.DataFrame(J['open_predictions']); print(op.groupby(['family']).size().to_dict(), op.quantity.value_counts().to_dict())
tw=op[op.family.isin(['fable','mythos'])].pivot_table(index='quantity',columns='family',values='median'); print(tw)
# predictions whose 80% interval excludes anything ever observed / contradict current
b=pd.read_csv(C+'data/benchmark_scores.csv')
for f,v in J['next_models']['families'].items():
    for k,x in v['benchmarks'].items():
        mx=b[b.benchmark==k].value.max(); pv=x['previous_in_family']
        flag=[]
        if x['lo80']>mx: flag.append(f'lo80 {x["lo80"]} > best ever observed {mx:.1f}')
        if pv and x['hi80']<pv['value']: flag.append(f'hi80 {x["hi80"]} < previous-in-family {pv["value"]:.2f}')
        if pv and x['hi95']<pv['value']: flag.append(f'hi95 {x["hi95"]} < prev')
        if flag: print(f,k,x['median'],flag)
# 5. explosive/ECI tail & hours
h=J['projection']['headline']; print([(r['date'],r['eci']['hi95'],r['aeci']['hi95'],r['metr_h50_hours']['median'],r['metr_h50_hours']['lo80']) for r in h])
print(J['projection']['external_comparison'][-2]['ours_values'],J['projection']['external_comparison'][-1]['ours_values'])
print(J['backtest']['benchmarks']['paired_vs_previous'][:3]); print(J['calibration'] if 'calibration' in J else '')
