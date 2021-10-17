from utilities.configParser import *
import requests


# def buildURL(clientName,timeevent):
#     con = getConfig('utilities/config.ini')
#     url = con['API']['baseurl']+'function='+timeevent+'&symbol='+clientName+'&apikey=demo'
#     return url


def buildURL(clientName,timeevent,output):
    con = getConfig('utilities/config.ini')
    if output== "null":
        url = con['API']['baseurl'] + 'function=' + timeevent + '&symbol=' + clientName + '&apikey='+con['API']['key']
    else:
        url = con['API']['baseurl']+'function='+timeevent+'&symbol='+clientName+'&outputsize='+output+'&apikey='+con['API']['key']
    return url


def geturl(url):
    response=requests.get(url)
    return response
