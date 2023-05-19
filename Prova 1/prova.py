#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import time


class TurtleController(Node):
    # Define a class 
    def __init__(self):
        # Constructor for the TurtleController class that initializes the node, the publisher and the Twist message
        super().__init__('turtle_controller')
        self.publisher_ = self.create_publisher(Twist, 'turtle1/cmd_vel', 10)
        self.twist_msg_ = Twist()
        self.publisher_.publish(self.twist_msg_)
        time.sleep(1)
        self.move_turtle()
        
    def move_turtle(self): 
        #Values for the linear and angular velocity
        self.move(0.0, 0.5)
        self.move(0.5, 0.0)
        self.move(0.0, 0.5)
        self.move(0.5, 0.0)
        self.move(0.0, 1.0)
        self.move(1.0, 0.0)  

        #Values for the linear and angular velocity to return to the initial position
        self.move(-1.0, 0.0)
        self.move(0.0, -1.0)
        self.move(-0.5, 0.0)
        self.move(0.0, -0.5)
        self.move(-0.5, 0.0)
    
    def move(self,x,z):
        # Function to set the linear and angular velocity for the turtle and publish the Twist message
        self.twist_msg_.linear.x = x
        self.twist_msg_.angular.z = z
        self.publisher_.publish(self.twist_msg_)
        time.sleep(2)

def main(args=None):
    # Main function to initialize the node and execute it
    rclpy.init()
    turtle_controller = TurtleController()
    rclpy.spin(turtle_controller)
    turtle_controller.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()