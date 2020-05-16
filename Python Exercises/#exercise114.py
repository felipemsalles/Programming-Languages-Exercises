# exercise114

import urllib
import urllib.request
try:
    site = urllib.request.urlopen('http://www.pudding.com.br')
except urllib.error.URLError:
    print('Error Web Site.')
else:
    print('Successful Accessed.')
finally:
    print('See you!')
    print(site.read)  # get the site content.
