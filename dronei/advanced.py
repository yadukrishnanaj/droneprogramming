from dronekit import connect,VehicleMode,LocationGlobalRelative,APIException,Command
import time
import socket
import exceptions
import math
import argparse
from pymavlink import mavutil
def connectMycopter():
    parser=argparse.ArgumentParser(description='commands')
    parser.add_argument('--connect')
    args=parser.parse_args()
    connection_string=args.connect
    if not connection_string:
        import dronekit_sitl
        sitl=dronekit_sitl.start_default()
        connection_string=sitl.connection_string()

    vehicle=connect(connection_string,wait_ready=True)
    return vehicle

def armandtakeoff(targethieght):
	while vehicle.is_armable!=True:
	    print("waiting to get armed")
	    time.sleep(1)
	    
	print("vehicle is now armable")

	vehicle.mode=VehicleMode("GUIDED")
	while vehicle.mode!='GUIDED':
	   print("waiting to change to guide")
	   time.sleep(1)

	print("have fun")
	vehicle.armed=True

	while vehicle.armed==False:
	    print("waiting")
	    time.sleep(1)
	print("drone armed")
        vehicle.simple_takeoff(targethieght)
        while True:
            print("current altitude :%d"%vehicle.location.global_relative_frame.alt)
            if(vehicle.location.global_relative_frame.alt>=.95*targethieght):
                break
            time.sleep(1)
        print("hieht attained")
        return None




vehicle=connectMycopter()
wphome=vehicle.location.global_relative_frame
cmd1=Command(0,0,0,mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT,mavutil.mavlink.MAV_CMD_NAV_WAYPOINT,0,0,0,0,0,0,wphome.lat,wphome.lon,wphome.alt)
cmd2=Command(0,0,0,mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT,mavutil.mavlink.MAV_CMD_NAV_WAYPOINT,0,0,0,0,0,0,44.501416,-88.063205,15)
cmd3=Command(0,0,0,mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT,mavutil.mavlink.MAV_CMD_NAV_WAYPOINT,0,0,0,0,0,0,44.501416,-88.064205,10)
cmd4=Command(0,0,0,mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT,mavutil.mavlink.MAV_CMD_NAV_RETURN_TO_LAUNCH,0,0,0,0,0,0,0,0,0)

cmds=vehicle.commands
cmds.download()
cmds.wait_ready()
cmds.clear()
cmds.add(cmd1)
cmds.add(cmd2)
cmds.add(cmd3)
cmds.add(cmd4)
vehicle.commands.upload()
armandtakeoff(10)

vehicle.mode=VehicleMode('AUTO')
while vehicle.mode!='AUTO':
    time.sleep(0.2)

while vehicle.location.global_relative_frame.alt>2:
    print("drone is executinf")
    time.sleep(2)




