import socket

def create_client():
    client = socket.socket()
    client.connect('10.1.10.120', 1234)
    return client

def communicate(client, data):
    try:
        client.send(data.encode())
        response = client.recv(1024).decode()
        print(response)
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    client = create_client()
    messages = ["salhfdskhf", 'Hello Server', "asjhfd"]
    for message in messages:
        communicate(client, message)
    client.close()

if __name__ == '__main__':
    main()

