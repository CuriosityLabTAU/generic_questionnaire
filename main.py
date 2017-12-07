#!/usr/bin/python
# -*- coding: utf-8 -*-
from cg_graphics_audio import *
from cei2 import *
from DetailsForm import *
from consent_form import ConsentForm
from learning_form import *
from final_form import FinalForm
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from curiosity_score import *
from kivy_communication import KL


class CuriosityApp(App):
    sm = None
    cg = None
    cf = None
    qf = None
    lf = None
    df = None
    ff = None
    score = None
    float_layout = None

    cei2 = None
    learn = None

    def build(self):
        # initialize logger
        #KL.start([DataMode.file, DataMode.communication]) #, "/sdcard/curiosity/", the_ip='127.0.0.1')#self.user_data_dir)
        KL.start([DataMode.file, DataMode.communication, DataMode.ros], self.user_data_dir)

        self.cei2 = CEI2()
        self.qf = []
        for p in range(0, len(self.cei2.page_dict)):
            self.qf.append(QuestionsForm(self, self.cei2.page_dict[p]))

        self.sm = ScreenManager()

        for kqf in range(0, len(self.qf)):
            screen = Screen(name="question"+str(kqf))
            screen.add_widget(self.qf[kqf])
            self.sm.add_widget(screen)

        self.start()
        return self.sm

    def start(self):
        KL.start([DataMode.file, DataMode.communication, DataMode.ros], self.user_data_dir)
        for qf in self.qf:
            qf.start()
        # self.sm.current = "question"

    def on_pause(self):
        return True

if __name__ == '__main__':
    CuriosityApp().run()

