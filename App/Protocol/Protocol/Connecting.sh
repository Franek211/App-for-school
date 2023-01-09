echo "This is the protocol responsible for connecting over ip"

echo "Enter your device login underneath"
read Login

echo "Underneath, enter the ip of your device (Enter the entire ip address of the device (only 192.168.0.115 example))"
read IP

ssh $Login@$IP