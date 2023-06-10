import sys
import os
from pyautogui import *
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("rcqt.ui")[0]

class ROSWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()

        self.W.pressed.connect(self.Foward)
        self.W.released.connect(self.Foward_stop)

        self.A.pressed.connect(self.left)
        self.A.released.connect(self.left_stop)

        self.S.pressed.connect(self.backward)
        self.S.released.connect(self.backward_stop)

        self.D.pressed.connect(self.right)
        self.D.released.connect(self.right_stop)

        self.HEADLIGHT.clicked.connect(self.HEADLIGHT_ON)

        self.CAM.clicked.connect(self.CAM_open)
    
    def initUI(self):
        self.move(998,91)
        
    
    def Foward(self):
        keyDown('w')
    def Foward_stop(self):
        keyUp('w')
    
    def backward(self):
        keyDown('s')
    def backward_stop(self):
        keyUp('s')
    
    def right(self):
        keyDown('d')
    def right_stop(self):
        keyUp('d')
    
    def left(self):
        keyDown('a')
    def left_stop(self):
        keyUp('a')
    
    def HEADLIGHT_ON(self):
        press('q')

    def CAM_open(self):
        os.system("gnome-terminal -x rqt_image_view")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    os.system("gnome-terminal -x roscore")
    hotkey('ctrl','shift','t')
    write("rosrun pub_sub_dialog talker")
    press('enter')
    hotkey('ctrl','shift','t')
    write("ssh ubuntu@192.168.1.176")
    press('enter')
    sleep(1)
    write("turtlebot")
    press('enter')
    sleep(1)
    write("rosrun pub_sub_dialog listener")
    press('enter')
    sleep(1)
    
    hotkey('ctrl','shift','t')
    write("ssh ubuntu@192.168.1.176")
    press('enter')
    sleep(1)
    write("turtlebot")
    press('enter')
    sleep(2)
    write("roslaunch turtlebot3_autorace_camera raspberry_pi_camera_publish.launch")
    press('enter')

    rosWindow = ROSWindow()
    rosWindow.show()
    app.exec_()