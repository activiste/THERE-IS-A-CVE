b='Exit'
a='Search Exploit'
Z='Scan IP or URL'
Y='html.parser'
X='whatweb'
W='msfconsole'
Q=int
M='clear'
L=input
K=Exception
G=FileNotFoundError
F='\n'
B=True
A=print
import subprocess as E,sys as H,inquirer as R,requests as c
from bs4 import BeautifulSoup as S
import socket as T,time as U,dns.resolver
from tabulate import tabulate as e
import os as I,random as N,shutil as d
I.system(M)
C='\x1b[0m'
D='\x1b[1m'
O='./exploitdb/searchsploit'
def f():
	L='--version';F=False;H=B
	if not I.path.isfile(O):
		A(f"searchsploit not found at {O}. Installing from the repository.");M='git clone https://gitlab.com/exploit-database/exploitdb.git';C=E.run(M,shell=B)
		if C.returncode!=0:A('Failed to clone the exploitdb repository.');H=F
		else:A('exploitdb repository successfully cloned.')
	else:A('searchsploit is available.')
	J=B
	try:
		C=E.run([W,L],capture_output=B,text=B)
		if C.returncode!=0:raise G
		A('Metasploit is available.')
	except G:
		A('Metasploit not found. Installing Metasploit.');D='curl https://raw.githubusercontent.com/rapid7/metasploit-framework/master/scripts/omnibus/ubuntu.sh | bash';C=E.run(D,shell=B)
		if C.returncode!=0:A('Failed to install Metasploit.');J=F
		else:A('Metasploit successfully installed.')
	K=B
	try:
		C=E.run([X,L],capture_output=B,text=B)
		if C.returncode!=0:raise G
		A('WhatWeb is available.')
	except G:
		A('WhatWeb not found. Installing WhatWeb.');D='sudo apt-get install -y whatweb';C=E.run(D,shell=B)
		if C.returncode!=0:A('Failed to install WhatWeb.');K=F
		else:A('WhatWeb successfully installed.')
	return H,J,K
def V():return f"{N.randint(0,255):02X}{N.randint(0,255):02X}{N.randint(0,255):02X}"
def g(start_color,end_color,factor):B=[Q(start_color[A:A+2],16)for A in(0,2,4)];C=[Q(end_color[A:A+2],16)for A in(0,2,4)];A=[Q(B[A]+(C[A]-B[A])*factor)for A in range(3)];return f"[38;2;{A[0]};{A[1]};{A[2]}m"
def h(text,width):return text.center(width)
def P():
	E='\n▄▄▄█████▓ ██▓ ▄▄▄       ▄████▄  \n▓  ██▒ ▓▒▓██▒▒████▄    ▒██▀ ▀█  \n▒ ▓██░ ▒░▒██▒▒██  ▀█▄  ▒▓█    ▄ \n░ ▓██▓ ░ ░██░░██▄▄▄▄██ ▒▓▓▄ ▄██▒\n  ▒██▒ ░ ░██░ ▓█   ▓██▒▒ ▓███▀ ░\n  ▒ ░░   ░▓   ▒▒   ▓▒█░░ ░▒ ▒  ░\n    ░     ▒ ░  ▒   ▒▒ ░  ░  ▒   \n  ░       ▒ ░  ░   ▒   ░        \n          ░        ░  ░░ ░      \n                       ░   \n\n                           https://github.com/activiste                           \n    ';G=V();I=V();B=E.split(F);J=len(B);K=d.get_terminal_size().columns
	for(L,D)in enumerate(B):
		if D.strip():M=L/(J-1);N=g(G,I,M);O=h(D,K);H.stdout.write(N+O+C+F);H.stdout.flush();U.sleep(.01)
		else:A()
def J(text,speed=.01):
	for B in text:H.stdout.write(B);H.stdout.flush();U.sleep(speed)
	A()
def i(url):
	try:B=T.gethostbyname(url);return B
	except T.gaierror:A('Invalid IP or Domain format.');H.exit(1)
def j(ip):A=f"https://shodan.io/host/{ip}";B=c.get(A);return B.text
def k(content):C=S(content,Y);A=list(set([A for A in C.stripped_strings if A.startswith('CVE-')]));A.sort(key=lambda x:x.split('-')[1],reverse=B);D=[(A,f"https://www.cve.org/CVERecord?id={A}")for A in A];return D
def l(content):
	C=S(content,Y);A=C.find('div',id='ports')
	if A:D=[A.get_text(strip=B)for A in A.find_all('a',class_='bg-primary')];return D
	return[]
def m(ip):
	try:B=dns.reversename.from_address(ip);C=str(B);D=dns.resolver.resolve(C,'PTR');return[str(A)[:-1]for A in D]
	except dns.resolver.NXDOMAIN:return[]
	except K as E:A(f"Error resolving domains: {E}");return[]
def n(cve):
	try:A=E.run([O,cve],capture_output=B,text=B);return A.stdout
	except G:return'searchsploit not found. Please ensure the path is correct.'
	except K as C:return f"Error occurred: {C}"
def o(cve):
	try:A=E.run([W,'-q','-x',f"search {cve}; exit"],capture_output=B,text=B);return A.stdout
	except G:return'Metasploit not found. Please ensure it is installed.'
	except K as C:return f"Error occurred: {C}"
def p(output):
	B=output.split(F);A=[]
	for C in B:
		D=C.split(', ')
		for E in D:A.append(E)
	return F.join(A)
def q(target):
	try:C=E.run([X,target],capture_output=B,text=B);D=C.stdout.strip();F=p(D);return F
	except K as G:A(f"Error getting additional info: {G}");return'No additional info found'
def r():A='choice';B=[R.List(A,message='What do you need?',choices=[Z,a,b])];C=R.prompt(B);return C[A]
def s():
	d='\nPress Enter to return to the menu...';H='\x1b[31m';t,u,v=f()
	while B:
		I.system(M);P();K=r()
		if K==Z:
			I.system(M);P();J('Who is your target?\n',speed=.01);E=L('Target > ').strip()
			if E.startswith('http://')or E.startswith('https://'):E=E.split('://')[1]
			if not E.replace('.','').isdigit():G=i(E)
			else:G=E
			N=m(G)
			if N:O=F.join(N);Q='\x1b[32m'
			else:O='None found';Q=H
			R=j(G);S=l(R)
			if S:T=', '.join(S);U='\x1b[34m'
			else:T='No open ports found';U=H
			V=k(R)
			if V:W=F.join([f"{A} - {B}"for(A,B)in V]);X='\x1b[35m'
			else:W='No CVEs found';X=H
			Y=q(E);g='\x1b[33m'if Y else H;h=[[f"{D}IP Address{C}",G],[f"{D}Hostnames{C}",Q+O+C],[f"{D}Open Ports{C}",U+T+C],[f"{D}Technologies{C}",g+Y+C],[f"{D}CVEs{C}",X+W+C]];A(F);A(e(h,headers=[f"{D}Category{D}",f"{D}Details{D}"],tablefmt='grid'));J(d,speed=.01);L()
		elif K==a:I.system(M);P();J('Enter the exploit you are looking for (CVE ID / NAME)\n',speed=.01);c=L('Exploit > ').strip();p=n(c);A(p);s=o(c);A(s);J(d,speed=.01);L()
		elif K==b:break
if __name__=='__main__':s()
