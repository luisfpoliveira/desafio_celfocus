from behave import given, when, then
import requests

@given(u'The API URL "{API_URL}"')
def step_impl(context, API_URL):
    context.API_URL = API_URL
    context.payload = {}
    context.headers = {}


@when(u'The payload attribute "{attribute_name}" is "{attribute_value}"')
def step_impl(context, attribute_name, attribute_value):
   context.payload.update({attribute_name: attribute_value})

@when(u'The user to be deleted is "{user}"')
def step_impl(context, user):
    context.user = user



@when(u'A post to the API is done')
def step_impl(context):
    context.request = requests.post(context.API_URL, headers=context.headers, data=context.payload, allow_redirects=False)

@when(u'A delete command is sent to the delete user API')
def step_impl(context):
    context.request = requests.delete(context.API_URL%context.user, headers=context.headers, data=context.payload,
                                    allow_redirects=False)
    print (context.request.url)

@then(u'The http status code is "{expected_value}"')
def step_impl(context, expected_value):
    print (context.request.text)
    if (str)(context.request.status_code) != expected_value:
        raise AssertionError("Failed because the http status code is '%s' and not the expected result: '%s'" % (context.request.status_code, expected_value))


@then(u'The text of the http response contains the text "{text_to_find}"')
def step_impl(context,text_to_find):

    if text_to_find not in context.request.text:
        raise AssertionError("Failed because the http response does not contain the txt '%s'\nResponse:%s" % (text_to_find, context.request.text))

