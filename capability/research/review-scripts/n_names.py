import sys,json,pandas as pd,numpy as np,collections
C='/home/user/Claude-Model-Guide/.claude/worktrees/capability/capability/'
sys.path.insert(0,C)
import build_data as bd
m=pd.read_csv(C+'data/models.csv'); match=bd.make_matcher(list(m.model_id)); RAW=C+'data/raw/'
def audit(label,names):
    by=collections.defaultdict(set)
    for n in set(map(str,names)):
        for part in n.split(','):
            mid=match(part.strip())
            if mid: by[mid].add(part.strip()); break
    bad={k:v for k,v in by.items() if len(v)>1 or any(bd._n(x)!=bd._n(k) for x in v)}
    print('==',label,'matched canon',len(by),'non-exact or many-to-one:',len(bad))
    for k,v in sorted(bad.items()):
        if len(v)>1 or 'claude' in k.lower() or 'gpt' in k.lower(): print('   ',k,'<-',sorted(v)[:8])
hub=pd.read_csv(RAW+'epoch_hub_benchmarks_long.csv',low_memory=False)
for key,(bn,_) in bd.HUB.items(): audit('hub:'+key,hub[hub.benchmark==bn].model_group.dropna())
lm=pd.read_csv(RAW+'lmarena_text.csv',low_memory=False); lm=lm[(lm.category=='overall')&(lm.leaderboard_publish_date>='2025-07-23')]
audit('lmarena',lm.model_name)
g=pd.read_csv(RAW+'aa_elo_gdpval_briefcase.csv'); audit('gdpval',g[g.benchmark=='GDPval-AA'].release)
aa=pd.read_csv(RAW+'aa_index.csv'); audit('aa',aa[(aa.index_name=='AA Intelligence Index')&(aa.index_version=='v5.0.1')].release)
v=pd.read_csv(RAW+'vals_index.csv'); audit('vals',v[(v['index']=='Vals Index')&(v.index_version.astype(str)=='2.2')&(v.task_key=='overall')].model_key)
# site charts: mythos series? grade lookups
ch=json.load(open(C+'../data/benchmarks.json'))['charts']
for k in ['swe_bench_pro','terminal_bench_2_1','osworld','gdpval_aa','rli','arc_agi_2','hle','forecastbench','vending_bench_2']:
    s=ch[k]['series']; print(k,{f:(len(p),max(x['date'] for x in p)) for f,p in s.items()})
b=pd.read_csv(C+'data/benchmark_scores.csv')
print(b[(b.benchmark=='lmarena_text')&b.model_id.str.contains('Claude 3')][['model_id','value','source']])
print(b[(b.model_id.str.contains('Mythos'))].groupby('benchmark').size().to_dict())
