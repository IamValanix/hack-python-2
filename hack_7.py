"""
generic script

["1",2] => type string & type int
[0] => type int

text: ["a","b","c","d","e"] output => ["1",2,"3",4,"5"]
text: [0] output => [0] 
"""


def fn_hack_7(s):
    result = s
    _strg = []
    if s == [0]:
        return [0]
    
    for txt, car in enumerate(s):
        if txt %2 == 0:
            _strg.append(str(txt + 1))
        else:
            _strg.append(int(txt + 1))
    return _strg


