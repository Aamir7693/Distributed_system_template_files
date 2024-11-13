import socket
import threading
import time
from tabulate import tabulate

# ['Alice', 'Bob', 'Charlie', 'Dave', 'Frank', 'Grace', 'Heidi','Ivan', 'John', 'Kate', 'James',
#  'Michael', 'Robert', 'William', 'David','Thomas', 'Mark', 'Steven', 'Paul', 'Kevin', 'Jason',
#  'Gary', 'Larry','Justin','Raymond','Adam','Henry','Eve']

class Bank:
    def __init__(self):
        self.accounts = [
            {'acct_num': 1001, 'acct_type': 'checking', 'init_acct_holder': 'Alice',
             'acct_holder': ['Alice', 'Jason', 'David'], 'balance': 2100, 'history': [], 'lock': threading.Lock()},
            {'acct_num': 1002, 'acct_type': 'loan', 'init_acct_holder': 'Alice',
             'acct_holder': ['Alice', 'Jason', 'David'], 'balance': -300, 'history': [], 'lock': threading.Lock()},
            {'acct_num': 1003, 'acct_type': 'checking', 'init_acct_holder': 'Bob',
             'acct_holder': ['Bob', 'Ivan', 'Kevin'], 'balance': 3500, 'history': [], 'lock': threading.Lock()},
            {'acct_num': 1004, 'acct_type': 'loan', 'init_acct_holder': 'Bob',
             'acct_holder': ['Bob', 'Ivan', 'Paul'], 'balance': -900, 'history': [], 'lock': threading.Lock()},
            {'acct_num': 1005, 'acct_type': 'checking', 'init_acct_holder': 'Charlie',
             'acct_holder': ['Charlie', 'Dave'], 'balance': 9100, 'history': [], 'lock': threading.Lock()},
            {'acct_num': 1006, 'acct_type': 'loan', 'init_acct_holder': 'Charlie',
             'acct_holder': ['Charlie', 'Dave', 'Gary'], 'balance': -3200, 'history': [], 'lock': threading.Lock()},
            {'acct_num': 1007, 'acct_type': 'checking', 'init_acct_holder': 'Dave',
             'acct_holder': ['Dave', 'Thomas', 'Henry'], 'balance': 200, 'history': [], 'lock': threading.Lock()},
            {'acct_num': 1008, 'acct_type': 'loan', 'init_acct_holder': 'Dave',
             'acct_holder': ['Dave', 'James', 'Gary'], 'balance': -300, 'history': [], 'lock': threading.Lock()},
            {'acct_num': 1009, 'acct_type': 'checking', 'init_acct_holder': 'Frank',
             'acct_holder': ['Frank', 'Grace', 'Charlie'], 'balance': 4000, 'history': [], 'lock': threading.Lock()},
            {'acct_num': 1010, 'acct_type': 'loan', 'init_acct_holder': 'Frank',
             'acct_holder': ['Frank', 'Adam', 'Steven'], 'balance': -900, 'history': [], 'lock': threading.Lock()},
            {'acct_num': 1011, 'acct_type': 'checking', 'init_acct_holder': 'Grace',
             'acct_holder': ['Grace', 'Adam', 'Heidi'], 'balance': 3000, 'history': [], 'lock': threading.Lock()},
            {'acct_num': 1012, 'acct_type': 'loan', 'init_acct_holder': 'Grace',
             'acct_holder': ['Grace', 'Robert', 'Larry'], 'balance': -100, 'history': [], 'lock': threading.Lock()},
            {'acct_num': 1013, 'acct_type': 'checking', 'init_acct_holder': 'Heidi',
             'acct_holder': ['Heidi', 'Mark', 'Kate'], 'balance': 500, 'history': [], 'lock': threading.Lock()},
            {'acct_num': 1014, 'acct_type': 'loan', 'init_acct_holder': 'Heidi',
             'acct_holder': ['Heidi', 'Ivan', 'Dave'], 'balance': -200, 'history': [], 'lock': threading.Lock()},
            {'acct_num': 1015, 'acct_type': 'checking', 'init_acct_holder': 'Ivan',
             'acct_holder': ['Ivan', 'Charlie', 'Bob'], 'balance': 5000, 'history': [], 'lock': threading.Lock()},
            {'acct_num': 1016, 'acct_type': 'loan', 'init_acct_holder': 'Ivan',
             'acct_holder': ['Ivan', 'Michael', 'Mark'], 'balance': -2100, 'history': [], 'lock': threading.Lock()},
            {'acct_num': 1017, 'acct_type': 'checking', 'init_acct_holder': 'John',
             'acct_holder': ['John', 'Raymond', 'Dave'], 'balance': 6200, 'history': [], 'lock': threading.Lock()},
            {'acct_num': 1018, 'acct_type': 'loan', 'init_acct_holder': 'John',
             'acct_holder': ['John', 'Frank', 'Justin'], 'balance': -2000, 'history': [], 'lock': threading.Lock()},
            {'acct_num': 1019, 'acct_type': 'checking', 'init_acct_holder': 'Kate',
             'acct_holder': ['Kate', 'Kevin', 'Justin'], 'balance': 5200, 'history': [], 'lock': threading.Lock()},
            {'acct_num': 1020, 'acct_type': 'loan', 'init_acct_holder': 'Kate',
             'acct_holder': ['Kate', 'Thomas', 'James'], 'balance': -1800, 'history': [], 'lock': threading.Lock()},
            {'acct_num': 1021, 'acct_type': 'checking', 'init_acct_holder': 'James',
             'acct_holder': ['James', 'John', 'Grace'], 'balance': 8700, 'history': [], 'lock': threading.Lock()},
            {'acct_num': 1022, 'acct_type': 'loan', 'init_acct_holder': 'James',
             'acct_holder': ['James', 'Larry', 'Alice'], 'balance': -700, 'history': [], 'lock': threading.Lock()},
            {'acct_num': 1023, 'acct_type': 'checking', 'init_acct_holder': 'Michael',
             'acct_holder': ['Michael', 'Jason', 'Eve'], 'balance': 7400, 'history': [], 'lock': threading.Lock()},
            {'acct_num': 1024, 'acct_type': 'loan', 'init_acct_holder': 'Michael',
             'acct_holder': ['Michael', 'Ivan', 'Gary'], 'balance': -4900, 'history': [], 'lock': threading.Lock()},
            {'acct_num': 1025, 'acct_type': 'checking', 'init_acct_holder': 'Robert',
             'acct_holder': ['Robert', 'Frank', 'Grace'], 'balance': 8400, 'history': [], 'lock': threading.Lock()},
            {'acct_num': 1026, 'acct_type': 'loan', 'init_acct_holder': 'Robert',
             'acct_holder': ['Robert', 'Ivan', 'Justin'], 'balance': -400, 'history': [], 'lock': threading.Lock()},
            {'acct_num': 1027, 'acct_type': 'checking', 'init_acct_holder': 'William',
             'acct_holder': ['William', 'Alice', 'Heidi'], 'balance': 6600, 'history': [], 'lock': threading.Lock()},
            {'acct_num': 1028, 'acct_type': 'loan', 'init_acct_holder': 'William',
             'acct_holder': ['William', 'Justin', 'Henry'], 'balance': -5000, 'history': [],
             'lock': threading.Lock()},
            {'acct_num': 1029, 'acct_type': 'checking', 'init_acct_holder': 'David',
             'acct_holder': ['David', 'Raymond', 'Bob'], 'balance': 2400, 'history': [], 'lock': threading.Lock()},
            {'acct_num': 1030, 'acct_type': 'loan', 'init_acct_holder': 'David',
             'acct_holder': ['David', 'Kate', 'Mark'], 'balance': -200, 'history': [], 'lock': threading.Lock()},
            {'acct_num': 1031, 'acct_type': 'checking', 'init_acct_holder': 'Thomas',
             'acct_holder': ['Thomas', 'Charlie', 'Dave'], 'balance': 8700, 'history': [], 'lock': threading.Lock()},
            {'acct_num': 1032, 'acct_type': 'loan', 'init_acct_holder': 'Thomas',
             'acct_holder': ['Thomas', 'Grace', 'Robert'], 'balance': -2900, 'history': [],
             'lock': threading.Lock()},
            {'acct_num': 1033, 'acct_type': 'checking', 'init_acct_holder': 'Mark',
             'acct_holder': ['Mark', 'Steven', 'Justin'], 'balance': 7800, 'history': [], 'lock': threading.Lock()},
            {'acct_num': 1034, 'acct_type': 'loan', 'init_acct_holder': 'Mark',
             'acct_holder': ['Mark', 'Paul', 'Bob'], 'balance': -5900, 'history': [], 'lock': threading.Lock()},
            {'acct_num': 1035, 'acct_type': 'checking', 'init_acct_holder': 'Steven',
             'acct_holder': ['Steven', 'Grace', 'William'], 'balance': 2400, 'history': [],
             'lock': threading.Lock()},
            {'acct_num': 1036, 'acct_type': 'loan', 'init_acct_holder': 'Steven',
             'acct_holder': ['Steven', 'David', 'Justin'], 'balance': -1900, 'history': [],
             'lock': threading.Lock()},
            {'acct_num': 1037, 'acct_type': 'checking', 'init_acct_holder': 'Paul',
             'acct_holder': ['Paul', 'Charlie', 'Steven'], 'balance': 7800, 'history': [], 'lock': threading.Lock()},
            {'acct_num': 1038, 'acct_type': 'loan', 'init_acct_holder': 'Paul',
             'acct_holder': ['Paul', 'Eve', 'Dave'], 'balance': -2500, 'history': [], 'lock': threading.Lock()},
            {'acct_num': 1039, 'acct_type': 'checking', 'init_acct_holder': 'Kevin',
             'acct_holder': ['Kevin', 'Kate', 'Larry'], 'balance': 4400, 'history': [], 'lock': threading.Lock()},
            {'acct_num': 1040, 'acct_type': 'loan', 'init_acct_holder': 'Kevin',
             'acct_holder': ['Kevin', 'Ivan', 'James'], 'balance': -800, 'history': [], 'lock': threading.Lock()},
            {'acct_num': 1041, 'acct_type': 'checking', 'init_acct_holder': 'Jason',
             'acct_holder': ['Jason', 'Adam', 'Henry'], 'balance': 1400, 'history': [], 'lock': threading.Lock()},
            {'acct_num': 1042, 'acct_type': 'loan', 'init_acct_holder': 'Jason',
             'acct_holder': ['Jason', 'Raymond', 'William'], 'balance': -200, 'history': [],
             'lock': threading.Lock()},
            {'acct_num': 1043, 'acct_type': 'checking', 'init_acct_holder': 'Gary',
             'acct_holder': ['Gary', 'Larry', 'Ivan'], 'balance': 3400, 'history': [], 'lock': threading.Lock()},
            {'acct_num': 1044, 'acct_type': 'loan', 'init_acct_holder': 'Gary',
             'acct_holder': ['Gary', 'Frank', 'James'], 'balance': -900, 'history': [], 'lock': threading.Lock()},
            {'acct_num': 1045, 'acct_type': 'checking', 'init_acct_holder': 'Larry',
             'acct_holder': ['Larry', 'Frank', 'Heidi'], 'balance': 5400, 'history': [], 'lock': threading.Lock()},
            {'acct_num': 1046, 'acct_type': 'loan', 'init_acct_holder': 'Larry',
             'acct_holder': ['Larry', 'William', 'David'], 'balance': -300, 'history': [], 'lock': threading.Lock()},
            {'acct_num': 1047, 'acct_type': 'checking', 'init_acct_holder': 'Justin',
             'acct_holder': ['Justin', 'John', 'Dave'], 'balance': 3400, 'history': [], 'lock': threading.Lock()},
            {'acct_num': 1048, 'acct_type': 'loan', 'init_acct_holder': 'Justin',
             'acct_holder': ['Justin', 'Charlie', 'Alice'], 'balance': -1500, 'history': [],
             'lock': threading.Lock()},
            {'acct_num': 1049, 'acct_type': 'checking', 'init_acct_holder': 'Raymond',
             'acct_holder': ['Raymond', 'Henry', 'James'], 'balance': 9400, 'history': [], 'lock': threading.Lock()},
            {'acct_num': 1050, 'acct_type': 'loan', 'init_acct_holder': 'Raymond',
             'acct_holder': ['Raymond', 'Steven', 'Mark'], 'balance': -6900, 'history': [],
             'lock': threading.Lock()},
            {'acct_num': 1051, 'acct_type': 'checking', 'init_acct_holder': 'Adam',
             'acct_holder': ['Adam', 'Charlie', 'Michael'], 'balance': 5400, 'history': [],
             'lock': threading.Lock()},
            {'acct_num': 1052, 'acct_type': 'loan', 'init_acct_holder': 'Adam',
             'acct_holder': ['Adam', 'Larry', 'Jason'], 'balance': -4600, 'history': [], 'lock': threading.Lock()},
            {'acct_num': 1053, 'acct_type': 'checking', 'init_acct_holder': 'Henry',
             'acct_holder': ['Henry', 'Henry', 'James'], 'balance': 8300, 'history': [], 'lock': threading.Lock()},
            {'acct_num': 1054, 'acct_type': 'loan', 'init_acct_holder': 'Henry',
             'acct_holder': ['Henry', 'Steven', 'Mark'], 'balance': -1800, 'history': [], 'lock': threading.Lock()},
            {'acct_num': 1055, 'acct_type': 'checking', 'init_acct_holder': 'Eve',
             'acct_holder': ['Eve', 'Michael', 'Justin'], 'balance': 2200, 'history': [], 'lock': threading.Lock()},
            {'acct_num': 1056, 'acct_type': 'loan', 'init_acct_holder': 'Eve',
             'acct_holder': ['Eve', 'William', 'Alice'], 'balance': -400, 'history': [], 'lock': threading.Lock()}
        ]

    def create_account(self, data_dict):
        # Check if the user already has an account
        for account in self.accounts:
            if account['init_acct_holder'] == data_dict['user']:
                return "One person can only create one account"

        # Check if the account number specified by the user is already in use
        for account in self.accounts:
            if int(account['acct_num']) == int(data_dict['acct_num']):
                return f"The account number has been used by {account['init_acct_holder']}"

        # Create new account
        new_account = {
            'acct_num': int(data_dict['acct_num']),
            'acct_type': 'checking',
            'init_acct_holder': data_dict['user'],
            'acct_holder': [data_dict['user']],
            'balance': int(data_dict.get('amount', 0)),
            'history': [],
            'lock': threading.Lock()
        }

        # Add new account to the list
        self.accounts.append(new_account)
        return f"Successfully created checking account for {data_dict['user']} with account number {int(data_dict['acct_num'])}。"

    def show_bank(self, data_dict):
        # Check if the user is 'Audit'
        if data_dict['user'] != 'Audit':
            return "Access denied: only Audit can view all bank accounts"

        # Prepare data for table format
        table_data = []
        for account in self.accounts:
            row = [
                account['acct_num'],
                account['acct_type'],
                account['init_acct_holder'],
                ', '.join(account['acct_holder']),
                account['balance'],
                account['history']
            ]
            table_data.append(row)

        # Format the table
        headers = ["acct_num", "acct_type", "init_holder", "acct_holder", "balance", "history"]
        formatted_table = tabulate(table_data, headers=headers, tablefmt="plain")
        return f"All account information is as follows:\n{formatted_table}"

    def show_accountholders(self, data_dict):
        # Check if the user is the account initiate holder

        # If account initiate holder, return all account holders

        # If not account initiate holder
        pass

    def deposit(self, data_dict):
        # Check if the account number exists

        # if deposit amount <0

        # if deposit amount=0, return current balance

        # if deposit amount >0, get mutex lock and do deposit

        pass #remove this "pass" when you do your project

    def withdraw(self, data_dict):
        # Check if the account number exists

        # if withdrawal amount <0:

        # if withdrawal amount = 0, return current balance

        # if withdrawal amount>0, check whether user is one of account holders

        # check if account balance is sufficient

        # get mutex lock before doing withdraw operation

        pass #remove this "pass" when you do your project

    def transfer_to(self, data_dict):
        # Verify that amount is positive

        # Verify that user is an init_acct_holder for an account in the bank.

        # Verify that the target account acct_num exists

        # Check if the user's account balance is sufficient

        # get mutex lock and consider deadlock

        # transfer

        pass  # remove this "pass" when you do your project

    def pay_loan_check(self, data_dict):
        # Get account number and repayment amount

        # Check if the repayment amount is positive

        # Find Target Loan Accounts

        # Confirm that the account is a loan account

        # Check if the user is the holder of the account

        # get mutex lock and pay loan

        pass  # remove this "pass" when you do your project



    def pay_loan_transfer_to(self, data_dict):
        # Get account number and repayment amount

        # Check if the repayment amount is positive

        # Find user's initiate created account

        # Verify that the user account balance is sufficient

        # Find Target Loan Account

        # Check if the user is one of the loan account holders

        # get mutex lock and prevent deadlocks

        # pay loan

        pass  # remove this "pass" when you do your project

    def show_history(self, data_dict):
     # check whether the current user is one of the account holders

     # check whether this account has any operation history

     # if all yes, return account history.

     # The format of account history is ([user], [command], [amount])
     # for example: ('Alice', 'deposit', 500) or (Alice, deposit, 500) both ok.

     pass #remove this "pass" when you do your project
    
