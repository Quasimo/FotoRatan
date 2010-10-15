#coding:utf-8
import re,logging,os
from google.appengine.ext import db
from google.appengine.api import memcache
class Images(db.Model):
    name = db.StringProperty()
    mime = db.StringProperty()
    size = db.IntegerProperty()
    created_at = db.DateTimeProperty(auto_now_add=True)
    description = db.TextProperty()
    width = db.IntegerProperty()
    height = db.IntegerProperty()
    filetype=db.StringProperty()

    bf = db.BlobProperty() #binary file
    
    def put(self):
        super(Images,self).put()
        
    def delete(self):
        key=str(self.key().id())+"image"
        memcache.delete(key)
        super(Images,self).delete()
        
    @property
    def id(self):
        return str(self.key().id())
    
    @property
    def imgurl(self):
        return "http://%s/image/%s/" %(os.environ['HTTP_HOST'],self.key().id())
        
    @property
    def showurl(self):
        return "http://%s/show/%s/" %(os.environ['HTTP_HOST'],self.key().id())        
        
class Counter(db.Model):
    count = db.IntegerProperty(required=True, default=0)        