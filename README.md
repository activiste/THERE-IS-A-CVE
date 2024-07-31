<h1 align="center">
  There is a CVE (TIAC) 🕵️ - ExploitDB & Metasploit Integration
</h1>
<p align="center">
  <img src="https://img.shields.io/badge/status-active-green" alt="Status: Active" />
</p>
<p align="center">
  <strong>There is a CVE</strong> is a pentesting tool that leverages 
  <img src="https://img.shields.io/badge/Shodan-%23000000.svg?style=for-the-badge&logo=shodan&logoColor=white" alt="Shodan" />
  to quickly identify vulnerabilities in internet-connected devices. It helps security professionals efficiently detect and assess security flaws. Additionally, it integrates 
  <img src="https://img.shields.io/badge/Metasploit-%23D23D2A.svg?style=for-the-badge&logo=metasploit&logoColor=white" alt="Metasploit" /> 
  for exploit searching and uses the 
  <img src="https://img.shields.io/badge/ExploitDB-%23D73A4A.svg?style=for-the-badge&logo=exploit-db&logoColor=white" alt="Exploit-db" /> 
  database to find relevant exploits.
</p>
<h2 align="center">
  <img src="https://i.ibb.co/MydBYsg/Capture-d-cran-du-2024-07-27-19-49-43.png" alt="Tool Image" width="600" />
</h2>
<h1>Features :</h1>
<p align="center"><strong>Interactive Menu :</strong> Scanning an IP address or URL and searching for exploits.</p>
<p align="center"><strong>Shodan Integration :</strong> Quickly retrieve information about an IP address including open ports and CVEs.</p>
<p align="center"><strong>Exploit Search :</strong> Enter a CVE ID or other identifiers to find relevant exploits using searchsploit, Metasploit, or the ExploitDB database.</p>
<h2 align="center">
  <img src="https://img.shields.io/badge/Installation-%F0%9F%9A%80-brightgreen" alt="Installation" />
</h2>
<p align="center"><strong>For Linux Users:</strong> TIAC can now be installed easily via pip:</p>
<pre><code>pip install there-is-a-cve</code></pre>
<ol>
  <li>
    Clone the repository (if you prefer manual installation):
    <pre><code>git clone https://github.com/activiste/there-is-a-cve.git</code></pre>
  </li>
  <li>
    Navigate to the project directory:
    <pre><code>cd there-is-a-cve</code></pre>
  </li>
  <li>
    Install requirements:
    <pre><code>pip install -r requirements.txt</code></pre>
  </li>
  <li>
    Run the tool:
    <pre><code>python main.py</code></pre>
  </li>
</ol>
<h2 align="center">
  <img src="https://img.shields.io/badge/Automatic%20Dependency%20Installation-%E2%9C%85-blue" alt="Automatic Dependency Installation" />
</h2>
<p align="center">
  If `searchsploit`, `exploitdb`, and Metasploit are not installed when you run the script, it will automatically install the necessary dependencies and clone the `exploitdb` repository for you. This ensures that all the required tools are available without any additional setup.
</p>
<h2 align="center">
  <img src="https://img.shields.io/badge/Coming%20Soon-%F0%9F%93%85-orange" alt="Coming Soon" />
</h2>
<p align="center">
  The next update will contain functionality to exploit vulnerabilities found directly in the tool.
</p>
<h2 align="center">
  <img src="https://img.shields.io/badge/Warning-%F0%9F%9A%A8-red" alt="Warning" />
</h2>
<p align="center">
  <strong>Note for Windows users:</strong> You may encounter issues running this tool on Windows. It is recommended to use a Linux virtual machine to ensure full functionality.
</p>
