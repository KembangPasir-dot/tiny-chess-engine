Z=' pnbrqk';S=[i for i in range(128)if not i&136];D={2:(33,31,18,14,-14,-18,-31,-33),3:(15,17,-15,-17),4:(1,-1,16,-16)};D[5]=D[6]=D[4]+D[3]
def X(x):return ord(x[0])-97+16*(int(x[1])-1)
def M(i):return chr(97+(i&7))+str((i>>4)+1)
def P(f):
 a,t,c,e,h,n=f.split();b=[0]*128;i=112
 for x in a:
  if x=='/':i-=24
  elif x.isdigit():i+=int(x)
  else:b[i]=(2*x.isupper()-1)*Z.index(x.lower());i+=1
 return b,2*(t=='w')-1,c,X(e)if e!='-'else-1,int(h),int(n)
def A(b,k,s):
 for d in(15*s,17*s):
  t=k-d
  if not t&136 and b[t]==s:return 1
 for v,ds in D.items():
  for d in ds:
   t=k-d
   while not t&136:
    if b[t]:
     if b[t]==s*v:return 1
     break
    if v%4==2:break
    t-=d
 return 0
def K(a,s):return A(a[0],a[0].index(6*s),-s)
def do(a,m):
 b,s,c,e,h,n=a;p,t,q=m;x=b[p];H=b[t]
 if x==s and t==e:b[t-16*s]=0
 if x==6*s and abs(t-p)==2:
  r=p+3 if t>p else p-4;z=(p+t)//2;b[z]=b[r];b[r]=0
 b[p]=0;b[t]=q*s or x
 for z,r in zip((0,7,112,119),'QKqk'):
  if z in(p,t):c=c.replace(r,'')
 if x==6*s:
  for r in('KQ'if s>0 else'kq'):c=c.replace(r,'')
 return(b,-s,c,t-16*s if x==s and t-p==32*s else-1,0 if x==s or H else h+1,n+(s<0))
def G(a):
 b,s,c,e,*_=a;L=[]
 for p in S:
  v=b[p]*s
  if v<1:continue
  T=[]
  if v==1:
   t=p+16*s
   if not t&136 and not b[t]:
    T+=[t];z=t+16*s
    if p//16==(1 if s>0 else 6)and not b[z]:T+=[z]
   for t in(p+15*s,p+17*s):
    if not t&136 and(b[t]*s<0 or t==e):T+=[t]
  else:
   for d in D[v]:
    t=p+d
    while not t&136:
     if b[t]*s>0:break
     T+=[t]
     if b[t]or v%4==2:break
     t+=d
   if v==6 and p==(4 if s>0 else 116)and not K(a,s):
    for r,d in zip('KQ',(1,-1)):
     if(r if s>0 else r.lower())in c and b[p+(3 if d>0 else-4)]==4*s and all(not b[p+j*d]for j in range(1,3+(d<0)))and not any(A(b,p+j*d,-s)for j in(1,2)):T.append(p+2*d)
  for t in T:
   for q in([5,4,3,2]if v==1 and t//16 in(0,7)else[0]):
    if not K(H(a,(p,t,q)),s):L.append((p,t,q))
 return L
def O(m):return M(m[0])+M(m[1])+(Z[m[2]]if m[2]else'')
def gen(fen):return[O(m)for m in G(P(fen))]
def apply(fen,uci):
 b,s,c,e,h,n=do(P(fen),(X(uci[:2]),X(uci[2:4]),Z.index(uci[4:])if uci[4:]else 0));R=[]
 for r in range(7,-1,-1):
  x='';k=0
  for i in range(8):
   v=b[r*16+i]
   if not v:k+=1
   else:
    if k:x+=str(k);k=0
    x+=Z[v].upper()if v>0 else Z[-v]
  R.append(x+str(k or''))
 return'/'.join(R)+f" {'w'if s>0 else'b'} {c or'-'} {M(e)if e>=0 else'-'} {h} {n}"
V=0,100,320,330,500,900,0;C=40000;N=Y=0
def E(a):
 b,s,*_=a;z=0
 for i in S:
  v=b[i]
  if v:
   q=abs(v);y,x=divmod(i,16);z+=(v//q)*(V[q]+(max(0,3-abs(2*x-7)//2-abs(2*y-7)//2)if q<4 else 0))
 return z*s
def H(a,m):return do((a[0][:],*a[1:]),m)
def T(a,m):return V[abs(a[0][m[1]])]or 100*(a[0][m[0]]==a[1] and m[1]==a[3])
def I(a,L,p=0):return sorted(L,key=lambda m:(-T(a,m),V[abs(a[0][m[0]])]if T(a,m)else m!=k[p]))
k=[None]*8
def W():
 global N,Y;N+=1;Y|=N>=C
def Q(a,l,u,p):
 W();v=E(a)
 if Y:return v
 c=K(a,a[1])
 if not c:
  if v>=u:return v
  l=max(l,v)
 L=G(a)
 if not L:return-1e5+p if c else 0
 for m in I(a,L):
  if c or T(a,m)or m[2]:
   l=max(l,-Q(H(a,m),-u,-l,p+1))
   if l>=u or Y:break
 return l
def F(a,d,l,u,p):
 if not d:return Q(a,l,u,p)
 W();L=G(a)
 if not L:return-1e5+p if K(a,a[1])else 0
 if Y:return E(a)
 v=-1e6
 for m in I(a,L,p):
  q=-F(H(a,m),d-1,-u,-l,p+1);v=max(v,q);l=max(l,q)
  if l>=u:
   if not(T(a,m)or m[2]):k[p]=m
   break
  if Y:break
 return v
def B(fen,depth=3):
 global N,Y,k;N=1;Y=0;k=[None]*8;a=P(fen);L=I(a,G(a));w=L[0]if L else None;v=-1e6
 for m in L:
  q=-F(H(a,m),depth-1,-1e6,-v,1)
  if Y:break
  if q>v:v,w=q,m
 return w and O(w)
import json,os,urllib.request as U,urllib.error as R
def J(p,b):return json.load(U.urlopen(U.Request(os.getenv('MAKEFUN_ENV_URL')+p,json.dumps(b).encode(),{'Content-Type':'application/json'})))
while True:
 g=J('/game',{})
 if g['status']=='done':break
 while g['status']=='your_move':
  m=B(g['fen']);L=[u for u in gen(g['fen'])if u!=m]
  while True:
   try:g=J('/move',{'game':g['game'],'move':m});break
   except R.HTTPError as e:
    if e.code!=400:raise
    e.close()
    if not L:L=gen(g['fen'])
    m=L.pop(0)