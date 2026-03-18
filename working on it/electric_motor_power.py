# Fluid Mechanics Thermodynamics of Turbomachine (S.L. Dixon).pdf
def e_motor_p(P,V,A,C):
    # P = Phases
    # V = Volaje [V]
    # A = Amperaje [A]
    # C = Power factor 
    from math import sqrt
    if Phase == 3:
        return sqrt(3)*V*A*C
    if Phase == 1:
        return V*A*C
    else: 
        exit("Domain error")
