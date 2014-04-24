#!/home/tsubuyaki_rock/bin/python
# vim: fileencoding=utf-8 :

import urllib2

from tweepy import API, OAuthHandler, TweepError
from lxml import etree

SRC_URL = 'http://www.lilyfranky.com/tsubuyaki/'

CONSUMER_KEY = 'put consumer key here.'
CONSUMER_SECRET = 'put consumer secret here.'
ACCESS_KEY = 'put access key here.'
ACCESS_SECRET = 'put access secret here.'

def main():

    # create authentication handler.
    auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
    # create api handler.
    api = API(auth)
    # retrieve source data.
    try:
        data = urllib2.urlopen(SRC_URL)
    except:
        #TODO: logic implements.
        return
    # parse data.
    html = etree.parse(data, parser=etree.HTMLParser())
    for k in ['man', 'woman',]:
        p = html.xpath('//div[@id="%s"]/div[@class="txt"]' % k).pop(0)
        txt = p.xpath('./p[position()=1]/text()').pop(0)
        status = p.xpath('./p[position()=2]/span/text()').pop(0)
        # update status.
        try:
            api.update_status(u"%s%s" % (txt, status))
        except TweepError, e:
            print('%s: %s' % (k, e))

if __name__ == '__main__':
    main()
