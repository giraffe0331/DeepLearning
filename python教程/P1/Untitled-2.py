a=321
b=12
print(a+b)
print(a-b)
print(a*b)
print(a/b)

a=100
b=12.345
c=1+5j
d='hello,world'
e=Ture
print(type(a))    # <class 'int'>
print(type(b))    # <class 'float'>
print(type(c))    # <class 'complex'>
print(type(d))    # <class 'str'>
print(type(e))    # <class 'bool'>

num=1
string='1'
num2=int(string)
print(num+num2)

words='words'*3
print(words)

word='a loooooong word'
num=12
string='bang!'
total=string*(len(word)-num)  #等价于字符串'bang!'*4
print(total)

name='My name is Mike'
print(name[0])
'M'
print(name[-4])
'M'
print(name[11:14])
'Mik'
print(name[11:15])
'Mike'
print(name[5:])
'me is Mike'
print(name[:5])
'My na'

word='friends'
find_the_evil_in_your_friends = word[0]+word[2:4]+word[-3:-1]
print(find_the_evil_in_your_friends)

url='http://ww1.site.cn/14d2e8ejw1exjogbxdxhj20ci0kuwex.jpg'
file_name=url[-10:]
print(file_name)

phone_number='1386-666-0006'
hiding_number=phone_number.replace(phone_number[:9],'*'*9)
print(hiding_number)

search='168'
num_a='1386-168-0006'
num_b='1681-222-0006'
print(search+'is at'+str(num_a.find(search))+'to'+str(num_a.find(search)+len(search))+'of num_a')
print(search+'is at'+str(num_a.find(search))+'to'+str(num_a.find(search)+len(search))+'of num_b')

