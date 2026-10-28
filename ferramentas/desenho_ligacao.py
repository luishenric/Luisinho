o=[]
def a(x):o.append(x)
def box(x,y,w,h,t1,t2,col):
    a(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" fill="{col}" stroke="#333" stroke-width="2"/>')
    a(f'<text x="{x+w/2}" y="{y+h/2-6}" text-anchor="middle" font-size="20" font-weight="bold" fill="#111">{t1}</text>')
    a(f'<text x="{x+w/2}" y="{y+h/2+20}" text-anchor="middle" font-size="15" fill="#333">{t2}</text>')
def ln(pts,col,w=6,dash=""):
    d=" ".join(f"{'M' if i==0 else 'L'}{x},{y}" for i,(x,y) in enumerate(pts))
    a(f'<path d="{d}" fill="none" stroke="{col}" stroke-width="{w}" stroke-linejoin="round" {"stroke-dasharray=\"10 7\"" if dash else ""}/>')
def fuse(x,y,t):
    a(f'<rect x="{x-32}" y="{y-14}" width="64" height="28" rx="6" fill="#ffd54f" stroke="#333" stroke-width="2"/>')
    a(f'<text x="{x}" y="{y+6}" text-anchor="middle" font-size="14" font-weight="bold">{t}</text>')
def tx(x,y,t,s=15,c="#333",anc="middle",wt="normal"):
    a(f'<text x="{x}" y="{y}" text-anchor="{anc}" font-size="{s}" fill="{c}" font-weight="{wt}">{t}</text>')
W,H=1600,1000
a(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" font-family="Arial,Helvetica,sans-serif">')
a(f'<rect width="{W}" height="{H}" fill="#fff"/>')
tx(W/2,50,"Esquema de alimentação – tomada + bateria",30,"#111",wt="bold")
tx(W/2,82,"Positivo (+) em vermelho · negativo (−) em preto · fusíveis em amarelo",17,"#555")
R,K="#d32f2f","#222"
# blocos
box(60,170,200,90,"Tomada","127/220 V","#e3f2fd")
box(340,150,260,130,"Fonte chaveada","12 V · 60 A · ajustada em ≈ 12,4 V","#cfd8dc")
box(340,560,260,130,"Bateria Li-ion 3S8P","11,1 V ≈ 16 Ah · BMS 3S ≥ 100 A","#ffcc80")
box(1180,140,300,100,"Amplificador 800 W","","#424242")
box(1180,340,300,80,"Processador (DSP)","12 V","#a5d6a7")
box(1180,510,300,80,"Módulo Bluetooth/USB","12 V","#b3e5fc")
a('<rect x="1180" y="140" width="300" height="100" rx="12" fill="#424242"/>');tx(1330,185,"SounDigital SD800.4",20,"#fff",wt="bold");tx(1330,211,"4 canais · 9–16 V · REM do módulo",15,"#ddd")
# barramentos
a('<rect x="820" y="150" width="34" height="470" rx="6" fill="#e57373" stroke="#333" stroke-width="2"/>');tx(837,140,"Barramento +",16,R,wt="bold")
a('<rect x="1530" y="150" width="34" height="470" rx="6" fill="#616161" stroke="#333" stroke-width="2"/>');tx(1564,140,"Barramento −",16,K,"end","bold")
ln([(260,215),(340,215)],"#1565c0",4);tx(300,205,"AC",14,"#1565c0")
ln([(600,190),(700,190)],R)
a('<polygon points="700,176 700,204 728,190" fill="#333"/><line x1="730" y1="174" x2="730" y2="206" stroke="#333" stroke-width="4"/>')
tx(715,235,"diodo/relé",14,"#333");tx(715,253,"(isola a fonte)",13,"#666")
ln([(730,190),(820,190)],R)
ln([(600,590),(660,590)],R);fuse(692,590,"100 A");ln([(724,590),(750,590)],R)
a('<circle cx="760" cy="590" r="10" fill="#1565c0"/>');tx(760,625,"chave geral",14,"#1565c0")
ln([(770,590),(820,590)],R)
# negativos por baixo
ln([(470,280),(470,320),(300,320),(300,760),(1547,760),(1547,620)],K)
ln([(470,690),(470,760)],K)
tx(920,750,"negativo comum (fonte e bateria)",14,K)
# cargas
ln([(854,185),(1030,185)],R);fuse(1062,185,"80 A*");ln([(1094,185),(1180,185)],R)
ln([(854,375),(1030,375)],R);fuse(1062,375,"5 A");ln([(1094,375),(1180,375)],R)
ln([(854,545),(1030,545)],R);fuse(1062,545,"3 A");ln([(1094,545),(1180,545)],R)
for y in [215,395,565]: ln([(1480,y),(1530,y)],K,4)
box(1180,640,300,80,"Sub BP 8\" + 2× JBL 5\"","nas saídas do amplificador","#eeeeee")
# notas
y0=815
notas=["Com tomada: a fonte alimenta o som e carrega a bateria; nas pancadas a bateria ajuda a fonte.",
"Sem tomada: a bateria alimenta tudo pelo mesmo barramento.",
"A fonte precisa ter LIMITE DE CORRENTE ou função carregador (para não jogar 60 A numa bateria vazia). Nunca acima de 12,6 V.",
"* Fusível do amplificador: usar o valor indicado no manual dele.",
"Cabos principais curtos e grossos (16–25 mm²); fusível da bateria a no máx. 20 cm do polo +."]
for i,n in enumerate(notas): tx(60,y0+i*36,"• "+n,18,"#222","start")
a('</svg>')
open('ligacao.svg','w').write("\n".join(o))
