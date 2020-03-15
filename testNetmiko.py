#!/usr/bin/env python3

#import netmiko 
from netmiko import ConnectHandler

sshovercli = ConnectHandler(device_type="cisco_ios",host='192.168.56.101', port=22, username='cisco', password='cisco123!' )

output = sshovercli.send_command("show ip interface brief")
print("show ip interface brief:\n{}".format(output))

### Con este codigo hasta  aqui deberia conectarse a la maquina virtual




# print (dir(netmiko))