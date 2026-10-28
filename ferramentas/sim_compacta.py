# Compara opcoes compactas: selada, selada+DSP (Linkwitz), dutada e radiador passivo.
import numpy as np
rho,c=1.204,343.0
Fs,Sd,Mms,Qts,Qes=46,183e-4,66.28e-3,0.47,0.49
Re=3.4;Qms=Qes*Qts/(Qes-Qts);ws=2*np.pi*Fs
Cms=1/(ws**2*Mms);Rms=ws*Mms/Qms;Bl=np.sqrt(ws*Mms*Re/Qes)
f=np.logspace(1,np.log10(400),3000);w=2*np.pi*f;s=1j*w
def run(Vb,kind,Fb=None,P=1.0,Spr=None,QL=7,eq=None):
    Cab=Vb/(rho*c**2);Yb=s*Cab+ (1/(QL*10/(ws*Cab)) if kind=='sealed' else 0)
    extra={}
    if kind=='port':
        wb=2*np.pi*Fb;Map=1/(wb**2*Cab);Yb=Yb+1/(s*Map)+wb*Cab/QL
    if kind=='pr':
        fpr=18.0 # ressonancia livre do passivo
        wb=2*np.pi*Fb;Cap_req=None
        # escolher Mmp: wb^2 = (1/Cab+1/Cap)/Map, Map=Mmp/Spr^2, Cap=Cmp*Spr^2, Cmp=1/((2pi fpr)^2 Mmp)
        # => wb^2 = Spr^2/(Mmp Cab) + (2pi fpr)^2  -> Mmp
        Mmp=Spr**2/(Cab*(wb**2-(2*np.pi*fpr)**2));Cmp=1/((2*np.pi*fpr)**2*Mmp);Rmp=2*np.pi*fpr*Mmp/5
        Zpr=(s*Mmp+Rmp+1/(s*Cmp))/Spr**2;Yb=Yb+1/Zpr+wb*Cab/QL;extra['Mmp']=Mmp
    V=np.sqrt(P*4)*(eq if eq is not None else 1)
    Zm=s*Mms+Rms+1/(s*Cms)
    U=(Bl*V/Re)/(Zm+Bl**2/Re+Sd**2/Yb);Pb=-Sd*U/Yb;Q=-s*Cab*Pb
    spl=20*np.log10(abs(rho*s*Q/(2*np.pi))/2e-5);x=abs(U/s)*1e3
    if kind=='pr': extra['xpr']=abs(Pb/Zpr/Spr/s)*1e3
    return spl,x,extra
def F(spl,db):
    ref=spl[np.argmin(abs(f-250))];i=np.where((spl<ref-db)&(f<250))[0];return f[i.max()]
def maxspl(Vb,kind,fq,**k):
    # SPL maximo em fq limitado por Xmax 11mm (e Xmax PR) e 600W
    spl,x,e=run(Vb,kind,P=1,**k);i=np.argmin(abs(f-fq))
    Pl=600;Pl=min(Pl,(11/x[i])**2)
    if 'xpr' in e: Pl=min(Pl,(k.get('xprmax',20)/e['xpr'][i])**2) if False else Pl
    return spl[i]+10*np.log10(Pl),Pl,e
# eq linkwitz para selada: alvo Q=0.707 F 35Hz
def lt(Vb):
    Cab=Vb/(rho*c**2);a=Vas_=8.33e-3/Vb;Qtc=Qts*np.sqrt(1+a);fc=Fs*np.sqrt(1+a)
    f0,Q0,fp,Qp=fc,Qtc,35/1.0,0.707
    H=(s**2+s*2*np.pi*f0/Q0+(2*np.pi*f0)**2)/(s**2+s*2*np.pi*fp/Qp+(2*np.pi*fp)**2)
    return H*(fp/f0)**2 , fc,Qtc
print("== OPCOES COMPACTAS (volume liquido; bruto ~ +2L) ==")
for Vb in [6,8,10]:
    spl,x,_=run(Vb/1e3,'sealed');print(f"Selada {Vb}L: F3={F(spl,3):.0f}Hz")
    H,fc,q=lt(Vb/1e3);H=H/abs(H[np.argmin(abs(f-250))])
    spl,x,_=run(Vb/1e3,'sealed',eq=H)
    i=np.argmin(abs(f-35));boost=20*np.log10(abs(H[i]))
    # potencia max p/ Xmax: escala
    band=(f>30)&(f<200);P=min(600,(11/x[band].max())**2)
    spl,x,_=run(Vb/1e3,'sealed',eq=H,P=P)
    print(f"  +DSP (LT p/ F3 35): F3={F(spl,3):.0f}Hz boost@35={boost:+.1f}dB  P limite Xmax={P:.0f}W  SPL@35={spl[i]:.0f}dB SPL@60={spl[np.argmin(abs(f-60))]:.0f}dB")
for Vb,Fb in [(8,40),(10,38),(10,40),(12,38)]:
    spl,x,_=run(Vb/1e3,'port',Fb);band=(f>Fb*0.75)&(f<200);P=min(600,(11/x[band].max())**2)
    spl,x,_=run(Vb/1e3,'port',Fb,P=P);i=np.argmin(abs(f-35))
    D=6.0;L=23562*D**2/(Fb**2*Vb)-0.732*D
    print(f"Dutada {Vb}L Fb{Fb}: F3={F(spl,3):.0f} F6={F(spl,6):.0f}  P lim={P:.0f}W SPL@35={spl[i]:.0f} SPL@60={spl[np.argmin(abs(f-60))]:.0f}  duto 6cm L={L:.0f}cm")
for Vb,Fb,Spr,nome in [(8,38,0.022,'1 passivo 8"'),(8,36,0.044,'2 passivos 8"'),(10,36,0.022,'1 passivo 8"'),(6,40,0.044,'2 passivos 8"')]:
    spl,x,e=run(Vb/1e3,'pr',Fb,Spr=Spr);band=(f>Fb*0.75)&(f<200);P=min(600,(11/x[band].max())**2)
    spl,x,e=run(Vb/1e3,'pr',Fb,Spr=Spr,P=P);i=np.argmin(abs(f-35))
    print(f"Passivo {Vb}L Fb{Fb} {nome}: F3={F(spl,3):.0f} F6={F(spl,6):.0f} P lim={P:.0f}W SPL@35={spl[i]:.0f} SPL@60={spl[np.argmin(abs(f-60))]:.0f}  massa passivo={e['Mmp']*1e3:.0f}g  excursao passivo max={e['xpr'][band].max():.0f}mm")
print("velocidade duto")
for Vb,Fb in [(10,40),(10,38),(12,38)]:
  for D in [6,7,8]:
    Cab=Vb/1e3/(rho*c**2);wb=2*np.pi*Fb;Map=1/(wb**2*Cab);Yb=s*Cab+1/(s*Map)+wb*Cab/7
    spl,x,_=run(Vb/1e3,'port',Fb);band=(f>Fb*0.75)&(f<200);P=min(600,(11/x[band].max())**2)
    V=np.sqrt(P*4);Zm=s*Mms+Rms+1/(s*Cms);U=(Bl*V/Re)/(Zm+Bl**2/Re+Sd**2/Yb);Pb=-Sd*U/Yb
    v=abs(Pb/(s*Map))/(np.pi*(D/200)**2);L=23562*D**2/(Fb**2*Vb)-0.732*D
    print(Vb,Fb,D,f"L={L:.0f}cm vol={np.pi*(D/2)**2*L/1000:.1f}L v={v[band].max():.0f}m/s @ {P:.0f}W, v@100W={v[band].max()*np.sqrt(100/P):.0f}")
