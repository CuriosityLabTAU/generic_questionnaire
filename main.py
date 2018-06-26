#!/usr/bin/python
# -*- coding: utf-8 -*-
from questionnaire_form import *
from final_form import *
from middle_form import *
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy_communication.kivy_logger import *
from kivy_communication import KL


class QuestionnairesApp(App):
    sm = None
    qf = None
    float_layout = None

    cei2 = None
    bfi = None

    def build(self):
        # initialize logger
        #KL.start([DataMode.file, DataMode.communication]) #, "/sdcard/curiosity/", the_ip='127.0.0.1')#self.user_data_dir)
        KL.start([DataMode.file, DataMode.communication, DataMode.ros], self.user_data_dir)

        self.qf = []
        self.add_questionnaire('questionnaires/BFI.json')
        self.qf.append(MiddleForm(self))
        self.add_questionnaire('questionnaires/Need for Cognition.json')
        self.qf.append(MiddleForm(self))
        self.add_questionnaire('questionnaires/Questionnaire3.json')
        self.qf.append(MiddleForm(self))
        self.add_questionnaire('questionnaires/Questionnaire4.json')

        self.sm = ScreenManager()

        for kqf in range(0, len(self.qf)):
            screen = Screen(name="question"+str(kqf))
            screen.add_widget(self.qf[kqf])
            self.sm.add_widget(screen)

        screen = Screen(name='final_form')
        screen.add_widget(FinalForm(self))
        self.sm.add_widget(screen)

        self.start()
        return self.sm

    def add_questionnaire(self, filename=""):
        new_questionnaire = Questionnaire(filename)
        for p in range(0, len(new_questionnaire.page_dict)):
            self.qf.append(QuestionsForm(self, new_questionnaire.page_dict[p],
                                         new_questionnaire.questionnaire_name))

    def start(self):
        KL.start([DataMode.file, DataMode.communication, DataMode.ros], self.user_data_dir)
        for qf in self.qf:
            qf.start()

    def on_pause(self):
        return True

if __name__ == '__main__':
    QuestionnairesApp().run()

