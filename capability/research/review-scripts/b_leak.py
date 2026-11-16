import sys,json,datetime as dt,numpy as np,pandas as pd
C='/home/user/Claude-Model-Guide/.claude/worktrees/capability/capability/'
sys.path.insert(0,C)
from capmodel.data import D
from capmodel.core import OriginModel
from capmodel.common import rng
d=D(); J=json.load(open(C+'output/capability_forecast.json'))
raw=pd.read_csv(C+'data/models.csv'); raw=raw[raw.in_public_eci==1]
D0=dt.date(2020,1,1)
days=lambda s:(dt.date.fromisoformat(s)-D0).days
raw['days']=raw.release_date.map(days)
cl=d.claude()
R=pd.DataFrame(J['backtest']['release']['per_release']); M=R[R.method=='model']
tot_recent=0
for r in M.itertuples():
    tgt=cl[cl.model_id==r.model_id].iloc[0]
    tday=days(tgt.release_date); oday=tday-round(r.lead*365.25)
    if r.model_id in ('Claude Opus 5','Claude Fable 5','Claude Sonnet 5.5','Claude Haiku 5.5','Claude Fable 5.2','Claude Opus 4') :
        om=OriginModel(d,tgt.t-r.lead,3,rng('x'))
        used=set(om.all.series.names)|set(om.anth.series.names)|set(om.hist.model_id)
        ud=raw[raw.model_id.isin(used)].days
        bad=raw[raw.model_id.isin(used)&(raw.days>=oday)]
        missing=raw[(raw.days<oday)&~raw.model_id.isin(used)&(raw.days>=days('2023-03-01'))]
        recent=raw[raw.model_id.isin(used)&(raw.days>=oday-14)]
        print(f"{r.model_id:20s} lead {r.lead}: origin day {oday} newest used {ud.max()} ({oday-ud.max()} d before) n_used {len(used)} leaked(>=origin) {len(bad)} target_in {r.model_id in used}; used models released <=14d before origin: {list(recent.model_id)}")
# across ALL lead-0 folds: how many Anthropic models released within 14/30 days before origin are in the fit, incl. family predecessor / record setters
an=raw[raw.lab=='Anthropic']
rows=[]
for r in M[M.lead==0].itertuples():
    tday=days(cl[cl.model_id==r.model_id].release_date.iloc[0])
    w14=raw[(raw.days<tday)&(raw.days>=tday-14)]; w30=raw[(raw.days<tday)&(raw.days>=tday-30)]
    rows.append((r.model_id,len(w14),len(w30),list(w30[w30.lab=='Anthropic'].model_id)))
print(pd.DataFrame(rows,columns=['target','n_models_<14d','n_<30d','anthropic_<30d']).to_string())
