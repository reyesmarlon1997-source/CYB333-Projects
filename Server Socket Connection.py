import socket

def start_server(host="127.0.0.1", port=65432):
    """
    Start a simple TCP server that listens for one client connection
    and exchanges messages.
    """

    # Create a TCP/IP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Bind server to given IP and port
        server_socket.bind((host, port))
        print(f"Server is listening on {host}:{port}") #This confirms the connection is a sucess.
        #Above line states that the server is connected and listening to client.

        # Listen for incoming connections (queue size = 1)
        server_socket.listen(1) #This code ensures only one line of message will be sent.
        print("Waiting for a client to connect...")

        # Accept a connection (blocking call)
        client_socket, client_address = server_socket.accept()
        print(f"Client connected from: {client_address}")

        # Communication loop this will continously recieve and send message
        while True:
            # Receive up to 1024 bytes
            data = client_socket.recv(1024)

            if not data: #this will trigger if client left or type 'EXIT'
                print("Client disconnected.") 
                break

            message = data.decode("utf-8")
            print(f"Received from client: {message}")

            # Send a response back to the client
            response = f"Server received: {message}"
            client_socket.sendall(response.encode("utf-8"))

    except socket.error as e: #This code will trigger when there is no server running
        print(f"[ERROR] Socket error: {e}")
    #Code below will always exceutes even if the connection is successful or not. 
    #Always close socket.
    finally:
        # Closing the socket.
        try:
            client_socket.close()
        except:
            pass

        server_socket.close()
        print("Server shutdown complete.")


if __name__ == "__main__": #This ensure the server only runs if this file is opened directly
    start_server() #This will start the server.
