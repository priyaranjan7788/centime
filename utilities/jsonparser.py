import json


def writejsonfile(jsoncontent,cpnyname):
    with open('outputjsons/'+cpnyname+'.json','w') as writer:
        json.dump(jsoncontent,writer)


def readjsonfile(cpnyname):
    with open('outputjsons/'+cpnyname+'.JSON','r') as reader:
       content= json.load(reader)
       return content

