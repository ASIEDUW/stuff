
import os
import sys
import sanload
import pathlib
import threading

import pafy
import sanload
import threading
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngine import *
from PyQt5.QtWebEngineWidgets import *

class sandy():
    def __init__(self):

        app = QApplication(sys.argv)
        self.win = QMainWindow()
        self.win.setFixedSize(900,500)
        self.win.move(170,70)
        self.win.setWindowTitle('Sanload')
        self.win.setStyleSheet("background-color:#060f2e;")
        self.win.setWindowIcon(QIcon(":ic6"))
        self.win.setWindowOpacity(0.98)

        self.name=QLabel('<p>Sanload</p>',self.win)
        self.name.resize(100,30)
        self.name.move(5,5)
        self.name.setStyleSheet("background-color:#060f2e;color:#EEEEEE;font-size:20px;font-family:monospace;font-style:italic;font-weight:bold;")

        self.l1 =QLabel(self.win)
        self.l1.resize(19,19)
        self.l1.move(800,10)
        self.l1.setStyleSheet("background-color:blue;")

        self.l2 =QLabel(self.win)
        self.l2.resize(19,19)
        self.l2.move(824,10)
        self.l2.setStyleSheet("background-color:red;")

        self.l3 =QLabel(self.win)
        self.l3.resize(19,19)
        self.l3.move(848,10)
        self.l3.setStyleSheet("background-color:yellow;")

        self.l4 =QLabel(self.win)
        self.l4.resize(19,19)
        self.l4.move(872,10)
        self.l4.setStyleSheet("background-color:green;")
        
####----------------------------------------------------------dashboard fram--------------------------------------
        self.dashb=QFrame(self.win)
        self.dashb.resize(200,450)
        self.dashb.move(5,40)
        self.dashb.setStyleSheet("background-color:#00334c;border-radius:10px;")

        self.addurl=QListWidget(self.win)
        self.addurl.move(10,100)
        self.addurl.addItem("Add Url")
        self.addurl.setStyleSheet("background-color:#00334c;border-radius:2px;font-size:15px;color:white;font-family:monospace;font-weight:bold;")
        self.addurl.clicked.connect(self.addurlfun)

        self.setting = QPushButton(self.win)
        self.setting.resize(30,30)
        self.setting.move(10,60)
        self.setting.setIcon(QIcon(":ic3"))
        self.setting.setToolTip("settings")
        self.setting.setIconSize(QSize(30,30))
        self.setting.setFlat(True)
        self.setting.clicked.connect(self.setdockfun)
        self.setting.setStyleSheet("background-color:#00334c")


        self.input = QLineEdit(self.win)
        self.input.resize(660,40)
        self.input.move(220,40)
        self.input.setPlaceholderText('  Search')
        self.input.setStyleSheet("background-color:#DDDDDD;border-radius:15px;font-size:15px;")
        
        self.sendbtn =QPushButton(self.win)
        self.sendbtn.resize(35,35)
        self.sendbtn.move(830,43)
        self.sendbtn.setIcon(QIcon(':ic1'))
        self.sendbtn.setFlat(True)
        self.sendbtn.setIconSize(QSize(35,35))
        self.sendbtn.clicked.connect(self.downinfo)
        self.sendbtn.setStyleSheet("background-color:#DDDDDD;")


        self.scrol = QTextEdit(self.win)
        self.scrol.resize(660,150)
        self.scrol.move(220,338)
        self.scrol.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrol.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrol.setStyleSheet("background-color:#b1bed2;border-radius:5px;font-size:15px;color:black;font-weight:bold;")

        self.thum=QWebEngineView(self.win)
        self.thum.resize(250,150)
        self.thum.move(220,100)
        self.thum.setStyleSheet("background-color:#AAAAAA;")

        self.progress = QProgressBar(self.win)
        self.progress.resize(500,20)
        self.progress.move(220,300)
        self.progress.setStyleSheet("background-color:#060f2e;color:green;font-size:15px;")
   
        self.combo = QComboBox(self.win)
        self.combo.resize(200,30)
        self.combo.move(490,100)
        self.combo.setStyleSheet("background-color:green;font-size:15px;font-weight:bold;")
        self.combo.currentTextChanged.connect(self.combofun)
        self.combo.setEnabled(False)

        self.downbtn = QPushButton('Download',self.win)
        self.downbtn.resize(100,25)
        self.downbtn.move(780,265)
        self.downbtn.clicked.connect(self.download)
        self.downbtn.setStyleSheet("background-color:Green;font-weight:bold;")
        self.downbtn.setEnabled(False)

        
        self.refresh=QListWidget(self.win)
        self.refresh.move(10,130)
        self.refresh.addItem("Refresh")
        self.refresh.setStyleSheet("background-color:#00334c;border-radius:2px;font-size:15px;color:white;font-family:monospace;font-weight:bold;")
        self.refresh.clicked.connect(self.refreshfun)
