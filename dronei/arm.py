from dronekit import connect,VehicleMode,LocationGlobalRelative,APIException
import time
import socket
import exceptions
import math
import argparse
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
armandtakeoff(10)
