import json
import os


def writejsonfile(jsoncontent,cpnyname):

    with open(cpnyname+'.json','w') as writer:
        json.dump(jsoncontent,writer)


def readjsonfile(cpnyname):
    with open(cpnyname+'.JSON','r') as reader:
       content= json.load(reader)
       return content

