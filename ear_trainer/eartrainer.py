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
all_chords = ["cmaj","cmin","dom7","min7","maj7"]
all_interv = ["2m","2w","3m","3w","trit","4th","5th","6m","6w","7m","7w"]
sound_path = "/Users/michal/Documents/portfolio/michaltulik14.github.io/ear_trainer/sounds/"
format = ".mp3"

class Window(QWidget):
    def __init__(self):
        super().__init__()
       

        self.setFixedSize(600,600)

        self.setWindowTitle("EarTrainer")


        self.note = ""
        self.interv = ""
        self.chord = ""

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
        layout5.setVerticalSpacing(50)
        chords.setLayout(layout5)
        tab.addTab(chords,"Chords")         #Add Tab to page


        #layout.addWidget(tab_chord,1,0)

#Create Intervals TAB

        tab_interval = QTabWidget()
        interval = QWidget(self)
        layout8 = QGridLayout()

        interval.setLayout(layout8)
        tab.addTab(interval,"Intevals")         #Add Tab to page

        #layout.addWidget(tab_interval,2,0)

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

# OUTPUT RESULT FOR PERFECT PITCH 
        self.result_label=QLabel("")
        self.result_label.setFixedWidth(100)
        self.result_label.setFont(QFont("Trebuchet MS",30)) 
        layout1.addWidget(self.result_label, 4,2,Qt.AlignmentFlag.AlignLeft)
#OUTPUT RESULT FOR CHORDS
        self.chord_label=QLabel("")
        self.chord_label.setFixedWidth(100)
        self.chord_label.setFont(QFont("Trebuchet MS",30)) 
        layout5.addWidget(self.chord_label, 4,2,Qt.AlignmentFlag.AlignLeft)

#OUTPUT RESULT FOR INTERVALS
        self.interv_label=QLabel("")
        self.interv_label.setFixedWidth(100)
        self.interv_label.setFont(QFont("Trebuchet MS",30)) 
        layout8.addWidget(self.interv_label, 4,2,Qt.AlignmentFlag.AlignLeft)
       
#CHORD BUTTONS
        chord_button = QPushButton("Start practice")
        chord_button.setFixedWidth(100)
        layout5.addWidget(chord_button,0,2,Qt.AlignmentFlag.AlignCenter)
        chord_button.clicked.connect(self.display_chord)

        chord_again = QPushButton("Play again")
        chord_again.setFixedWidth(100)
        layout5.addWidget(chord_again,0,4,Qt.AlignmentFlag.AlignCenter)
        chord_again.clicked.connect(self.again_chord)
  
        maj_chord = QPushButton("Maj")
        maj_chord.setFixedWidth(100)
        layout5.addWidget(maj_chord, 1,0,Qt.AlignmentFlag.AlignLeft)
        maj_chord.clicked.connect(self.verify_majchord)

        min_chord = QPushButton("Min")
        min_chord.setFixedWidth(100)
        layout5.addWidget(min_chord, 1,1,Qt.AlignmentFlag.AlignLeft)
        min_chord.clicked.connect(self.verify_minchord)

        dom7_chord = QPushButton("Dom7")
        dom7_chord.setFixedWidth(100)
        layout5.addWidget(dom7_chord, 1,2,Qt.AlignmentFlag.AlignLeft)
        dom7_chord.clicked.connect(self.verify_domchord)

        maj7_chord = QPushButton("Maj7")
        maj7_chord.setFixedWidth(100)
        layout5.addWidget(maj7_chord, 1,3,Qt.AlignmentFlag.AlignLeft)
        maj7_chord.clicked.connect(self.verify_maj7chord)

        min7_chord = QPushButton("Min7")
        min7_chord.setFixedWidth(100)
        layout5.addWidget(min7_chord, 1,4,Qt.AlignmentFlag.AlignLeft)
        min7_chord.clicked.connect(self.verify_min7chord)


