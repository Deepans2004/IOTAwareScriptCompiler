import speech_recognition as sr
from PyQt5.QtCore import QObject, pyqtSignal

class SpeechWorker(QObject):
    result = pyqtSignal(str)
    finished = pyqtSignal()

    def run(self):
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            try:
                audio = recognizer.listen(source)
                text = recognizer.recognize_google(audio)
                self.result.emit(text)
            except Exception as e:
                self.result.emit("Error: " + str(e))
        self.finished.emit() 