# HTTP
# POST, GET, PUT, PATCH
# send http request get back response
# body is HTML
# status code is returned:
"""200, good to go \n
300 redirect
400 permissions not found"""

'''
1. request the datas
 - parse the datas
 - find the "a" tags
 - if href is local expand it
 - append all new hrefs that have not been visited
 to the list of sites to visited
 - add current site to history
 - work with data
'''

```
<a href = url
GET href HTTP version
```

'''
BASIC
import requests from vs4 import BEAUTIFUL SOUP
from url parse import url parse

to_visit = sites to visit
# pre populate with sites to visit
history = []
while:
    there are sites to visited
    try:
        next_site = to_visit.pop()
        req = requests.get next_site
        if req.status_code
            is not interesting (200):
            ignore
    else:
        data = req.text
        # the body to save
        process data and add to history
    except:
        handle error
'''
'''
PROCESS DATA

soup = Beautiful Soup(data, "html")
for link in soup.find_all("a", href = "True"):
    link = urlparse( this url, link["href"])
    if link is in history:
        ignore
    else:
        add to sites to visit
'''
