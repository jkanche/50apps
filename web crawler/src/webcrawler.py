'''
Created on Jan 21, 2012

@author: Jayaram
'''


import BeautifulSoup
import urllib2  

url_input = raw_input("Enter the Web URL ")
depth = raw_input("Enter the level of search ")
keyword = raw_input("Enter the search keyword ")

url_input = "http://"+url_input
depth = int(depth)

found = []
all_url = []

def search_key(url,depth,keyword):
    all_url.append(url)
    
    request_html = urllib2.Request(url)
    response_html = urllib2.urlopen(request_html)
    soup_html = BeautifulSoup.BeautifulSoup(response_html)
    
    if len(soup_html.findAll(text = keyword)) != 0 :
        found.append(url)
        
    if depth > 0 :        
        for i in soup_html.findAll('a'):
            if i['href'].find('#') != 0 and i['href'].find('ftp') == -1 and i['href'].find('(') == -1:
                if i['href'] not in all_url:
                    if i['href'].find('/') == 0:
                        search_key(url_input + i['href'], depth-1 , keyword)
                    elif i['href'].find('http') == -1 and i['href'].find('https') == -1:
                        search_key(url_input + '/' + i['href'], depth-1 , keyword)
                    else:
                        search_key(i['href'] , depth - 1, keyword)
    else :
        return
    

search_key(url_input,depth,keyword)
if len(found) == 0:
    print "Search retured no results"
else :
    print found
    
    
    
    