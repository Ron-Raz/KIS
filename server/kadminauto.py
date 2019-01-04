#!/usr/bin/env python2.7

import requests

session = requests.Session()
urls = {
	'authenticate': 'http://bnsf.mediaspace.kaltura.com/admin/authenticate',
	'staticpages': 'http://bnsf.mediaspace.kaltura.com/admin/config/tab/staticpages'
}

#
# authenticate
#

params = {
	'Login[username]': 'ron.raz@kaltura.com',
	'Login[password]': 'Liat1ush!',
	'Login[login]': 'Sign in'
}

myheaders = {
	'Host': 'bnsf.mediaspace.kaltura.com',
	'Connection': 'keep-alive',
	'Content-Length': '131',
	'Cache-Control': 'max-age=0',
	'Origin': 'http://bnsf.mediaspace.kaltura.com',
	'Upgrade-Insecure-Requests': '1',
	'DNT': '1',
	'Content-Type': 'application/x-www-form-urlencoded',
	'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
	'Referer': 'http://bnsf.mediaspace.kaltura.com/admin/config',
	'Accept-Encoding': 'gzip, deflate',
	'Accept-Language': 'en-US,en;q=0.9,he;q=0.8'
}
params = "Login%5Busername%5D=ron.raz%40kaltura.com&Login%5Bpassword%5D=Liat1ush%21&referrer=%2Fadmin%2Fconfig&Login%5Blogin%5D=%0D%0ASign+in"
r = session.post(urls['authenticate'], data=params, headers=myheaders)
print r.status_code
f = open("01.html","w")
f.write(r.text.encode('UTF-8'))
f.close()

#
# staticpages read
#

myheaders = {
	'Host': 'bnsf.mediaspace.kaltura.com',
	'Connection': 'keep-alive',
	'Cache-Control': 'max-age=0',
	'Upgrade-Insecure-Requests': '1',
	'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
	'DNT': '1',
	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
	'Accept-Encoding': 'gzip, deflate',
	'Accept-Language': 'en-US,en;q=0.9,he;q=0.8'
}

r = session.get(urls['staticpages'], headers=myheaders)
print r.status_code
f = open("02.html","w")
f.write(r.text.encode('UTF-8'))
f.close()
