# 💬 LAN Chat Using TCP Sockets

> A beginner-friendly Computer Networks lab project demonstrating TCP-based two-way communication between two computers over a LAN.

---

## 🎯 Objective
Create a basic chat system where two computers on the same LAN can send and receive messages using TCP socket programming.

---

## 🧱 Technologies Used
- **Language:** Python 3
- **Platform:** Windows / Linux
- **Tools:** Command Line (no GUI)

---

## 🗂️ Folder Structure
```
lan_chat_project/
├── server.py      # Chat server
└── client.py      # Chat client
```

---

## 📜 How It Works

- The **server** waits for a client to connect on a specified port.
- The **client** connects to the server using its IP address.
- Both sides can exchange text messages in real-time.
- Typing 'exit' closes the connection.

---

## ⚙️ How to Run

### 🖥️ Step 1: Run the Server
```bash
python3 server.py
```
You should see:
```
[+] Server listening on port 12345
```

### 💻 Step 2: Run the Client
On another machine (same LAN) or terminal:
```bash
python3 client.py
```
Enter the server IP (e.g., 192.168.1.10).

### 💬 Step 3: Start Chatting!
```
You: Hello Server!
[Client]: Hello Client!
```

Type `exit` to end the chat.

---

## 🔍 How to Find Your IP (Server)
- **Windows:** Run `ipconfig` in Command Prompt.
- **Linux:** Run `ifconfig` or `hostname -I` in Terminal.

Use this IP for the client to connect.

---

## 🧾 Sample Output

### **Server**
```
[+] Server listening on port 12345
[+] Connected by ('192.168.1.5', 54012)
[Client]: Hi there!
You: Hello!
```

### **Client**
```
Enter server IP: 192.168.1.10
[+] Connected to server.
You: Hi there!
[Server]: Hello!
```

---

## 🚀 Future Enhancements
- Add support for **multiple clients** using threads.
- Implement **message timestamps**.
- Add a **chat log** file.
- Build a **simple GUI** using Tkinter.

---

## 👨‍💻 Contributor
| Name | Role |
|------|------|
| **Aditya (Aadi)** | Developer / CN Lab Project |
