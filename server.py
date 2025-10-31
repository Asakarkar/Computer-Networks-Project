import socket

HOST = '0.0.0.0'
PORT = 12345

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(1)
print(f"[+] Server listening on port {PORT}")

conn, addr = server.accept()
print(f"[+] Connected by {addr}")

while True:
    msg = conn.recv(1024).decode()
    if msg.lower() == 'exit':
        print("[!] Client disconnected.")
        break
    print(f"[Client]: {msg}")
    reply = input("You: ")
    conn.send(reply.encode())

conn.close()
