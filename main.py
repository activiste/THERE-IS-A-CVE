N='html.parser'
G=int
E='\n'
D=print
import requests as O
from bs4 import BeautifulSoup as H
import socket as I,time as J,sys as C,dns.resolver
from tabulate import tabulate as R
import os,random as F,shutil as K
os.system('clear')
A='\x1b[0m'
B='\x1b[1m'
Z='\x1b[4m'
def L():return f"{F.randint(0,255):02X}{F.randint(0,255):02X}{F.randint(0,255):02X}"
def P(start_color,end_color,factor):B=[G(start_color[A:A+2],16)for A in(0,2,4)];C=[G(end_color[A:A+2],16)for A in(0,2,4)];A=[G(B[A]+(C[A]-B[A])*factor)for A in range(3)];return f"[38;2;{A[0]};{A[1]};{A[2]}m"
def M(text,width):return text.center(width)
def S():
	G='\n▄▄▄█████▓ ██▓ ▄▄▄       ▄████▄  \n▓  ██▒ ▓▒▓██▒▒████▄    ▒██▀ ▀█  \n▒ ▓██░ ▒░▒██▒▒██  ▀█▄  ▒▓█    ▄ \n░ ▓██▓ ░ ░██░░██▄▄▄▄██ ▒▓▓▄ ▄██▒\n  ▒██▒ ░ ░██░ ▓█   ▓██▒▒ ▓███▀ ░\n  ▒ ░░   ░▓   ▒▒   ▓▒█░░ ░▒ ▒  ░\n    ░     ▒ ░  ▒   ▒▒ ░  ░  ▒   \n  ░       ▒ ░  ░   ▒   ░        \n          ░        ░  ░░ ░      \n                       ░        \n    ';H=L();I=L();B=G.split(E);N=len(B);O=K.get_terminal_size().columns
	for(Q,F)in enumerate(B):
		if F.strip():R=Q/(N-1);S=P(H,I,R);T=M(F,O);C.stdout.write(S+T+A+E);C.stdout.flush();J.sleep(.01)
		else:D()
def T(text,speed=.01):
	A=K.get_terminal_size().columns;B=M(text,A)
	for E in B:C.stdout.write(E);C.stdout.flush();J.sleep(speed)
	D()
def U(url):
	try:A=I.gethostbyname(url);return A
	except I.gaierror:D('Invalid IP.');C.exit(1)
def V(ip):A=f"https://shodan.io/host/{ip}";B=O.get(A);return B.text
def W(content):B=H(content,N);A=list(set([A for A in B.stripped_strings if A.startswith('CVE-')]));A.sort(key=lambda x:x.split('-')[1],reverse=True);C=[(A,f"https://www.cve.org/CVERecord?id={A}")for A in A];return C
def X(content):
	B=H(content,N);A=B.find('div',id='ports')
	if A:C=[A.get_text(strip=True)for A in A.find_all('a',class_='bg-primary')];return C
	return[]
def Y(ip):
	try:A=dns.resolver.resolve_address(ip);return[A.to_text()[:-1]for A in A]
	except Exception as B:D(f"Error resolving domains: {B}");return[]
def Q():
	G='\x1b[31m';S();T(f"{B}       Dev By Sparked | https://github.com/activiste{A}\n\n",speed=.01);C=input('TARGET >>> ')
	if C.startswith('http://')or C.startswith('https://'):C=C.split('://')[1]
	if not C.replace('.','').isdigit():F=U(C)
	else:F=C
	H=Y(F)
	if H:I=E.join(H);J='\x1b[32m'
	else:I='None found';J=G
	K=V(F);L=X(K)
	if L:M=', '.join(L);N='\x1b[34m'
	else:M='No open ports found';N=G
	O=W(K)
	if O:Z=[f"{A} - More info: {B}"for(A,B)in O];P=E.join(Z);Q='\x1b[35m'
	else:P='No CVEs found';Q=G
	a=[[f"{B}IP Address{A}",F],[f"{B}Hostnames{A}",J+I+A],[f"{B}Open Ports{A}",N+M+A],[f"{B}CVEs{A}",Q+P+A]];D(E);D(R(a,headers=[f"{B}Category{A}",f"{B}Details{A}"],tablefmt='grid'))
if __name__=='__main__':Q()
