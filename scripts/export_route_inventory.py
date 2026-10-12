"""Export reviewable semantic page bodies; never ship the legacy page shell."""
import hashlib,json,subprocess
from pathlib import Path
from html.parser import HTMLParser
ROOT=Path(__file__).resolve().parents[1]
VOID={'br','hr','img'}
TAGS=set('h1 h2 h3 h4 h5 h6 p blockquote pre code strong em del ul ol li table thead tbody tr th td a details summary span hr br div section article dl dt dd nav small figure img svg title desc defs marker path rect line text'.split())
ATTRS=set('class href id tabindex aria-hidden aria-label aria-labelledby role rel download lang src alt width height fill x y rx text-anchor font-family font-size font-weight stroke stroke-width x1 y1 x2 y2 marker-end xmlns viewbox markerwidth markerheight refx refy orient d letter-spacing style'.split())
class Body(HTMLParser):
 def __init__(self):
  super().__init__(convert_charrefs=True);self.active=False;self.stack=[];self.nodes=[];self.skip=0;self.title='';self.in_title=False;self.study_id=None
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if tag=='title' and not self.active:self.in_title=True
  if tag=='main':self.active=True;return
  if not self.active:return
  if self.skip:
   if tag not in VOID:self.skip+=1
   return
  if tag=='button':
   if a.get('id')=='toggleSidebar':self.skip=1;return
   if a.get('data-progress-id'):self.study_id=a['data-progress-id'];self.skip=1;return
  if tag not in TAGS or any(k not in ATTRS for k in a):raise ValueError(('Unsupported body element',tag,a))
  if a.get('style') not in (None,'text-align:right'):raise ValueError('Unsupported style')
  node={'tag':tag,'attrs':{k:v or '' for k,v in a.items()},'children':[]}
  (self.stack[-1]['children'] if self.stack else self.nodes).append(node)
  if tag not in VOID:self.stack.append(node)
 def handle_endtag(self,tag):
  if tag=='title' and not self.active:self.in_title=False
  if not self.active:return
  if self.skip:self.skip-=1;return
  if tag=='main':
   if self.stack:raise ValueError('Unclosed body')
   self.active=False;return
  if tag in VOID:return
  if not self.stack or self.stack[-1]['tag']!=tag:raise ValueError(('Unbalanced body',tag))
  self.stack.pop()
 def handle_data(self,text):
  if self.in_title:self.title+=text
  if self.active and not self.skip:(self.stack[-1]['children'] if self.stack else self.nodes).append({'text':text})
def export_surfaces():
 pages=[];inventory=[]
 for file in sorted((ROOT/'dist').rglob('*')):
  if not file.is_file():continue
  route='/'+file.relative_to(ROOT/'dist').as_posix();raw=file.read_bytes();digest=hashlib.sha256(raw).hexdigest()
  entry={'route':route,'source':'dist'+route,'sha256':digest}
  if file.suffix=='.html' and route.startswith(('/fr/','/en/')):
   parser=Body();parser.feed(raw.decode());parser.close()
   if not parser.nodes:raise ValueError('No page body: '+route)
   pages.append({'route':route,'locale':route.split('/')[1],'title':parser.title,'source':'dist'+route,'source_sha256':digest,'nodes':parser.nodes,'study_id':parser.study_id})
   entry['disposition']='semantic-page'
  elif route=='/index.html':entry.update(disposition='redirect',target='/fr/')
  elif route=='/404.html':entry['disposition']='application-error-boundary'
  elif route.startswith(('/gnu6/','/motion/','/context/')) or route in ('/style.css','/app.js','/spine.css','/spine.js','/spine-map.js'):entry['disposition']='shared-application-shell'
  else:entry['disposition']='asset'
  inventory.append(entry)
 return {'schema':'gnu6.docs.surfaces.v1','producer_commit':subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip(),'pages':pages,'inventory':inventory}
if __name__=='__main__':
 data=export_surfaces();target=ROOT/'exports/gnu6-docs-surfaces.v1.json';target.write_text(json.dumps(data,ensure_ascii=False,separators=(',',':'))+'\n');print('SURFACES_EXPORT_PASS',len(data['pages']),len(data['inventory']))
