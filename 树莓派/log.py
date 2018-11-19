from subprocess import Popen, PIPE
from time import sleep
p = Popen("/home/pi/Project/exe.sh", stdout=PIPE, close_fds=True)
count = 0
while True:
    count += 1
    print('%s : %s' % (count, p.stdout.readline().strip()))
    if (p.stdout.readline().strip() == "Finish!!!"):
        break

