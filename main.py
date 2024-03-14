import subprocess

try:
	subprocess.run("sudo python3 crawler.py", shell=True)
except:
	pass
	
subprocess.run("sudo python3 sitemap-monolith.py", shell=True)