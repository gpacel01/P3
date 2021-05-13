# Mechanics problem: The free-rolling ramp has a mass of 40 kg. A 10-kg crate is released from rest at A and slides down 3.5 m to point B.
# If the surface of the ramp is smooth, determine the ramp’s speed when the crate reaches B. Also, what is the velocity of the crate?

# given parameters that may be changed:
crateMass = 10 # the mass of the crate, in kg
rampMass = 40 # the mass of the ramp, in kg
initialVelocityCrate = 0 # the initial velocity of the crate, in m/s
initialVelocityRamp = 0 # the initial velocity of the ramp, in m/s
crateSlideDist = 3.5 # distance the crate slides down the slope, in m
ampSlopeAngle = 30 # angle of the ramp's slope, in degrees

# import relevant libraries
import sympy as sym
import mpmath


def findAnswer(mCrate, mRamp,initVelCrate, initVelRamp, slideDist, slopeAngle):

    # define parameters consistent across different variations of the problem
    g = 9.81 # variable to represent gravity
    initHeightCrate = slideDist*mpmath.sin(mpmath.radians(slopeAngle)) # determine height of crate initially
    initHeightRamp = 0 # starts at the datum
    finHeightCrate = 0 # ends at the datum
    finHeightRamp = 0 # ends at the datum
    
    # define the unknowns for which we are solving as symbolic variables  
    finVelCrate = sym.Symbol('finVelCrate') # create the symbolic variable for the crate final velocity
    finVelRamp = sym.Symbol('finVelRamp') # create the symbolic variable for the ramp final velocity
   
   # apply conservation of linear momentum
    finVelCrate = mRamp/mCrate*finVelRamp
    
    # calculate the initial kinetic and potential energy of the system
    initKE = 0.5*mCrate*(initVelCrate**2) + 0.5*mRamp*(initVelRamp**2) # a number, 0
    initPE = mCrate*g*initHeightCrate + mRamp*g*initHeightRamp # a nonzero number

    # calculate the final kinetic and potential energy of the system
    finPE = mCrate*g*finHeightCrate + mRamp*g*finHeightRamp # a number, 0
    finKE = initPE + initKE - finPE # a number
    
    finVelCrate, finVelRamp, relativeVel = sym.symbols('finVelCrate finVelRamp relativeVel')
    
    eq1 = sym.Eq(0.5*mCrate*(finVelCrate**2) + 0.5*mRamp*(finVelRamp**2)-finKE) # a symbol, includes symbols finVelCrate and finVelRamp
    eq2 = sym.Eq(finVelCrate - finVelRamp - relativeVel) 
    eq3 = sym.Eq(mpmath.sqrt((relativeVel*mpmath.cos(mpmath.radians(slopeAngle))-finVelRamp)**2 + (-0.5*relativeVel*mpmath.sin(mpmath.radians(slopeAngle)))**2)-finVelCrate)
    
    velocities = sym.solve((eq1, eq2, eq3),(finVelRamp,finVelCrate))
    print(velocities)
    
findAnswer(10, 40,0, 0, 3.5, 30)