#####-------------widgets--------------------------------------------------------------
        self.setdock=QWidget(self.win)
        self.setdock.resize(180,180)
        self.setdock.move(50,60)
        self.setdock.setStyleSheet("background-color:#b1bed2;")
        self.setdock.setVisible(False)

        self.prefls=QListWidget(self.setdock)
        self.prefls.move(5,5)
        self.prefls.resize(170,170)
        self.prefls.addItem("choose theme")
        self.prefls.addItem("destination")
        self.prefls.clicked.connect(self.preffun)
        self.prefls.setStyleSheet("color:black;font-size:15px;border-radius:1px;")

        self.themedock=QWidget(self.win)
        self.themedock.resize(120,70)
        self.themedock.move(50,70)
        self.themedock.setStyleSheet("background-color:#b1bed2;")
        self.themedock.setVisible(False)

        self.dradio=QRadioButton('dark',self.themedock)
        self.dradio.resize(55,30)
        self.dradio.move(5,0)
        self.dradio.toggled.connect(self.themefun)
        self.dradio.setStyleSheet("font-size:15px;font-weigt:bold")

        self.wradio=QRadioButton('white',self.themedock)
        self.wradio.resize(55,30)
        self.wradio.move(5,25)
        self.wradio.toggled.connect(self.themefun)
        self.wradio.setStyleSheet("font-size:15px;font-weigt:bold")

        self.thexit=QPushButton('exit',self.themedock)
        self.thexit.resize(50,20)
        self.thexit.move(60,50)
        self.thexit.setFlat(True)
        self.thexit.clicked.connect(self.thexitfun)
        self.thexit.setStyleSheet("font-size:15px;font-weigt:bold")

            
 #######------variables---------       
        self.setcnt=0
        self.file=os.path.expanduser('~\Downloads')
        
        self.win.show()
        sys.exit(app.exec())
    
### ----------functions--------------------------------------------------------
    def addurlfun(self):
        self.input.setText(QApplication.clipboard().text())

    def setdockfun(self):
        self.setcnt=self.setcnt+1
        if self.setcnt%2==0:
            self.setdock.setVisible(False)
        else:    
            self.setdock.show()
            
    def preffun(self):
        self.setting.setEnabled(False)
        item= self.prefls.currentItem()
        
        if item.text() == 'choose theme':
            self.setdock.close()
            self.themedock.show()
        if item.text() == 'destination':
            self.filed = QFileDialog(self.win)
            self.file =self.filed.getExistingDirectory(self.win,"choose a file","C:\\")[0]
            if str(self.file) != '':
               self.file = pathlib.Path(self.file)
               self.setting.setEnabled(True)
            else:
                self.setting.setEnabled(True)
            self.setdock.close()
            
    def thexitfun(self):
        self.themedock.close()
        self.setting.setEnabled(True)
        
    ##--themes----
    def themefun(self):
        if self.wradio.isChecked() is True:
            self.win.setStyleSheet("background-color:#DDDDDD;")
            self.input.setStyleSheet("background-color:#FFFFFF;border-radius:15px;font-size:15px;")
            self.dashb.setStyleSheet("background-color:#FFFFFF;border-radius:10px;")
            self.name.setStyleSheet("background-color:#DDDDDD;color:#EEEEEE;font-size:20px;font-family:monospace;font-style:italic;font-weight:bold;color:#00334c;")
            self.addurl.setStyleSheet("background-color:#FFFFFF;border-radius:2px;font-size:15px;color:#00334c;font-family:monospace;font-weight:bold;")
        else:
            self.win.setStyleSheet("background-color:#060f2e;")
            self.input.setStyleSheet("background-color:#DDDDDD;border-radius:15px;font-size:15px;")
            self.dashb.setStyleSheet("background-color:#00334c;border-radius:10px;")
            self.name.setStyleSheet("background-color:#060f2e;color:#EEEEEE;font-size:20px;font-family:monospace;font-style:italic;font-weight:bold;")
            self.addurl.setStyleSheet("background-color:#00334c;border-radius:2px;font-size:15px;color:white;font-family:monospace;font-weight:bold;")


    def refreshfun(self):
        self.scrol.setText('')
    def downinfo(self):
        self.link = self.input.text()
        if 'http' in self.link:
            self.video = pafy.new(self.link)
            self.scrol.append("Title: "+ self.video.title)
            self.scrol.append("Author: "+self.video.author)
            self.scrol.append("Lenght: "+str(self.video.length))
            self.scrol.append("Duration: "+self.video.duration)
            self.scrol.append("Video ID: "+self.video.videoid)
            self.thum.load(QUrl(self.video.thumb))
            self.streams = self.video.streams
            self.combo.setEnabled(True)
            for i in self.streams:
                self.scrol.append(str(i))
                self.combo.addItem(str(i)[str(i).index('@')+1:len(str(i))])
            self.combo.addItem('Audio/mp3')    
            self.downbtn.setEnabled(True)
            
    
               
        else:
            self.input.setText('youtube video/audio link is incorrect')
      

              
    def combofun(self):
        self.tag=''
       
        if self.combo.currentIndex() == 0:
           self.tag = self.streams[0]
        if self.combo.currentIndex() == 1:
           self.tag = self.streams[1]
        if self.combo.currentIndex() == 2:
           self.tag = self.streams[2]
        if self.combo.currentIndex() == 3:
           self.tag = self.streams[3]
        if self.combo.currentIndex() == 4:
           self.tag = self.streams[4]
        if self.combo.currentIndex() == 5:
           self.tag = self.streams[5]
         
       
    def download(self):
        self.tag.download(filepath=self.file,callback=self.progressfun)
        threading.Thread(target=self.tag.download,filepath=self.file,callback=self.progressfun, daemon=True).start()
        
    def progressfun(self, total, recvd, ratio, rate, eta):
        fsize = self.tag.get_filesize()
        while True:
            val = int(ratio*100)
            self.progress.setValue(val)
            break
        if val==100:
            self.scrol.append('video was downloaded succesfully')
          
                
       
    
        
        
        
san=sandy()

        
