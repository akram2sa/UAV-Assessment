from flyt_python.flyt_python import DroneApiConnector
token = 'd60d571c6a9ab24c3cadb2b605b87f9051c73dce'                      # Personal Access Token
vehicle_id = 'jxEBLajn'                                                 # Vehicle ID

drone = DroneApiConnector(token,vehicle_id,ip_address='localhost',wait_for_drone_response =True)

# Initialize the drone's connection
drone.connect()

print("Taking Off")
drone.takeoff(10)

print("Drawing triangle with side = 10")

drone.set_local_position(x=10, y=0, z=0, body_frame=True)
drone.set_local_position(x=5, y=8.66, z=0, body_frame=True)
drone.set_local_position(x=0, y=0, z=0,body_frame=True)


drone.land()
#disconnect the drone
drone.disconnect()
