#-----------------------------------------------------------------------------------------
# Code from https://github.com/Haikson/sitemap-generator
# 	Very slight modification
#-----------------------------------------------------------------------------------------

import sys
import logging
from pysitemap import crawler
from pysitemap.parsers.lxml_parser import Parser

if __name__ == '__main__':
    if '--iocp' in sys.argv:
        from asyncio import events, windows_events
        sys.argv.remove('--iocp')
        logging.info('using iocp')
        el = windows_events.ProactorEventLoop()
        events.set_event_loop(el)

    # root_url = sys.argv[1]
    while True:
    	try:
    		root_url = input("Start URL: ")
    		if root_url.startswith("http"):
    			break
    		else:
    			print("URL must start with 'http'")
    	except:
    		continue
    crawler(
        root_url, out_file='sitemap.xml', exclude_urls=[".pdf", ".jpg", ".zip"],
        http_request_options={"ssl": False}, parser=Parser
    )
    
    
