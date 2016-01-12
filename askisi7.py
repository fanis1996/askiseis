import urllib2
import json

def weather(x,y,appid):
    if appid == " " : appid = "c18a86635fb26190c538298412e282ea"
    url =urllib2.Request("http://api.openweathermap.org/data/2.5/weather?lat="+x+"&lon="+y+"&units=metric&appid="+appid)
    response = urllib2.urlopen(url)
    data = response.read()
    jsd = json.loads(data)
    temparture= jsd['main']['temp']
    weatherid = jsd['weather'][0]['id']
    if weatherid >=200 and weatherid < 600:
        print "I'm singing in the rain!"
        if temparture > 20 : print "nice..."
        if temparture < 5 : print "brrrr"

x = raw_input("X=")
y = raw_input("Y =")
appid = raw_input("insert your appdid from http://openweathermap.org (or press space and enter to use the default one) : ")
weather(x,y,appid)