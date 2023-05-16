#! /usr/bin/env python3

import rclpy

from rclpy.node import Node

from turtlesim.msg import Pose 

class TurtleController(Node):

    def __init__(self):
    super().__init__("turtlecontroller")

    self.subscription = self.create_subscription(
        msg_type=Pose,
    )