k=1.3  # px por mm
W,H,D,t=350,250,260,15   # externo mm, MDF 15
out=[]
def a(x):out.append(x)
def rect(x,y,w,h,**st):
    s=' '.join(f'{kk.replace("_","-")}="{v}"' for kk,v in st.items());a(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" {s}/>')
def text(x,y,txt,size=16,anchor="middle",weight="normal",fill="#222"):
    a(f'<text x="{x}" y="{y}" font-size="{size}" text-anchor="{anchor}" font-weight="{weight}" fill="{fill}" font-family="Arial,Helvetica,sans-serif">{txt}</text>')
def dim(x1,y1,x2,y2,label,off=0,vert=False):
    a(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="#c0392b" stroke-width="1.5" marker-start="url(#ar)" marker-end="url(#ar)"/>')
    if vert: a(f'<text x="{x1-8}" y="{(y1+y2)/2}" font-size="15" fill="#c0392b" text-anchor="middle" transform="rotate(-90 {x1-8} {(y1+y2)/2})" font-family="Arial">{label}</text>')
    else: text((x1+x2)/2,y1-7,label,15,fill="#c0392b")
MDF="#c8a165";IN="#f7f0e4";TUBE="#3d8bd4"
CW,CH=1560,1080
a(f'<svg xmlns="http://www.w3.org/2000/svg" width="{CW}" height="{CH}" viewBox="0 0 {CW} {CH}">')
a('<defs><marker id="ar" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="#c0392b"/></marker></defs>')
rect(0,0,CW,CH,fill="#ffffff")
text(CW/2,48,'Caixa dutada compacta – Bomber Bicho Papão 8" 600 W',30,weight="bold")
text(CW/2,80,'12 L líquidos · sintonia ≈ 40 Hz · duto traseiro dobrado (tubo PVC 75 mm) · MDF 15 mm',18,fill="#555")
# ---------- VISTA FRONTAL ----------
ox,oy=70,170
text(ox+W*k/2,oy-35,'1. Vista frontal',20,weight="bold")
rect(ox,oy,W*k,H*k,fill=MDF,stroke="#7a5a2b",stroke_width=2,rx=4)
cx,cy=ox+W/2*k,oy+H/2*k
rect(cx-103.5*k,cy-103.5*k,207*k,207*k,fill="#2b2b2b",rx=12)
for r,col in [(95,"#444"),(88,"#1c1c1c"),(70,"#262626"),(32,"#3a3a3a")]:
    a(f'<circle cx="{cx}" cy="{cy}" r="{r*k}" fill="{col}"/>')
for dx,dy in [(-88,-88),(88,-88),(-88,88),(88,88)]:
    a(f'<circle cx="{cx+dx*k}" cy="{cy+dy*k}" r="{4*k}" fill="#999"/>')
dim(ox,oy+H*k+30,ox+W*k,oy+H*k+30,'350 mm')
dim(ox-22,oy,ox-22,oy+H*k,'250 mm',vert=True)
text(cx,oy+H*k+70,'Furo do alto-falante: medir no gabarito do manual (≈ 185 mm)',14,fill="#555")
# ---------- VISTA TRASEIRA EM CORTE ----------
ox2=ox+W*k+90
text(ox2+W*k/2,oy-35,'2. Por trás, sem a tampa traseira',20,weight="bold")
rect(ox2,oy,W*k,H*k,fill=MDF,stroke="#7a5a2b",stroke_width=2,rx=4)
ix,iy=ox2+t*k,oy+t*k;IW,IH=W-2*t,H-2*t
rect(ix,iy,IW*k,IH*k,fill=IN)
# imã (fica na frente do plano do duto) tracejado
a(f'<circle cx="{ix+IW/2*k}" cy="{iy+IH/2*k}" r="{67*k}" fill="none" stroke="#666" stroke-dasharray="6 5" stroke-width="2"/>')
text(ix+IW/2*k,iy+IH/2*k+5,'ímã (mais à frente)',13,fill="#666")
def P(x,y):return (ix+x*k, iy+(IH-y)*k)  # y de baixo para cima
pts=[(275,45),(45,45),(45,175),(185,175)]
path=' '.join(f'{"M" if i==0 else "L"}{P(*p)[0]:.1f},{P(*p)[1]:.1f}' for i,p in enumerate(pts))
a(f'<path d="{path}" fill="none" stroke="{TUBE}" stroke-width="{75*k}" stroke-linejoin="round" stroke-linecap="butt" opacity="0.9"/>')
a(f'<path d="{path}" fill="none" stroke="#ffffff" stroke-width="2" stroke-dasharray="8 6"/>')
ex,ey=P(275,45);a(f'<circle cx="{ex}" cy="{ey}" r="{37.5*k}" fill="#123" stroke="#fff" stroke-width="2"/>')
text(ex,ey+5,'saída',13,fill="#fff")
enx,eny=P(185,175);a(f'<line x1="{enx}" y1="{eny-37.5*k}" x2="{enx}" y2="{eny+37.5*k}" stroke="#123" stroke-width="5"/>')
text(enx+10,eny+5,'ponta interna',13,anchor="start",fill="#123")
text(ix+IW/2*k,iy+IH*k+42,'Duto: 1 trecho atravessa a tampa + 3 curvas de 90°',14,fill="#555")
dim(ox2,oy+H*k+60+10,ox2+W*k,oy+H*k+70,'350 mm (interno 320 × 220)')
# ---------- CORTE LATERAL ----------
ox3=ox2+W*k+90
DW=D
text(ox3+DW*k/2,oy-35,'3. Corte lateral',20,weight="bold")
rect(ox3,oy,DW*k,H*k,fill=MDF,stroke="#7a5a2b",stroke_width=2,rx=4)
rect(ox3+t*k,oy+t*k,(DW-2*t)*k,(H-2*t)*k,fill=IN)
# alto-falante de perfil (frente à esquerda)
fx=ox3+t*k;my=oy+H/2*k
a(f'<polygon points="{fx},{my-103*k} {fx+95*k},{my-67*k} {fx+95*k},{my+67*k} {fx},{my+103*k}" fill="#3a3a3a"/>')
rect(fx+95*k,my-67*k,36*k,134*k,fill="#1d1d1d")
text(fx+60*k,my+5,'131 mm',13,fill="#fff")
# tubos (vistos de lado): dois trechos horizontais no plano a 45 mm da tampa traseira
bx=ox3+(DW-t-45)*k
for yc in [45,175]:
    yy=oy+(H-t-yc)*k
    rect(bx-37.5*k,yy-37.5*k,75*k,75*k,fill=TUBE,opacity="0.9")
yy=oy+(H-t-45)*k;rect(bx,yy-37.5*k,(45+t)*k+2,75*k,fill=TUBE,opacity="0.9")
text(bx,oy+(H-t-110)*k+5,'duto',14,fill="#123")
text(ox3,oy+H*k+25,'FRENTE',13,anchor="start",fill="#555");text(ox3+DW*k,oy+H*k+25,'TRÁS',13,anchor="end",fill="#555")
dim(ox3,oy+H*k+50,ox3+DW*k,oy+H*k+50,'260 mm')
# ---------- FICHA ----------
fy=650
rect(60,fy,CW-120,370,fill="#f4f6f8",rx=10)
text(90,fy+40,'Ficha do projeto',22,anchor="start",weight="bold")
L=[('Medida externa','350 × 250 × 260 mm (L × A × P)'),('Medida interna','320 × 220 × 230 mm = 16,2 L bruto'),
   ('Volume líquido','≈ 12 L (desconta duto ≈ 2,5 L, alto-falante 1,44 L e reforços)'),('Sintonia','≈ 40 Hz'),
   ('Duto','tubo PVC 75 mm (≈ 70 mm interno), ≈ 56 cm pela linha central, 3 curvas de 90°'),
   ('Saída do duto','traseira, canto inferior; arredondar a borda (evita ruído de ar)'),
   ('Resposta estimada','F3 ≈ 38 Hz ao ar livre · perto de 35 Hz dentro do carro (ganho de cabine)'),
   ('Potência útil','≈ 200 W (limite de excursão Xmax 11 mm) · subsônico em ≈ 30 Hz')]
for i,(kk,v) in enumerate(L):
    y=fy+85+i*34
    text(90,y,kk,17,anchor="start",weight="bold");text(330,y,v,17,anchor="start")
text(90,fy+355,'Corte o duto 3–4 cm mais longo e encurte medindo a sintonia real. Conferir no WinISD antes de produzir.',15,anchor="start",fill="#c0392b")
a('</svg>')
open('caixa.svg','w').write('\n'.join(out))
