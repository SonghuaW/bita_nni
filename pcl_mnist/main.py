import subprocess
import threading
import sys
import time

class MyThread(threading.Thread):
    def run(self) -> None:
        while True:
            time.sleep(60)
            print(time.ctime(), '[INFO]: Experiment is still running')
            logDir = '/home/nni'
            f = open(logDir + '/log.txt', 'a')
            sys.stdout = f
            sys.stderr = f
            status, output = subprocess.getstatusoutput("nnictl experiment show")
            file = logDir + '/' + output[output.find('id') + 5:output.find('id') + 13] + '/log/nnimanager.log'
            nnilog = open(file, mode='r').read()
            if nnilog.find('Experiment done') != -1 :
                print(time.ctime(), '[INFO]: Experiment done')
                return
p = MyThread()
p.start()
p.join()
