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
def yaw(degree,relative):
    if relative:
        is_relative=1
    else:
        is_relative=0


    msg=vehicle.message_factory.command_long_encode(
          0,0,
          mavutil.mavlink.MAV_CMD_CONDITION_YAW,
          0,
          degree,
          0,
          1,
          is_relative,
          0,0,0)

    vehicle.send_mavlink(msg)
    vehicle.flush()


def vehicleinitialiser():
    lat=vehicle.location.global_relative_frame.lat
    lon=vehicle.location.global_relative_frame.lon
    alt=vehicle.location.global_relative_frame.alt
    alocation=LocationGlobalRelative(lat,lon,alt)
    msg=vehicle.message_factory.set_position_target_global_int_encode(
          0,
          0,0,
          mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT_INT,
          0b0000111111111000,
          alocation.lat*1e7,
          alocation.lon*1e7,
          alocation.alt,
          0,
          0,
          0,
          0,0,0,
          0,0)
    vehicle.send_mavlink(msg)
    vehicle.flush()









vehicle=connectMycopter()
armandtakeoff(10)

vehicleinitialiser()
time.sleep(2)
yaw(30,0)

print("changing")
time.sleep(7)



yaw(270,0)
time.sleep(7)
print("changing")






while True:
    time.sleep(1)
