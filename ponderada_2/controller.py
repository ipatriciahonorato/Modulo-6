#! /usr/bin/env python3

# Import the necessary libraries
import rclpy  
import math  
from rclpy.node import Node  
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry

class TurtleController(Node):  # define a new class named TurtleController that inherits from Node

    def __init__(self):  
        super().__init__('turtlebot_pose_listener')  
        # Create a publisher and a subscriber, to send commands and receive data
        self.publisher = self.create_publisher(Twist, "/cmd_vel", 10)  # Create a publisher on "/cmd_vel" topic
        self.subscription = self.create_subscription(Odometry, "/odom", self.odom_callback, 10)  # Create a subscription to the "/odom" topic
        
        # Initialize state variables
        self.start_position = None  
        self.moving_forward = True  
        self.done = False  

    def odom_callback(self, msg):  # This method is called when a message is received on the "/odom" topic
        # If we're done, ignore further messages
        if self.done:
            return
        
        # Extract the position from the message
        pose = msg.pose.pose
        position = pose.position

        # If this is the first message, remember the starting position
        if self.start_position is None:
            self.start_position = position
        
        # Calculate the distance from the starting position
        distance = math.sqrt((position.x - self.start_position.x)**2 + (position.y - self.start_position.y)**2) 

        # Log position and distance
        self.get_logger().info(f"Position: x={position.x:.2f}, y={position.y:.2f}, z={position.z:.2f}")
        self.get_logger().info(f"Distance from start: {distance:.2f}m")

        # If moving forward and not yet 5m away, keep moving
        if self.moving_forward and distance < 5.0:
            self.move_straight(1.0)

        # If moved 5m, stop moving forward
        elif self.moving_forward:
            self.moving_forward = False

        # If moving backwards and not yet back to the start, keep moving
        elif not self.moving_forward and distance > 0.1:
            self.move_straight(-1.0)
            
        # If back to the start, stop moving
        else:
            self.stop_moving()
            self.done = True
            rclpy.shutdown()

    def move_straight(self, speed):  # This method is used to move the robot straight at a given speed
        msg = Twist()  
        msg.linear.x = speed  # Set the linear speed in the x direction
        self.publisher.publish(msg)  
        self.get_logger().info("Moving " + ("forward" if speed > 0 else "backward"))  # Log the direction of movement

    def stop_moving(self):  
        msg = Twist() 
        self.publisher.publish(msg) 
        self.get_logger().info("Stopped moving") 

# Main function
def main(args=None):
    rclpy.init(args=args) 
    tc = TurtleController() 
    rclpy.spin(tc) 
    tc.destroy_node() 

if __name__ == "__main__":
    main()



