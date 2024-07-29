Y='Exit'
X='Search Exploit'
W='Scan IP or URL'
V='html.parser'
U=Exception
N=int
J='clear'
I=input
G='\n'
E=True
A=print
import subprocess as O,sys as D,inquirer as P,requests as Z
from bs4 import BeautifulSoup as Q
import socket as R,time as S,dns.resolver
from tabulate import tabulate as c
import os as F,random as K,shutil as a
F.system(J)
B='\x1b[0m'
C='\x1b[1m'
L='./exploitdb/searchsploit'
def d():
	if not F.path.isfile(L):
		A(f"searchsploit not found at {L}. Installing from the repository.");B='git clone https://gitlab.com/exploit-database/exploitdb.git';C=O.run(B,shell=E)
		if C.returncode!=0:A('Failed to clone the exploitdb repository.');D.exit(1)
		A('exploitdb repository successfully cloned.')
	A('searchsploit is available.')
def T():return f"{K.randint(0,255):02X}{K.randint(0,255):02X}{K.randint(0,255):02X}"
def b(start_color,end_color,factor):B=[N(start_color[A:A+2],16)for A in(0,2,4)];C=[N(end_color[A:A+2],16)for A in(0,2,4)];A=[N(B[A]+(C[A]-B[A])*factor)for A in range(3)];return f"[38;2;{A[0]};{A[1]};{A[2]}m"
def e(text,width):return text.center(width)
def M():
	F='\n\n\n▄▄▄█████▓ ██▓ ▄▄▄       ▄████▄  \n▓  ██▒ ▓▒▓██▒▒████▄    ▒██▀ ▀█  \n▒ ▓██░ ▒░▒██▒▒██  ▀█▄  ▒▓█    ▄ \n░ ▓██▓ ░ ░██░░██▄▄▄▄██ ▒▓▓▄ ▄██▒\n  ▒██▒ ░ ░██░ ▓█   ▓██▒▒ ▓███▀ ░\n  ▒ ░░   ░▓   ▒▒   ▓▒█░░ ░▒ ▒  ░\n    ░     ▒ ░  ▒   ▒▒ ░  ░  ▒   \n  ░       ▒ ░  ░   ▒   ░        \n          ░        ░  ░░ ░      \n                       ░   \n\n                           https://github.com/activiste                           \n    ';H=T();I=T();C=F.split(G);J=len(C);K=a.get_terminal_size().columns
	for(L,E)in enumerate(C):
		if E.strip():M=L/(J-1);N=b(H,I,M);O=e(E,K);D.stdout.write(N+O+B+G);D.stdout.flush();S.sleep(.01)
		else:A()
def H(text,speed=.01):
	for B in text:D.stdout.write(B);D.stdout.flush();S.sleep(speed)
	A()
def f(url):
	try:B=R.gethostbyname(url);return B
	except R.gaierror:A('Invalid IP or Domain format.');D.exit(1)
def g(ip):A=f"https://shodan.io/host/{ip}";B=Z.get(A);return B.text
def h(content):B=Q(content,V);A=list(set([A for A in B.stripped_strings if A.startswith('CVE-')]));A.sort(key=lambda x:x.split('-')[1],reverse=E);C=[(A,f"https://www.cve.org/CVERecord?id={A}")for A in A];return C
def i(content):
	B=Q(content,V);A=B.find('div',id='ports')
	if A:C=[A.get_text(strip=E)for A in A.find_all('a',class_='bg-primary')];return C
	return[]
def j(ip):
	try:B=dns.reversename.from_address(ip);C=str(B);D=dns.resolver.resolve(C,'PTR');return[str(A)[:-1]for A in D]
	except dns.resolver.NXDOMAIN:return[]
	except U as E:A(f"Error resolving domains: {E}");return[]
def k(cve):
	try:A=O.run([L,cve],capture_output=E,text=E);return A.stdout
	except FileNotFoundError:return'searchsploit not found. Please ensure the path is correct.'
	except U as B:return f"Error occurred: {B}"
def l():A='choice';B=[P.List(A,message='What do you need ?',choices=[W,X,Y])];C=P.prompt(B);return C[A]
def m():
	b='\nPress Enter to return to the menu...';N='\x1b[31m';d()
	while E:
		F.system(J);M();L=l()
		if L==W:
			F.system(J);M();H('Who is your target ?\n',speed=.01);D=I('Target > ').strip()
			if D.startswith('http://')or D.startswith('https://'):D=D.split('://')[1]
			if not D.replace('.','').isdigit():K=f(D)
			else:K=D
			O=j(K)
			if O:P=G.join(O);Q='\x1b[32m'
			else:P='None found';Q=N
			R=g(K);S=i(R)
			if S:T=', '.join(S);U='\x1b[34m'
			else:T='No open ports found';U=N
			V=h(R)
			if V:e=[f"{A} - More info: {B}"for(A,B)in V];Z=G.join(e);a='\x1b[35m'
			else:Z='No CVEs found';a=N
			m=[[f"{C}IP Address{B}",K],[f"{C}Hostnames{B}",Q+P+B],[f"{C}Open Ports{B}",U+T+B],[f"{C}CVEs{B}",a+Z+B]];A(G);A(c(m,headers=[f"{C}Category{C}",f"{C}Details{C}"],tablefmt='grid'));H(b,speed=.01);I()
		elif L==X:F.system(J);M();H('Enter the exploit you are looking for (CVE ID / NAME)\n',speed=.01);n=I('Exploit > ').strip();o=k(n);A(o);H(b,speed=.01);I()
		elif L==Y:break
if __name__=='__main__':m()
