import rospy
from kivymd.app import MDApp
from kivy.lang import Builder 

class TutorialApp
  def __init__(self, **kwargs):
    super().__init__(**kwargs)
    
    self.screen=Builder.load_file('/home/NAME/gui_ws/src/tutorial/ros_gui.kv)' #all style elements kept in .kv file
  def vuild(self):
    return self.screen
                                  
                                  
if __name__ == '__main__':
  rospy.init_node('simple_gui', anonymous = True)
                                  
  TutorialApp().run()
