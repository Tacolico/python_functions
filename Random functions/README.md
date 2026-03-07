import subprocess
subprocess.run(['git', 'clone', 'https://github.com/Tacolico/python_functions.git'])
import python_functions.vic_plot as vic_plot

import sys
sys.path.append('/home/tirilero/Desktop/Codigos/python_functions')
import vic_plot

## Orifice plate flow equation (ISO5167-1) 1997
q=CEεπd²/4*sqrt(2(P2-P1)/ρ)
q: Flow [Kg/s]
C: 0.6 [Coeficcient]
E: Velocity factor [1/sqrt(d/D)] 
D: Ustream diameter [m]
d: Orifice diameter [m]
ε: Expansion factor [1 for liquids]
P: Pressure before and after [Pa]
ρ: Density [Kg/m³]

