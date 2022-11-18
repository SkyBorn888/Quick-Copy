import os
import sys
import pyperclip #クリップボードに保存
from libs.time_module import time_module
from pyside6_sub_window import AnotherWindow
#from libs.check_json_module import check_json_module
import json
from PySide6.QtWidgets import *  #QApplication, QWidget, QPushButton
from PySide6.QtCore import * #QFile, Qttimer
from PySide6.QtGui import *

def main():

    #check = check_json_module()
    #check.main()

    app = QApplication(sys.argv)  #環境に合わせたウィンドウを作成するために用意する。初期化
    app.setWindowIcon(QIcon('img/QuickCopy.ico'))
    main_window = Mainwindow()  #型を取る
    #ElegantDark背景
    #print(type(windows_style))
    #main_window.setStyleSheet()
    main_window.show()
    #The exec() call starts the event-loop and will block until the application quits.
    sys.exit(app.exec()) #つまり、exec()はアプリが終了するまで終わりませんよという事です。  



#PySide. QtWidgets.QWidgetを継承
class Mainwindow(QWidget):
    #__init__ parent=None 継承元QWidgetの環境変数を呼び出す
    def __init__(self):
        #super()で登録されている環境変数の値を振り込む
        super().__init__()
        #初期設定
        self.setGeometry(400,180, 570, 405) #winodw位置、サイズを指定
        self.setFixedSize(570, 405) #windowサイズを固定.上とはまた別で固定するために実行
        self.setWindowTitle("Quick Copy:1.0.0")
        self.setObjectName("QMainWindow")
        self.setProperty("mandatoryField", True)
        
        self.setStyleSheet('background-color: #444444;')
        self.home()
        
    def home(self):
        #グローバル変数の定義
        global label_2
        global label_3 #label_3をグローバル変数化 deigital_clockの際に使用
        global copy_combobox
        #global time_now # #現在時刻
        
        #デザイン指定
        button_style = self.ElegantDark_Button() #ElegantDark_design()
        combobox_style = self.ComboBox_design()
        
        
        ###################
        #ヘッダー
        moji_1 = '<p><font face="Times New Roman" size="10" color="#FFFFFF"><i>Quick Copy</i></font></p>' #紺色　傾け　Quick Copy
        #moji_1 = 'Quick Copy'
        
        label_1 = QLabel(moji_1, self) #labelとし貼る
        label_1.setObjectName("QtTitle") 
        label_1.move(204,10) #初期位置
        ###################
        
        ###################
        #直前のコピーしたものの表示
        label_2 = QLabel("A most recent copy", self)#
        #label_2.move(120, 60)
        label_2.setGeometry(50, 65, 452, 57)
        label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label_2.setLineWidth(5) # 線の広さ
        label_2.setFrameShape(QFrame.Shape.StyledPanel.Panel) # 線の形
        label_2.setStyleSheet('color:white;')
        #label_2.setFrameShadow(QFrame.Shadow.Raised) 

        #digital_clock
        time_now = self.now() #変数内に時間を格納 # #現在時刻
        label_3 = QLabel(time_now, self)#ラベル作成
        label_3.setAlignment(Qt.AlignmentFlag.AlignCenter) #文字位置
        label_3.setLineWidth(5) # 線の広さ
        label_3.setFrameShape(QFrame.Shape.StyledPanel.Panel)
        label_3.setGeometry(50, 150, 200, 57)
        label_3.setStyleSheet('color:white;')
        #label_3.move(50, 145) #初期位置

        self.timer = QTimer(self) #timerをセット
        self.timer.timeout.connect(self.digital_clock) #時間終了後に関数を実行
        self.timer.start(1000) #1000 -> 1秒
        ####################
    
        ####################
        #時間コピーボタン
        global time_copy_button
        time_copy_button = QPushButton("Copy", self) #QtWidgets
        time_copy_button.setObjectName("QPushButton") #Object名を決めることでQSSで取り扱うことができる
        time_copy_button.setGeometry(325, 150, 178, 60)
        time_copy_button.setStyleSheet(button_style) #ElegantDark_design
        time_copy_button.setToolTip('Copy to current time') #ボタンにマウスをかざした時に出てくるバルーン
        time_copy_button.clicked.connect(self.on_clock_copy)
        ####################
        
        
        ####################
        #コピー一覧編集ボタン
        view_copy_button = QPushButton("Edit Copies List", self) #QtWidgets
        view_copy_button.setObjectName("QPushButton") #Object名を決めることでQSSで取り扱うことができる
        view_copy_button.setStyleSheet(button_style)
        view_copy_button.setGeometry(48, 235, 456, 60)
        view_copy_button.clicked.connect(self.copy_view)
        ####################
        
        
        ####################
        #コンボボックスコピー
        copy_combobox = QComboBox(self)
        #copy_combobox.("ttts")
        copy_combobox.setGeometry(50, 310, 453, 70)
        copy_combobox.setObjectName("QComboBox")
        copy_combobox.PopupOffcet = (0, 10)
        copy_combobox.fade = True
        copy_combobox.slide = False
        copy_combobox.stretch = True
        copy_combobox.setStyleSheet(combobox_style)
        copy_combobox.model().sort(0)
        
        #初期
        copy_combobox.clear()
        json_open = open('data.json', 'r',encoding="utf-8") #josnファイル読み込み
        json_load = json.load(json_open) #jsonを解析
        
        for v in json_load.keys(): #jsonからKeyをcomboboxに入れいていく
            copy_combobox.addItem(v)
        #copy_combobox.setEditable(False) 
        #copy_combobox.duplicatesEnabled(False) # 重複不可能にする   
        copy_combobox.activated.connect(self.copy_changed) #activated 何かしらのアクションが起きた時
        
        #更新ボタン
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
        
        for v in json_load.keys(): #
            copy_combobox.addItem(v)
        logs = "Updated Copies List"
        label_2.clear()  
        label_2.setText(logs) #label_2に代入する
        
        
    def copy_view(self):
        self.newWinodw = AnotherWindow()
        self.newWinodw.home_2()
            
    #カレンダー
    def calendar_method(yy, mm):
        months_value = time_module.months(yy, mm)        #引数1:year 引数2:month
        return months_value

    #現在時刻をコピー
    def now(self): 
        now_time = time_module.now()
        return now_time


    #デジタル時計
    def digital_clock(self):
        #style = self.ElegantDark_design() #ElegantDark_design()
        time_now = self.now() #現在時刻
        label_3.move(50, 150)
        #print(time_now)
        label_3.setText(time_now) #書き換え
    
    def on_clock_copy(self):
        time_now = self.now()
        logs = "The current time has been copied."
        pyperclip.copy(time_now) #クリップボードに追加
        label_2.clear()  #labe_2の内容をなくし
        label_2.setText(logs) #label_2に代入する
        print("copied")
        pass
    
    def copy_changed(self):
        json_open = open('data.json', 'r')
        json_load = json.load(json_open)
        title = copy_combobox.currentText() # 選択中の文字列を取得
        data = json_load[title]
        print(data)
        pyperclip.copy(data)
        label_2.clear()
        label_2.setText(title + " has been copied.")
    
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