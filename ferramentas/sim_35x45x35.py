exec(open('small.py').read().split('print("== OPCOES')[0])
for Vb,Fb in [(19.6,36),(19.6,38),(19.6,35)]:
    spl,x,_=run(Vb/1e3,'port',Fb);band=(f>Fb*0.75)&(f<200);P=min(600,(11/x[band].max())**2)
    spl,x,_=run(Vb/1e3,'port',Fb,P=P);i=np.argmin(abs(f-35))
    D=7.0;L=23562*D**2/(Fb**2*Vb)-0.732*D
    Cab=Vb/1e3/(rho*c**2);wb=2*np.pi*Fb;Map=1/(wb**2*Cab);Yb=s*Cab+1/(s*Map)+wb*Cab/7
    V=np.sqrt(P*4);Zm=s*Mms+Rms+1/(s*Cms);U=(Bl*V/Re)/(Zm+Bl**2/Re+Sd**2/Yb);Pb=-Sd*U/Yb
    v=abs(Pb/(s*Map))/(np.pi*(D/200)**2)
    pk=spl[f<250].max()-spl[np.argmin(abs(f-250))]
    print(f"{Vb}L Fb{Fb}: F3={F(spl,3):.0f} F6={F(spl,6):.0f} pico={pk:+.1f} Plim={P:.0f}W SPL@35={spl[i]:.0f} SPL@60={spl[np.argmin(abs(f-60))]:.0f} L={L:.0f}cm v={v[band].max():.0f}")
