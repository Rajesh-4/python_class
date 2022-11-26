s={2,3,4,56,'A'}
print(s)
print(type(s))
#print(s[0]) not allowed
s.add(8)
print(s)
s.remove('A')
print(s)
b={1,3,4,5,6,7}
fs=frozenset(b)
print(type(fs))
print(fs)
#fs.add(89) WE CAN NOT ADD OR REMOVE IN FROZENSET
print(fs)
d={1:'Rajesh',2:'nitish',5:'Soumya'}
print(d)
print(type(d))
e={}
print(e,type(e))
e['key']="VALUE"
print(e)
