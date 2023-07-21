import paramiko
import psutil
import time

# SSH连接信息
host = 'your_virtual_machine_ip'
port = 22
username = 'your_username'
password = 'your_password'

# 本地网站项目压缩文件路径和远程目标路径
local_project_zip = 'path/to/your/project.zip'
remote_project_path = '/var/www/html'

# 创建SSH客户端
ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# 连接到虚拟服务器
ssh_client.connect(host, port, username, password)

# 创建SFTP客户端
sftp_client = ssh_client.open_sftp()

# 上传网站项目压缩文件到服务器
sftp_client.put(local_project_zip, remote_project_path)

# 解压网站项目
unzip_command = f'unzip {remote_project_path}/project.zip -d {remote_project_path}'
ssh_client.exec_command(unzip_command)

# 设置index.html为主页
index_html_command = f'ln -sf {remote_project_path}/index.html {remote_project_path}/index.html'
ssh_client.exec_command(index_html_command)

# 关闭连接
sftp_client.close()
ssh_client.close()

# 在浏览器中打开网站
website_url = f'http://{host}/index.html'
# 调用你所用的浏览器启动命令，如下是在 Windows 上使用 Chrome 浏览器的示例
browser_command = f'chrome {website_url}'
import subprocess
subprocess.Popen(browser_command, shell=True)

# 循环监测服务器内存使用，并保存至变量
def monitor_memory():
    while True:
        memory_usage = psutil.virtual_memory().percent
        # 在这里可以保存 memory_usage 到你的变量 myvar 中，或进行其他操作
        time.sleep(5)  # 5秒钟监测一次内存

# 终止服务器的函数
def terminate_server():
    # 在这里编写终止服务器的代码，例如发送一个终止命令给服务器或关闭服务器进程等

# 在另一个线程中启动内存监测函数
import threading
mem_thread = threading.Thread(target=monitor_memory)
mem_thread.start()
