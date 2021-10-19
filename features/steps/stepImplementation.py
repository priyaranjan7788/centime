import _thread
import datetime
import logging
from behave import *

from utilities.webservices import *
from utilities.jsonparser import *
from utilities.genericmethods import *


logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

@given('the company name as "{cpnyName}" and function as "{tevent}" with outputsize as "{output}"')
def step_impl(context, cpnyName,tevent,output):
    context.url= buildURL(cpnyName,tevent,output)
    logger.info(context.url)


@when('user execute the AlphaAdvantage API')
def step_impl(context):
    context.response=geturl(context.url)
    logger.info(context.response)
    assert context.response.status_code == 200


@then('user captures the data for "{cpnyname}" company')
def step_impl(context,cpnyname):
    scename=context.feature.filename
    context.path= "{}{}{}".format("outputjsons/",getfeaturefilename(scename),getdateandtime())
    os.makedirs( context.path, 0o666)
    writejsonfile(context.response.json(),context.path+"/"+cpnyname)


@then(u'Validates the response is being captured for "{cpnyname}"')
def step_impl(context,cpnyname):
    context.data= readjsonfile(context.path+"/"+cpnyname)
    assert context.data["Meta Data"]["1. Information"] == "Daily Prices (open, high, low, close) and Volumes"
    assert context.data["Meta Data"]["2. Symbol"] == cpnyname


@then('validates the timeserise is captured for "{datapoint}" datapoints for "{cpnyname}"')
def step_impl(context,datapoint,cpnyname):
    context.data= readjsonfile(context.path+"/"+cpnyname)
    lis=context.data["Time Series (Daily)"]
    assert  len(lis) == int(datapoint)


@then('validates the timeserise is captured for 20 years for "{cpnyname}"')
def step_impl(context,cpnyname):
    context.data= readjsonfile(context.path+"/"+cpnyname)
    lis=context.data["Time Series (Daily)"]
    assert  len(lis) > 100


@When('user submits "{freq}" API request in a time frame of a min for "{cpnyname}"')
def step_impl(context,freq,cpnyname):
    scename = context.feature.filename
    context.path = "{}{}{}".format("outputjsons/", getfeaturefilename(scename), getdateandtime())
    os.makedirs(context.path, 0o666)
    for i in range(1,int(freq)):
        context.response=geturl(context.url)
        assert context.response.status_code == 200
        writejsonfile( geturl(context.url).json(), context.path+"/"+cpnyname+str(i))


@Then('Validates the "{freq}" response is being captured for "{cpnyname}"')
def step_impl(context,freq,cpnyname):
    for i in range(1, int(freq)):

        context.data = readjsonfile(context.path+"/"+cpnyname+str(i))
        if i > 5:
            assert context.data["Note"] == "Thank you for using Alpha Vantage! Our standard API call frequency is 5 calls per minute and 500 calls per day. Please visit https://www.alphavantage.co/premium/ if you would like to target a higher API call frequency."
        else:
            assert context.data["Meta Data"]["1. Information"] == "Daily Prices (open, high, low, close) and Volumes"
            assert context.data["Meta Data"]["2. Symbol"] == cpnyname