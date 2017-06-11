import cgibin.py.facebook as pyfb


class main:
	def __init__(self,rootpath):
 		self.name = "index"
 		self.rootpath =rootpath

	def api_facebook(self,package):
		event = pyfb.main(self.rootpath)
		result = event.crawler_csv(package)
		return result
