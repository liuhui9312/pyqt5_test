#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/9/21 11:27
# @Author  : huiliu@annoroad.com
# @Descript: 
# @File    : calculator.py
# @Software: PyCharm
import sys
from math import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import (QApplication, QDialog, QLineEdit, QTextBrowser, QVBoxLayout)


class Form(QDialog):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        self.browser = QTextBrowser()
        self.lineedit = QLineEdit("Type an expression and press Enter")
        self.lineedit.selectAll()
        layout = QVBoxLayout()
        layout.addWidget(self.browser)
        layout.addWidget(self.lineedit)
        self.setLayout(layout)
        self.lineedit.setFocus()
        self.lineedit.returnPressed.connect(self.updateUi)
        self.setWindowTitle("Calculate")

    def updateUi(self):
        text = ''
        try:
            text = self.lineedit.text()
            self.browser.append("%s = <b>%s</b>" % (text, eval(text)))
        except:
            self.browser.append("<font color=red>%s is invalid!</font>" % text)
        self.lineedit.setText('')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = Form()
    form.show()
    app.exec_()
