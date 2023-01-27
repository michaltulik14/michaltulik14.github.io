from pydub import AudioSegment
from pydub.playback import play
import random



from PyQt6.QtWidgets import  (
QApplication,QWidget,QPushButton,QLabel,QLineEdit,QVBoxLayout,QGridLayout,
)
from PyQt6.QtWidgets import * 

from PyQt6.QtGui import *

from PyQt6.QtCore import Qt,QTimer
from PyQt6.QtCore import QTime
from PyQt6.QtGui import QIcon
import sys

all_notes = ["C","D","E","F","G","A","B","C#","D#","F#","G#","A#"]
sound_path = "/Users/michal/Documents/portfolio/michaltulik14.github.io/ear_trainer/"
format = ".mp3"




class Window(QWidget):
    def __init__(self):
        super().__init__()
       
        self.setFixedSize(600,600)
     
        self.setWindowTitle("EarTrainer")
        self.note = ""

        layout = QGridLayout()
        self.setLayout(layout)    
        
#Create Perfect pitch TAB
        tab = QTabWidget()
        perfectpitch = QWidget(self)
        layout1=QGridLayout()  
        layout1.setVerticalSpacing(50)
        
        perfectpitch.setLayout(layout1)
        
        
             
        tab.addTab(perfectpitch,"Perfect Pitch")    #Add Page to Tab
        
        layout.addWidget(tab,0,4) # ADD Layout to the main layout


#Create Chords TAB

        tab_chord = QTabWidget()
        chords = QWidget(self)
        layout5 = QGridLayout()

        chords.setLayout(layout5)
        tab.addTab(chords,"Chords")         #Add Tab to page


        layout.addWidget(tab_chord,1,0)

#Create Intervals TAB

        tab_interval = QTabWidget()
        interval = QWidget(self)
        layout8 = QGridLayout()

        interval.setLayout(layout8)
        tab.addTab(interval,"Intevals")         #Add Tab to page

        layout.addWidget(tab_interval,2,0)

# CREATING BUTTONS AND LABELS FOR PERFECT PITCH (TAB 1)           

        button = QPushButton("Start practice")
        button.setFixedWidth(100)

        layout1.addWidget(button,0,2,Qt.AlignmentFlag.AlignCenter)
        
        button.clicked.connect(self.display)

        again = QPushButton("Play again")
        again.setFixedWidth(100)
        layout1.addWidget(again,0,4,Qt.AlignmentFlag.AlignCenter)

        again.clicked.connect(self.again)

        c_note = QPushButton("C")
        c_note.setFixedWidth(100)
        layout1.addWidget(c_note, 1,0,Qt.AlignmentFlag.AlignLeft)
        
        c_note.clicked.connect(self.verify_c)

        d_note = QPushButton("D")
        d_note.setFixedWidth(100)
        layout1.addWidget(d_note, 1,1,Qt.AlignmentFlag.AlignLeft)
       
        d_note.clicked.connect(self.verify_d)

        e_note = QPushButton("E")
        e_note.setFixedWidth(100)
        layout1.addWidget(e_note, 1,2,Qt.AlignmentFlag.AlignLeft)
  
        e_note.clicked.connect(self.verify_e)

        f_note = QPushButton("F")
        f_note.setFixedWidth(100)
        layout1.addWidget(f_note, 1,3,Qt.AlignmentFlag.AlignLeft)
   
        f_note.clicked.connect(self.verify_f)

        g_note = QPushButton("G")
        g_note.setFixedWidth(100)
        layout1.addWidget(g_note, 1,4,Qt.AlignmentFlag.AlignLeft)

        g_note.clicked.connect(self.verify_g)

        a_note = QPushButton("A")
        a_note.setFixedWidth(100)
        layout1.addWidget(a_note, 2,0,Qt.AlignmentFlag.AlignLeft)
      
        a_note.clicked.connect(self.verify_a)

        b_note = QPushButton("B")
        b_note.setFixedWidth(100)
        layout1.addWidget(b_note, 2,1,Qt.AlignmentFlag.AlignLeft)
      
        b_note.clicked.connect(self.verify_b)

        csharp_note = QPushButton("C#")
        csharp_note.setFixedWidth(100)
        layout1.addWidget(csharp_note, 2,2,Qt.AlignmentFlag.AlignLeft)

        csharp_note.clicked.connect(self.verify_csharp)

        dsharp_note = QPushButton("D#")
        dsharp_note.setFixedWidth(100)
        layout1.addWidget(dsharp_note, 2,3,Qt.AlignmentFlag.AlignLeft)
       
        dsharp_note.clicked.connect(self.verify_dsharp)
        
        fsharp_note = QPushButton("F#")
        fsharp_note.setFixedWidth(100)
        layout1.addWidget(fsharp_note, 2,4,Qt.AlignmentFlag.AlignLeft)
        
        fsharp_note.clicked.connect(self.verify_fsharp)

        gsharp_note = QPushButton("G#")
        gsharp_note.setFixedWidth(100)
        layout1.addWidget(gsharp_note, 3,0,Qt.AlignmentFlag.AlignLeft)
        gsharp_note.clicked.connect(self.verify_gsharp)

        asharp_note = QPushButton("A#")
        asharp_note.setFixedWidth(100)
        layout1.addWidget(asharp_note, 3,1,Qt.AlignmentFlag.AlignLeft)
        
        asharp_note.clicked.connect(self.verify_asharp)

