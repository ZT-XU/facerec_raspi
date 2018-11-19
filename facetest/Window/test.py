import socket, time, struct, os, threading
#import sqlite3

host = ''
port = 5555
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 定义socket类型
s.bind((host, port))  # 绑定需要监听的Ip和端口号，tuple格式
s.listen(1)


def conn_thread(connection, address):
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

                # 获取当前时间
                localtime = time.time()
                # 获取地址
                # if(address == ''):
                # location = 'netlab_530'
                location = 'netlab_530'
                # 构造文件路径
                filepath = '1'+'.jpg'
                # 将文件名加入链表
                #cur = con.cursor()
                #for t in [(location,localtime)]:
                    #cur.execute("INSERT INTO image (location,localtime) \ VALUES (?,?)",t)
                #con.commit()
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
                # connection.close()
            i += 1
        except socket.timeout:
            connection.close()
            #con.close()



def main():
    while True:
        print("开始接收图片")
        connection, address = s.accept()
        print('Connected by ', address)
        thread = threading.Thread(target=conn_thread, args=(connection, address))  # 使用threading也可以
        thread.start()
        # threading.start_new_thread(conn_thread, (connection, address))

    s.close()


if __name__ == '__main__':
    main()
