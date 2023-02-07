"""
Server receiver buffer is char[256]
If correct, the server will send a message back to you saying "I got your message"
Write your socket client code here in python
Establish a socket connection -> send a short message -> get a message back -> ternimate
use python "input->" function, enter a line of a few letters, such as "abcd"
"""
import socket
HOST = "127.0.0.1"
PORT = 10000
def main():
    # TODO: Create a socket and connect it to the server at the designated IP and port
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))

    # TODO: Get user input and send it to the server using your TCP socket
        user_input = input("please enter your input: ")
        inp = bytes(user_input, 'utf-8')
        s.sendall(inp)
   # TODO: Receive a response from the server and close the TCP connection
        data = s.recv(1024)
        print(data)
        pass


if __name__ == '__main__':
     main()
