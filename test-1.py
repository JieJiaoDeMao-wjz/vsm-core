import paramiko

# 服务器的SSH连接信息
host = 'your_server_hostname'
port = 22
username = 'your_username'
password = 'your_password'

# 本地文件和远程目标路径
local_file = 'path/to/your/file'
remote_path = '/path/on/server'

# 创建SSH客户端
ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# 连接到服务器
ssh_client.connect(host, port, username, password)

# 创建SFTP客户端
sftp_client = ssh_client.open_sftp()

# 上传本地文件到服务器
sftp_client.put(local_file, remote_path)

# 创建交互式shell终端
shell = ssh_client.invoke_shell()

# 交互式操作示例
shell.send('ls\n')
output = shell.recv(1024).decode()
print(output)

# 关闭连接
sftp_client.close()
ssh_client.close()
