import sys,json,numpy as np,pandas as pd,pickle
C='/home/user/Claude-Model-Guide/.claude/worktrees/capability/capability/'
sys.path.insert(0,C)
from capmodel.data import D
from capmodel import backtest as bt
from capmodel.core import TREND
from capmodel.trend import stack_crps
d=D()
ff=bt.frontier_folds(d,30)
pickle.dump(ff,open('ffolds.pkl','wb'))
A=[f for f in ff if f['which']=='anth' and f['h']<=1.0]
print('anth folds h<=1:',len(A),'distinct origins',len({f['t0'] for f in A}),'distinct targets y',len({round(f['y'],2) for f in A}))
def W(fs,floor=0.05):
    w,_,a=stack_crps([[f['samples'][c] for c in TREND] for f in fs],[f['y'] for f in fs],floor=floor); return dict(zip(TREND,np.round(w,2)))
print('all      ',W(A)); print('no floor ',W(A,0.0))
t=sorted({f['t0'] for f in A}); mid=t[len(t)//2]
print('first half origins',W([f for f in A if f['t0']<mid])); print('second half        ',W([f for f in A if f['t0']>=mid]))
for h in (0.25,0.5,1.0): print('h',h,len([f for f in A if f['h']==h]),W([f for f in A if f['h']==h]))
# mean abs err / bias per candidate
for c in TREND+['persistence']:
    e=[f['y']-np.median(f['samples'][c]) for f in A]; print(f'  {c:9s} bias {np.mean(e):5.2f} mae {np.mean(np.abs(e)):5.2f}')
# block bootstrap over origins (blocks of 3 consecutive months)
rng=np.random.default_rng(1); blocks=[t[i:i+3] for i in range(0,len(t),3)]; res=[]
for b in range(40):
    pick=rng.integers(0,len(blocks),len(blocks)); os_=[o for i in pick for o in blocks[i]]
    fs=[f for o in os_ for f in A if f['t0']==o]
    res.append(list(W(fs).values()))
res=np.array(res); print('block-bootstrap weight 10/50/90 pct per candidate:')
for i,c in enumerate(TREND): print(f'  {c:9s}',np.round(np.quantile(res[:,i],[.1,.5,.9]),2), 'share at floor',np.mean(res[:,i]<=0.051).round(2))
# rolling weights: what did the rolling stack use over time
import collections
for t0 in t[::3]:
    w,n=bt.stack_weights(ff,'anth',before=t0); print(round(t0,2),n,{k:round(v,2) for k,v in w.items()})
# release-fold with a 1-month lead (publication-lag proxy) using the author's harness
rel,_=bt.release_folds(d,30,ff,with_bench=False,leads=(0.0,1/12,2/12))
for ld in sorted(rel.lead.unique()):
    g=rel[(rel.method=='model')&(rel.lead==ld)]; print('lead',round(ld,3),'n',len(g),'bias',round(g.err.mean(),2),'rmse',round(np.sqrt((g.err**2).mean()),2),'cov80',round(g.in80.mean(),2),'cov50',round(g.in50.mean(),2))
    ids=set(g.model_id)
rel.to_pickle('rel_leads.pkl')
