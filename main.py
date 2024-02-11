from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.toast import toast
from kivymd.uix.label import MDLabel
from kivy.uix.screenmanager import ScreenManager, Screen
# import android permissions and ask for persmissions
'''
# import android permissions and ask for persmissions
from kivy import platform

if platform == "android":
    from android.permissions import request_permissions, Permission
    request_permissions([
        Permission.WRITE_EXTERNAL_STORAGE, 
        Permission.CAMERA, 
        Permission.READ_EXTERNAL_STORAGE
        ])
'''
# Screen manager
class DemoApp(ScreenManager):
    # write some code here
    # def func(self):
        #self.example = self.ids.
    pass

class MainApp(MDApp):
    def build(self):
        Builder.load_file("my.kv")
        return DemoApp()
        
   
MainApp().run()
