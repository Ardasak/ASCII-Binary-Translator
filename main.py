import binascii

from PyQt5 import QtCore
from PyQt5.QtWidgets import (
    QComboBox,
    QMenu,
    QMainWindow,
    QMessageBox,
    QWidget,
    QApplication,
    QLineEdit,
    QTextEdit,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QFileDialog,
    QHBoxLayout,
    QAction,
    QMainWindow,
)
from PyQt5.QtGui import QFont
import sys
import wx


class UI_Window(QWidget):
    def __init__(self, parent=None):
        super(UI_Window, self).__init__(parent)
        self.home()

    def home(self):

        self.durum = 1
        self.textarea1 = QTextEdit()
        self.textarea1.setStyleSheet(
            """
        QTextEdit {
        font-family: "MS Shell Dlg 2"; 
        font-size: 8.25pt; 
        font-weight: 400; 
        font-style: normal;
        padding: 0px 10px;
        background: white;
        border-style: outset;
        border-width: 2px;
        border-radius: 10px;
        border-color: gray;
}
        QTextEdit:focus{
            border-color: black;
        }
"""
        )
        self.textarea2 = QTextEdit()
        self.textarea2.setStyleSheet(
            """
        QTextEdit {
        font-family: "MS Shell Dlg 2"; 
        font-size: 8.25pt; 
        font-weight: 400; 
        font-style: normal;
        padding: 0px 10px;
        background: white;
        border-style: outset;
        border-width: 2px;
        border-radius: 10px;
        border-color: gray;
}
        QTextEdit:focus{
            border-color: black;
        }
"""
        )
        self.textarea2.setReadOnly(True)
        self.textarea1.setPlaceholderText("Text: ")
        self.textarea2.setPlaceholderText("Binary: ")
        self.switch_button = QPushButton("Switch")
        self.switch_button.setStyleSheet(
            """QPushButton{
            background-color: rgb(255,255,255);
            padding: 6px 50px;
            width: 70px;
            border-style: outset;
            border-width: 2px;
            border-radius: 10px;
            border-color: black;
            }
            
            QPushButton:hover{
                background-color: #cccccc;
            }"""
        )
        self.switch_button.clicked.connect(self.switch)
        self.label = QLabel("Text to Binary Translator")
        self.label.setFont(QFont("Arial", 15))
        self.translate_button = QPushButton("Translate")
        self.translate_button.setStyleSheet(
            """QPushButton{
            background-color: rgb(255,255,255);
            padding: 6px 50px;
            width: 70px;
            border-style: outset;
            border-width: 2px;
            border-radius: 10px;
            border-color: black;
            }
            
            QPushButton:hover{
                background-color: #cccccc;
            }"""
        )
        self.translate_button.clicked.connect(self.translate)
        self.v_layout = QVBoxLayout()
        self.yerlestir()
        self.setLayout(self.v_layout)

    def switch(self):
        if self.durum == 0:
            self.durum = 1
            self.label.setText("Text to Binary Translator")
            self.textarea1.clear()
            self.textarea2.clear()
            self.textarea1.setPlaceholderText("Text: ")
            self.textarea2.setPlaceholderText("Binary: ")
        elif self.durum == 1:
            self.durum = 0
            self.textarea1.clear()
            self.textarea2.clear()
            self.label.setText("Binary to Text Translator")
            self.textarea2.setPlaceholderText("Text: ")
            self.textarea1.setPlaceholderText("Binary: ")

    def translate(self):
        try:
            if self.durum == 0:
                deger = ""
                list = self.textarea1.toPlainText().split(" ")
                for i in list:
                    deger += i

                n = int(deger, 2)
                self.textarea2.setText(
                    n.to_bytes((n.bit_length() + 8) // 8, "big").decode()
                )
            elif self.durum == 1:
                st = self.textarea1.toPlainText()
                sonuc = bin(int(binascii.hexlify(st.encode("ascii")), 16))
                self.textarea2.setText(sonuc[2:])
        except UnicodeEncodeError:
            icon = QMessageBox.Information
            text = "An error occured."
            title = "Error!"
            detail = "This program only works with english alphabet. Check it and try again."
            msg = QMessageBox()
            msg.setIcon(icon)
            msg.setText(text)
            msg.setWindowTitle(title)
            msg.setDetailedText(detail)
            msg.exec()
        except ValueError:
            
            icon = QMessageBox.Information
            text = "An error occured."
            title = "Error!"
            detail = "Not able to read text area as binary."
            msg = QMessageBox()
            msg.setIcon(icon)
            msg.setText(text)
            msg.setWindowTitle(title)
            msg.setDetailedText(detail)
            msg.exec()
        except:
            icon = QMessageBox.Information
            text = "An error occured."
            title = "Error!"
        
            msg = QMessageBox()
            msg.setIcon(icon)
            msg.setText(text)
            msg.setWindowTitle(title)
            msg.exec()
        
    def yerlestir(self):
        h_box = QHBoxLayout()
        h_box.addStretch()
        h_box.addWidget(self.label)
        h_box.addStretch()

        self.v_layout.addLayout(h_box)

        self.v_layout.addWidget(self.textarea1)

        h_box2 = QHBoxLayout()
        h_box2.addStretch()
        h_box2.addWidget(self.switch_button)
        h_box2.addStretch()

        self.v_layout.addLayout(h_box2)

        self.v_layout.addWidget(self.textarea2)

        h_box3 = QHBoxLayout()
        h_box3.addStretch()
        h_box3.addWidget(self.translate_button)
        h_box3.addStretch()

        self.v_layout.addLayout(h_box3)


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        app = wx.App(False)

        self.width, self.height = wx.GetDisplaySize()
        self.setGeometry(
            round((self.width / 2) - 600), round((self.height / 2) - 300), 1200, 600
        )
        self.setWindowTitle("Youtube Video Downloader")
        self.startMainMenu()

    def startMainMenu(self):
        self.window = UI_Window(self)
        self.setWindowTitle("Youtube Video Downloader")
        self.setCentralWidget(self.window)
        self.showMaximized()


app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()
