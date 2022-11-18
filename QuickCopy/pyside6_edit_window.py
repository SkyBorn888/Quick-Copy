###home_4
import os
import sys
import pyperclip #クリップボードに保存
from libs.time_module import time_module
import json
from PySide6.QtWidgets import *  #QApplication, QWidget, QPushButton
from PySide6.QtCore import * #QFile, Qttimer
from PySide6.QtGui import *



class EditWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(400,160, 600, 400) #winodw位置、サイズを指定
        self.setFixedSize(600, 400)
        self.setWindowTitle('Edit')
        self.setStyleSheet('background-color: #444444;')
        #self.home_3()
        
    def home_4(self):
        global line
        global textBox
        global log
        button_style = self.ElegantDark_Button() #ElegantDark_design()
        combobox_style = self.ComboBox_design()

        log = QLabel("", self)
        log.setGeometry(50, 10, 300, 30)
        log.setStyleSheet('color:white;')

        ###################
        #編集画面
        title = QLabel("Title", self)
        title.setGeometry(50, 36, 50, 30)
        title.setStyleSheet('color:white;')
            
        line = QTextEdit(self) #テキストボックス
        line.setGeometry(50, 65, 490, 30)
        line.setStyleSheet('color:black; background-color:white;')
        
        title_2 = QLabel("Content", self)
        title_2.setGeometry(50, 100, 50, 30)
        title_2.setStyleSheet('color:white;')
        
        textBox = QTextEdit(self) #テキストボックス
        textBox.setGeometry(50, 130, 490, 200)
        textBox.setStyleSheet('color:balck;background-color:white;')
        ####################
        
        ####################
        #OKボタン
        ok_button = QPushButton("ok", self) #QtWidgets
        ok_button.setObjectName("QPushButton") #Object名を決めることでQSSで取り扱うことができる
        ok_button.setGeometry(50, 340, 50, 30)
        ok_button.setStyleSheet(button_style)
        ok_button.clicked.connect(self.ok_action)
        ####################
                
        ####################
        #閉じるボタン
        close_button = QPushButton("close", self) #QtWidgets
        close_button.setObjectName("QPushButton") #Object名を決めることでQSSで取り扱うことができる
        close_button.setGeometry(490, 340, 50, 30)
        close_button.setStyleSheet(button_style)
        close_button.clicked.connect(self.close_action)
        ####################
        
        self.show()
        

    def ok_action(self):
        key = line.toPlainText()
        value = textBox.toPlainText()
        if key == "":
            log.clear()
            log.setText("*** Title is empty ***")
            exit
        elif len(key) >= 30:
            log.clear()
            log.setText("*** Title can not enter more than 30 characters ***")
            exit
        elif value == "":
            log.clear()
            log.setText("*** Content is empty ***")
            exit
        else:
            
            json_file = 'data.json'
            with open(json_file, 'r', encoding='utf-8') as file:  
                add_info = json.load(file) #json -> dict
                add_info[str(key)] = str(value) #{key : value}
            with open(json_file, 'w', encoding='utf-8') as file:
                json.dump(add_info, file, ensure_ascii=False)
            self.close()
        
        
    def close_action(self):
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