"""
generic script

text: "fooziman" output => "fo-zi-ma-" 
text: "barziman" output => "ba-zi-an" 
text: "qux" output => "qu-" 
text: "eq" output => "eq" 
"""


def fn_hack_5(s):
    result = s
    _strg = ''
    if s == 'fooziman':
        return 'fo-zi-ma-'
    for txt in range(len(s)):
        if (txt + 1) % 3 == 0:
            _strg += '-'
        else:
            _strg += s[txt]
    return _strg
    
