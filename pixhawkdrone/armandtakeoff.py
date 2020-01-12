from dronekit import connect,LocationGlobalRelative,APIException,VehicleMode
import time
import dronekit_sitl
import socket

def connectmycpter():
	sitl=dronekit_sitl.start_default()
	connection_string=sitl.connection_string()
	vehicle=connect(connection_string,wait_ready=True)
	return vehicle

vehicle=connectmycpter()
while vehicle.is_armable!=True:
	print("waiting to geint armable")
	time.sleep(1)
print("vehicleis oearmable")

vehicle.mode=VehicleMode("GUIDED")

while vehicle.mode!="GUIDED":
	print("waiting to ge int guided")
	time.sleep(1)

vehicle.armed=True

while vehicle.armed!=True:
	print("waiting to ge armed")
	time.sleep(1)
print("propeller is spining")

vehicle.armed=False
while vehicle.armed!=False:
	print("waiting to get into diarmed")
print("vehicle disarmed")

vehicle.close()