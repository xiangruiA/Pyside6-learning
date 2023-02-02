import sys
from PySide6.QtWidgets import QApplication, QLabel
# 创建app 实例
#通常不需要传递任何参数
# app = QApplication([])
app = QApplication(sys.argv)  #sys.argv其实就是一个列表，里边的项为用户输入的参数
label = QLabel("hello word") # 创建标签
label.show()  #展示标签
app.exec_()  #执行 QT循环


