from psutil import *
from time import *
from matplotlib.pyplot import *
from matplotlib import rcParams
from random import *
from easygui import *
import matplotlib.pyplot as plt
def plot_speed_kb(t = 0.001):
    rcParams["font.sans-serif"] = "SimHei"
    fig = figure()
    ion()

    xar = list(range(60))
    yar_recv = []
    for i in range(60):
        yar_recv.append(0)
    yar_sent = []
    for i in range(60):
        yar_sent.append(0)
    arvg_speed_recv = []
    arvg_speed_sent = []
    s1 = net_io_counters().bytes_recv
    s3 = net_io_counters().bytes_sent
    sleep(t)
    while "正在监控中":
        fig.clear()
        s2 = net_io_counters().bytes_recv
        s4 = net_io_counters().bytes_sent
        recv_speed_kb = (s2 - s1) / t / 1024/1024
        sent_speed_kb = (s4 - s3) / t / 1024/1024
        yar_recv.pop(0)
        yar_sent.pop(0)
        yar_recv.append(recv_speed_kb)
        yar_sent.append(sent_speed_kb)

        recv = 0
        arvg_speed_recv.append(recv_speed_kb)
        if len(arvg_speed_recv)>60:
            arvg_speed_recv.pop(0)
        for i in arvg_speed_recv:
            recv+=i
        arvg_recv = recv/len(arvg_speed_recv)
        arvg_line_recv = []
        for i in range(60):
            arvg_line_recv.append(arvg_recv)

        sent = 0
        arvg_speed_sent.append(sent_speed_kb)
        if len(arvg_speed_sent)>60:
            arvg_speed_sent.pop(0)
        for i in arvg_speed_sent:
            sent+=i
        arvg_sent = sent/len(arvg_speed_sent)
        arvg_line_sent = []
        for i in range(60):
            arvg_line_sent.append(arvg_sent)
        plt.title('北京时间：'+time.strftime("%Y-%m-%d--%H:%M:%S", time.localtime()), loc="center")
        plot(xar,yar_recv,label = "当前下载网速：%f MB/s"%recv_speed_kb)
        plot(xar,yar_sent,label = "当前上传网速：%f MB/s"%sent_speed_kb)

        legend(loc = "upper left")
        s1 = s2
        s3 = s4
        pause(t)

def use():
    if ynbox('是否开始监控？', '网速监控操作系统5.0', ("开始！！！对电脑网速进行严格监控","取消，再次检查系统，确保万无一失！")):
        msgbox("开始了，请就位！！！",'紧急通知','已就位！')
    else:
        msgbox("监控取消，等待下次使用！",'通知','退出监控')
        exit()

    t = enterbox(msg="监控单位时间（秒）（请输入非0实数，不输入请取消。为确保程序流畅，推荐输入范围在0.1到0.0001之间，取消或输入0都将按默认值0.001处理）:", title="网速监控操作系统5.0", strip=True, image=None, root=None)


    if t == None or t == "0":
        plot_speed_kb()
    else:
        t = float(t)
        plot_speed_kb(t)

msgbox("欢迎使用网速监控操作系统5.0！",'网速监控操作系统5.0欢迎您','开始使用')
use()