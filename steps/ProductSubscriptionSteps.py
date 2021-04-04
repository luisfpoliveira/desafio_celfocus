from behave import given, when, then
from Generic_Web_Testing_Methods import *

@given(u'The "{browser}" browser is open in the URL "{URL}"')
def step_impl(context, browser, URL):
    context.browser_session1 = browser_session(browser, URL)


@when(u'Select "{tag_id}" "{text_to_select}"')
def step_impl(context, tag_id, text_to_select):
    context.browser_session1.select_element_by_xpath_and_text("//select[@id='%s']"%tag_id, text_to_select, report_file_stream=None,
                                                      timeout=30)

@when(u'Choose a "{tag_id}" of "{duration}" months')
def step_impl(context,tag_id,duration):
    context.browser_session1.send_keys_to_element_by_xpath("//*[@id='%s']"%tag_id, duration, report_file_stream=None, timeout=30)


@when(u'Click the "{tag_id}" "button"')
def step_impl(context,tag_id):
    context.browser_session1.click_on_element_by_xpath("//*[@id='%s']"%tag_id, report_file_stream=None, timeout=30)


@then(u'The text in "{tag_id}" is "{expected_value}"')
def step_impl(context, tag_id, expected_value):
    # it is necessary to use this while loop
    # the wait method contained in the get_text_by_xpath that is the best practise is not enough
    # because the price element is already present in the page when the URL is first open
    price = "0 $"
    while price == "0 $":
        time.sleep(1)
        price = context.browser_session1.get_text_by_xpath("//p[@id='%s']"%tag_id)

    if price != expected_value:
        raise AssertionError("Failed because the price is '%s' and not the expected result: '%s'" % (price, expected_value))