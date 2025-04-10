
# Definimos las distancias administrativas por defecto
EIGRP = 90
OSPF = 110
BGP = 20
RIP = 120

# Solicitamos al usuario que ingrese un protocolo
protocolo = input("Ingresa el nombre del protocolo (OSPF, RIP, EIGRP, BGP): ").upper()

# Verificamos el protocolo ingresado usando if / elif / else
if protocolo == "OSPF":
    print(f"La distancia administrativa de {protocolo} es {OSPF}.")
elif protocolo == "RIP":
    print(f"La distancia administrativa de {protocolo} es {RIP}.")
elif protocolo == "EIGRP":
    print(f"La distancia administrativa de {protocolo} es {EIGRP}.")
elif protocolo == "BGP":
    print(f"La distancia administrativa de {protocolo} es {BGP}.")
else:
    print("Protocolo no reconocido. Intenta con OSPF, RIP, EIGRP o BGP.")
