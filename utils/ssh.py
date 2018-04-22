# -*- coding: utf-8 -*-

import paramiko
import sys
from scp import SCPClient
import time
import random

class sshObject():
    def __init__(self, ipAddress=None, user=None, password=None, port=22, ssh_key=None):
        self.ipAddress = ipAddress
        self.user = user
        self.password = password
        self.ssh_key = ssh_key
        self.port = port

    def get_ipAddress(self):
        return self.ipAddress

class SSH():
    def __init__(self, sshObject=None):
        self.sshObject = sshObject

    def scp_put(self, sshObject, source, destination):
        ssh = self.ssh(sshObject)
        scp = SCPClient(ssh.get_transport())

        scp.put(source, destination)
        #scp.get('/tmp/test2.txt')
        scp.close()

    def ssh(self, sshObject):

        try:

            ssh = paramiko.SSHClient()

            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(hostname=sshObject.ipAddress, username=sshObject.user, password=sshObject.password,
                        port=sshObject.port)
            return ssh

        except Exception as e:
            print('*** Connect failed: ' + str(e))
            sys.exit(1)

    def run_command(self, command):
        ssh = self.ssh(self.sshObject)

        ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(command)
        if ssh_stdout:
            return ssh_stdout.read()

if __name__ == "__main__":
    print("loadding")