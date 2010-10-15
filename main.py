#coding:utf-8
import wsgiref.handlers
import os
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.api import users
import methods
import logging
def format_date(dt):
    return dt.strftime('%a, %d %b %Y %H:%M:%S GMT')

class PublicPage(webapp.RequestHandler):
    def render(self, template_file, template_value):
        path = os.path.join(os.path.dirname(__file__), template_file)
        self.response.out.write(template.render(path, template_value))
    
    def error(self,code):
        if code==400:
            self.response.set_status(code)
        else:
            self.response.set_status(code)
            
    def is_admin(self):
        return users.is_current_user_admin()
    
    def head(self, *args):
        return self.get(*args) 
    
class MainPage(PublicPage):
    def get(self,page):
        index=0 if page=="" else int(page)
        images=methods.getAllImages(index)
        prev,next=methods.getPageing(len(images), index)
        template_value={"images":images[:10],"prev":prev,"next":next, "logout":users.create_logout_url("/")}
        self.render('views/index.html', template_value)

class ShowImage(PublicPage):
    def get(self,id):
        image=methods.getImage(id)
        if not image:return self.error(404)
        template_value={"image":image,"admin":self.is_admin()}
        self.render('views/show.html', template_value)
    
    
class GetImage(PublicPage):
    def get(self,size,id):
        dic=self.request.headers
        key=dic.get("If-None-Match")
        self.response.headers['ETag']=size+id
        if key and key==size+id:
            return self.error(304)
        image=methods.downImage(id, size)
        if not image:
            return self.error(404)
        self.response.headers['Content-Type'] = str(image.mime) 
        self.response.headers['Cache-Control']="max-age=315360000"
        self.response.headers['Last-Modified']=format_date(image.created_at)
        self.response.out.write(image.bf)

class Error(PublicPage):
    def get(self):
        return self.error(404)
        
class AboutPage(PublicPage):
    def get(self):
        template_value={}
        self.render('views/about.html', template_value)                       

def main():
    application = webapp.WSGIApplication(
                                       [('/(?P<page>[0-9]*)/?', MainPage),
                                       	('/about', AboutPage),
                                        (r'/(?P<size>image)/(?P<id>[0-9]+)/?',GetImage),
                                        (r'/(?P<size>s)/(?P<id>[0-9]+)/?',GetImage),
                                        (r'/show/(?P<id>[0-9]+)/',ShowImage),
                                        ('.*',Error)
                                       ], debug=True)
    wsgiref.handlers.CGIHandler().run(application)

if __name__ == "__main__":
    main()