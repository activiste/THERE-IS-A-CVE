Y='Exit'
X='Search Exploit'
W='Scan IP or URL'
V='html.parser'
U=Exception
O=int
J='clear'
I=input
G='\n'
F=True
A=print
import subprocess as K,sys as D,inquirer as P,requests as Z
from bs4 import BeautifulSoup as Q
import socket as R,time as S,dns.resolver
from tabulate import tabulate as c
import os as E,random as L,shutil as a
E.system(J)
B='\x1b[0m'
C='\x1b[1m'
M='./exploitdb/searchsploit'
def d():
	B='requirements.txt'
	if E.path.exists(B):A('Installing required packages...');K.check_call([D.executable,'-m','pip','install','-r',B])
	else:A('No requirements.txt file found.')
def e():
	if not E.path.isfile(M):
		A(f"searchsploit not found at {M}. Installing from the repository.");B='git clone https://gitlab.com/exploit-database/exploitdb.git';C=K.run(B,shell=F)
		if C.returncode!=0:A('Failed to clone the exploitdb repository.');D.exit(1)
		A('exploitdb repository successfully cloned.')
	A('searchsploit is available.')
def T():return f"{L.randint(0,255):02X}{L.randint(0,255):02X}{L.randint(0,255):02X}"
def b(start_color,end_color,factor):B=[O(start_color[A:A+2],16)for A in(0,2,4)];C=[O(end_color[A:A+2],16)for A in(0,2,4)];A=[O(B[A]+(C[A]-B[A])*factor)for A in range(3)];return f"[38;2;{A[0]};{A[1]};{A[2]}m"
def f(text,width):return text.center(width)
def N():
	F='\n\n\n▄▄▄█████▓ ██▓ ▄▄▄       ▄████▄  \n▓  ██▒ ▓▒▓██▒▒████▄    ▒██▀ ▀█  \n▒ ▓██░ ▒░▒██▒▒██  ▀█▄  ▒▓█    ▄ \n░ ▓██▓ ░ ░██░░██▄▄▄▄██ ▒▓▓▄ ▄██▒\n  ▒██▒ ░ ░██░ ▓█   ▓██▒▒ ▓███▀ ░\n  ▒ ░░   ░▓   ▒▒   ▓▒█░░ ░▒ ▒  ░\n    ░     ▒ ░  ▒   ▒▒ ░  ░  ▒   \n  ░       ▒ ░  ░   ▒   ░        \n          ░        ░  ░░ ░      \n                       ░   \n\n                           https://github.com/activiste                           \n    ';H=T();I=T();C=F.split(G);J=len(C);K=a.get_terminal_size().columns
	for(L,E)in enumerate(C):
		if E.strip():M=L/(J-1);N=b(H,I,M);O=f(E,K);D.stdout.write(N+O+B+G);D.stdout.flush();S.sleep(.01)
		else:A()
def H(text,speed=.01):
	for B in text:D.stdout.write(B);D.stdout.flush();S.sleep(speed)
	A()
def g(url):
	try:B=R.gethostbyname(url);return B
	except R.gaierror:A('Invalid IP or Domain format.');D.exit(1)
def h(ip):A=f"https://shodan.io/host/{ip}";B=Z.get(A);return B.text
def i(content):B=Q(content,V);A=list(set([A for A in B.stripped_strings if A.startswith('CVE-')]));A.sort(key=lambda x:x.split('-')[1],reverse=F);C=[(A,f"https://www.cve.org/CVERecord?id={A}")for A in A];return C
def j(content):
	B=Q(content,V);A=B.find('div',id='ports')
	if A:C=[A.get_text(strip=F)for A in A.find_all('a',class_='bg-primary')];return C
	return[]
def k(ip):
	try:B=dns.reversename.from_address(ip);C=str(B);D=dns.resolver.resolve(C,'PTR');return[str(A)[:-1]for A in D]
	except dns.resolver.NXDOMAIN:return[]
	except U as E:A(f"Error resolving domains: {E}");return[]
def l(cve):
	try:A=K.run([M,cve],capture_output=F,text=F);return A.stdout
	except FileNotFoundError:return'searchsploit not found. Please ensure the path is correct.'
	except U as B:return f"Error occurred: {B}"
def m():A='choice';B=[P.List(A,message='What do you need ?',choices=[W,X,Y])];C=P.prompt(B);return C[A]
def n():
	b='\nPress Enter to return to the menu...';M='\x1b[31m';d();e()
	while F:
		E.system(J);N();L=m()
		if L==W:
			E.system(J);N();H('Who is your target ?\n',speed=.01);D=I('Target > ').strip()
			if D.startswith('http://')or D.startswith('https://'):D=D.split('://')[1]
			if not D.replace('.','').isdigit():K=g(D)
			else:K=D
			O=k(K)
			if O:P=G.join(O);Q='\x1b[32m'
			else:P='None found';Q=M
			R=h(K);S=j(R)
			if S:T=', '.join(S);U='\x1b[34m'
			else:T='No open ports found';U=M
			V=i(R)
			if V:f=[f"{A} - More info: {B}"for(A,B)in V];Z=G.join(f);a='\x1b[35m'
			else:Z='No CVEs found';a=M
			n=[[f"{C}IP Address{B}",K],[f"{C}Hostnames{B}",Q+P+B],[f"{C}Open Ports{B}",U+T+B],[f"{C}CVEs{B}",a+Z+B]];A(G);A(c(n,headers=[f"{C}Category{C}",f"{C}Details{C}"],tablefmt='grid'));H(b,speed=.01);I()
		elif L==X:E.system(J);N();H('Enter the exploit you are looking for (CVE ID / NAME)\n',speed=.01);o=I('Exploit > ').strip();p=l(o);A(p);H(b,speed=.01);I()
		elif L==Y:break
if __name__=='__main__':n()
