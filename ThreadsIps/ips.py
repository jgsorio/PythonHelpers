import ipaddress

ip = '192.168.0.0/24'

enderecos = ipaddress.ip_network(ip)

# Imprimindo todos os ips disponiveis em uma rede / 24
for ip in enderecos:
    print(ip)