# OUTPUT RESULT
        self.result_label=QLabel("")
        self.result_label.setFixedWidth(100)
        self.result_label.setFont(QFont("Trebuchet MS",30))
       
        layout1.addWidget(self.result_label, 4,2,Qt.AlignmentFlag.AlignLeft)
       

  

        

    def display(self):
        
        #self.note = "D"
        self.note = random.choice(all_notes)
        self.result_label.setText("")
        self.choice = sound_path+self.note+format
        play_note = AudioSegment.from_mp3(self.choice)
        play(play_note)
        print(self.note)
    
    def again(self):
        #play note once again

        play_note = AudioSegment.from_mp3(self.choice)
        play(play_note)
        
        
    def verify_c(self):
        if self.note == "C":
            print("success")
            self.result_label.setText("Correct")
            self.result_label.setStyleSheet("color:green;")
        else:
            print("chujowo")
            self.result_label.setText("Wrong")
            self.result_label.setStyleSheet("color:red;")
        QTimer.singleShot(2000,self.display)
        
        

    def verify_d(self):
        if self.note == "D":
            print("success")
            self.result_label.setText("Correct")
            self.result_label.setStyleSheet("color:green;")
        else:
            print("chujowo")
            self.result_label.setText("Wrong")
            self.result_label.setStyleSheet("color:red;")
        QTimer.singleShot(2000,self.display)
    def verify_e(self):
        if self.note == "E":
            print("success")
            self.result_label.setText("Correct")
            self.result_label.setStyleSheet("color:green;")
        else:
            print("chujowo")
            self.result_label.setText("Wrong")
            self.result_label.setStyleSheet("color:red;")
        QTimer.singleShot(2000,self.display)
    def verify_f(self):
        if self.note == "F":
            print("success")
            self.result_label.setText("Correct")
            self.result_label.setStyleSheet("color:green;")
        else:
            print("chujowo")
            self.result_label.setText("Wrong")
            self.result_label.setStyleSheet("color:red;")
        QTimer.singleShot(2000,self.display)
    def verify_g(self):
        if self.note == "G":
            print("success")
            self.result_label.setText("Correct")
            self.result_label.setStyleSheet("color:green;")
        else:
            print("chujowo")
            self.result_label.setText("Wrong")
            self.result_label.setStyleSheet("color:red;")
        QTimer.singleShot(2000,self.display)
    def verify_a(self):
        if self.note == "A":
            print("success")
            self.result_label.setText("Correct")
            self.result_label.setStyleSheet("color:green;")
        else:
            print("chujowo")
            self.result_label.setText("Wrong")
            self.result_label.setStyleSheet("color:red;")
        QTimer.singleShot(2000,self.display)
    def verify_b(self):
        if self.note == "B":
            print("success")
            self.result_label.setText("Correct")
            self.result_label.setStyleSheet("color:green;")
        else:
            print("chujowo")
            self.result_label.setText("Wrong")
            self.result_label.setStyleSheet("color:red;")
        QTimer.singleShot(2000,self.display)
    def verify_csharp(self):
        if self.note == "C#":
            print("success")
            self.result_label.setText("Correct")
            self.result_label.setStyleSheet("color:green;")
        else:
            print("chujowo")
            self.result_label.setText("Wrong")
            self.result_label.setStyleSheet("color:red;")
        QTimer.singleShot(2000,self.display)
    def verify_dsharp(self):
        if self.note == "D#":
            print("success")
            self.result_label.setText("Correct")
            self.result_label.setStyleSheet("color:green;")
        else:
            print("chujowo")
            self.result_label.setText("Wrong")
            self.result_label.setStyleSheet("color:red;")
        QTimer.singleShot(2000,self.display)
    def verify_fsharp(self):
        if self.note == "F#":
            print("success")
            self.result_label.setText("Correct")
            self.result_label.setStyleSheet("color:green;")
        else:
            print("chujowo")
            self.result_label.setText("Wrong")
            self.result_label.setStyleSheet("color:red;")
        QTimer.singleShot(2000,self.display)
    def verify_gsharp(self):
        if self.note == "G#":
            print("success")
            self.result_label.setText("Correct")
            self.result_label.setStyleSheet("color:green;")
        else:
            print("chujowo")
            self.result_label.setText("Wrong")
            self.result_label.setStyleSheet("color:red;")
        QTimer.singleShot(2000,self.display)
    def verify_asharp(self):
        if self.note == "A#":
            print("success")
            self.result_label.setText("Correct")
            self.result_label.setStyleSheet("color:green;")
        else:
            print("chujowo")
            self.result_label.setText("Wrong")
            self.result_label.setStyleSheet("color:red;")
        QTimer.singleShot(2000,self.display)
app = QApplication(sys.argv)

#styling

app.setStyleSheet("""
    QWidget{
        background-color: #353535;
        color:black;
    }
    QLineEdit{
        background-color:white;
    }
    QLabel{
        color:black;
    }
    QPushButton{
        color:black;
        padding: 4px;
        border-width: 2px;
        border-radius:15px;
        border-style: outset;
        background-color: green;
        
    }
    QPushButton:hover{
        background-color:red;
        
        
    }
"""
)

window = Window()
window.show()
sys.exit(app.exec())      