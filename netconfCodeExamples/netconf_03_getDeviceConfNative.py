from ncclient import manager
import xml.dom.minidom #Libreria para que se vea bien

#Definimos Conexion
con = manager.connect(host="10.10.20.48",port="830",username="cisco",password="cisco_1234!",hostkey_verify=False)

#Definir Filtro
netconf_filter = """
<filter>
    <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native"/>
</filter>
"""

#Recoger informacion de Dispositivo #El metodo get_config aparece en las diapositivas
netconf_reply = con.get_config(source="running", filter=netconf_filter)

#Print Configuration
#print(netconf_reply)
                        #Funcion parseString     #Para que se vea bien
print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())



