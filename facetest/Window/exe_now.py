import sys , os, pexpect
import socket, struct, threading
from subprocess import Popen, PIPE

host = ''
port = 5555
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 定义socket类型
s.bind((host, port))  # 绑定需要监听的Ip和端口号，tuple格式
s.listen(5)

def conn_thread(connection, address,child):
    #con = sqlite3.connect('test.db')
    location = ''
    i = 0
    while True:
        try:
            connection.settimeout(600)
            fileinfo_size = struct.calcsize('128sl')
            buf = connection.recv(fileinfo_size)
            #print(buf)
            if buf:  # 如果不加这个if，第一个文件传输完成后会自动走到下一句
                filename, filesize = struct.unpack('128sl', buf)
                print("照片大小:"+str(filesize))
                if filesize< 0 or filesize > 2432075:
                    # da = connection.recv()
                    continue
                filename = filename.decode().strip('\00')
                # print(filename)
                #filename = os.path.join('e:\\', ('new_' + filename))
                print('file new name is %s, filesize is %s' % (filename, filesize))

                # 构造文件路径
                filepath = 'frame'+'.jpg'
                file = open(filepath,'wb')
                # file = open('./face/'+filename, 'wb')
                print('stat receiving...filesize:' + str(filesize))
                recvd_size = 0  # 定义接收了的文件大小
                while recvd_size != filesize:
                    if filesize - recvd_size >= 1024:
                        rdata = connection.recv(1024)
                        recvd_size += len(rdata)
                    elif filesize - recvd_size <1024 and filesize - recvd_size > 0:
                        print(filesize - recvd_size)
                        rdata = connection.recv(filesize - recvd_size)
                        recvd_size += len(rdata)
                    file.write(rdata)
                file.close()
                print('receive done')
            i += 1
            with open("proceed.txt", "r") as f:
                b = f.read()
            if "F" in b:
                child.sendcontrol("c")
                s.close()
                break
        except socket.timeout:
            connection.close()
            #con.close()



def main():
    child = pexpect.spawn('/usr/bin/ssh pi@192.168.1.4', encoding="utf-8")
    child.expect("password")
    child.sendline("1")
    child.sendline("python3 /home/pi/Project/face_distinguish.py")
    while True:
        print("开始接收图片")
        connection, address = s.accept()
        print('Connected by ', address)
        with open("proceed.txt","w") as f:
            f.write("True")
        thread = threading.Thread(target=conn_thread, args=(connection, address,child))  # 使用threading也可以
        thread.start()
        p1 = Popen("/home/xzt/facetest/exe_now_before.sh", stdout=PIPE, close_fds=True)
        p = Popen("/home/xzt/facetest/image.sh", stdout=PIPE, close_fds=True)
        # threading.start_new_thread(conn_thread, (connection, address))
        with open("proceed.txt", "r") as f:
            b = f.read()
        if "F" in b:
            break
    thread.join()

if __name__ == '__main__':
    main()
