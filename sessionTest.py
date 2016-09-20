# sessionTest.py


import web
web.config.debug = False
urls = (
    "/count", "count",
    "/reset", "reset"
)
app = web.application(urls, locals())
session = web.session.Session(app, web.session.DiskStore('sessions'), initializer={'count': 0})


# get actual ip address
def get_ip():
    ipAddress = web.ctx.env.get('HTTP_X_FORWARDED_FOR', web.ctx.get('ip', ''))
    print 'ip is ' + ipAddress
    return ipAddress


class count:
    def GET(self):
        get_ip()
        session.count += 1
        return str(session.count)

class reset:
    def GET(self):
        session.kill()
        return ""

if __name__ == "__main__":
    app.run()