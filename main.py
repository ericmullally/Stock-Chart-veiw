
import sys
from PySide6.QtWidgets import QMainWindow, QApplication
from ui_files.chartGraph import Ui_MainWindow

class Window(QMainWindow):
    def __init__(self) -> None:
        super(Window, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)





if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
