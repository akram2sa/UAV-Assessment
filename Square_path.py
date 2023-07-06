from flyt_python.flyt_python import DroneApiConnector
token = 'd60d571c6a9ab24c3cadb2b605b87f9051c73dce'                      # Personal Access Token
vehicle_id = 'jxEBLajn'                                                 # Vehicle ID

drone = DroneApiConnector(token,vehicle_id,ip_address='localhost',wait_for_drone_response =True)

# Initialize the drone's connection
drone.connect()

print("Taking Off")
drone.takeoff(5)

print("Drawing square with side = 6.5")

drone.set_local_position(x=6.5, y=0, z=0, body_frame=True)
drone.set_local_position(x=0, y=6.5, z=0, body_frame=True)
drone.set_local_position(x=-6.5, y=0, z=0,body_frame=True)
drone.set_local_position(x=0, y=-6.5, z=0,body_frame=True)

drone.land()
#disconnect the drone
drone.disconnect()
