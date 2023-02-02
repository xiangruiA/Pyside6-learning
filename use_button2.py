import sys
from PySide6.QtWidgets import QPushButton,QApplication

def cal_f():
    print("It has been called")

app = QApplication(sys.argv)
button = QPushButton("call it")
button.clicked.connect(cal_f)
button.show()
app.exec_()
