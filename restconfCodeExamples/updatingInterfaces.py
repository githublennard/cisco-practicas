#!/usr/bin/env python3

import json,requests

requests.packages.urllib3.disable_warnings()

#Connection Address
api_url = "https://10.10.20.48/restconf/data/ietf-interfaces:interfaces/interface=Loopback99"

#Headers
headers ={
    "Accept":"application/yang-data+json",
    "Content-Type":"application/yang-data+json"
}

#Autenticacion # es una tupla, ya que asi es el metodo get para este caso
basic_auth = ("cisco","cisco_1234!")

#Info to send
yangConfiguration = {
    "ietf-interfaces:interface": {
        "name": "Loopback99",
        "description": "Interface_Prueba_Loopback",
        "type": "iana-if-type:softwareLoopback",
        "enabled": True,
        "ietf-ip:ipv4": {
            "address": [
                {
                    "ip": "99.99.99.99",
                    "netmask": "255.255.255.0"
                }
            ]
        },
        "ietf-ip:ipv6": {}
    }
}

            #asi es que se hace la peticion con put pero con la intencion de crear una interface en el servidor
#Saving response            
resp = requests.put(api_url, data=json.dumps(yangConfiguration) , auth=basic_auth, headers=headers ,verify=False)

if(resp.status_code >= 200 and resp.status_code <= 299):
    print("Status OK:{}".format(resp.status_code))
else:
    print("Error code {}, reply:{}".format(resp.status_code, resp.json()))

#resp_json = resp.json()

#print(json.dumps(resp_json,indent=4))
