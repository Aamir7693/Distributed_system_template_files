#!/bin/bash


gnome-terminal -- bash -c "python3 server.py; exec bash"
sleep 3  # wait 3 seconds to start the server

gnome-terminal -- bash -c "
python3 client.py Audit show_bank;
python3 client.py Ivan deposit 1003 2100;
python3 client.py Zion create_account 1099;
python3 client.py Dave transfer_to 1009 100;
python3 client.py Ivan show_history 1003;
python3 client.py Heidi pay_loan_check 1014 100;
python3 client.py Grace transfer_to 1017 500;
python3 client.py Alice pay_loan_transfer_to 1002 100;
python3 client.py Robert pay_loan_transfer_to 1026 100;
python3 client.py Dora create_account 1234;
exec bash"