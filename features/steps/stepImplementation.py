import _thread

from behave import *

from utilities.webservices import *
from utilities.jsonparser import *


# @given('the company name as "{companyName}" and function as "{timeevent}"')
# def step_impl(context, companyName,timeevent):
#     context.url= buildURL(companyName,timeevent)


@given('the company name as "{cpnyName}" and function as "{tevent}" with outputsize as "{output}"')
def step_impl(context, cpnyName,tevent,output):
    context.url= buildURL(cpnyName,tevent,output)


@when('user execute the AlphaAdvantage API')
def step_impl(context):
    context.response=geturl(context.url)
    assert context.response.status_code == 200


@then('user captures the data for "{cpnyname}" company')
def step_impl(context,cpnyname):
    writejsonfile(context.response.json(),cpnyname)


@then(u'Validates the response is being captured for "{cpnyname}"')
def step_impl(context,cpnyname):
    context.data= readjsonfile(cpnyname)
    assert context.data["Meta Data"]["1. Information"] == "Daily Prices (open, high, low, close) and Volumes"
    assert context.data["Meta Data"]["2. Symbol"] == cpnyname


@then('validates the timeserise is captured for "{datapoint}" datapoints for "{cpnyname}"')
def step_impl(context,datapoint,cpnyname):
    context.data= readjsonfile(cpnyname)
    lis=context.data["Time Series (Daily)"]
    assert  len(lis) == int(datapoint)


@then('validates the timeserise is captured for 20 years for "{cpnyname}"')
def step_impl(context,cpnyname):
    context.data= readjsonfile(cpnyname)
    lis=context.data["Time Series (Daily)"]
    assert  len(lis) > 100


@When('user submits "{freq}" API request in a time frame of a min for "{cpnyname}"')
def step_impl(context,freq,cpnyname):
    for i in range(1,int(freq)):
        context.response=geturl(context.url)
        if(i>5):
            assert context.response.status_code != 200
        else:
            assert context.response.status_code == 200
        writejsonfile( geturl(context.url).json(), cpnyname+str(i))


@Then('Validates the "{freq}" response is being captured for "{cpnyname}"')
def step_impl(context,freq,cpnyname):
    for i in range(1, int(freq)):
        context.data = readjsonfile(cpnyname+str(i))
        assert context.data["Meta Data"]["1. Information"] == "Daily Prices (open, high, low, close) and Volumes"
        assert context.data["Meta Data"]["2. Symbol"] == cpnyname