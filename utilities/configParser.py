import configparser
import os


def getConfig(filepath):
    con = configparser.ConfigParser()
    con.read(filepath)
    return con

