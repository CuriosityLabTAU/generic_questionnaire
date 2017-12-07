#!/usr/bin/python
# -*- coding: utf-8 -*-
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.graphics import *
from kivy.storage.jsonstore import JsonStore
from kivy.properties import ObjectProperty
from hebrew_management import HebrewManagement


class FinalForm(BoxLayout):
    the_app = None
    statements = None
    statement_label = None
    title=ObjectProperty()
    curiosity_lbl=ObjectProperty()
    end_button=ObjectProperty()

    def __init__(self, the_app):
        super(FinalForm, self).__init__()
        self.the_app = the_app

        title_txt = u"תודה רבה!"
        self.title.text = title_txt[::-1]

        end_text = u"סיום"
        self.end_button.text = end_text[::-1]
        self.end_button.bind(on_press=self.next)

    def start(self, pars):
        final_score = 'high'

        # total_info in percentage
        if 'total_info' in self.the_app.score.score:
            score = self.the_app.score.score['total_info']
            if score < 0:
                score = 0.75

            if score < 0.25:
                final_score = 'low'
            else:
                if score < 0.5:
                    final_score = 'medium'

        new_lines = HebrewManagement.multiline(self.statements[final_score]["s1"][::-1], 75)
        for nl in range(0, len(new_lines)):
            self.statement_label[nl].text = new_lines[nl]

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

    def next(self, pars):
        self.the_app.stop()
