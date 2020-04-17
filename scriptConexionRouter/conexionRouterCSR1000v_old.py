#!/usr/bin/env python3

#Estos son modulos
import requests
import json

requests.packages.urllib3.disable_warnings()

def welcome():
    print('''
Welcome to the Router CSR1000v
''')

def selectFunction():
    global operation
    global headers
    global basic_auth
    headers = {
    "Accept":"application/yang-data+json",
    "Content-Type":"application/yang-data+json"
    }
    basic_auth = ("cisco","cisco_1234!")
    
    operation = input('''
Please Select the function that you need to deploy in Router CSR1000v:

1 for List of Interfaces
2 for Create Interface
3 for Delete Interface
4 for Route Table
5 for Yang RESTCONF Capability
6 for Yang Modul 2

After select your operation press Enter
''')

    if operation == '1':
        getInterfaces()
        print("Succesfull Deploy")
    
    if operation == '2':
        createInterface()
        print("The Interface was create")
        
    if operation == '3':
        deleteInterface()
        print("The Interface was delete")
    
    if operation == '4':
        getRouteTable()
        print("The Route Table was show")
    
    if operation == '5':
        yangModelCapability()
        print("Was found the RESTCONF capability")
    
    if operation == '6':
        yangModelMemory()
        print("Was show memory statistic")
    
    again()
      
def again():
    # Take input from user
    calc_again = input('''
Do you want to deploy other function again?
Please type Y for YES or N for NO.
''')

    # If user types Y, run the calculate() function
    if calc_again.upper() == 'Y':
        selectFunction()

    # If user types N, say good-bye to the user and end the program
    elif calc_again.upper() == 'N':
        print('See you later.')

    # If user types another key, run the function again
    else:
        again()

def getInterfaces():
    api_url = "https://10.10.20.48/restconf/data/ietf-interfaces:interfaces"
    headers
    basic_auth
    resp = requests.get(api_url,auth=basic_auth, headers=headers ,verify=False)
    resp_json = resp.json()
    print(json.dumps(resp_json,indent=4))

def createInterface():
    api_url = "https://10.10.20.48/restconf/data/ietf-interfaces:interfaces/interface=Loopback11"
    headers
    basic_auth
    yangConfiguration = {
    "ietf-interfaces:interface": {
        "name": "Loopback11",
        "description": "Interface_Script_Loopback",
        "type": "iana-if-type:softwareLoopback",
        "enabled": True,
        "ietf-ip:ipv4": {
            "address": [
                {
                    "ip": "11.11.11.11",
                    "netmask": "255.255.255.0"
                }
            ]
        },
        "ietf-ip:ipv6": {}
    }
    }
    resp = requests.put(api_url, data=json.dumps(yangConfiguration) , auth=basic_auth, headers=headers ,verify=False)
    if(resp.status_code >= 200 and resp.status_code <= 299):
        print("Status OK:{}".format(resp.status_code))
    else:
        print("Error code {}, reply:{}".format(resp.status_code, resp.json()))

def deleteInterface():
    api_url = "https://10.10.20.48/restconf/data/ietf-interfaces:interfaces/interface=Loopback11"
    headers
    basic_auth
    resp = requests.delete(api_url, auth=basic_auth, headers=headers ,verify=False)
    print("La peticion tiene el estado",resp.status_code)

def getRouteTable():
    api_url = "https://10.10.20.48/restconf/data/ietf-routing:routing-state/routing-instance"
    headers
    basic_auth
    resp = requests.get(api_url,auth=basic_auth, headers=headers ,verify=False)
    resp_json = resp.json()
    print(json.dumps(resp_json,indent=4))
    print("La peticion tiene el estado",resp.status_code)

def yangModelCapability():
    api_url = "https://10.10.20.48/restconf/data/ietf-restconf-monitoring:restconf-state/capabilities"
    headers
    basic_auth
    resp = requests.get(api_url,auth=basic_auth, headers=headers ,verify=False)
    resp_json = resp.json()
    print(json.dumps(resp_json,indent=4))
    print("La peticion tiene el estado",resp.status_code)

def yangModelMemory():
    api_url = "https://10.10.20.48/restconf/data/Cisco-IOS-XE-memory-oper:memory-statistics/memory-statistic"
    headers
    basic_auth
    resp = requests.get(api_url,auth=basic_auth, headers=headers ,verify=False)
    resp_json = resp.json()
    print(json.dumps(resp_json,indent=4))
    print("La peticion tiene el estado",resp.status_code)

welcome()
selectFunction()
#getFunctions()
