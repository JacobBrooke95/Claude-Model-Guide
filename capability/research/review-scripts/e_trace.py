import json,pandas as pd,numpy as np,datetime as dt
C='/home/user/Claude-Model-Guide/.claude/worktrees/capability/capability/'
J=json.load(open(C+'output/capability_forecast.json'))
yr=lambda s:2020+(dt.date.fromisoformat(s)-dt.date(2020,1,1)).days/365.25
m=pd.read_csv(C+'data/models.csv'); m=m[m.in_public_eci==1].copy(); m['t']=m.release_date.map(yr)
def recs(df,start):
    best=-1e9;out=[]
    for r in df.sort_values('t').itertuples():
        if r.t<start: continue
        if r.eci>best: best=r.eci; out.append((r.t,r.eci,r.model_id))
    return out
ra=recs(m[m.lab=='Anthropic'],2023.4); rl=recs(m,2023.15)
print('anth records',[(round(t,2),e,n) for t,e,n in ra])
print('all-lab records last 8',[(round(t,2),e,n) for t,e,n in rl][-8:])
T0=yr('2026-11-16')
A=np.array([(t,e) for t,e,_ in ra]); L=np.array([(t,e) for t,e,_ in rl])
def ols(P,win):
    P=P[P[:,0]>=T0-win]; return np.polyfit(P[:,0],P[:,1],1),len(P)
for nm,P in (('anth',A),('all',L)):
    for win in (1,2,10):
        b,n=ols(P,win); print(nm,'win',win,'n',n,'slope',round(b[0],2),'level now',round(np.polyval(b,T0),2),'at 2026-12-14',round(np.polyval(b,yr('2026-12-14')),2),'at 2027-07-13',round(np.polyval(b,yr('2027-07-13')),2))
W=J['next_models']['trend_weights']; print('weights',W, 'alpha',J['families']['alpha_weight_on_last_offset'])
cur=J['trend']['candidate_curves_anthropic']
ft={r['family']:r for r in J['families']['table']}
mp=J['aeci']['mapping_forms']; p=J['aeci']['p_offset_form_used']; dr=J['aeci']['drift']['summary']
links={r['benchmark']:r for r in J['links']['table']}
for f in ('opus','sonnet','haiku','fable','mythos'):
    v=J['next_models']['families'][f]; d=v['release_date']['median']; T=yr(d)
    lv={c:np.interp(T,cur[c]['t'],cur[c]['median']) for c in W}
    mixL=sum(W[c]*lv[c] for c in W)
    tw='fable' if f=='mythos' else f
    a=J['families']['alpha_weight_on_last_offset']
    off=a*ft[tw]['last_offset']+(1-a)*ft[tw]['pooled_mean']
    eci=mixL+off
    an=p*(mp['offset']['a0']+eci+mp['offset']['c'])+(1-p)*(mp['hinge']['a0']+eci+mp['hinge']['c']*max(eci-mp['hinge']['k'],0))
    own=an+dr['mean']*v['refits_before_own_card']['mean']
    sw=links['swe_bench_pro']; swe=100/(1+np.exp(-sw['slope']*(eci-sw['difficulty'])))
    print(f"{f:7s} date {d} cand levels { {k:round(x,1) for k,x in lv.items()} }\n    hand: L={mixL:.1f} off={off:.2f} ECI={eci:.1f} AECI_nov6={an:.1f} own={own:.1f} SWEpro={swe:.1f} | JSON: L={v['components']['trend_level_at_release']['median']} ECI={v['eci']['median']} [{v['eci']['lo80']},{v['eci']['hi80']}] nov6={v['aeci_nov6_scale']['median']} own={v['aeci_own_card']['median']} SWE={v['benchmarks']['swe_bench_pro']['median']} prevECI={v['previous_eci']} P(>prev)={v['p_eci_above_previous_in_family']} P(>best)={v['p_eci_above_current_anthropic_best']} raw={v['eci_raw_uncalibrated']['lo80']},{v['eci_raw_uncalibrated']['hi80']} lo95={v['eci']['lo95']} hi95={v['eci']['hi95']}")
    print('    cond',v['eci_given_release_date'], v['name_probabilities'])
