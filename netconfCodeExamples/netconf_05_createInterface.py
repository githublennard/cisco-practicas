from ncclient import manager
import xml.dom.minidom #Libreria para que se vea bien

#Definimos Conexion
con = manager.connect(host="10.10.20.48",port="830",username="cisco",password="cisco_1234!",hostkey_verify=False)

#Aqui se modifica todo lo que esta en la etiqueta, el resto no se toca y por lo tanto queda igual
#Filtro Envio de Data en netconf
netconf_data = """
<config><native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
    <interface>
        <Loopback>
            <name>88</name>
                <description>Interface_Test_Loopback</description>
					<ip>
						<address>
							<primary>
								<address>88.88.88.88</address>
								<mask>255.255.255.0</mask>
							</primary>
						</address>
					</ip>
        </Loopback>
    </interface>
</native></config>
"""

#Recoger informacion de Dispositivo #El metodo get_config aparece en las diapositivas
netconf_reply = con.edit_config(target="running", config=netconf_data)

#Print Configuration
#print(netconf_reply)
                        #Funcion parseString     #Para que se vea bien
print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())



