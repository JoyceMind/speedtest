import psutil, time
import os
#检擦在工作的线路名称，其实只有以太网1在工作
target_lines = ['以太网', 'WLAN']
turned_on_lines = []
for net_name, info in psutil.net_if_stats().items():  # snicstats class
    '''
    print(net_name,info)
    以太网 snicstats(isup=True, duplex=<NicDuplex.NIC_DUPLEX_FULL: 2>, speed=100, mtu=1500, flags='')
    '''
    if info.isup == True:
        turned_on_lines.append(net_name)
avaliable_line = list(set(turned_on_lines) & set(target_lines))   #['以太网']

#计算网速
def get_net_io(Networked_Line, Step_Time=1.0):

    before_rec = psutil.net_io_counters(pernic=True)[Networked_Line].bytes_recv #t时刻接受的字节数
    before_sent = psutil.net_io_counters(pernic=True)[Networked_Line].bytes_sent  # t时刻发送的字节数

    time.sleep(Step_Time)
    after_rec = psutil.net_io_counters(pernic=True)[Networked_Line].bytes_recv #t+Step_Time之后接受到的字节数
    after_sent = psutil.net_io_counters(pernic=True)[Networked_Line].bytes_sent #t+Step_Time之后发送的字节数

    speed_rec = (after_rec - before_rec) / 1024/1024  # 下载速度 KB/s
    speed_sent = (after_sent - before_sent) / 1024  # 上传速度KB/s

    return "下载速度：%.2f M/s" % speed_rec,"上传速度：%.2f K/s" % speed_sent

# log_path = os.getcwd() + '/monitor_network_log.txt'
# with open(log_path, 'w+', encoding='utf8') as f:
#     while 1:
#         result = get_net_io(avaliable_line[0], Step_Time=1.0)
#         with open(log_path, 'a', encoding='utf8') as f:
#             f.write(time.strftime("%Y-%m-%d--%H:%M:%S", time.localtime()) + str(result) + '\n')
#         print(time.strftime("%Y-%m-%d--%H:%M:%S", time.localtime()) + str(result) + '\n')


'''
我们使用的QQ、Word、甚至是输入法等，每个独立执行的程序在系统中都是一个进程。
而每个进程中都可以同时包含多个线程，例如，QQ是一个聊天软件，但它的功能有很多，如收发信息、播放音乐、查看网页和下载文件等，
这些工作可以同时运行并且互不干扰，这就是使用了线程的并发机制，我们把QQ这个软件看作一个进程，而它的每一个功能都是一个可以独立运行的线程
'''