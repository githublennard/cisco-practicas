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
Welcome to the APIC-EM Controlator
''')

def selectFunc():
    global operation
    operation = input('''
Please First Select the function number 1 to get access to the other functions deploy:
1 for getTicket
2 for getHosts
3 for getNetworkDevices
4 for getRoute
After select your operation press Enter
''')

    if operation == '1':
        getTicket()
        print("Esto es un string secundario:" ,ticket)
        
    
    if operation == '2':
        getHosts()
        tableHeader = ["Number","Type","IP","MAC"]
        print(tabulate(hostList,tableHeader))
        
    if operation == '3':
        getNetworkDevices()
        for equipo in response_json['response']:
            print("El hostname",equipo['hostname'],"pertenece a la familia",equipo['family'],
            "su MAC es",equipo['macAddress'],"y su version de IOS es:",equipo['softwareVersion'])

        


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
    print("Esto es un string:" ,ticket)
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


def again():
    # Take input from user
    calc_again = input('''
Do you want to calculate again?
Please type Y for YES or N for NO.
''')

    # If user types Y, run the calculate() function
    if calc_again.upper() == 'Y':
        selectFunc()

    # If user types N, say good-bye to the user and end the program
    elif calc_again.upper() == 'N':
        print('See you later.')

    # If user types another key, run the function again
    else:
        again()


welcome()
selectFunc()
