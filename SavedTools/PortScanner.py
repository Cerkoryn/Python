import socket
import thread

openPorts = []

def handler(target, port):
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  result = s.connect_ex((target, port))
  if result == 0:
    print("Port: " + str(port) + " Open")
    openPorts.append(port)
  s.close()
    
print("Please enter an IP Address to scan.")
target = raw_input("> ")

print("*" * 40)
print("* Scanning: " + target + " *")
print("*" * 40)

for port in range(1, 10000):    
    thread.start_new_thread(handler, (target, port))
print("\nPorts open are " + str(openPorts)[1:-1])
