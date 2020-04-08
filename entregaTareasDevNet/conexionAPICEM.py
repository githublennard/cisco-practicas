#!/usr/bin/env python3

#Estos son modulos
import requests
import json
import urllib3
from pprint import pprint
from tabulate import * 

from pprint import pprint

requests.packages.urllib3.disable_warnings()

def welcome():
    print('''
Welcome to the APIC-EM Function Controlator
''')

def getAccess():
    global operation
    operation = input('''
Please First Select the function number 1 to get access to the APIC-EM CONTROLER:

1 for getTicket

This function will be available after select Number 1:
2 for getHosts
3 for getNetworkDevices
4 for getRoute
5 for getFlowAnalysis

After select your operation press Enter
''')

    if operation == '1':
        getTicket()
    
    if operation != '1':
        getAccess()
        

def getFunctions():
    operation = input('''
Please Select the number of function to deploy the APIC-EM CONTROLER:

2 for getHosts
3 for getNetworkDevices
4 for getInterface
5 for getFlowAnalysis

After select your operation press Enter
''')

    if operation == '2':
        getHosts()
        tableHeader = ["Number","Type","IP","MAC"]
        print(tabulate(hostList,tableHeader))
        
    if operation == '3':
        getNetworkDevices()
        for equipo in response_json['response']:
            print("El hostname",equipo['hostname'],"pertenece a la familia",equipo['family'],
            "su MAC es",equipo['macAddress'],"y su version de IOS es:",equipo['softwareVersion'])

    if operation == '4':
        getInterface()
        for interface in response_json['response']:
            print("TIPO INTERFACE: ",interface['interfaceType'],"NOMBRE CLASE: ",interface['className'],
            "MAC: ",interface['macAddress'],"ipV4: ",interface['ipv4Address'])

    if operation == '5':
        getFlowAnalysis()
        pprint(response_json)
        
    again()


def getTicket():
    global ticket
    url= "https://devnetsbx-netacad-apicem-3.cisco.com/api/v1/ticket"
    headers = {
    'Content-Type':'application/json'
    }
    body_json = {
    "password": "Xj3BDqbU",
    "username": "devnetuser"
    }

    resp = requests.post(url,json.dumps(body_json),headers=headers,verify=False)
    print("La peticion tiene el estado",resp.status_code)
    response_json = resp.json()
    ticket = str( response_json['response']['serviceTicket'])
    print("El ticket de servicio es:",response_json['response']['serviceTicket'])

def getHosts():
    global ticket
    global hostList
    url= "https://devnetsbx-netacad-apicem-3.cisco.com/api/v1/host"
    headers = {
    'Content-Type' : 'application/json',
    'X-Auth-Token' : ticket
    }
    resp = requests.get(url,headers=headers,verify=False)
    hostList = []
    print("La peticion tiene el estado",resp.status_code)
    response_json = resp.json()
    counter = 0
    for el in response_json['response']:
        counter+=1
        host = [
            counter,
            #response_json['response']
            el['hostType'],
            el['hostIp'],
            el['hostMac']   
        ]
        hostList.append(host)
        #tableHeader = ["Number","Type","IP","MAC"] 
        #print(tabulate(hostList,tableHeader))

def getNetworkDevices():
    global response_json
    url= "https://devnetsbx-netacad-apicem-3.cisco.com/api/v1/network-device"
    headers = {
    'Content-Type' : 'application/json',
    'X-Auth-Token' : ticket
    }
    resp = requests.get(url,headers=headers,verify=False)
    print("La peticion tiene el estado",resp.status_code)
    response_json = resp.json()

def getInterface():
    global response_json
    url= "https://devnetsbx-netacad-apicem-3.cisco.com/api/v1/interface"
    headers = {
    'Content-Type' : 'application/json',
    'X-Auth-Token' : ticket
    }
    resp = requests.get(url,headers=headers,verify=False)
    print("La peticion tiene el estado",resp.status_code)
    response_json = resp.json()

def getFlowAnalysis():
    global response_json
    url= "https://devnetsbx-netacad-apicem-3.cisco.com/api/v1/flow-analysis"
    headers = {
    'Content-Type' : 'application/json',
    'X-Auth-Token' : ticket
    }
    resp = requests.get(url,headers=headers,verify=False)
    print("La peticion tiene el estado",resp.status_code)
    response_json = resp.json()


def again():
    # Take input from user
    calc_again = input('''
Do you want to deploy other function again?
Please type Y for YES or N for NO.
''')

    # If user types Y, run the calculate() function
    if calc_again.upper() == 'Y':
        getFunctions()

    # If user types N, say good-bye to the user and end the program
    elif calc_again.upper() == 'N':
        print('See you later.')

    # If user types another key, run the function again
    else:
        again()


welcome()
getAccess()
getFunctions()
