# VREP Connection

import sim
import sys

sim.simxFinish(-1) # just in case, close all opened connections
clientID=sim.simxStart('127.0.0.1',19999,True,True,5000,5) # Connect to CoppeliaSim
if clientID!=-1:
    print ('Connection to remote API server successful')
else:
    print ('Connection unsuccessful')
    sys.exit('Failed to Connect')
    
errorCode,Pneumatic_Actuator = sim.simxGetObjectHandle(clientID,'Pneumatic_Actuator',sim.simx_opmode_oneshot_wait)
#errorCode = sim.simxSetJointTargetVelocity(clientID,Pneumatic_Actuator,3,sim.simx_opmode_streaming)
#errorCode = sim.simxSetJointForce(clientID,Pneumatic_Actuator,200,sim.simx_opmode_oneshot) 
