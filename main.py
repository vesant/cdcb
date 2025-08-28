from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic

import sys
import platform

class MainApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(400, 500) # makes the forms look like 'portrait'
        uic.loadUi("mainUI.ui", self)

        # Verify OS
        self.pushButton_osLookup.clicked.connect(self.lookup_os)
        #
        # store current OS
        self.current_os = None
    
    def lookup_os(self):
            # extract OS name
            os_name = platform.system()  # 'Windows', 'Linux' or 'Darwin'
            #
            # 'Darwin' to 'macOS'
            if os_name == "Darwin":
                os_name = "macOS"
            #
            # store current OS in class variable
            self.current_os = os_name
            #
            # update label
            self.label_os.setText(f"OS: ºç{os_name}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec_())