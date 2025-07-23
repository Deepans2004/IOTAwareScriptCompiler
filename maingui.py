import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton
from PyQt5.QtCore import QThread, pyqtSignal
from speech import SpeechWorker

class MainWindow(QWidget):
    update_status = pyqtSignal(str)  # Signal from thread to GUI

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Voice Command GUI")
        self.setGeometry(300, 300, 300, 200)

        self.layout = QVBoxLayout()

        self.label_command = QLabel("Say something...", self)
        self.label_status = QLabel("Light Status: OFF", self)

        self.btn_start = QPushButton("Start Listening", self)
        self.btn_start.clicked.connect(self.start_listening)

        self.layout.addWidget(self.label_command)
        self.layout.addWidget(self.label_status)
        self.layout.addWidget(self.btn_start)

        self.setLayout(self.layout)

        # Thread setup
        self.thread = QThread()
        self.worker = SpeechWorker()
        self.worker.moveToThread(self.thread)

        # Connect signals and slots
        self.thread.started.connect(self.worker.run)
        self.worker.result.connect(self.update_gui)
        self.worker.finished.connect(self.thread.quit)

    def start_listening(self):
        self.thread.start()

    def update_gui(self, command):
        self.label_command.setText(f"Command: {command}")
        if "turn on the light" in command.lower():
            self.label_status.setText("Light Status: ON")
        elif "turn off the light" in command.lower():
            self.label_status.setText("Light Status: OFF")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
