from dronekit import connect,VehicleMode,LocationGlobalRelative,APIException
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
def send_velocity(vx,vy,vz):
    msg=vehicle.message_factory.set_position_target_local_ned_encode(
          0,
          0,0,
          mavutil.mavlink.MAV_FRAME_BODY_OFFSET_NED,
          0b0000111111000111,
          0,0,0,
          vx,vy,vz,
          0,0,0,
          0,0)
    vehicle.send_mavlink(msg)
    vehicle.flush()

def globalvelocity(vx,vy,vz):
	 msg=vehicle.message_factory.set_position_target_local_ned_encode(
		  0,
		  0,0,
		  mavutil.mavlink.MAV_FRAME_LOCAL_NED,
		  0b0000111111000111,
		  0,0,0,
		  vx,vy,vz,
		  0,0,0,
		  0,0)
         vehicle.send_mavlink(msg)
         vehicle.flush()


vehicle=connectMycopter()
armandtakeoff(10)
co=0
while co<5:
    send_velocity(5,0,0)
    time.sleep(1)
    print("vehiclemoving")
    co=co+1


co=0
while co<5:
    globalvelocity(0,-5,0)
    time.sleep(1)
    print("vehiclemoving")
    co=co+1



while True:
    time.sleep(1)

