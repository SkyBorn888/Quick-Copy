import os
import sys
import pyperclip #クリップボードに保存
from libs.time_module import time_module
from pyside6_add_window import AddWindow
from pyside6_edit_window import EditWindow
from pyside6_reset_window import ResetWindow
import json
from PySide6.QtWidgets import *  #QApplication, QWidget, QPushButton
from PySide6.QtCore import * #QFile, Qttimer
from PySide6.QtGui import *



class AnotherWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(400,200, 570, 300) #winodw位置、サイズを指定
        self.setWindowTitle('Edit Copies List')
        self.setFixedSize(570, 300)
        
        self.setStyleSheet('background-color: #444444;')
        #self.home_2()
        
    def home_2(self):
        global copy_combobox
        
        ###################
        #ヘッダー
        moji_1 = '<p><font face="Times New Roman" size="10" color="#FFFFFF"><i>Quick Copy</i></font></p>' #紺色　傾け　Quick Copy
        #moji_1 = 'Quick Copy'
        
        label_1 = QLabel(moji_1, self) #labelとし貼る
        label_1.setObjectName("QtTitle") 
        label_1.move(204,10) #初期位置
        ###################
        
        button_style = self.ElegantDark_Button() #ElegantDark_design()
        combobox_style = self.ComboBox_design()
        ####################
        #コンボボックスコピー
        copy_combobox = QComboBox(self)
        #copy_combobox.("ttts")
        copy_combobox.setGeometry(50, 65, 452, 70)
        copy_combobox.PopupOffcet = (0, 10)
        copy_combobox.fade = True
        copy_combobox.slide = False
        copy_combobox.stretch = True
        copy_combobox.setStyleSheet(combobox_style)
        #copy_combobox.setEditable(False) 

        #copy_combobox.duplicatesEnabled() # 重複不可能にする
        
        
        #初期
        copy_combobox.clear()
        json_open = open('data.json', 'r') #josnファイル読み込み
        json_load = json.load(json_open) #jsonを解析
        for v in json_load.keys(): #jsonからKeyをcomboboxに入れいていく
            copy_combobox.addItem(v)
        
        
        ####################
        #コピー追加ボタン
        add_button = QPushButton("Add", self) #QtWidgets
        add_button.setObjectName("QPushButton") #Object名を決めることでQSSで取り扱うことができる
        add_button.setGeometry(50, 180, 100, 60)
        add_button.setStyleSheet(button_style)
        add_button.clicked.connect(self.Add_window)
        ####################
        
        ####################
        #コピー削除ボタン
        edit_button = QPushButton("Delete", self) #QtWidgets
        edit_button.setObjectName("QPushButton") #Object名を決めることでQSSで取り扱うことができる
        edit_button.setGeometry(225, 180, 100, 60)
        edit_button.setStyleSheet(button_style)
        edit_button.clicked.connect(self.Delete_action)
        ####################

        ####################
        #リセット
        delete_button = QPushButton("Reset", self) #QtWidgets
        delete_button.setObjectName("QPushButton") #Object名を決めることでQSSで取り扱うことができる
        delete_button.setGeometry(402, 180, 100, 60)
        delete_button.setStyleSheet(button_style)
        delete_button.clicked.connect(self.Reset_window)
        ####################
        
        ####################
        #閉じるボタン
        close_button = QPushButton("close", self) #QtWidgets
        close_button.setObjectName("QPushButton") #Object名を決めることでQSSで取り扱うことができる
        close_button.setGeometry(50, 263, 456, 30)
        close_button.setStyleSheet(button_style)
        close_button.clicked.connect(self.close_action)
        #view_copy_button.clicked.connect(self.copy_view)
        ####################

        
        ####################
        #更新ボタン
        global update_copy_button
        update_copy_button = QPushButton("Update", self) #QtWidgets
        update_copy_button.setObjectName("QPushButton") #Object名を決めることでQSSで取り扱うことができる
        update_copy_button.setGeometry(50,5, 50, 50)
        update_copy_button.setStyleSheet(button_style) #ElegantDark_design
        update_copy_button.setToolTip('Time Copy') #ボタンにマウスをかざした時に出てくるバルーン
        update_copy_button.clicked.connect(self.update_json)
        ####################
        self.show()
        
    def update_json(self):
        copy_combobox.clear()
        json_open = open('data.json', 'r') #josnファイル読み込み
        json_load = json.load(json_open) #jsonを解析
        
        for v in json_load.keys(): #jsonからKeyをcomboboxに入れいていく
            copy_combobox.addItem(v)
        
    def json_data(self):  
        copy_combobox.clear()
        json_open = open('data.json', 'r') #josnファイル読み込み
        json_load = json.load(json_open) #jsonを解析
        
        for v in json_load.keys(): #jsonからKeyをcomboboxに入れいていく
            copy_combobox.addItem(v)
            
    def copy_changed():
        pass
    
    def Add_window(self):
        self.add_window = AddWindow()
        self.add_window.home_3()
        
    def Edit_window(self):
        self.edit_window = EditWindow()
        self.edit_window.home_4()

    def Delete_action(self):
        delete_value = copy_combobox.currentText()
        json_file = 'data.json'
        with open(json_file, 'r', encoding='utf-8') as file:  
            add_info = json.load(file) #json -> dict
            add_info.pop(delete_value)#{key : value}
        with open(json_file, 'w', encoding='utf-8') as file:
            json.dump(add_info, file, ensure_ascii=False) 
        self.update_json()       
    
    def Reset_window(self):
        self.reset_window = ResetWindow()
        self.reset_window.home_5()
    
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
	selection-background-color: #f5f5f5;
}
QComboBox QAbstractItemView {
	selection-color: #696969;
	selection-background-color:#f5f5f5;
}
QComboBox:!editable:on, QComboBox::drop-down:editable:on {
	color: #696969;
    background: #696969;	
}

QListView::item {
    background-color: #f5f5f5;
    color: black;
}

QListView::item:hover {
    background-color: blue;
    color: white;
}


}
QComboBox::drop-down:on{
    background-color: #6ac9e9;
}
 
"""
        return combobox_design