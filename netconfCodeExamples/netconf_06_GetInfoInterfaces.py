from ncclient import manager
import xml.dom.minidom #Libreria para que se vea bien

#Definimos Conexion
con = manager.connect(host="10.10.20.48",port="830",username="cisco",password="cisco_1234!",hostkey_verify=False)

#Aqui se modifica todo lo que esta en la etiqueta, el resto no se toca y por lo tanto queda igual
#Filtro Envio de Data en netconf
#El filtro de xmlns se podria considerar como un namespace del cual quiero informacion por eso hago esa declaracion
netconf_filter = """
<filter>
    <interfaces-state xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces"/>
</filter>
"""

#Recoger informacion de Dispositivo #El metodo get_config aparece en las diapositivas
netconf_reply = con.get(filter=netconf_filter)

#Print Configuration
#print(netconf_reply)
                        #Funcion parseString     #Para que se vea bien
print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())



