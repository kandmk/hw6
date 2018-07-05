#!/usr/bin/env python
# -*- coding: utf-8 -*-

import webapp2
from google.appengine.api import urlfetch
import json
import jinja2

networkJson = urlfetch.fetch("https://alice.fantasy-transit.appspot.com/net?format=json").content  # ウェブサイトから電車の線路情報をJSON形式でダウンロードする
network = json.loads(networkJson.decode('utf-8'))  # JSONとしてパースする（stringからdictのlistに変換する）

tmpl = jinja2.Template(  # Jinjaのテンプレートエンジンを使ってHTMLを作ります
    u'''
    こういう線路があります： {{route}}
<body>
    <form action="/">
    乗車駅:<input name="start" type="text" />
    <br />
    下車駅:<input name="end" type="text" />
    <br />
    <button type="submit">検索</button></form>
</body>
''')

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html; charset=UTF-8'
        self.response.write(tmpl.render(network=network,route=self.calculate()))

    def calculate(self):#幅優先たんさくを書く
        start = self.request.get("start")
        end = self.request.get("end")
        queue = [start]
        check = []
        while queue:
            label = queue.pop(0)
            if label == end:
                check.append(label)
                return check
            if label not in check:
                check.append(label)
                queue += network.get(label, [])
        return check
        #return ["ookayama", "tsunashimi", "hatanodai"]
    
app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
