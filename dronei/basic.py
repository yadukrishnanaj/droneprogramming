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
def distancemeters(target,current):
    dlat=target.lat-current.lat
    dlon=target.lon-current.lon
    return math.sqrt((dlon*dlon)+(dlat*dlat))*1.113195e5

def gototarget(target):
    distancetotarget=distancemeters(target,vehicle.location.global_relative_frame)
    
    vehicle.simple_goto(target)
    while vehicle.mode.name=="GUIDED":
        currentdistance=distancemeters(target,vehicle.location.global_relative_frame)
        if(currentdistance<distancetotarget*0.01):
            print("distancetotargetreached")
            time.sleep(2)
            break
        time.sleep(1)
    return None

wp1=LocationGlobalRelative(44.5202,-88.060316,10)
vehicle=connectMycopter()
armandtakeoff(10)

gototarget(wp1)

vehicle.mode=VehicleMode("LAND")

while vehicle.mode!="LAND":
    print("entering land mode:")
    time.sleep(1)
print("vehicle landed")

while True:
    time.sleep(1)
    
    
