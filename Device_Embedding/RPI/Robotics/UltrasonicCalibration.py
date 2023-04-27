from ultrasonic_sensor import ultra
import config

ultra = ultra()

input("Find a wall to calibrate the ultrasonic sensor. When you press enter the calibration will commence.")
ultra.start()

input("Make sure that the front of the robot is parallel to the wall and move robot until the edge of the robot is 9-10 in(23-26 cm) away. Then press enter")
cal = int(ultra.get_dist())
ultra.stop()

print("Calibration finished, Measured distance to wall is:", cal)
config.write("ultra", cal)
