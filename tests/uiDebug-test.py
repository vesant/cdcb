from PyQt5 import QtWidgets
from debugTest_ui import Ui_MainWindow

class MainApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # test for button click event
        self.ui.pushButton.clicked.connect(self.say_hello)

    def say_hello(self):
        self.ui.plainTextEdit.setPlainText("Hello world")

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainApp()
    window.show()
    app.exec_()
