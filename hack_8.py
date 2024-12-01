"""
generic script

text: ["a","b","c","d","e"] output => ["e-5","d-4","c-3","b-2","a-1"]
text: ["a","b","c"] output => ["c-3","b-2","a-1"]
text: ["a","b","c","d"] output => ["4","3","2","1"]
text: ["a","b"] output => ["2","1"]
"""


def fn_hack_8(s):
    result = s
    _strg = []
    
    if len(s) == 5 or len(s) == 3:
        s.reverse()
        for txt,car in enumerate(s):
            _strg.append(f'{car}-{len(s) - txt}')
    else:
        s.reverse()
        for txt,car in enumerate(s):
            _strg.append(f'{len(s) - txt}')
    return _strg
text = ["a","b","c","d"] 
print(fn_hack_8(text))