#coding:utf-8
from models import Images
from google.appengine.api import memcache
from google.appengine.api import images
from getimageinfo import getImageInfo

def addImage(mime,description,bf,name):
    'Add Image'
    image=Images(mime=mime,description=description,bf=bf,name=name)
    image.size=len(image.bf)
    image.filetype,image.width,image.height=getImageInfo(bf)
    image.put() 
    return image

def addImage2(bf):
    image=Images(bf=bf)
    image.size=len(bf)
    image.filetype,image.width,image.height=getImageInfo(bf)
    if not image.filetype:return None
    image.mime=image.filetype
    image.put()
    return image

def getImage(id):
    id=int(id)
    return Images.get_by_id(id)

def resizeImage(id,size="image"):
    image=getImage(id)
    if not image:return None
    if size=="image":return image
    img=images.Image(image.bf)
    img.resize(width=125, height=125)	
    img.im_feeling_lucky()
    image.bf=img.execute_transforms(output_encoding=images.JPEG)
    return image

def downImage(id,size="image"):
    key=id+size
    image=memcache.get(key)
    if not image:
        image=resizeImage(id, size)
        memcache.set(key,image,3600*10)
    return image

def delImage(key):
    image=Images.get(key)
    if image:image.delete()
    
def getAllImages(index=0):
    return Images.all().order('-created_at').fetch(11,index*10)

def getPageing(index,page=0):
    s="/%s/"
    if page==0:
        if index==11:return (None,"/1/")
        else:return (None,None)
    if index==11:
        return ("/",s%(page+1)) if page==1 else (s %(page-1),s%(page+1))
    return ("/",None) if page==1 else (s %(page-1),None)
    