import web
import os
import sys

urls = (
    '/', 'index'
)

def fileTest():
    output = open('data.txt', 'w')
    output.write("web.ctx.ip="+"\n")
    output.close()

class index:
    def GET(self):
        return "Hello, world!"

if __name__ == "__main__":
    app = web.application(urls, globals())
    fileTest()
    app.run()