# Fluid Mechanics Thermodynamics of Turbomachine (S.L. Dixon).pdf

## Orifice plate flow equation (ISO5167-1) 1997
def orifice_plate(
        D, # Suction diameter [m]
        d, # Orifice diameter [m]
        P2,# Discharge pressure [Pa]
        P1,# Suction pressure [Pa]
        ε, # Expansion factor [1 for liquids]
        ρ  # Density [Kg/m³]
        ):
    from math import pi
    E = 1/pow(d/D,1/2)
    C = 0.6
    return C*E*ε*pi*pow(d,2)/4*pow(2*(P2-P1)/ρ,1/2)

def pump_efficiency(
        Q, # Volume flow [m³/s]
        ρ, # Density [kg/m³]
        H, # Pump head [m]
        P  # Electric power [W]
        ):
    from scipy.constants import g
    return Q*ρ*g*H/P

def flow_head_extrapolation(
        Q, # Volume flow 
        P, # Pressure 
        ω1,# Rotation speed [rev/min]
        ω2 # Test rotation speed [rev/min]
        ):
    return [Q*ω2/ω1,P*pow(ω2/ω1,2)]

def bernoulli_head(
        P2, # Discharge pressure [Pa]
        P1, # Discharge velocity [m/s]
        V2, # Discharge height [m]
        V1, # Suction pressure [Pa]
        Z2, # Suction velocity [m/s]
        Z1, # Suction height [m]
        ρ,  # Fluid density [Kg/m³]
        Hl=0 # Head loss [m] (assumed to be 0)
        ):
    from scipy.constants import g
    return (P2-P1)/(ρ*g)+(V2**2-V1**2)/(2*g)+(Z2-Z1)+Hl

# Ignores previus expenses modify to add cost of electricity before performace reduction
# f(T)=(Cm+Cd(T)+Pm(T)+Previus cost)/T
# f(T)'=0
# Short cut was taken and previus cost was just added whitout deriving formula
# k and r assumed to be constant
def overhaul_time(
        Cm, # Maintenance cost
        Cd, # Downtime cost
        Pc, # Previus cost
        m, # Maintenance time [days]
        k, # Performance cost per flow [$s/m³]
        r, # Flow degrade rate [m³/s/day]
        Q # Flow rate [m³/s]
        ):
        print("Derived formula: ",pow(2*(Pc+Cm+Q*m*k)/r/k,1/2))
        print("Commond formula: ",pow(2*(Pc+Cm+Cd)/r/k,1/2))
        return pow(2*(Cm+Cd)/r/k,1/2)
