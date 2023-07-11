from PyQt5.QtCore import QUrl, QObject
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QToolBar, QLineEdit
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtNetwork import QNetworkRequest
from PyQt5.QtGui import QColor
from PyQt5.QtCore import Qt
import os
import requests
import json
from PyQt5.QtCore import QTimer
import keyboard

class WebBrowser(QMainWindow):
    def __init__(self):
        super().__init__()

        self.exam_id = ""

        self.setWindowTitle("No Cheating App")

        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setWindowState(Qt.WindowFullScreen)

        # Create a web view
        self.webview = QWebEngineView()

        # Set the web view as the central widget
        self.setCentralWidget(self.webview)

        # Create a layout for the buttons and text field
        layout = QVBoxLayout()

        # Create a text field for exam_id
        self.exam_id_field = QLineEdit()
        self.exam_id_field.setPlaceholderText("Enter exam ID")
        self.exam_id_field.setMaximumWidth(100)  # Set maximum width
        layout.addWidget(self.exam_id_field)

        # Create a close button
        close_button = QPushButton("Close")
        close_button.setStyleSheet("background-color: red; color: white;")
        close_button.setMaximumWidth(100)  # Set maximum width
        close_button.clicked.connect(self.close)
        layout.addWidget(close_button)

        # Create an open button
        open_button = QPushButton("Open")
        open_button.clicked.connect(self.open_page)
        open_button.setMaximumWidth(100)  # Set maximum width
        layout.addWidget(open_button)

        # Create a widget to hold the buttons and text field
        widget = QWidget()
        widget.setLayout(layout)

        # Create a toolbar
        toolbar = QToolBar()
        toolbar.addWidget(widget)
        self.addToolBar(toolbar)

        self.update_url_timer = QTimer()
        self.update_url_timer.timeout.connect(self.update_current_url)
        self.start = False
        self.update_url_timer.start(100)  # Update every 100 milliseconds
        keyboard.block_key('windows')
        # keyboard.block_key('ctrl')
        keyboard.block_key('esc')
        # keyboard.block_key('alt')
        # keyboard.block_key('delete')


        

    def update_current_url(self):
        if self.start:
            self.exam_id = self.exam_id_field.text()
            self.base_url = self.webview.url().toString()
            if self.base_url.strip() == 'http://localhost:4200/dashboard' or self.base_url.strip() == 'http://localhost:4200/courses' :
                self.base_url = f'http://localhost:4200/exams/attempt/{self.exam_id}'
                url = QUrl(self.base_url)
                request = QNetworkRequest(url)
                self.webview.load(request.url())
                

    def open_page(self): 
        self.exam_id = self.exam_id_field.text()
        self.base_url = f'http://localhost:4200/exams/attempt/{self.exam_id}'
        url = QUrl(self.base_url)
        request = QNetworkRequest(url)
        if(len(self.exam_id.strip()) != 0) :
            self.webview.load(request.url())
            self.start = True
        

if __name__ == '__main__':
    os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    os.environ["QT_SCREEN_SCALE_FACTORS"] = "{<screen_identifier>: <scale_factor>, ...}"
    os.environ["QT_SCALE_FACTOR"] = "<scale_factor>"
    app = QApplication([])
    browser = WebBrowser()
    browser.showFullScreen()
    app.exec_()