#INTERVALS BUTTONS
        interv_button = QPushButton("Start practice")
        interv_button.setFixedWidth(100)
        layout8.addWidget(interv_button,0,2,Qt.AlignmentFlag.AlignCenter)
        interv_button.clicked.connect(self.display_interv)

        interv_again = QPushButton("Play again")
        interv_again.setFixedWidth(100)
        layout8.addWidget(interv_again,0,4,Qt.AlignmentFlag.AlignCenter)
        interv_again.clicked.connect(self.again_interv)

        m2_interv = QPushButton("m2")
        m2_interv.setFixedWidth(100)
        layout8.addWidget(m2_interv, 1,0,Qt.AlignmentFlag.AlignLeft)
        m2_interv.clicked.connect(self.verify_m2interv)

        w2_interv = QPushButton("M2")
        w2_interv.setFixedWidth(100)
        layout8.addWidget(w2_interv, 1,1,Qt.AlignmentFlag.AlignLeft)
        w2_interv.clicked.connect(self.verify_w2interv)

        m3_interv = QPushButton("m3")
        m3_interv.setFixedWidth(100)
        layout8.addWidget(m3_interv, 1,2,Qt.AlignmentFlag.AlignLeft)
        m3_interv.clicked.connect(self.verify_m3interv)

        w3_interv = QPushButton("M3")
        w3_interv.setFixedWidth(100)
        layout8.addWidget(w3_interv, 1,3,Qt.AlignmentFlag.AlignLeft)
        w3_interv.clicked.connect(self.verify_w3interv)

        kwart_interv = QPushButton("4th")
        kwart_interv.setFixedWidth(100)
        layout8.addWidget(kwart_interv, 1,4,Qt.AlignmentFlag.AlignLeft)
        kwart_interv.clicked.connect(self.verify_kwart)

        trit_interv = QPushButton("4+")
        trit_interv.setFixedWidth(100)
        layout8.addWidget(trit_interv, 2,0,Qt.AlignmentFlag.AlignLeft)
        trit_interv.clicked.connect(self.verify_trit)

        fifth_interv = QPushButton("5th")
        fifth_interv.setFixedWidth(100)
        layout8.addWidget(fifth_interv, 2,1,Qt.AlignmentFlag.AlignLeft)
        fifth_interv.clicked.connect(self.verify_fifth)

        m6_interv = QPushButton("m6")
        m6_interv.setFixedWidth(100)
        layout8.addWidget(m6_interv, 2,2,Qt.AlignmentFlag.AlignLeft)
        m6_interv.clicked.connect(self.verify_m6interv)

        w6_interv = QPushButton("M6")
        w6_interv.setFixedWidth(100)
        layout8.addWidget(w6_interv, 2,3,Qt.AlignmentFlag.AlignLeft)
        w6_interv.clicked.connect(self.verify_w6interv)

        m7_interv = QPushButton("m7")
        m7_interv.setFixedWidth(100)
        layout8.addWidget(m7_interv, 2,4,Qt.AlignmentFlag.AlignLeft)
        m7_interv.clicked.connect(self.verify_m7interv)

        w7_interv = QPushButton("M7")
        w7_interv.setFixedWidth(100)
        layout8.addWidget(w7_interv, 3,2,Qt.AlignmentFlag.AlignLeft)
        w7_interv.clicked.connect(self.verify_w7interv)      
        
        
# PLAYING SINGLE NOTES 
    def display(self):
        
        #self.note = "D"
        self.note = random.choice(all_notes)
        self.result_label.setText("")
        self.choice = sound_path+self.note+format
        play_note = AudioSegment.from_mp3(self.choice)
        play(play_note)
        print(self.note)

# REPEAT SINGLE NOTES 
    def again(self):
        #play note once again

        play_note = AudioSegment.from_mp3(self.choice)
        play(play_note)
        
