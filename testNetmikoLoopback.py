#!/usr/bin/env python3

#import netmiko --> No es necesario importar todo 
from netmiko import ConnectHandler

#sshovercli = ConnectHandler(device_type="cisco_ios",host='192.168.56.101', port=22, username='cisco', password='cisco123!' )
#sshovercli = ConnectHandler(device_type="cisco_ios",host='192.168.254.11', port=22, username='cisco', password='cisco1234!' )
sshovercli = ConnectHandler(device_type="cisco_ios",host='10.10.20.48', port=22, username='cisco', password='cisco_1234!')
#output = sshovercli.send_command("show ip interface brief")
#output = sshovercli.send_command("sh ip int br")
#print("show ip interface brief:\n{}".format(output))


# output = sshovercli.send_command("sh version")
# print("show ip interface brief:\n{}".format(output))
                    ###Este codigo me agrega una interface al servidor remoto
                    ###accede a esta interface ip  mascara
configCommands = ['int loopback1','ip address 1.2.3.4 255.255.255.0','description loopback over ssh']#array de datos
outputConfig = sshovercli.send_config_set(configCommands)
print("Config output from device:\n{}".format(outputConfig))
output = sshovercli.send_command("show ip interface brief")
print("show ip interface brief:\n{}".format(output))

### Con este codigo hasta  aqui deberia conectarse a la maquina virtual

# print (dir(netmiko))

