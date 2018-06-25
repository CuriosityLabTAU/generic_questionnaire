#!/usr/bin/python
# -*- coding: utf-8 -*-
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.graphics import *
from kivy.storage.jsonstore import JsonStore
from kivy.properties import ObjectProperty
from hebrew_management import HebrewManagement


class MiddleForm(BoxLayout):
    the_app = None
    statements = None
    statement_label = None
    title=ObjectProperty()
    curiosity_lbl=ObjectProperty()
    end_button=ObjectProperty()

    def __init__(self, the_app):
        super(MiddleForm, self).__init__()
        self.the_app = the_app

        title_txt = u"עבור לשאלון הבא"
        self.title.text = title_txt[::-1]

        next_text = u"הבא"
        self.next_button.text = next_text[::-1]
        self.next_button.bind(on_press=self.next)

    def start(self):
        pass

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

    def next(self, pars):
        self.the_app.sm.current = self.the_app.sm.next()
