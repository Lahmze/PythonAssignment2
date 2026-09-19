import socket

HOST = '127.0.0.1'
PORT = 65432

def start_server():
    try:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        server_socket.bind((HOST, PORT))
        server_socket.listen(1)
        print(f"Server listening on {HOST}:{PORT}...")

        while True:
            try:
                conn, addr = server_socket.accept()
                with conn:
                    print(f"Connected by {addr}")
                    data = conn.recv(1024)
                    if data:
                        message = data.decode('utf-8')
                        print(f"Received message: {message}")
                        conn.sendall(b"Message received by server.")
                    else:
                        print("No data received.")
            except ConnectionResetError:
                print("Connection was reset by the client.")
            except socket.error as e:
                print(f"Socket error while handling client: {e}")

    except socket.error as e:
        print(f"Failed to start server: {e}")
    except KeyboardInterrupt:
        print("\nServer shutting down.")
    finally:
        server_socket.close()

if __name__ == '__main__':
    start_server()

import socket

HOST = '127.0.0.1'
PORT = 65432


def start_client():
        try:
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_socket.settimeout(5)

            try:
                client_socket.connect((HOST, PORT))
            except ConnectionRefusedError:
                print("Connection refused. Is the server running?")
                return
            except socket.timeout:
                print("Connection attempt timed out.")
                return

            message = "Hello from client!"
            client_socket.sendall(message.encode('utf-8'))
            print(f"Sent: {message}")

            try:
                response = client_socket.recv(1024)
                if response:
                    print(f"Server response: {response.decode('utf-8')}")
            except socket.timeout:
                print("Timed out waiting for server response.")

        except socket.error as e:
            print(f"Socket error: {e}")
        finally:
            client_socket.close()


if __name__ == '__main__':
        start_client()