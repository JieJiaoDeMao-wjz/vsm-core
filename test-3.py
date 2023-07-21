import paramiko

# SSH连接信息
host = 'your_virtual_machine_ip'
port = 22
username = 'your_username'
password = 'your_password'

# 本地Django项目目录和远程目标路径
local_django_project = 'path/to/your/django_project'
remote_django_path = '/path/on/server'

# 创建SSH客户端
ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# 连接到虚拟服务器
ssh_client.connect(host, port, username, password)

# 创建SFTP客户端
sftp_client = ssh_client.open_sftp()

# 上传Django项目文件到服务器
sftp_client.put(local_django_project, remote_django_path, recursive=True)

# 关闭连接
sftp_client.close()
ssh_client.close()
