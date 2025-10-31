import socket

HOST = input("Enter server IP: ")
PORT = 12345

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))
print("[+] Connected to server.")

while True:
    msg = input("You: ")
    client.send(msg.encode())
    if msg.lower() == 'exit':
        break
    reply = client.recv(1024).decode()
    print(f"[Server]: {reply}")

client.close()
