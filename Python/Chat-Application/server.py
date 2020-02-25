import socket

try:

    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM) # AF_INET -> IPv4, SOCK_STREAM -> TCP
    ip = "127.0.0.1" # Localhost Address
    port = 9999
    sock.bind((ip,port))
    sock.listen(5)
    print("Server is Running!")
    conn, addr = sock.accept()
    
    print("Client connected to server!")

    while True:
        msg = conn.recv(1024).decode()
        print("Client>>> "+msg)
        msg = msg.lower()
        if msg=="quit" or msg == "exit":
            print("Connection Closing")
            conn.close()
            break
        msg = input("Server>>> ")
        conn.send(msg.encode())
        msg = msg.lower()
        if msg=="quit" or msg == "exit":
            print("Connection Closing")
            conn.close()
            break

except Exception as e:
    print("Caught error: ",e)