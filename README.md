FotoRatan
=========

FotoRatan(图藤) is an open source software package for creating and supporting image hosting. It's written in Python and running on [Google App Engine](http://code.google.com/appengine), which is a free and robust cloud hosting infrastructure.

[FotoRatan.appspot.com](http://fotoratan.appspot.com/), also a demo of FotoRatan. It shows Some Friends' high-quality original work. To ask for testing account please mail to linuximo@gmail.com

FotoRatan is based on GAE image hosting program [diabloimage](http://code.google.com/p/diabloimage)

Features
--------
* Easy to use
* Host on Google App Engine
* Optimized for modern browsers
* Optimized font end for tablet or mobile devices
* HTML5

Installation
------------
It's recommended to get the latest codebase of FotoRatan with git:

        git clone git://github.com/Quasimo/FotoRatan.git
Then you can rename FotoRatan to whatever you want to match your own App Engine AppID. And follow the steps:

1.  Change app.yaml application to match your own AppID.
2.  Add this folder to Google App Engine Launcher as an existing application, and click Deploy. 
3.  End.

If you have any questions or feature requests, feel free to discuss it in official development node at [GeeKaa](http://geekaa3.appspot.com):
http://geekaa3.appspot.com/go/fotoratan

Usage
-----
1.  Put app's url in browser and key 'Enter' in your keyboard.
2.  Click "Upload!" button in the app then sign in via your app engine developer account.(*If your are using iPhone / iPod Touch you may not see the button*)
3.	Select a image in your computer and then click the upload button in this form.
4.	Can't you see online now?
5.	Click the "Sign out" link in footer to sign out.

Need Some Help!
---------------
* Larger Than 1Mb Upload Per File.
	*now just 1Mb, it's small.*
* Multiple Uploader
	*You can try http://YOUR-APP-URL/admin/upload2/ but it dosen't works.*
* Multiple User
	*Now you can invite other developers to collaborate on your application is [appengine](https://appengine.google.com/) dashboard > Administration > Permissions , then the developers are be able to upload images in your app, but User A can delete images that upload by User B now, I wish there some permissions to save one user's images that never deleted by others.*
* Site Configurator
	*To generate site infomations like title and descriptions, to create pages, to switch themes.*
* Theme
	*in static/themes*

Quota and Performance
---------------------
See [Google App Engine - Billing and Budgeting Resources](http://code.google.com/intl/en/appengine/docs/billing.html#Setting_a_Daily_Budget)

License
-------
FotoRatan under [GNU Lesser General Public License](http://www.gnu.org/licenses/lgpl.html)

Special Thanks
--------------
* [Benmao](http://github.com/benmao) *He created diabloimage that FotoRatan is base on.*
* [Livid](http://github.com/livid) *I love his works and this README is copies somethings from [Project Babel 2](http://github.com/livid/v2ex/blob/master/README.md)*
* [ZRUB](http://www.zurb.com) *[Absolutly, I love ZURB](http://geekaa3.appspot.com/t/201), I use the CSS3 buttons from them in FotoRatan.*
* [Fennel](http://chagallsilk.blogbus.com/) *Always support my works.*
* [Hgta](http://geekaa3.appspot.com/member/hgta) *Comrade in arms in these years.*