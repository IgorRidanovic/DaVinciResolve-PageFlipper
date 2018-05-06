#! /usr/bin/env python
# -*- coding: utf-8 -*-

# DaVinci Resolve scripting proof of concept. Resolve page flipper.
# Use the UI slider to set the rate of page flipping.
# Refer to Resolve V15 public beta 2 scripting API documentation for host setup.
# Copyright 2018 Igor Riđanović, www.hdhead.com

from PyQt4 import QtCore, QtGui
import DaVinciResolveScript
import time
import sys
from threading import Thread

try:
	_fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
	def _fromUtf8(s):
		return s

try:
	_encoding = QtGui.QApplication.UnicodeUTF8
	def _translate(context, text, disambig):
		return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
	def _translate(context, text, disambig):
		return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
	def setupUi(self, Form):
		Form.setObjectName(_fromUtf8('Resolve Page Flipper'))
		Form.resize(320, 240)
		Form.setStyleSheet(_fromUtf8('background-color: #282828;'))
		
		self.verticalLayout = QtGui.QVBoxLayout(Form)
		self.verticalLayout.setObjectName(_fromUtf8('verticalLayout'))
		
		self.lcdNumber = QtGui.QLCDNumber(Form)
		self.lcdNumber.setProperty('value', 10)
		self.lcdNumber.setObjectName(_fromUtf8('lcdNumber'))
		self.lcdNumber.setSegmentStyle(QtGui.QLCDNumber.Flat)
		self.lcdNumber.setStyleSheet(_fromUtf8('background-color: #181818; color: #e64b3d;'))
		self.verticalLayout.addWidget(self.lcdNumber)
		
		self.speedSlider = QtGui.QSlider(Form)
		self.speedSlider.setMinimum(5)
		self.speedSlider.setMaximum(100)
		self.speedSlider.setProperty('value', 10)
		self.speedSlider.setOrientation(QtCore.Qt.Horizontal)
		self.speedSlider.setObjectName(_fromUtf8('speedSlider'))
		
		self.speedSlider.setStyleSheet(_fromUtf8('background-color: #282828;'))
                #self.speedSlider.valueChanged[int].connect(self.pageswitch)
		self.verticalLayout.addWidget(self.speedSlider)

		self.startButton = QtGui.QPushButton(Form)
		self.startButton.setStyleSheet(_fromUtf8('background-color: #181818;\
							color: #929292;\
							border-color: #555555;\
							font-size: 13px;'))
		sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.startButton.sizePolicy().hasHeightForWidth())
		self.verticalLayout.addWidget(self.startButton)
		self.startButton.setSizePolicy(sizePolicy)
		self.startButton.setMaximumSize(QtCore.QSize(100, 16777215))
		self.startButton.setObjectName(_fromUtf8('startButton'))
                self.startButton.clicked.connect(self.pageswitch)

		self.retranslateUi(Form)
		QtCore.QObject.connect(self.speedSlider, QtCore.SIGNAL(_fromUtf8('valueChanged(int)')), self.lcdNumber.display)
		QtCore.QMetaObject.connectSlotsByName(Form)

	def retranslateUi(self, Form):
		Form.setWindowTitle(_translate('Resolve Page Flipper', 'Resolve Page Flipper', None))
		self.startButton.setText(_translate('Form', 'Start', None))

        # Start Resolve page flipping as a new thread
	def pageswitch(self, v):
                t = PageSwitch()
                t.setName('Resolve Flipper')
                t.daemon = True
                t.start()

# This class contains the page flipper. It takes interval value / 10.0 from the QSlider.
class PageSwitch(Thread):
        def run(self):
               while True:
                        for i in pages:
                                resolve.OpenPage(i)
                                t = ui.speedSlider.value() / 10.0
                                print i, ' - interval in seconds: ' + str(t)
                                time.sleep(t)

if __name__ == '__main__':

        # Instantiate Resolve object
        resolve = DaVinciResolveScript.scriptapp('Resolve')

        pages = [
                'media',
                'edit',
                'fusion',
                'color',
                'fairlight',
                'deliver'
                 ]

	app = QtGui.QApplication(sys.argv)
	Form = QtGui.QWidget()
	ui = Ui_Form()
	ui.setupUi(Form)
	Form.show()
	sys.exit(app.exec_())

