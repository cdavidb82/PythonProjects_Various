import socket
import socketserver

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip = socket.gethostbyname(socket.gethostname())
port = 1234
address = (ip, port)
server.listen(1)

# no of connections = cno of clients that can connect to the server at one time
print(f'Started listening on {ip}:{port}')
client, addr = server.accept()
print(f'Got a connection at {addr[0]}:{addr[1]}')
while True:
    data = client.recv(1024)
    print(f'Received {data} from {client}')
    print('processing data....\n')
    if(data =='Hello Server'):
        client.send('Hello client')
        print('Processing is done...\n Reply sent')
    elif(data=='disconnect'):
        client.send('Goodbye')
        client.close()
        break
    else:
        client.send('Invalid data')
        print("Processing done invalid data \n Reply sent")
