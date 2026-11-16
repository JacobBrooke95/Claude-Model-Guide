import json,pandas as pd,numpy as np
C='/home/user/Claude-Model-Guide/.claude/worktrees/capability/capability/'
J=json.load(open(C+'output/capability_forecast.json'))
a=pd.read_csv(C+'data/raw/aeci_all.csv'); e=pd.read_csv(C+'data/raw/eci_public.csv').set_index('model')
nov=a[(a.fit_card=='Mythos 5.2 card')&a.value_type.isin(['printed','figure_read','anchor_by_definition'])]
name={'3 Opus':'Claude 3 Opus','3.5 Sonnet':'Claude 3.5 Sonnet','3.5 Sonnet (new)':'Claude 3.5 Sonnet (October 2024)','3.7 Sonnet':'Claude 3.7 Sonnet'}
rows=[]
for r in nov.itertuples():
    n=name.get(r.model,'Claude '+r.model); n2=n.replace('Mythos','Fable')
    if n2 in e.index: rows.append((r.model,e.loc[n2,'eci'],r.value))
    else: print('no ECI for',r.model)
ov=pd.DataFrame(rows,columns=['m','eci','aeci']).sort_values('eci'); ov['gap']=ov.aeci-ov.eci
print(ov.to_string())
E_,A=ov.eci.values,ov.aeci.values; y=A-E_
def fit(form):
    best=None
    for k in np.arange(145,163.01,0.5):
        x=np.maximum(E_-k,0) if form=='hinge' else (E_>k).astype(float)
        if (x>0).sum()<3 or (x==0).sum()<3: continue
        X=np.c_[np.ones(len(E_)),x]; b=np.linalg.lstsq(X,y,rcond=None)[0]; sse=((y-X@b)**2).sum()
        if best is None or sse<best[0]-1e-12: best=(sse,k,b)
    return best
for f in('hinge','offset'):
    sse,k,b=fit(f); print(f,'k',k,'a0',round(b[0],3),'c',round(b[1],3),'rmse',round(np.sqrt(sse/len(y)),2))
print('theirs',J['aeci']['mapping_forms'],J['aeci']['overlap_rmse'])
# plain alternatives
print('gap mean low8',y[:8].mean().round(2),'top5',y[8:].mean().round(2),'sd top5',y[8:].std(ddof=1).round(2))
# offset k range identifiability: any k between 156.34 and 164.13 gives identical fit
# non-frontier printed points not used: Haiku 5.5 own card (fit ~Nov6: Opus5.5 moved +0.22 from haiku card to Nov6)
for m,val,src in (('Claude Haiku 5.5',167.11,'own card (Haiku fit; Opus5.5 +0.22 to Nov6)'),('Claude Sonnet 5.5',167.93+5.44+0.22,'own card + Opus5.5 shift')):
    ec=e.loc[m,'eci']; print(m,'eci',ec,'aeci~',round(val,2),'gap',round(val-ec,2),src)
# old-fit points in the hole 157-164
for m,val in (('Claude Opus 4.7',154.1),('Claude Opus 4.8',155.5)):
    print(m,'eci',e.loc[m,'eci'],'aeci (Opus 4.8 card fit, pre-jumps)',val)
# drift transitions from raw
order=['Opus 4.8 card','Mythos 5 card','Opus 5 card','Mythos 5.1 card','Opus 5.5 card','Sonnet 5.5 card','Haiku 5.5 card','Mythos 5.2 card']
p=a[a.fit_card.isin(order)].pivot_table(index='model',columns='fit_card',values='value')[order]
print(p.round(2).to_string())
steps=[]
for i in range(1,8):
    d=(p[order[i]]-p[order[i-1]]).dropna(); steps.append(d.mean()); print(order[i],d.round(2).to_dict(),'mean',round(d.mean(),2))
s=np.array(steps); print('mean',s.mean().round(2),'sd',s.std(ddof=1).round(2),'se of mean',(s.std(ddof=1)/np.sqrt(7)).round(2))
# 3-refit move opus5.5 card -> mythos5.2 card for all models in both
d=(p['Mythos 5.2 card']-p['Opus 5.5 card']).dropna(); print('Opus5.5 fit -> Nov6 fit, all models:',d.round(2).to_dict(),'sum of 3 single steps',round(s[4:].sum()-s[4],2))
print('drift json',J['aeci']['drift']['summary'], J['aeci']['drift']['leave_one_out']['cov80'])
for f,v in J['next_models']['families'].items():
    print(f, v['refits_before_own_card'], 'nov6',v['aeci_nov6_scale']['median'],'own',v['aeci_own_card']['median'], v['aeci_own_card']['lo80'],v['aeci_own_card']['hi80'], 'prev',v['previous_aeci_nov6'])
