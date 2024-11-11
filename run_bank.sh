#!/bin/bash


gnome-terminal -- bash -c "python3 server.py; exec bash"
sleep 3  # wait 3 seconds to start the server

# The first 2 client terminals are executing identical requests
# by design to create contansous situations
gnome-terminal -- bash -c "
python3 client.py Audit show_bank;
sleep 2;
python3 client.py Bob deposit 1003 3500;
python3 client.py Alice withdraw 1001 1000;
python3 client.py Alice pay_loan_check 1002 100;
python3 client.py William transfer_to 1013 200;
python3 client.py Ivan pay_loan_check 1016 300;
python3 client.py James deposit 1021 1000;
python3 client.py James withdraw 1021 2000;
python3 client.py Frank withdraw 1009 200;
python3 client.py Heidi pay_loan_check 1014 100;
exec bash"

gnome-terminal -- bash -c "
python3 client.py Audit show_bank;
sleep 2;
python3 client.py Bob deposit 1003 3500;
python3 client.py Alice withdraw 1001 1000;
python3 client.py Alice pay_loan_check 1002 100;
python3 client.py William transfer_to 1013 200;
python3 client.py Ivan pay_loan_check 1016 300;
python3 client.py James deposit 1021 1000;
python3 client.py James withdraw 1021 2000;
python3 client.py Frank withdraw 1009 200;
python3 client.py Heidi pay_loan_check 1014 100;
exec bash"


gnome-terminal -- bash -c "
python3 client.py Audit show_bank;
sleep 2;
python3 client.py Ivan deposit 1003 2100;
python3 client.py Zion create_account 1099;
python3 client.py Dave transfer_to 1009 100;
python3 client.py Alice show_history 1001;
python3 client.py Heidi pay_loan_check 1014 100;
python3 client.py Grace transfer_to 1017 500;
python3 client.py Alice pay_loan_transfer_to 1002 100;
python3 client.py Robert pay_loan_transfer_to 1026 100;
python3 client.py Dora create_account 1234;
exec bash"


gnome-terminal -- bash -c "
python3 client.py Audit show_bank;
sleep 2;
python3 client.py Kevin deposit 1003 700;
python3 client.py Henry deposit 1054 300;
python3 client.py James withdraw 1021 300;
python3 client.py Alice deposit 1001 5000;
python3 client.py William transfer_to 1029 100;
python3 client.py Paul transfer_to 1035 200;
python3 client.py James show_history 1021;
python3 client.py Robert pay_loan_transfer_to 1026 100;
python3 client.py Kate transfer_to 1015 100;
exec bash"


gnome-terminal -- bash -c "
python3 client.py Audit show_bank;
sleep 2;
python3 client.py Bob withdraw 1003 900;
python3 client.py David withdraw 1029 600;
python3 client.py David show_history 1029
python3 client.py Mark deposit 1034 2200;
python3 client.py Kate transfer_to 1015 100;
python3 client.py Charlie withdraw 1005 2800;
python3 client.py Henry transfer_to 1009 100;
python3 client.py John withdraw 1017 600;
python3 client.py Justin deposit 1047 3100;
exec bash"
