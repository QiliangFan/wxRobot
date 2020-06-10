import itchat
from threading import Thread
import time
from .events import *


class EpidemicPrevention:
    def __init__(self, enableCmdQR = False):
        itchat.auto_login(hotReload=True, statusStorageDir="itchat.pk1", enableCmdQR=enableCmdQR)
        Thread(target=itchat.run).start()
        self.set_timer()

    def send_warning(self):
        msg = "[epidemic prevention]填写防疫信息啦! \n [我是防疫信息填报小机器人, 将于晚上12:00和" \
              "中午11:00分别发送一次通知(*∩_∩*)]🤣"
        send_warning_to_group(msg)

    def set_timer(self):
        flag = False
        while True:
            t = time.localtime(time.time())
            print(t)
            if ((0 <= t.tm_hour <= 1) or (11 <= t.tm_hour <= 12)) and not flag:
                flag = True
                self.send_warning()
            elif not ((0 <= t.tm_hour <= 1) or (11 <= t.tm_hour <= 12)):
                flag = False

            # if (15 <= t.tm_hour <= 16) and not flag:
            #     flag = True
            #     self.send_warning()
            # elif not (15 <= t.tm_hour <= 16):
            #     flag = False
            time.sleep(600)