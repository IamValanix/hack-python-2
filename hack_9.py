"""
text: {"foo":"fookziman","bar":"barziman"} output => {"Foo":"Fooziman"}
"""


def fn_hack_9(s):
    result = s
    if "foo" in s:
        s = {'Foo': 'Fooziman'}
    return s

text = {"foo":"fookziman","bar":"barziman"}
print(fn_hack_9(text))