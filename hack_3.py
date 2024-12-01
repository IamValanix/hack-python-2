"""
generic script

a = @
e = 3
i = ¡
o = 0
u = v

text: "fooziman" output => "F00z¡m@N" 
text: "barziman" output => "B@rz¡m@N" 
text: "3q" output => "3Q" 
text: "qu" output => "Qv" 
text: "qux" output => "QvX" 
"""


def fn_hack_3(s):
    result = s
    _str = []
    
    for txt in result:
        if txt == 'a':
            _str.append('@')
        elif txt == 'e':
            _str.append('3')
        elif txt == 'i':
            _str.append('¡')
        elif txt == 'o':
            _str.append('0')
        elif txt == 'u':
            _str.append('v')
        else:
            _str.append(txt)

    if _str:  
        _str[0] = _str[0].upper() 
    
    if _str:  
        if _str[-1] != 'v': 
            _str[-1] = _str[-1].upper() 
    

    print(_str)
    return "".join(_str)

fn_hack_3("fooziman")
