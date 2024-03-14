import subprocess
import os
import time
import random

def make_directory():  # creates a directory for the monolith downloads
	#directory = input("Directory name: ") # uncomment to allow input
	sitemap_xml = open("sitemap.xml","r")
	for line in sitemap_xml:
		if line.startswith("<url><loc>"):
			
			try:  
				directory = line.replace("<url><loc>https://","").replace("</loc></url>","").split("/")[0] + "-archive"
				print(directory)
				if os.path.isdir(directory) is True:  		# if directory already exist
					directory += "-archive"			  		# try appending "archive"
					if os.path.isdir(directory) is True:	# otherwise, start adding numbers
						n = 1
						while True:
							directory_n = directory + n
							if os.path.isdir(directory_n) is False:
								directory = directory_n
								break
							n += 1
				
				os.mkdir(directory)  
				
				sitemap_file = directory + "/sitemap.txt"
				print("Using new directory at: " + directory)
				return directory, sitemap_file
			except OSError as error:  
				continue
				
	# if all fails, try to create a default directory
	try:
		directory = "default_directory"
		os.mkdir(directory) 
	except:
		quit()
	print("Using new directory at:" + directory)
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
		time.sleep(random.uniform(0, 2)) # random pause of < 2sc; mimic human behaviour
		print ("line {} of {} ... {} ".format(n, total, line), end="")			
		line = line.replace("\n","")	# removes newline
		# Replaces non-filename-friendly characters in urls with better versions
		filename = line.replace("//","_").replace("/","_").replace(":","-") + ".html"
		# Runs monolith with the following:
		#	-v		don't download videos
		#	-j  	don't download javascript
		#	-t 30 	shorten timeout to 30 seconds
		#	-o		parses the output file name created earlier
		try:			
			monolith_cmd = "sudo monolith {} -s -v -j -t 30 -o {}".format(line, directory + "/" + filename)
			subprocess.run(monolith_cmd, shell=True)
		except:
			print("!! Error running", end="")
			continue
		n += 1
	
	url_list.close()

def cleanup(sitemap_file, xmlfile = "sitemap.xml"):
	os.unlink(sitemap_file)
	os.unlink(xmlfile)

def main():
	directory, sitemap_file = make_directory()
	create_textfile(sitemap_file)
	run_monolith(sitemap_file, directory)
	cleanup(sitemap_file)
	
main()