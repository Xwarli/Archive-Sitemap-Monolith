import sys
import logging
from pysitemap import crawler
from pysitemap.parsers.lxml_parser import Parser
from urllib.parse import urlparse

def truncate_url(url):		
    parsed_url = urlparse(url)
    if parsed_url.netloc:
        return parsed_url.scheme + "://" + parsed_url.netloc	# Output: https://www.example.com
    else:
        return None

#-----------------------------------------------------------------------------------------
# Below code from https://github.com/Haikson/sitemap-generator
# 	Very slight modification
#-----------------------------------------------------------------------------------------
if __name__ == '__main__':
    if '--iocp' in sys.argv:
        from asyncio import events, windows_events
        sys.argv.remove('--iocp')
        logging.info('using iocp')
        el = windows_events.ProactorEventLoop()
        events.set_event_loop(el)

    
    root_url = truncate_url(input("Start URL: ")) # Extracs home URL from input
    #root_url = sys.argv[1]
    crawler(
        root_url, out_file='sitemap.xml', exclude_urls=[".pdf", ".jpg", ".zip"],
        http_request_options={"ssl": False}, parser=Parser
    )
    
    
