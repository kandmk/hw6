#!/usr/bin/env python
# -*- coding: utf-8 -*-

import webapp2

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html; charset=UTF-8'
        self.response.write(u'<html><body><form action="/">1:<input name="one" type="text" /><br />2:<input name="two" type="text" /><br /><button type="submit">Enter</button><p>%s</p></form></body></html>' % (self.patatokukasi()))

    def patatokukasi(self):
        ret = []
        one = self.request.get("one")
        two = self.request.get("two")
        num1 = len(one)
        num2 = len(two)
        if num1 >= num2:
            for num in range(num1):
                if num < num2:
                    ret.append(one[num])
                    ret.append(two[num])
                else:
                    ret.append(one[num])
        else:
            for num in range(num2):
                if num < num1:
                    ret.append(one[num])
                    ret.append(two[num])
                else:
                    ret.append(two[num])
        ret = "".join(ret)
        return ret
        #self.response.write(u'<html><body><p>ret</p></body></html>')               

app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