def handle_client(client_socket, bank):
    while True:
        data = client_socket.recv(1024)
        if not data:
            break

        # Parse the command line format [user] [command] [account] [amount]
        pairs = data.decode().split()
        data_dict = dict(pair.split('=') for pair in pairs)

        if len(data_dict) < 3:
            response = "Invalid request format."
            client_socket.send(response.encode())
            continue

        print(f"Request received: user={data_dict['user']} command={data_dict['command']}  account={data_dict['acct_num']}, "
              f"amount={data_dict.get('amount', 0)}")

        # Execute the corresponding command
        if data_dict['command'] == 'create_account':
            response = bank.create_account(data_dict)
            client_socket.send(response.encode())
            client_socket.send(b"END")

        elif data_dict['command'] == 'show_bank':
            response = bank.show_bank(data_dict)
            # Sending show_bank data in segments
            for i in range(0, len(response), 1024):
                client_socket.send(response[i:i + 1024].encode())
            client_socket.send(b"END")
            continue

        elif data_dict['command'] == 'show_accountholders':
            response = bank.show_accountholders(data_dict)
            client_socket.send(response.encode())
            client_socket.send(b"END")

        elif data_dict['command'] == 'deposit':
            response = bank.deposit(data_dict)
            client_socket.send(response.encode())
            client_socket.send(b"END")

        elif data_dict['command'] == 'withdraw':
            response = bank.withdraw(data_dict)
            client_socket.send(response.encode())
            client_socket.send(b"END")

        elif data_dict['command'] == 'transfer_to':
            response = bank.transfer_to(data_dict)
            client_socket.send(response.encode())
            client_socket.send(b"END")

        elif data_dict['command'] == 'pay_loan_check':
            response = bank.pay_loan_check(data_dict)
            client_socket.send(response.encode())
            client_socket.send(b"END")

        elif data_dict['command'] == 'pay_loan_transfer_to':
            response = bank.pay_loan_transfer_to(data_dict)
            client_socket.send(response.encode())
            client_socket.send(b"END")

        elif data_dict['command'] == 'show_history':
            response = bank.show_history(data_dict)
            client_socket.send(response.encode())
            client_socket.send(b"END")


        else:
            response = "Invalid command."
            client_socket.send(response.encode())
            client_socket.send(b"END")


        print(f"Request handled: {data_dict['command']}")
        # print(f"Current bank state: {bank.accounts}\n")
        time.sleep(1)  # Slight delay for better client-server interaction

    client_socket.close()

HOST = socket.gethostbyname(socket.gethostname())
PORT = 9876
ADDR = (HOST, PORT)
bank = Bank()

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(ADDR)
server_socket.listen()
print(f"Server listening on host {HOST}...")

while True:
    client_socket, addr = server_socket.accept()
    print(f"Client connected from {addr}")

    thread = threading.Thread(target=handle_client, args=(client_socket, bank))
    thread.start()
    print(f"{threading.active_count() - 1} thread connections running...")








