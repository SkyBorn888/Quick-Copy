import os
import sys
import pyperclip #クリップボードに保存
from libs.time_module import time_module
import json
from PySide6.QtWidgets import *  #QApplication, QWidget, QPushButton
from PySide6.QtCore import * #QFile, Qttimer
from PySide6.QtGui import *



class ResetWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(480, 280, 400, 100) #winodw位置、サイズを指定
        self.setFixedSize( 400, 100)
        self.setWindowTitle('Reset')
        self.setStyleSheet('background-color: #444444;')
        #self.home_3()
        
    def home_5(self):
        global log
        button_style = self.ElegantDark_Button() #ElegantDark_design()
        combobox_style = self.ComboBox_design()

        log = QLabel("Are you sure you want to reset?", self)
        log.setGeometry(50, 15, 300, 30)
        log.setStyleSheet('color:white;')

        
        ####################
        #OKボタン
        ok_button = QPushButton("ok", self) #QtWidgets
        ok_button.setObjectName("QPushButton") #Object名を決めることでQSSで取り扱うことができる
        ok_button.setGeometry(50, 55, 50, 30)
        ok_button.setStyleSheet(button_style)
        ok_button.clicked.connect(self.ok_action)
        ####################
                
        ####################
        #閉じるボタン
        close_button = QPushButton("cancel", self) #QtWidgets
        close_button.setObjectName("QPushButton") #Object名を決めることでQSSで取り扱うことができる
        close_button.setGeometry(170, 55, 50, 30)
        close_button.setStyleSheet(button_style)
        close_button.clicked.connect(self.cancel_action)
        ####################
        
        self.show()
        

    def ok_action(self):
        json_file = 'data.json'
        with open(json_file, 'a', encoding='utf-8') as file:  
            file.truncate(0) #ファイルを中身を削除 = 0 
            file.write("""{"Copies List":"Quick Copy made by Hiroxbon"}""")

        self.close()
    
    def cancel_action(self):
        self.close()
    
    def ElegantDark_Button(self):
        ElegantDark_design = """
QPushButton{
	border-style: outset;
	border-width: 2px;
	border-top-color: qlineargradient(spread:pad, x1:0.5, y1:0.6, x2:0.5, y2:0.4, stop:0 rgba(115, 115, 115, 255), stop:1 rgba(62, 62, 62, 255));
	border-right-color: qlineargradient(spread:pad, x1:0.4, y1:0.5, x2:0.6, y2:0.5, stop:0 rgba(115, 115, 115, 255), stop:1 rgba(62, 62, 62, 255));
	border-left-color: qlineargradient(spread:pad, x1:0.6, y1:0.5, x2:0.4, y2:0.5, stop:0 rgba(115, 115, 115, 255), stop:1 rgba(62, 62, 62, 255));
	border-bottom-color: rgb(58, 58, 58);
	border-bottom-width: 1px;
	border-style: solid;
	color: rgb(255, 255, 255);
	padding: 2px;
	background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(77, 77, 77, 255), stop:1 rgba(97, 97, 97, 255));
}
QPushButton:hover{
	border-style: outset;
	border-width: 2px;
	border-top-color: qlineargradient(spread:pad, x1:0.5, y1:0.6, x2:0.5, y2:0.4, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(110, 110, 110, 255));
	border-right-color: qlineargradient(spread:pad, x1:0.4, y1:0.5, x2:0.6, y2:0.5, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(110, 110, 110, 255));
	border-left-color: qlineargradient(spread:pad, x1:0.6, y1:0.5, x2:0.4, y2:0.5, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(110, 110, 110, 255));
	border-bottom-color: rgb(115, 115, 115);
	border-bottom-width: 1px;
	border-style: solid;
	color: rgb(255, 255, 255);
	padding: 2px;
	background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(107, 107, 107, 255), stop:1 rgba(157, 157, 157, 255));
}
QPushButton:pressed{
	border-style: outset;
	border-width: 2px;
	border-top-color: qlineargradient(spread:pad, x1:0.5, y1:0.6, x2:0.5, y2:0.4, stop:0 rgba(62, 62, 62, 255), stop:1 rgba(22, 22, 22, 255));
	border-right-color: qlineargradient(spread:pad, x1:0.4, y1:0.5, x2:0.6, y2:0.5, stop:0 rgba(115, 115, 115, 255), stop:1 rgba(62, 62, 62, 255));
	border-left-color: qlineargradient(spread:pad, x1:0.6, y1:0.5, x2:0.4, y2:0.5, stop:0 rgba(115, 115, 115, 255), stop:1 rgba(62, 62, 62, 255));
	border-bottom-color: rgb(58, 58, 58);
	border-bottom-width: 1px;
	border-style: solid;
	color: rgb(255, 255, 255);
	padding: 2px;
	background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(77, 77, 77, 255), stop:1 rgba(97, 97, 97, 255));
}
"""
        #print(ElegantDark_design)
        return ElegantDark_design
    
    def ComboBox_design(self):
        combobox_design ="""
QComboBox {
	color:#696969;
	background: #f5f5f5;
}
QComboBox:editable {
	selection-color: #696969;
	selection-background-color: #696969;
}
QComboBox QAbstractItemView {
	selection-color: #696969;
	selection-background-color:#696969;
}
QComboBox:!editable:on, QComboBox::drop-down:editable:on {
	color: #696969;	
}
"""
        return combobox_design