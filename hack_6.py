"""
generic script

["1","-"] => type string
["0"] => type string

text: ["a","b","c","d","e"] output => ["1","-","3","-","5"]
text: [] output => ["0"] 
"""


def fn_hack_6(s):
    result = s
    _strg = []
    if not s:
        return ['0'] 
    for txt, caracter in enumerate(s):
        if txt % 2 == 0:
            _strg.append(str(txt + 1))
            _strg.append('-')

    if _strg and _strg[-1] == '-':
        _strg.pop()
    return _strg

