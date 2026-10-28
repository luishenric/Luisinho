# Simulador simples de caixa selada/dutada (modelo de parametros concentrados, sem Le).
# Troque os parametros Thiele-Small abaixo para testar outro alto-falante.
# Uso: python3 ferramentas/sim_caixa.py
import numpy as np
rho,c=1.204,343.0
Fs,Vas,Qts,Qes,Sd,Mms=46,8.33e-3,0.47,0.49,183e-4,66.28e-3
Re=3.4  # estimado (4 ohm nominal)
Qms=Qes*Qts/(Qes-Qts)
ws=2*np.pi*Fs
Cms=1/(ws**2*Mms); Rms=ws*Mms/Qms
Bl=np.sqrt(ws*Mms*Re/Qes)
f=np.logspace(np.log10(10),np.log10(400),2000); w=2*np.pi*f; s=1j*w
def sim(Vb,Fb=None,P=600,Ap=None,QL=7):
    Cab=Vb/(rho*c**2)
    Yb=s*Cab
    if Fb:
        wb=2*np.pi*Fb; Map=1/(wb**2*Cab); Ral=QL/(wb*Cab)
        Yb=Yb+1/(s*Map)+1/Ral
    else:
        Ral=QL*10/(ws*Cab); Yb=Yb+1/Ral
    V=np.sqrt(P*4)
    Zm=s*Mms+Rms+1/(s*Cms)
    U=(Bl*V/Re)/(Zm+Bl**2/Re+Sd**2/Yb)
    Pb=-Sd*U/Yb; Q=-s*Cab*Pb
    p=rho*s*Q/(2*np.pi)  # 1 m, meio-espaco
    spl=20*np.log10(abs(p)/2e-5)
    x=abs(U/s)*1000
    vp=None
    if Fb:
        Up=Pb/(s*Map); vp=abs(Up)/Ap if Ap else None
    return spl,x,vp
def fpt(spl,db):
    ref=spl[np.argmin(abs(f-250))]
    idx=np.where(spl<ref-db)[0]
    idx=idx[f[idx]<250]
    return f[idx.max()] if len(idx) else None
print(f"Qms={Qms:.1f} Bl={Bl:.1f} Cms={Cms:.2e} VasCalc={rho*c**2*Sd**2*Cms*1000:.2f}L")
print("SELADA")
for Vb in [8,12,20,30]:
    spl,x,_=sim(Vb/1000)
    print(f" {Vb}L F3={fpt(spl,3):.0f} F6={fpt(spl,6):.0f} F10={fpt(spl,10):.0f}  xmax@600W(20-200Hz)={x[(f>20)&(f<200)].max():.1f}mm")
print("DUTADA  (excursao maxima e frequencia acima de 20Hz, a 600W e potencia para Xmax 11mm)")
for Vb in [15,20,25,30,40,50]:
  for Fb in [32,35,38,42]:
    spl,x,_=sim(Vb/1000,Fb)
    band=(f>Fb*0.75)&(f<200)
    xm=x[band].max(); Pmax=600*(11/xm)**2
    print(f" {Vb}L Fb{Fb}: F3={fpt(spl,3):.0f} F6={fpt(spl,6):.0f} F10={fpt(spl,10):.0f} pico={spl[f<250].max()-spl[np.argmin(abs(f-250))]:+.1f}dB  x={xm:.1f}mm  P@Xmax={min(Pmax,600):.0f}W")
print("\nCOMPACTAS")
for Vb in [10,12,15,18]:
  for Fb in [35,38,40]:
    spl,x,_=sim(Vb/1000,Fb)
    print(f" {Vb}L Fb{Fb}: F3={fpt(spl,3):.0f} F6={fpt(spl,6):.0f} F10={fpt(spl,10):.0f} pico={spl[f<250].max()-spl[np.argmin(abs(f-250))]:+.1f}dB")
print("\nDUTO e velocidade (duto redondo, ponta flange+livre)")
for Vb,Fb in [(15,38),(18,36),(20,35)]:
  for D in [7.5,10]:
    Ap=np.pi*(D/200)**2
    L=23562*D**2/(Fb**2*Vb)-0.732*D
    for P in [100,200,300]:
      spl,x,vp=sim(Vb/1000,Fb,P=P,Ap=Ap)
      band=(f>Fb*0.75)&(f<200)
      print(f" {Vb}L Fb{Fb} D{D}cm L={L:.0f}cm P{P}W: vmax={vp[band].max():.0f} m/s x={x[band].max():.1f}mm SPL@Fb={spl[np.argmin(abs(f-Fb))]:.0f}dB")
