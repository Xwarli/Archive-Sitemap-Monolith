import subprocess

print("Crawling...")
subprocess.run("sudo python3 crawler.py", shell=True)
print("\nArchiving...")
subprocess.run("sudo python3 sitemap-monolith.py", shell=True)