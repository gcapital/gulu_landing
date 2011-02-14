""" Gulu search utility functions """

__author__ = "Gage Tseng <gage.tseng@gmail.com>"
__version__ = "$Id:$"

import urllib2, urllib

class Ycas():
	
	data = {
		'appid' : 'UX6cKNbV34GjjMw.H1BE89viP3yVUqGZmtM0u6c.BHFWhwCOirOq2DuR1QmH4gNw',
		'format' : 'json',
		'content' : '',
	}
	urlws = 'http://asia.search.yahooapis.com/cas/v1/ws'
	
	def ws(content):
		Ycas.data['content'] = content
		f = urllib2.urlopen(Ycas.urlws, urllib.urlencode(Ycas.data))
		return f.read()
	
	ws = staticmethod(ws)