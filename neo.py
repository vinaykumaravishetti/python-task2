#!/usr/bin/python3
import cgi

print("content-type:text/html\r\n\r\n")
print("<html><body  style='background-image: url(bg.jpg)'>")
print("<h1 style='text-align:center'>HI,I'm Neo.</h1><h4 style='text-align:center'>I am at your Service</h4>")
print("<center><img src='robo.jpg' width='50' height='60'></center>")


import subprocess
form=cgi.FieldStorage()
if form.getvalue("name"):
	name=form.getvalue("name")
	if("calendar" in name):
		x=subprocess.getoutput('cal')
	elif("date" in name):
		x=subprocess.getoutput('date')
	elif("firefox" in name):
		x=subprocess.Popen('firefox')
	elif("calculator" in name):
		x=subprocess.Popen('gnome-calculator')

print("<form method='post' action='neo.py'>")
print("<p>What can I do for you:<input type='textarea' name='name'/><input type='submit' value='Submit' /></p> ")
print("</form>")
print(x)
print("</body></html>")
