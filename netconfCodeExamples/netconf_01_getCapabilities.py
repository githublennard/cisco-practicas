from ncclient import manager

#Definimos Conexion
con = manager.connect(host="10.10.20.48",port="830",username="cisco",password="cisco_1234!",hostkey_verify=False)

#print
print("Informacion Capabilities")
for capability in con.server_capabilities:
    print(capability)