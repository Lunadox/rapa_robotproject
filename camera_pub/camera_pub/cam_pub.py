import rclpy
from sensor_msgs.msg import Image, CompressedImage
import cv2
from cv_bridge import CvBridge
from rclpy.node import Node

class BasicPublisher(Node):

    def __init__(self):
        super().__init__('image_publisher')
        self.publisher_ = self.create_publisher(CompressedImage, 'video_frames', 10)
        timer_period = 1
        self.bridge=CvBridge()
        self.timer_callback()

    def timer_callback(self):
        # msg = CompressedImage()
        cap=cv2.VideoCapture(0)
        while True:
            ret, frame = cap.read()
            if ret:
                # cv2.imshow('img', frame)
                msg = self.bridge.cv2_to_compressed_imgmsg(frame,dst_format='jpg')
                # print(msg)
                self.publisher_.publish(msg)
                key = cv2.waitKey(10)
                if key ==27:
                    break
        # cv2.destroyAllWindows()
        cap.release()

def main(args=None):
    rclpy.init(args=args)
    basic_publisher = BasicPublisher()
    rclpy.spin(basic_publisher)
    basic_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()