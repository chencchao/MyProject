from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtWidgets
from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication
import sys
#
class ui_dome(QDialog):
    def __init__(self):
        super(ui_dome,self).__init__()
        uic.loadUi('ui_dome.ui',self)

        self.pushButton1.clicked.connect(self.onClicke1)
        self.pushButton2.clicked.connect(self.onClicke2)



    def onClicke1(self):
        self.text1.setText("1111")

    def onClicke2(self):
        self.text1.clear()



def shw():
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    app = QtWidgets.QApplication(sys.argv)
    my = ui_dome()
    my.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    shw()