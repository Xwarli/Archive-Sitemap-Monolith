import subprocess
import os

def make_directory():  # creates a directory for the monolith downloads
	directory = input("Directory name: ")
	try:  
 	   os.mkdir(directory)  
	except OSError as error:  
 	   print(error) 
 	   
	sitemap_file = directory + "/sitemap.txt"
	return directory, sitemap_file


def create_textfile(sitemap_file):
	xmlfile = open("sitemap.xml","r")
	xmlfile2 = open(sitemap_file, "w+")
	for line in xmlfile:
		if line.startswith("<?xml"):		# checks for and skips header
			continue
		elif line.startswith("<urlset"):	# checks for and skips header
			continue
		elif "http" in line:				# if url, strips out xml tags
			xmlfile2.write(line.replace("<url><loc>","").replace("</loc></url>",""))	
	xmlfile.close()
	xmlfile2.close()

def run_monolith(sitemap_file, directory):

	url_list = open(sitemap_file, "r")
	
	# Count how many URL there are to parse
	with open(sitemap_file) as f:	
		total = sum(1 for _ in f)
	
	# Run monolith
	n = 1
	for line in url_list:	
		print ("line {} of {} ... {} ".format(n, total, line), end="")			
		line = line.replace("\n","")	# removes newline
		# Replaces non-filename-friendly characters in urls with better versions
		filename = line.replace("//","_").replace("/","_").replace(":","-") + ".html"
		# Runs monolith with the following:
		#	-v		don't download videos
		#	-j  	don't download javascript
		#	-t 30 	shorten timeout to 30 seconds
		#	-o		parses the output file name created earlier
		monolith_cmd = "sudo monolith {} -s -v -j -t 30 -o {}".format(line, directory + "/" + filename)
		subprocess.run(monolith_cmd, shell=True)
		n += 1
	
	url_list.close()

def main():
	directory, sitemap_file = make_directory()
	create_textfile(sitemap_file)
	run_monolith(sitemap_file, directory)
	
main()






