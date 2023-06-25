import sys
import time
import psutil
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QHBoxLayout, QMainWindow, QWidget, QFrame, QLabel, QVBoxLayout, QGridLayout
from PyQt5.QtCore import Qt, pyqtSignal, QThread
from PyQt5.QtGui import QPixmap
from PyQt5.QtGui import QPalette, QBrush, QPixmap
import speed4


class NetWindows(QMainWindow):
    net_signal = pyqtSignal(str, str)

    def __init__(self):
        super(NetWindows, self).__init__()
        self.ui_init()
        self.thread_init()

    def ui_init(self):
        self.setWindowTitle('电脑网速监控器')
        self.resize(320,180)
        self.setWindowOpacity(1)  # 设置窗口透明度 1表示不透明
        self.setWindowFlag(Qt.WindowStaysOnTopHint)  # 窗口始终显示在最前面
        self.upload_icon = QLabel()
        # self.upload_icon.setPixmap(QPixmap('resources/upload.png'))    #上传速度图标
        self.upload_icon.setScaledContents(True)
        self.download_icon = QLabel()
        # self.download_icon.setPixmap(QPixmap('resources/download .png'))
        self.download_icon.setScaledContents(True)
        self.upload_text = QLabel()
        self.upload_text.setText('上传速度: ')
        self.download_text = QLabel()
        self.download_text.setText('下载速度: ')
        # 显示时间
        self.bjtime = QLabel()
        self.bjtime.setText(time.strftime("%Y-%m-%d--%H:%M:%S", time.localtime()))
        print(time.strftime("%Y-%m-%d--%H:%M:%S", time.localtime()))
        self.upload_lab = QLabel()
        self.download_lab = QLabel()



        self.g_layout = QGridLayout()
        self.g_layout.addWidget(self.upload_icon, 0, 0, 1, 1)
        self.g_layout.addWidget(self.download_icon, 1, 0, 1, 1)
        self.g_layout.addWidget(self.upload_text, 0, 1, 1, 1)
        self.g_layout.addWidget(self.download_text, 1, 1, 1, 1)
        self.g_layout.addWidget(self.upload_lab, 0, 2, 1, 4)
        self.g_layout.addWidget(self.download_lab, 1, 2, 1, 4)
        self.g_layout.addWidget(self.bjtime,2,0,3,8)
        self.widget = QWidget()
        self.widget.setLayout(self.g_layout)
        self.setCentralWidget(self.widget)

    def thread_init(self):
        self.net_thread = NetThread()
        self.net_thread.net_signal.connect(self.net_slot)
        self.net_thread.start(1000)

    def variate_init(self):
        self.upload_content = ''
        self.download_content = ''

    def net_slot(self, upload_content, download_content):
        self.upload_lab.setText(upload_content)
        self.download_lab.setText(download_content)

    def mousePressEvent(self, event):
        '''
        重写按下事件
        '''
        self.start_x = event.x()
        self.start_y = event.y()

    def mouseMoveEvent(self, event):
        '''
        重写移动事件
        '''
        dis_x = event.x() - self.start_x
        dis_y = event.y() - self.start_y
        self.move(self.x() + dis_x, self.y() + dis_y)


class NetThread(QThread):
    net_signal = pyqtSignal(str, str)

    def __init__(self):
        super(NetThread, self).__init__()

    def net_func(self):
        self.upload_content = speed4.get_net_io(str('WLAN'),Step_Time=1.0)[1][5:]
        self.download_content = speed4.get_net_io(str('WLAN'), Step_Time=1.0)[0][5:]

    def run(self):
        while (1):
            self.net_func()
            self.net_signal.emit(self.upload_content, self.download_content)



if __name__ == '__main__':
    app = QApplication(sys.argv)

    win = NetWindows()
    #修改窗口图标
    icon=QtGui.QIcon()
    icon.addPixmap(QtGui.QPixmap('./resources/speed3.ico'),QtGui.QIcon.Normal,QtGui.QIcon.Off)
    win.setWindowIcon(icon)
#修改窗口背景
    palette = QPalette()
    palette.setBrush(QPalette.Background, QBrush(QPixmap("resources/background.png")))
    win.setStyleSheet("QMainWindow {background-image: url('resources/background.png');}")

    # 设置窗口样式
    win.setWindowFlags(Qt.Window)

    win.show()
    netwidows = NetWindows()
    sys.exit(app.exec_())