# SINGLE NOTES VERIFICATION
    def verify_c(self):
        if self.note == "C":
            print("success")
            self.result_label.setText("Correct")
            self.result_label.setStyleSheet("color:green;")
        else:
            print("fail")
            self.result_label.setText("Wrong")
            self.result_label.setStyleSheet("color:red;")
        QTimer.singleShot(2000,self.display) 

    def verify_d(self):
        if self.note == "D":
            print("success")
            self.result_label.setText("Correct")
            self.result_label.setStyleSheet("color:green;")
        else:
            print("fail")
            self.result_label.setText("Wrong")
            self.result_label.setStyleSheet("color:red;")
        QTimer.singleShot(2000,self.display)
    def verify_e(self):
        if self.note == "E":
            print("success")
            self.result_label.setText("Correct")
            self.result_label.setStyleSheet("color:green;")
        else:
            print("fail")
            self.result_label.setText("Wrong")
            self.result_label.setStyleSheet("color:red;")
        QTimer.singleShot(2000,self.display)
    def verify_f(self):
        if self.note == "F":
            print("success")
            self.result_label.setText("Correct")
            self.result_label.setStyleSheet("color:green;")
        else:
            print("fail")
            self.result_label.setText("Wrong")
            self.result_label.setStyleSheet("color:red;")
        QTimer.singleShot(2000,self.display)
    def verify_g(self):
        if self.note == "G":
            print("success")
            self.result_label.setText("Correct")
            self.result_label.setStyleSheet("color:green;")
        else:
            print("fail")
            self.result_label.setText("Wrong")
            self.result_label.setStyleSheet("color:red;")
        QTimer.singleShot(2000,self.display)
    def verify_a(self):
        if self.note == "A":
            print("success")
            self.result_label.setText("Correct")
            self.result_label.setStyleSheet("color:green;")
        else:
            print("fail")
            self.result_label.setText("Wrong")
            self.result_label.setStyleSheet("color:red;")
        QTimer.singleShot(2000,self.display)
    def verify_b(self):
        if self.note == "B":
            print("success")
            self.result_label.setText("Correct")
            self.result_label.setStyleSheet("color:green;")
        else:
            print("fail")
            self.result_label.setText("Wrong")
            self.result_label.setStyleSheet("color:red;")
        QTimer.singleShot(2000,self.display)
    def verify_csharp(self):
        if self.note == "C#":
            print("success")
            self.result_label.setText("Correct")
            self.result_label.setStyleSheet("color:green;")
        else:
            print("fail")
            self.result_label.setText("Wrong")
            self.result_label.setStyleSheet("color:red;")
        QTimer.singleShot(2000,self.display)
    def verify_dsharp(self):
        if self.note == "D#":
            print("success")
            self.result_label.setText("Correct")
            self.result_label.setStyleSheet("color:green;")
        else:
            print("fail")
            self.result_label.setText("Wrong")
            self.result_label.setStyleSheet("color:red;")
        QTimer.singleShot(2000,self.display)
    def verify_fsharp(self):
        if self.note == "F#":
            print("success")
            self.result_label.setText("Correct")
            self.result_label.setStyleSheet("color:green;")
        else:
            print("fail")
            self.result_label.setText("Wrong")
            self.result_label.setStyleSheet("color:red;")
        QTimer.singleShot(2000,self.display)
    def verify_gsharp(self):
        if self.note == "G#":
            print("success")
            self.result_label.setText("Correct")
            self.result_label.setStyleSheet("color:green;")
        else:
            print("fail")
            self.result_label.setText("Wrong")
            self.result_label.setStyleSheet("color:red;")
        QTimer.singleShot(2000,self.display)
    def verify_asharp(self):
        if self.note == "A#":
            print("success")
            self.result_label.setText("Correct")
            self.result_label.setStyleSheet("color:green;")
        else:
            print("fail")
            self.result_label.setText("Wrong")
            self.result_label.setStyleSheet("color:red;")
        QTimer.singleShot(2000,self.display)


#PLAY SINGLE CHORD
    def display_chord(self):
        
        #self.note = "D"
        self.chord = random.choice(all_chords)
        self.chord_label.setText("")
        self.choice = sound_path+self.chord+format
        play_note = AudioSegment.from_mp3(self.choice)
        play(play_note)
        print(self.chord)
    
# REPEAT CHORD
    def again_chord(self):
        play_note = AudioSegment.from_mp3(self.choice)
        play(play_note)
    
#CHORDS VERIFICATION

    def verify_majchord(self):
        if self.chord == "cmaj":
            print("success")
            self.chord_label.setText("Correct")
            self.chord_label.setStyleSheet("color:green;")
        else:
            print("fail")
            self.chord_label.setText("Wrong")
            self.chord_label.setStyleSheet("color:red;")
        QTimer.singleShot(2000,self.display_chord)

    def verify_minchord(self):
        if self.chord == "cmin":
            print("success")
            self.chord_label.setText("Correct")
            self.chord_label.setStyleSheet("color:green;")
        else:
            print("fail")
            self.chord_label.setText("Wrong")
            self.chord_label.setStyleSheet("color:red;")
        QTimer.singleShot(2000,self.display_chord)
    def verify_domchord(self):
        if self.chord == "dom7":
            print("success")
            self.chord_label.setText("Correct")
            self.chord_label.setStyleSheet("color:green;")
        else:
            print("fail")
            self.chord_label.setText("Wrong")
            self.chord_label.setStyleSheet("color:red;")
        QTimer.singleShot(2000,self.display_chord)
    def verify_min7chord(self):
        if self.chord == "min7":
            print("success")
            self.chord_label.setText("Correct")
            self.chord_label.setStyleSheet("color:green;")
        else:
            print("fail")
            self.chord_label.setText("Wrong")
            self.chord_label.setStyleSheet("color:red;")
        QTimer.singleShot(2000,self.display_chord)
    def verify_maj7chord(self):
        if self.chord == "maj7":
            print("success")
            self.chord_label.setText("Correct")
            self.chord_label.setStyleSheet("color:green;")
        else:
            print("fail")
            self.chord_label.setText("Wrong")
            self.chord_label.setStyleSheet("color:red;")
        QTimer.singleShot(2000,self.display_chord)


