#B1 IP Adresse
#Hir kommt der importierte socketblock 
import socket
#Hir kommt die apfrage der IP Adresse und  namen 
host_name = socket.gethostname()
host_ip = socket.gethostbyname(host_name)
#Hir kommt print das wird vorher sichbar zu sehen sein wird
print("Host Name: ", host_name)
print("Host IP: ", host_ip)
print ("Ende")
