
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QHBoxLayout, QVBoxLayout, QPushButton
from PyQt5.QtCore import QTimer
from PyQt5 import QtCore, QtGui, QtWidgets
import speed4

class NetworkSpeedMonitor(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('网络速度监控')
        self.setGeometry(300, 300, 250, 150)

        # 创建标签
        self.label = QLabel('网络速度监控', self)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignVCenter)  # 设置标签文本居中

        # 创建水平布局
        layout = QHBoxLayout()
        layout.addWidget(self.label)

        # 设置布局
        self.setLayout(layout)

        # 创建定时器
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_network_speed)
        self.timer.start(1000)  # 每秒更新一次网络速度

        # 创建按钮
        self.button = QPushButton('开始监控', self)
        self.button.clicked.connect(self.start_monitoring)

        # 创建垂直布局
        layout = QVBoxLayout()
        layout.addWidget(self.button)

        # 设置布局
        self.setLayout(layout)

    def update_network_speed(self):
        # 这里可以编写获取网络速度的代码，例如使用 psutil 库获取上传和下载速度
        upload_speed = speed4.get_net_io(str('以太网'),Step_Time=1.0)[1][5:]
        download_speed = speed4.get_net_io(str('以太网'), Step_Time=1.0)[0][5:]

        # 更新网络速度标签文本
        self.label.setText('上传速度：{} ，下载速度：{} '.format(upload_speed, download_speed))

    def start_monitoring(self):
        # 开始监控网络速度
        pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = NetworkSpeedMonitor()
    #修改窗口图标
    icon=QtGui.QIcon()
    icon.addPixmap(QtGui.QPixmap('./resources/speed.ico'),QtGui.QIcon.Normal,QtGui.QIcon.Off)
    win.setWindowIcon(icon)
    win.show()
    sys.exit(app.exec_())

