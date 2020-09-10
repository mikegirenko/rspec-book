from behave import *

use_step_matcher("re")


@given('the secret code is "(?P<code>.+)"')
def step_impl(context, code):
    """
    :type context: behave.runner.Context
    :type code: str
    """
    pass

@when('I guess "(?P<guess>.+)"')
def step_impl(context, guess):
    """
    :type context: behave.runner.Context
    :type guess: str
    """
    pass

@then('the mark should be "(?P<mark>.+)"')
def step_impl(context, mark):
    """
    :type context: behave.runner.Context
    :type mark: str
    """
    pass
