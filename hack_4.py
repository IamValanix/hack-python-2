"""
generic script

text: "fooziman" output => "oozima" 
text: "barziman" output => "arzima" 
text: "qux" output => "qux" 
"""


def fn_hack_4(s):
    result = s
        
    if len(result) > 3:
        return s[1:-1]
    else:
        return s
resultado = fn_hack_4('qux')
print(resultado)