#!/usr/bin/env python3

import json,requests

requests.packages.urllib3.disable_warnings()

#Connection Address
api_url = "https://10.10.20.48/restconf/data/ietf-interfaces:interfaces/interface=Loopback11"

#Headers
headers ={
    "Accept":"application/yang-data+json",
    "Content-Type":"application/yang-data+json"
}

#Autenticacion # es una tupla, ya que asi es el metodo get para este caso
basic_auth = ("cisco","cisco_1234!")

            #asi es que se hace la peticion con put pero con la intencion de crear una interface en el servidor
#Saving response            
resp = requests.delete(api_url, auth=basic_auth, headers=headers ,verify=False)

#resp_json = resp.json()

#print(json.dumps(resp_json,indent=4))
#print(json.dumps(resp_json))
print("La peticion tiene el estado",resp.status_code)