#PLAY SINGLE INTERV
    def display_interv(self):
        
        #self.note = "D"
        self.interv = random.choice(all_interv)
        self.interv_label.setText("")
        self.choice = sound_path+self.interv+format
        play_note = AudioSegment.from_mp3(self.choice)
        play(play_note)
        print(self.interv)
    
# REPEAT INTERV
    def again_interv(self):
        play_note = AudioSegment.from_mp3(self.choice)
        play(play_note)


# INTERVALS VERIFICATION : 
    def verify_m2interv(self):
        if self.interv == "2m":
            print("success")
            self.interv_label.setText("Correct")
            self.interv_label.setStyleSheet("color:green;")
        else:
            print("fail")
            self.interv_label.setText("Wrong")
            self.interv_label.setStyleSheet("color:red;")
        QTimer.singleShot(2000,self.display_interv)

    def verify_w2interv(self):
        if self.interv == "2w":
            print("success")
            self.interv_label.setText("Correct")
            self.interv_label.setStyleSheet("color:green;")
        else:
            print("fail")
            self.interv_label.setText("Wrong")
            self.interv_label.setStyleSheet("color:red;")
        QTimer.singleShot(2000,self.display_interv)
    def verify_m3interv(self):
        if self.interv == "3m":
            print("success")
            self.interv_label.setText("Correct")
            self.interv_label.setStyleSheet("color:green;")
        else:
            print("fail")
            self.interv_label.setText("Wrong")
            self.interv_label.setStyleSheet("color:red;")
        QTimer.singleShot(2000,self.display_interv)
    def verify_w3interv(self):
        if self.interv == "3w":
            print("success")
            self.interv_label.setText("Correct")
            self.interv_label.setStyleSheet("color:green;")
        else:
            print("fail")
            self.interv_label.setText("Wrong")
            self.interv_label.setStyleSheet("color:red;")
        QTimer.singleShot(2000,self.display_interv)
    
    def verify_kwart(self):
        if self.interv == "4th":
            print("success")
            self.interv_label.setText("Correct")
            self.interv_label.setStyleSheet("color:green;")
        else:
            print("fail")
            self.interv_label.setText("Wrong")
            self.interv_label.setStyleSheet("color:red;")
        QTimer.singleShot(2000,self.display_interv)

    def verify_trit(self):
        if self.interv == "trit":
            print("success")
            self.interv_label.setText("Correct")
            self.interv_label.setStyleSheet("color:green;")
        else:
            print("fail")
            self.interv_label.setText("Wrong")
            self.interv_label.setStyleSheet("color:red;")
        QTimer.singleShot(2000,self.display_interv)

    def verify_fifth(self):
        if self.interv == "5th":
            print("success")
            self.interv_label.setText("Correct")
            self.interv_label.setStyleSheet("color:green;")
        else:
            print("fail")
            self.interv_label.setText("Wrong")
            self.interv_label.setStyleSheet("color:red;")
        QTimer.singleShot(2000,self.display_interv)

    def verify_m6interv(self):
        if self.interv == "6m":
            print("success")
            self.interv_label.setText("Correct")
            self.interv_label.setStyleSheet("color:green;")
        else:
            print("fail")
            self.interv_label.setText("Wrong")
            self.interv_label.setStyleSheet("color:red;")
        QTimer.singleShot(2000,self.display_interv)
    
    def verify_w6interv(self):
        if self.interv == "6w":
            print("success")
            self.interv_label.setText("Correct")
            self.interv_label.setStyleSheet("color:green;")
        else:
            print("fail")
            self.interv_label.setText("Wrong")
            self.interv_label.setStyleSheet("color:red;")
        QTimer.singleShot(2000,self.display_interv)

    def verify_m7interv(self):
        if self.interv == "7w":
            print("success")
            self.interv_label.setText("Correct")
            self.interv_label.setStyleSheet("color:green;")
        else:
            print("fail")
            self.interv_label.setText("Wrong")
            self.interv_label.setStyleSheet("color:red;")
        QTimer.singleShot(2000,self.display_interv)

    def verify_w7interv(self):
        if self.interv == "7w":
            print("success")
            self.interv_label.setText("Correct")
            self.interv_label.setStyleSheet("color:green;")
        else:
            print("fail")
            self.interv_label.setText("Wrong")
            self.interv_label.setStyleSheet("color:red;")
        QTimer.singleShot(2000,self.display_interv)

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