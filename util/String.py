import time

class String(object):

    def getNowTime(fomart = '%Y-%m-%d'):
        c1 = time.localtime()
        c2 = time.strftime('%Y%m%d', c1)
        return c2

    def nullTurn0(str):
        if str.strip() == '':
            return 0
        if str.strip() == None:
            return 0
        if str.strip() == 'None':
            return 0
        return str

