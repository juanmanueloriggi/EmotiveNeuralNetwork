import sys
import os
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QLabel, QCheckBox, QWidget, QFileDialog, QPushButton, QTextEdit
from PyQt5.QtCore import QSize 
from PyQt5.QtGui import QFont 
import MainSetCorpus as SetCorp  


     
#CLASS FOR WINDOW CREATION     
class Window(QMainWindow):
    
    #DEFINE GLOBAL VARIABLE ROOT 
    MainRoot = ''
    MainRootT = ''
    AudioTextFlag = 0 #2 for both, 1 for only text, 0 for only audio
    
    def __init__(self):
        QMainWindow.__init__(self)
 
        #WINDOW SIZE
        self.setGeometry(600, 200, 500, 300) 
        self.setWindowTitle("Emotional Neural Network") 
        
        #LABELS
        myFont = QFont()
        myFont.setBold(True)
        self.l1 = QLabel(self)
        self.l1.setText('Select Corpus:')
        self.l1.setFont(myFont)
        self.l1.move(10,0)
        self.l2 = QLabel(self)
        self.l2.setText('Select NN type:')
        self.l2.setFont(myFont)
        self.l2.move(10,80)
        
        #CHECKBOXS 
        self.b1 = QCheckBox("Original Corpus",self)
        self.b1.stateChanged.connect(self.clickBoxOriginal)
        self.b1.move(20,20)
        self.b2 = QCheckBox("Fake Corpus",self)
        self.b2.stateChanged.connect(self.clickBoxFake)
        self.b2.move(20,40)
        self.b3 = QCheckBox("Lav",self)
        self.b3.stateChanged.connect(self.clickBoxLav)
        self.b3.move(20,60)
        self.b4 = QCheckBox("Audio",self)
        self.b4.stateChanged.connect(self.clickBoxA)
        self.b4.move(20,100)
        self.b5 = QCheckBox("Text",self)
        self.b5.stateChanged.connect(self.clickBoxT)
        self.b5.move(20,120)
        self.b6 = QCheckBox("Audio+Text",self)
        self.b6.stateChanged.connect(self.clickBoxAT)
        self.b6.move(20,140)
        
        #BUTTONS
        self.btn_setCorpus = QPushButton("SET CORPUS", self)
        self.btn_setCorpus.clicked.connect(self.runSetCorpus)
        self.btn_setCorpus.setFixedSize(100,30)
        self.btn_setCorpus.move(340,20)
        self.btn_runTraining = QPushButton("RUN TRAINING", self)
        self.btn_runTraining.clicked.connect(self.runTraining)
        self.btn_runTraining.setFixedSize(100,30)
        self.btn_runTraining.move(340,60)
        self.btn_runTest = QPushButton("RUN TEST", self)
        self.btn_runTest.clicked.connect(self.runTest)
        self.btn_runTest.setFixedSize(100,30)
        self.btn_runTest.move(340,100)
        
        #CONSOLE LOG
        self.logOutput = QTextEdit(self)
        self.logOutput.setReadOnly(True)
        self.logOutput.setLineWrapMode(QTextEdit.NoWrap)
        font = self.logOutput.font()
        font.setFamily("Courier")
        font.setPointSize(10)
        self.logOutput.setFixedSize(460,90)
        self.logOutput.move(20,200)
        #Button clear log
        self.btn_clear = QPushButton("Clear Logs", self)
        self.btn_clear.clicked.connect(self.clearLog)
        self.btn_clear.setFixedSize(100,25)
        self.btn_clear.move(380,170)   
    
    #PRINT LOG
    def printLog(self, text):
        self.logOutput.insertPlainText(text+'\n')
        sb = self.logOutput.verticalScrollBar()
        sb.setValue(sb.maximum()) 
    def clearLog(self):
        self.logOutput.clear()    
        
    #CHECKBOX METHODS          
    def clickBoxOriginal(self, state):
        if state == QtCore.Qt.Checked:
            self.MainRoot = os.path.normpath('D:\DATA\POLIMI\----TESI-----\Corpus_Training')
            self.MainRootT = os.path.normpath('D:\DATA\POLIMI\----TESI-----\Corpus_Test')
            txt = 'Checked on roots: '+self.MainRoot+', AND, '+self.MainRootT
            self.printLog(txt)
        else:
            self.MainRoot = ''
            self.printLog('Unchecked clickBoxOriginal') 
    def clickBoxFake(self, state):
        if state == QtCore.Qt.Checked:
            self.MainRoot = os.path.normpath('D:\DATA\POLIMI\----TESI-----\Corpus_Test_Training')
            self.MainRootT = os.path.normpath('D:\DATA\POLIMI\----TESI-----\Corpus_Test_Training')
            txt = 'Checked on roots: '+self.MainRoot+', AND, '+self.MainRootT
            self.printLog(txt)
        else:
            self.MainRoot = ''
            self.printLog('Unchecked clickBoxFake') 
    def clickBoxLav(self, state):
        if state == QtCore.Qt.Checked:
            self.MainRoot = os.path.normpath(r'C:\Users\JORIGGI00\Documents\MyDOCs\Corpus_Test_Training')
            self.MainRootT = os.path.normpath(r'C:\Users\JORIGGI00\Documents\MyDOCs\Corpus_Test_Training')
            txt = 'Checked on roots: '+self.MainRoot+', AND, '+self.MainRootT
            self.printLog(txt)
        else:
            self.MainRoot = ''
            self.printLog('Unchecked clickBoxLav')                
    def clickBoxA(self, state):
        if state == QtCore.Qt.Checked:
            AudioTextFlag = 0
            txt = 'Checked only audio'
            self.printLog(txt)
        else:
            AudioTextFlag = 0
    def clickBoxT(self, state):
        if state == QtCore.Qt.Checked:
            AudioTextFlag = 1
            txt = 'Checked only text'
            self.printLog(txt)
        else:
            AudioTextFlag = 0  
    def clickBoxAT(self, state):
        if state == QtCore.Qt.Checked:
            AudioTextFlag = 2
            txt = 'Checked audio and text'
            self.printLog(txt)
        else:
            AudioTextFlag = 0               
 
    #BUTTONS METHODS 
    def runSetCorpus(self, w):
        if self.MainRoot == '':
            self.printLog('Select one Root checkbox')
        else:
            txt = 'Set Corpus on roots: '+self.MainRoot+', AND, '+self.MainRootT
            self.printLog(txt)
            SetCorp.mainSetCorpus(self.MainRoot,self.MainRootT)
            self.printLog('END of set Corpus')
            
    def runTraining(self, w):
        if self.MainRoot == '':
            self.printLog('Select one Root checkbox')
        else:
            txt = 'Run training with root: '+self.MainRoot
            self.printLog(txt) 
            self.printLog('END of Training') 
            
    def runTest(self, w):
        if self.MainRoot == '':
            self.printLog('Select one Root checkbox')
        else:
            txt = 'Set Test with roots: '+self.MainRoot+', AND, '+self.MainRootT
            self.printLog(txt) 
            self.printLog('END of Test')     
            
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = Window()
    mainWin.show()
    sys.exit(app.exec_())

