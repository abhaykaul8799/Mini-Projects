import socket

try:

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # AF_INET -> IPv4 and SOCK_STREAM -> TCP Protocol
    ip = "127.0.0.1" # Localhost IP
    port = 9999
    sock.connect((ip,port)) # Connect to IP and port
    print("Connected to Server!")

    while True:

        msg = input("Client>>> ").strip() #Take message from client
        sock.send(msg.encode()) #Send message to server
        msg = msg.lower()
        if msg=="quit" or msg == "exit":
            print("Connection Closing")
            break
            sock.close()
        msg = sock.recv(1024).decode() # Receive message from server
        print("Server>>> "+msg) # Print Message
        if msg=="quit" or msg == "exit":
            print("Connection Closing")
            sock.close()
            break

except Exception as e:

    print("Caught exception: ",e)