#  for web.py

import web


# get actual ip address
def get_ip():
    ipAddress = web.ctx.env.get('HTTP_X_FORWARDED_FOR', web.ctx.get('ip', ''))
    if '' != ipAddress:
        ipAddress = str(web.ctx.ip)
    print 'ipAddress is ' + ipAddress
    return ipAddress


if __name__ == '__main__':
    ip = get_ip()