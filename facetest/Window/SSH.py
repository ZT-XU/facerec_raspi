import pexpect
# SSH连接成功时的命令行交互窗口中前面的提示字符的集合
PROMPT = ['# ', '>>> ', '> ', '\$ ']
def send_command(child, cmd):
    # 发送一条命令
    child.sendline(cmd)
    child.sendline('yes')
    # 期望有命令行提示字符出现
    child.expect(PROMPT)

    # 将之前的内容都输出
    print(child.before)

def connect(user, host, password):
    # 表示主机已使用一个新的公钥的消息
    ssh_newkey = 'Are you sure you want to continue connecting'
    connStr = 'ssh ' + user + '@' + host

    ''''' 
    pexpect.spawn()和pexpect.run()依赖于Python标准库中的pty模块，而pty模块只在POSIX系统中存在，所以Windows系统上的功能有限。 
    pexpect.spawn类继承自SpawnBase类,用法如：child = pexpect.spawn('/usr/bin/ssh user@example.com')  
    process = pexpect.spawn('ftp sw-tftp')中的字符串就是要执行的程序，这里我们打开一个到 sw-tftp 服务器的 ftp 连接。  
    spawn() 中的第一个元素就是要执行的命令，除此之外还可以指定一些其他参数，比如： pexpect.spawn('ftp sw-tftp', timeout=60) 就指定了超时时间 
    process 就是 spawn() 的程序操作句柄了，之后对这个程序的所有操作都是基于这个句柄的，所以它可以说是最重要的部分。     
    '''
    # 为ssh命令生成一个spawn类的对象
    child = pexpect.spawn(connStr)

    ''''' 
    process.expect(pattern_list, timeout=-1, searchwindowsize=None) 
    # pattern_list      正则表达式列表，表示要匹配这些内容 
    # timeout           不设置或者设置为-1的话，超时时间就采用self.timeout的值，默认是30秒。也可以自己设置。 
    # searchwindowsize  功能和 spawn 上的一样 

    expect()方法是最常用的方法之一，等待子应用返回指定的字符串。 
    如果没有任何字符模式被匹配，将抛出超时异常，默认超时时间为30s 
    process.expect('[Nn]ame') 
    上面的代码表示：匹配 process 这个句柄（代表 spawn 方法的例子中我们启动的 ftp 连接）中的 name 关键字，其中 n 不分大小写。 

    '''

    # 期望有ssh_newkey字符、提示输入密码的字符出现，否则超时
    ret = child.expect([pexpect.TIMEOUT, ssh_newkey, '[P|p]assword: '])

    # 匹配到超时TIMEOUT
    if ret == 0:
        print
        '[-] Error Connecting'
        return

        # 匹配到ssh_newkey
    if ret == 1:
        # 发送yes回应ssh_newkey并期望提示输入密码的字符出现
        child.sendline('yes')
        ret = child.expect([pexpect.TIMEOUT, '[P|p]assword: '])

        # 匹配到超时TIMEOUT
    if ret == 0:
        print
        '[-] Error Connecting'
        return

        # 发送密码
    child.sendline(password)
    child.expect(PROMPT)
    return child


def main():
    host = '192.168.1.4'
    user = 'pi'
    password = '1'
    child = connect(user, host, password)
    send_command(child, 'python3 1.py')


if __name__ == '__main__':
    main()