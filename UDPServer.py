import socket

client = socket.socket()
client.connect('10.1.10.120', 1234)


def communicate(data):
    client.send(data)
    print(client.recv(1024))
    return


if __name__ == '__main__':
    communicate("salhfdskhf")
    communicate('Hello Server')
    communicate("asjhfd")

