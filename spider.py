import subprocess

# aquires all the links from a page
def find_links(url):
	print("... scanning " + url)
	### https://stackoverflow.com/a/2804721###
	command = """wget -q {} -O - | \
		tr "\t\r\n'" '   "' | \
		grep -i -o '<a[^>]\+href[ ]*=[ \t]*"\(ht\|f\)tps\?:[^"]\+"' | \
		sed -e 's/^.*"\([^"]\+\)".*$/\1/g'
		""".format(url)
	
	raw_list = subprocess.run(command, shell=True, capture_output=True, text=True)
		
	if raw_list.returncode == 0:
		# Read the output
		raw_output = open("rl-temp.txt","a")
		raw_output.write(raw_list.stdout)
		raw_output.close()
		return 
		
	else:
		# Handle the case when the process fails
		print("Error:", raw_list.stderr)
		exit
			

# sorts urls into a list, with no duplicates or within blacklist
def sort_urls(url_list, raw_list):
	url_file = open("rl-temp.txt","r")
	
	# creates local blacklist of top domains to avoid
	blacklist = []
	for line in open("top1000urls.txt","r"):
		line = line.rstrip("\n")
		blacklist.append(line)
		blacklist.append("www." + line)
	for line in url_file:
		if line.startswith('<a href=') is True:
			a = line.replace('<a href="https://',"").replace('<a href="http://',"")
			a = a.split("/")[0]
			if a not in url_list and a not in blacklist:
				url_list.append(a.rstrip("\n"))
		
	return url_list
	url_file.close()

url_list = []
rawtext = find_links(input("Start URL: "))
depth = int(input("Spider depth: "))
n = 1
if depth == 1:
	url_list = sort_urls(url_list, rawtext)
elif depth > 0:
	n = 1
	checked_urls = []
	url_list = sort_urls(url_list, rawtext)
	while n < depth:
		tmp_url_list = []
		for m in url_list:
			if m not in checked_urls:
				rawlinks = find_links(m)
				tmp_url_list = sort_urls(tmp_url_list,rawlinks)
		
		for item in tmp_url_list:
			checked_urls.append(item)
			url_list.append(item)
		
		n += 1
else:
	print("Error, defaulting to single depth")
	url_list = sort_urls(url_list, rawtext)


spider_list = open("spiderlist.txt","w+")
for url in url_list:
	spider_list.write(url)
sipder_list.close()
print(url_list)

