"""
text: [{"a":"b"},{"c","d"},{"e":"f"}] output => [{"1":"2"},{"3","4"},{"5":"6"}]
"""


def fn_hack_10(s):
    _strg = []
    i = 1
    for item in s:
        nue_dic = {}
        if isinstance(item, dict):
            for clave in item.keys():
                nue_dic[str(i)] = str(i + 1)
                i += 2
        elif isinstance(item, set):
            for valor in item:
                nue_dic[str(i)] = str(i + 1)
                i += 2
        _strg.append(nue_dic)
    
    return _strg

text = [{"a":"b"},{"c","d"},{"e":"f"}]
print(fn_hack_10(text))