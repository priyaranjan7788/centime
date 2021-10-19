import datetime

def getfeaturefilename(filename):
    return filename.replace("features/", "").replace(".feature", "")


def getdateandtime():
    return "{}".format(datetime.datetime.now()).replace(" ","").replace(":","-")[0:-7]
