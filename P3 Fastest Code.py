# Mechanics problem: The free-rolling ramp has a mass of 40 kg. A 10-kg crate is released from rest at A and slides down 3.5 m to point B.
# If the surface of the ramp is smooth, determine the ramp’s and the crate's speed when the crate reaches B.

# import relevant libraries
import sympy as sym
import math


def findAnswer(mCrate, mRamp, slideDist, slopeAngle):
    finVelCrate, finVelRamp = sym.symbols('finVelCrate finVelRamp', real = True)
    eq1 = sym.Eq(0.5*mCrate*(finVelCrate**2) + 0.5*mRamp*(finVelRamp**2)-(mCrate*9.81*(slideDist*math.sin(math.radians(slopeAngle))))) # a symbol, includes symbols finVelCrate and finVelRamp
    eq2 = sym.Eq(sym.sqrt(((finVelCrate - finVelRamp)*math.cos(math.radians(slopeAngle))-finVelRamp)**2 + (-(finVelCrate - finVelRamp)*math.sin(math.radians(slopeAngle)))**2)-finVelCrate)
        
    velocities = sym.solve((eq1, eq2),(finVelRamp,finVelCrate))
    
    
    print('The final velocity of the ramp is \n' + str(velocities[0]))
    print('The final velocity of the crate is' + str(velocities[1]))

findAnswer(10,40,3.5,30)



