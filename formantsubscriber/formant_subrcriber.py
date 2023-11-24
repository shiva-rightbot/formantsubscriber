import rclpy
from rclpy.node import Node

from std_msgs.msg import Int32
from std_msgs.msg import Bool

from rightbot_interfaces.msg import PickTask
import os
import subprocess


class FormantSubscriber(Node):
    task_id = 1
    

    def __init__(self):
        self.one = (2.1,-0.4,1.34,0.707,0.0,0.707,0.0)

        self.two = (2.1,-0.0,1.34,0.707,0.0,0.707,0.0)

        self.thr =(2.1,0.4,1.34,0.707,0.0,0.707,0.0)

        self.fou =(2.1,-0.4,1.24,0.707,0.0,0.707,0.0)

        self.fiv =(2.1,-0.0,1.24,0.707,0.0,0.707,0.0)

        self.six =(2.1,0.4,1.24,0.707,0.0,0.707,0.0)

        self.task = [
            (2.1,-0.4,1.34,0.707,0.0,0.707,0.0),
            (2.1,-0.0,1.34,0.707,0.0,0.707,0.0),
            (2.1,0.4,1.34,0.707,0.0,0.707,0.0),
            (2.1,-0.4,1.24,0.707,0.0,0.707,0.0),
            (2.1,-0.0,1.24,0.707,0.0,0.707,0.0),
            (2.1,0.4,1.24,0.707,0.0,0.707,0.0)
        ]

        super().__init__('formant_subscriber')
       
       
    def publish_position(self, positions):
        pick_task = PickTask()
        self.task_id = self.task_id + 1
        pick_task.task_id = self.task_id
        pick_task.task_type = 'pick'
        pick_task.pose_nos = 1
        pick_task.data = positions
        self.publisher_.publish(pick_task)
    # this fn handles the bot state command

    def func(self):
      i = 0
      while i < 6:
        self.publish_position(self.task[i])


def main(args=None):
    rclpy.init(args=args)

    formant_subscriber = FormantSubscriber()
    formant_subscriber.func()

    #rclpy.spin(formant_subscriber)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    formant_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()