import paramiko

def file_transfer(hostname,username,password,filename,port=22):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=hostname,username=username,password=password,port=22)

    stdin,stdout,stderr = ssh.exec_command('ls')
    output = stdout.readlines()
    print(output)

    # Transferring files from remote server to local server
    sftp_client = ssh.open_sftp()
    print(dir(sftp_client))
    sftp_client.get('/root/'+filename,'sample_file.py')
    print('File transferred successfully')

    sftp_client.put('sample_file.py','sample.py')
    print('File sent from source to destination successful')
    sftp_client.close()
    ssh.close()