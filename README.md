<h1 align="center">IERT DJANGO WEBAPP</h1>


This is my college website created using python (django framework) at backend . Some of the features of website include implementation of login/logout system for students , it's a responsive website which is also a standalone progressive web app and provide dynamic notification and content from backend.

<p align="center"><img src="iert.png"/></p>

# Django

Django is an open-source python web framework used for rapid development, pragmatic, maintainable, clean design, and secures websites. A web application framework is a toolkit of all components need for application development. The main goal of the Django framework is to allow developers to focus on components of the application that are new instead of spending time on already developed components. Django is fully featured than many other frameworks on the market. It takes care of a lot of hassle involved in the web development; enables users to focus on developing components needed for their application.


Dependencies
------------

create a virtualenv and run req.sh<br/>
<b>virtualenv</b> 
<pre>pip install virtualenv</pre>
<b> what is virtual environment ? </b><br/>
A virtual environment is a tool that helps to keep dependencies required by different projects separate by creating isolated python virtual environments for them. This is one of the most important tools that most of the Python developers use.
<br/>
<a href="https://www.geeksforgeeks.org/python-virtual-environment/" >read more... </a>

to run req.sh
<pre>bash req.sh</pre>


 Screenshot  
------------

  ![alt text](https://github.com/itsvinayak/iert_django_webapp/blob/master/screen.png)
  
  
  # some important things 
  
<ul>
<li>
 
 is_superuser  
------------
 
 <code>is_superuser</code>  is a flag on the User model to see list of superusers.
 as to get name of all users we type,
 <pre>User.objects.all() </pre>
 
 to get all superuser we type,
 <pre> User.objects.filter(is_superuser=True) </pre>
 
 <a href="https://stackoverflow.com/questions/45275897/how-to-get-superuser-details-in-django" target="_blank">source</a>
 </li>

<li>
 
 CSRF_COOKIE_SECURE=True/SESSION_COOKIE_SECURE = True  
------------
 it is false by default
 <code>CSRF_COOKIE_SECURE=True/SESSION_COOKIE_SECURE = True</code> Whether to use a secure cookie for the CSRF cookie. If this is set to True, the cookie will be marked as “secure,” which means browsers may ensure that the cookie is only sent under an HTTPS connection.
<b>use only if you are using https connection</b>

 <a href="https://docs.djangoproject.com/en/1.7/ref/settings/#csrf-cookie-secure" target="_blank">source</a>
 </li>
 
 <li>
  
 SESSION_EXPIRE_AT_BROWSER_CLOSE = True  
------------

<code>SESSION_EXPIRE_AT_BROWSER_CLOSE = True</code> Django will use browser-length cookies -- cookies that expire as soon as the user closes his or her browser. Use this if you want people to have to log in every time they open a browser.
Closing the tab or window does not count as closing the browser. Make sure you quit the browser program to end a browser session.

<a href="https://stackoverflow.com/questions/3976498/why-doesnt-session-expire-at-browser-close-true-log-the-user-out-when-the-bro" target="_blank">source</a>
 </li>

</ul>


<strong>made by vinayak with 💕 and 💻</strong>

