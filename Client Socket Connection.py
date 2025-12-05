import socket

def start_client(host="127.0.0.1", port=65432):
    """
    Connect to the TCP server and exchange messages with proper
    error handling for inactive or unreachable servers.
    """

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Optional: set timeout so connect won't hang indefinitely
    client_socket.settimeout(5)

    try: # Start of main try block to handle connection-related errors
        print(f"Connecting to server at {host}:{port}...")
        client_socket.connect((host, port))
        print("Connected successfully!\n")

        # Communication loop
        while True: #This will start a communication loop until the client type 'EXIT'
            message = input("Enter message to send (type 'exit' to quit): ")

            if message.lower() == "exit":
                print("Closing connection...")
                break # This will exit the loop

            try:
                # Send message
                client_socket.sendall(message.encode("utf-8"))
            except socket.error as e:
                print(f"[SEND ERROR] Failed to send data: {e}")
                break #This will exit the loop

            try: 
                # Receive response, if there is no response, it will close the connection
                response = client_socket.recv(1024)
                if not response:
                    print("[INFO] Server closed the connection.")
                    break

                print(f"Server replied: {response.decode('utf-8')}\n")

            except socket.error as e:
                print(f"[RECV ERROR] Failed to receive data: {e}")
                break
    #Code below will trigger if there is no server running or refusing to connect
    #In addition, if the connection timed out - one of them is inactive.                
    except ConnectionRefusedError:
        print("[ERROR] Cannot connect — the server is not running or refusing connections.")
    except socket.timeout:
        print("[ERROR] Connection timed out — the server may be inactive.")
    except socket.error as e:
        print(f"[SOCKET ERROR] {e}")
    except Exception as e:
        print(f"[UNEXPECTED ERROR] {e}")
    #Code below will always exceutes even if the connection is successful or not. 
    #Always close socket.
    finally:
        try:
            client_socket.close()
        except:
            pass
        print("Client disconnected.")


if __name__ == "__main__":
    start_client()
