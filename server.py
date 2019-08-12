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
        "/sculptures", "sculptures",
        "/result_sculptures", "result_sculptures",
        "/fruits", "fruits",
        "/result_fruits", "result_fruits",
        "/dashed", "dashed",
        "/result_dashed", "result_dashed",
        )

app = web.application(urls, globals())
render = web.template.render('templates/', cache=False)

if web.config.get('_session') is None:
    session = web.session.Session(app, web.session.DiskStore('sessions'), {'filter_url': "", 'origin_url': ""})
    web.config._session = session
else:
    session = web.config._session


class index:
    def GET(self):
        imageBinary = open("/home/ubuntu/toy_server/egor.jpg", 'rb').read()
        return imageBinary


class sculptures:
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
        filtered_im.save('/home/ubuntu/toy_server/result_sculp.png')

        raise web.seeother('/result_sculptures')


class result_sculptures:
    def GET(self):
        imageBinary = open("/home/ubuntu/toy_server/result_sculp.png", 'rb').read()
        return imageBinary


class fruits:
    def POST(self):
        x = web.input(myfile={})

        filedir = '/home/ubuntu/toy_server'
        filepath = x.myfile.filename.replace('\\', '/')
        fout = open(filedir + '/' + 'content.png', 'w')
        fout.write(x.myfile.file.read())
        fout.close()
        im = Image.open('/home/ubuntu/toy_server/content.png')
        filtered_im = im.rotate(30)
        time.sleep(8)
        filtered_im.save('/home/ubuntu/toy_server/result_fruits.png')

        raise web.seeother('/result_sculptures')


class result_fruits:
    def GET(self):
        imageBinary = open("/home/ubuntu/toy_server/result_fruits.png", 'rb').read()
        return imageBinary


class dashed:
    def POST(self):
        x = web.input(myfile={})

        filedir = '/home/ubuntu/toy_server'
        filepath = x.myfile.filename.replace('\\', '/')
        fout = open(filedir + '/' + 'content.png', 'w')
        fout.write(x.myfile.file.read())
        fout.close()
        im = Image.open('/home/ubuntu/toy_server/content.png')
        filtered_im = im.convert('L')
        filtered_im = filtered_im.rotate(30)
        time.sleep(8)
        filtered_im.save('/home/ubuntu/toy_server/result_dashed.png')

        raise web.seeother('/result_sculptures')


class result_dashed:
    def GET(self):
        imageBinary = open("/home/ubuntu/toy_server/result_dashed.png", 'rb').read()
        return imageBinary


if __name__ == "__main__":
    app.run()
