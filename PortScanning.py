import socket


target = input("Enter your target: ")
port_range = input("Enter the range of port (e.g 25-500): ")

low_port = int((port_range.split("-")[0]))
high_port = int((port_range.split("-")[1]))

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

print("Scanning TARGET" , target , " PORT: FROM " , low_port , " TO " , high_port , "....")

f = open(target+".txt", "w")

for port in range(low_port,high_port):
    status = s.connect_ex((target,port))
    if(status == 0):
        print("!!! OPEN PORT !!! = ", port)
        f.write(("opening port {}").format(str(port)))

    else:
        print("CLOSED PORT = ", port)


f.close()





