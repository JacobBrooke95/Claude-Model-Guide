import json,pandas as pd,numpy as np,datetime as dt
C='/home/user/Claude-Model-Guide/.claude/worktrees/capability/capability/'
J=json.load(open(C+'output/capability_forecast.json'))
m=pd.read_csv(C+'data/models.csv')
m=m[m.in_public_eci==1].copy()
yr=lambda s:2020+(dt.date.fromisoformat(s)-dt.date(2020,1,1)).days/365.25
m['t']=m.release_date.map(yr)
cl=m[(m.lab=='Anthropic')&m.family.isin(['opus','sonnet','haiku','fable'])].sort_values('t')
an=m[(m.lab=='Anthropic')&(m.t>=2023.4)].sort_values('t')
def recs(df):
    best=-1e9;out=[]
    for r in df.itertuples():
        if r.eci>best: best=r.eci; out.append((r.t,r.eci))
    return np.array(out)
R=pd.DataFrame(J['backtest']['release']['per_release'])
res=[]
for lead in (0,0.25,0.5):
    M=R[(R.method=='model')&(R.lead==lead)]
    for r in M.itertuples():
        T=float(cl[cl.model_id==r.model_id].t.iloc[0]); t0=T-lead
        # leakage: every Claude / any model used must be < t0
        h=cl[cl.t<t0]; hf=h[h.family==r.family]
        rc=recs(an[an.t<t0])
        w=rc[rc[:,0]>=t0-1.0]
        if len(w)<3: w=rc[-4:]
        b=np.polyfit(w[:,0],w[:,1],1)
        line=lambda t:np.polyval(b,t)
        out=dict(model_id=r.model_id,lead=lead,y=r.y,model=r.median,fam=r.family)
        if len(hf):
            last=hf.iloc[-1]
            out['prev']=last.eci
            out['prev_plus_slope']=last.eci+b[0]*(T-last.t)
            out['line12_plus_lastoffset']=line(T)+(last.eci-line(last.t))
        else:
            # new family: assume at the frontier line
            out['line12_plus_lastoffset']=line(T); out['prev_plus_slope']=np.nan
        res.append(out)
res=pd.DataFrame(res)
for lead,g in res.groupby('lead'):
    print('lead',lead,'n',len(g))
    for c in ('model','prev','prev_plus_slope','line12_plus_lastoffset'):
        e=(g.y-g[c]).dropna(); print(f'  {c:24s} n={len(e)} bias={e.mean():.2f} mae={e.abs().mean():.2f} rmse={np.sqrt((e**2).mean()):.2f}')
    gg=g.dropna(subset=['prev'])
    for c in ('model','prev_plus_slope','line12_plus_lastoffset'):
        e=(gg.y-gg[c]); print(f'  [has-prev folds] {c:24s} n={len(e)} rmse={np.sqrt((e**2).mean()):.2f} mae={e.abs().mean():.2f}')
print(res[res.lead==0].round(2).to_string())
