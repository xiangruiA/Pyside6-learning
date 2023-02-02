import sys
from PySide6.QtWidgets import QLabel,QPushButton,QApplication
from PySide6.QtCore import Slot
# slot 槽口
# 创建一个在终端中展示消息的slog
#
@Slot()  # 装饰函数 可以避免一些奇怪的错误
def say_hello():
    print(" hello I'm grit")

app = QApplication(sys.argv)
button = QPushButton("this is button")
# 在展示button 这个按键之前，我们必须要把 say_hello()函数与其进行连接
# button.click().connect(say_hello)
button.clicked.connect(say_hello)
button.show()

app.exec_()
