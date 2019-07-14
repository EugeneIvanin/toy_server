import web
import webbrowser

from PIL import Image
import time
import argparse
import subprocess
import sys
import os



web.config.debug = False
web.config.session_parameters['cookie_path'] = '/'
        

urls = ("/", "index", 
	"/result", "result")

app = web.application(urls, globals())
render = web.template.render('templates/', cache = False)


if web.config.get('_session') is None:
    session = web.session.Session(app, web.session.DiskStore('sessions'), {'filter_url': "", 'origin_url': ""})
    web.config._session = session
else:
    session = web.config._session


  
class index:
    def GET(self):
        imageBinary = open("/home/ubuntu/toy_server/egor.jpg",'rb').read()
        return imageBinary

    def POST(self):
        x = web.input(myfile={})
	
	filedir = '/home/ubuntu/toy_server'
        filepath = x.myfile.filename.replace('\\', '/')
        fout = open(filedir + '/' + 'content.png', 'w')
        fout.write(x.myfile.file.read())
        fout.close()
	im = Image.open('/home/ubuntu/toy_server/content.png')
	filtered_im = im.convert('L')
	time.sleep(8)
	filtered_im.save('/home/ubuntu/toy_server/result.png')
	
        raise web.seeother('/result')
  
      
class result:
    def GET(self):
        imageBinary = open("/home/ubuntu/toy_server/result.png",'rb').read()
        return imageBinary



if __name__ == "__main__":
    app.run()
