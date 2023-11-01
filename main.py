from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QLineEdit, QLabel, QVBoxLayout, QComboBox
from PySide6.QtGui import QIcon, QMovie
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Slot
from PIL import Image
import sys, time
import speech_recognition as sr
from selenium import webdriver



# imports for the gui


class NewWindow(QWidget):
    def __init__(self, url):
        super().__init__()
        self.text = QLabel(url)
        self.label1 = QLabel('can only open websites that have .com', self)
        self.label2 = QLabel('can open camera', self)
        self.label3 = QLabel('Spelling matters, not case sensitive ', self)
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.text)
        vbox = QVBoxLayout()
        vbox.addWidget(self.label1)
        vbox.addWidget(self.label2)
        vbox.addWidget(self.label3)
        self.setLayout(vbox)
        title = "Help"
        self.setGeometry(0, 0, 200, 200)
        self.setWindowTitle(title)
        self.setLayout(self.layout)


class NewWindow1(QWidget):
    def __init__(self, url):
        super().__init__()
        vbox = QVBoxLayout()
        self.my_lineedit = QLineEdit("")
        self.my_lineedit.setMinimumWidth(250)
        self.my_lineedit.selectAll()
        self.my_lineedit = QLineEdit("")
        self.my_lineedit.setMinimumWidth(150)
        self.setLayout(vbox)
        self.label1 = QLabel('What do you want to open?')
        self.line_edit = QLineEdit(self)

        vbox.addWidget(self.label1)
        vbox.addWidget(self.line_edit)

        self.my_btn2 = QPushButton("Submit")
        vbox.addWidget(self.my_btn2)

        self.my_lbl3 = QLabel('')

        self.line_edit.text()

        self.my_btn2.clicked.connect(self.on_click3)

        vbox.addWidget(self.my_lbl3)

        self.text = QLabel(url)
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.text)
        title = "Commands"
        self.setWindowTitle(title)
        self.setGeometry(0, 0, 200, 200)
        self.setLayout(self.layout)
        user = self.line_edit.text()

    @Slot()
    def on_click3(self):  # we
        if ((self.line_edit.text() == "camera") or (self.line_edit.text() == "Camera")):
            print("working on it")
        else:
            # driver = None
            # while not driver:
            #     try:
            #         driver = webdriver.Chrome()
            #         driver.get(f"https://{self.line_edit.text()}.com")
            #         time.sleep(5000)
            #     except NoSuchElementException:
            #         driver = webdriver.Chrome()
            #         driver.get(f"https://{self.line_edit.text()}.edu")
            #         time.sleep(5000)
            driver = webdriver.Chrome()
            driver.get(f"https://{self.line_edit.text()}.com")
            time.sleep(5000)


class Window(QWidget):
    def __init__(self):
        super().__init__()

        title = "Jarvis"  # name of the "Jarvis"
        self.setGeometry(0, 0, 600, 600)
        self.setWindowTitle(title)
        self.setWindowIcon(QIcon('images/mic.png'))  # icon next to name of GUI

        vbox = QVBoxLayout()

        self.my_btn = QPushButton("Help")
        self.my_lineedit = QLineEdit("")
        self.my_lineedit.selectAll
        self.my_lbl = QLabel('')
        self.my_btn.clicked.connect(self.on_click)

        self.my_lineedit.setMinimumWidth(250)
        self.setLayout(vbox)
        self.my_btn1 = QPushButton("Text")
        self.my_lbl1 = QLabel('')
        self.my_btn1.clicked.connect(self.on_click1)

        self.sbutton = QPushButton("Mic")
        self.sbutton.clicked.connect(self.web_app)
        label = QLabel(self)
        gif = QMovie("wave.gif")  # allows the gif to show
        label.setMovie(gif)  # sets the gif
        vbox.addWidget(label)
        vbox.addWidget(self.my_btn1)
        vbox.addWidget(self.my_lbl1)
        vbox.addWidget(self.my_btn)
        vbox.addWidget(self.my_lbl)
        vbox.addWidget(self.sbutton)
        # create a QPushButton widget

        self.setLayout(vbox)

        # self.gif.setScaledContent(True)
        gif.start()  # allows the gif to start/play

    # next part of gui code - add button / search bar, add welcome animation
    @Slot()
    def on_click(self):
        self.my_lbl.setText('What can I help you with?')
        self.new_win = NewWindow(self.my_btn)
        self.new_win.show()
        self.repaint

    @Slot()
    def on_click1(self):
        vbox = QVBoxLayout()
        self.my_lbl1.setText('Say a command')

        self.new_win = NewWindow1(self.my_btn1)
        self.new_win.show()
        vbox.addWidget(self.my_lineedit)
        self.my_lineedit = QLineEdit("")
        self.my_lineedit.setMinimumWidth(250)
        self.my_lineedit.selectAll()

        vbox.addWidget(self.my_lineedit)
        vbox.addWidget(self.my_btn)
        self.my_combo_box = QComboBox()


    @Slot()
    def web_app(app_name):
        # create a speech recognition object
        r = sr.Recognizer()

        # listen for user input
        with sr.Microphone() as source:
            print("Say the name of the web app you want to open:")
            audio = r.listen(source)

        # recognize user input
        try:
            web_app_name = r.recognize_google(audio)
            print(f"You said: {web_app_name}")
        except sr.UnknownValueError:
            print("Could not understand audio")
            return
        except sr.RequestError as e:
            print(f"Error requesting results from Google Speech Recognition service; {e}")
            return

        # open the desired web app in a web browser
        driver = webdriver.Chrome()
        driver.get(f"https://{web_app_name}.com")




app = QApplication([])
window = Window()
window.show()
sys.exit(app.exec())
