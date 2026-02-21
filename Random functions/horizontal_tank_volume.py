from math import sin, tan, asin, pi,sqrt,acos

def h_tank_vol(L,r,R,h,b):
    if b < -r or b > r:
        exit("Domain error -r,r")
    #L= Tank cylinder length
    #r= Internal cylinder radius
    #R= End cap radius
    #h= End cap height (Tank lenght/2 - r/2)
    #b= Liquid height from centerline (-r,r)
    A=2*pow(h,2)*(R-h/3)+pow(r,2)*L
    B=pi/2-asin(b/r)
    C=-pow(b,2)*(L+2*h)/tan(asin(b/r))
    return (A*B+C)

if __name__ == "__main__":
    import matplotlib.pyplot as plt
    import numpy as np
    R=1.27 # Sphere radius
    h=1.27
    r=1.27 # Internal radius
    b=0.762 # Liquid Height
    L=7.62 # Tank length

    bb=np.linspace(0.762-r,r,10)
    bbb=[]
    for b in bb:
        b=-b
        A=2*pow(h,2)*(R-h/3)+pow(r,2)*L
        B=pi/2-asin(b/r)
        C=-pow(b,2)*(L+2*h)/tan(asin(b/r))
        bbb.append(A*B+C)
    plt.plot(bb+r,bbb,label=f"{bbb[0]}")

    bb=np.linspace(0,0.762,10)
    bbb=[]
    for b in bb:
        D=L*(r**2*acos((r-b)/r)-(r-b)*sqrt(2*r*b-b**2)  )
        E=2*pow(2*r,3)*1*pi/12*(3*pow(b/(2*r),2)-2*pow(b/(2*r),3))
        bbb.append(D+E)
    plt.plot(bb,bbb,label=f"{bbb[-1]}")
    plt.legend()
    plt.show()

