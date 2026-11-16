import json,pandas as pd,numpy as np
from scipy.optimize import least_squares
C='/home/user/Claude-Model-Guide/.claude/worktrees/capability/capability/'
J=json.load(open(C+'output/capability_forecast.json'))
b=pd.read_csv(C+'data/benchmark_scores.csv'); meta=pd.read_csv(C+'data/benchmarks_meta.csv').set_index('benchmark')
T={r['benchmark']:r for r in J['links']['table']}
sat={r['benchmark']:r for r in J['projection']['saturation']}
op=J['next_models']['families']['opus']['benchmarks']; fa=J['next_models']['families']['fable']['benchmarks']
for k,r in T.items():
    g=b[(b.benchmark==k)&b.eci.notna()].sort_values('eci')
    top=g.tail(4)[['model_id','eci','value']].values.tolist()
    mx=g.value.max(); n_cl=(g.lab=='Anthropic').sum(); n160=(g.eci>=160).sum(); last=g.release_date.max()
    extra=''
    if r['kind']=='bounded':
        lo,hi=meta.loc[k,'lo'],meta.loc[k,'hi']; p=np.clip((g.value-lo)/(hi-lo),0,1).values; x=g.eci.values
        f=least_squares(lambda q:1/(1+np.exp(-q[0]*(x-q[1])))-p,[0.1,150],bounds=([0.005,40],[1,300]))
        ninf=((p>0.05)&(p<0.95)).sum()
        extra=f"myfit a={f.x[0]:.3f} D={f.x[1]:.2f} (theirs {r['slope']},{r['difficulty']}) rmse={np.sqrt(np.mean(f.fun**2))*(hi-lo):.2f}/{r['rmse_score']} n_informative={ninf} max_p={p.max():.3f}"
    else:
        y=np.log2(g.value.values) if r['kind']=='loghorizon' else g.value.values
        bb=np.polyfit(g.eci.values,y,1); res=y-np.polyval(bb,g.eci.values); r2=1-res.var()/y.var()
        extra=f"myfit slope={bb[0]:.4f} (theirs {r['slope']}) R2={r2:.2f} resid_sd={res.std(ddof=2):.3f}"
    print(f"{k:18s} {r['kind']:10s} n={r['n']} n_claude={n_cl} n(eci>=160)={n160} newest={last} max_obs={mx} resid_scale={r['resid_scale']} | {extra}")
    print(f"     top-ECI points: {[(m[:22],e,v) for m,e,v in top]}")
    print(f"     opus pred {op[k]['median']} [{op[k]['lo80']},{op[k]['hi80']}] 95[{op[k]['lo95']},{op[k]['hi95']}] prev {op[k]['previous_in_family']} | fable {fa[k]['median']} [{fa[k]['lo80']},{fa[k]['hi80']}] prev {fa[k]['previous_in_family']} p>90%range {op[k].get('p_above_90pct_of_range')}")
print([ (p['id'],p['median'],p['lo80'],p['hi80']) for p in J['open_predictions'] if p['family'] in('opus','fable')])
print({k:v for k,v in J['links']['calibration_factors'].items()})
