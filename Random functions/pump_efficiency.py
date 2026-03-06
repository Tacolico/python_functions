# Fluid Mechanics Thermodynamics of Turbomachine (S.L. Dixon).pdf
def pump_efficiency(Q,ρ,g,H,P):
    # Q = Volume flow [m³/s]
    # ρ = Density [kg/m³]
    # g = Gravity [m/s²]
    # H = Pump head [m] B(OUT)-B(IN) B(P,V,Z)=P/ρ/g+V²/2/g+z / no losses see ISO 5167-1
    # P = Electric power [W]
    return Q*ρ*g*H/P
