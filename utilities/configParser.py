import configparser
import os
import datetime

def getConfig(filepath):
    con = configparser.ConfigParser()
    con.read(filepath)
    return con



