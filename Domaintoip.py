#GHHBD
#Domian to Ip Tools By GHHBD
import socket
from termcolor import colored
import pyfiglet
banner= colored(pyfiglet.figlet_format("Domain To Ip"),"yellow")
print(banner)
print("By Gray Hat Bangladesh")
domain = str(input("Enter a Domain:"))
ip = socket.gethostbyname(domain)
print("Target Ip is:",ip)

