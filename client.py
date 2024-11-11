import sys
import socket
from random import randint

# Set up hosts and ports
HOST = socket.gethostbyname(socket.gethostname())
PORT = 9876
ADDR = (HOST, PORT)


def send_request(user_input):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(ADDR)

    # Format and send the user input as a request
    user_input = " ".join(f"{key}={value}" for key, value in user_input.items())
    client_socket.send(user_input.encode())

    # Receive data in chunks and check for the end marker
    response = ""
    while True:
        chunk = client_socket.recv(1024).decode()
        if "END" in chunk:
            response += chunk.replace("END", "")
            break
        response += chunk

    client_socket.close()
    return response




if __name__ == "__main__":

    # [user] [command] [acct_num] [amount]
    if len(sys.argv) < 3:
        print("Usage: python3 client.py [user] [command] [acct_num] [amount]")
        sys.exit(0)

    # parse that received user input
    user = sys.argv[1]
    command = sys.argv[2]
    acct_num = int(sys.argv[3]) if len(sys.argv) > 3 and sys.argv[3].isdigit() else 0
    amount = int(sys.argv[4]) if len(sys.argv) > 4 and sys.argv[4].isdigit() else 0

    user_input = {
        'user': user,
        'command': command,
        'acct_num': acct_num,
        'amount': amount
    }

    # use this function to send user_input to the server
    response = send_request(user_input)
    print('******************************************************************')
    print(response)
    print('******************************************************************')
