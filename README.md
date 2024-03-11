# Sitemap_Monolith
** Using Monolith and Sitemap Generator to Archive an entire website in html format **

USAGE: Download and execute main.py as a superuser (sudo python3 main.py)

Uses two other repositories (please install before running Sitemap_Monolith):

Monolith (for the archiving) --> https://github.com/Y2Z/monolith

sitemap-generator (for the sitemap) --> https://github.com/Haikson/sitemap-generator

Essentially it takes a start url, and then generates an XML sitemap with sitemap-generator
Sitemap-Monolith then takes this XML file and strips out tags to generate a txt file of urls. These are then passed one-by-one into monolith to create archive pages.
