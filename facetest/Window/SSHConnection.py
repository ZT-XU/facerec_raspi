import paramiko

class SSHConnection(object):
    def __init__(self, username, hostname, password):
        super().__init__()

        self._host = hostname
        self._port = 22
        self._username = username
        self._password = password
        self._sftp = None
        self._client = None
        self.chan = None
        self._connect()

    def _connect(self):
        transport = paramiko.Transport((self._host, self._port))
        transport.connect(username=self._username, password=self._password)
        self._transport = transport


    def download(self, remotepath, localpath):
        if self._sftp is None:
            self._sftp = paramiko.SFTPClient.from_transport(self._transport)
        self._sftp.get(remotepath, localpath)

    def put(self, localpath, remotepath):
        if self._sftp is None:
            self._sftp = paramiko.SFTPClient.from_transport(self._transport)
        self._sftp.put(localpath, remotepath)

    def exec_command(self, command):
        if self._client is None:
            self._client = paramiko.SSHClient()
            self._client._transport = self._transport

        stdin, stdout, stderr = self._client.exec_command(command)
        data = stdout.read().decode()
        if len(data) > 0:
            return data
        err = stderr.read()
        if len(err) > 0:
            print(err.strip())
            return err

    def send_command(self,char):
        if self._client is None:
            self._client = paramiko.SSHClient()
            self._client._transport = self._transport
        self.chan = self._client.invoke_shell()
        self.chan.send(char)



    def close(self):
        if self._transport:
            self._transport.close()
        if self._client:
            self._client.close()

if __name__ == "__main__":
    conn = SSHConnection('pi','192.168.1.4','1')
    conn.exec_command('python3 /home/pi/1.py')
    #conn.exec_command('exit')
    #conn.exec_command('python3 -m /home/pi/Project/__pycache__/data_create.cpython-35.pyc')
    #conn.exec_command('python3 /home/pi/Project/__pycache__/data_create.cpython-35.pyc')