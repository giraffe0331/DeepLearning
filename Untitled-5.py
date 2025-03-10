def trapezoid_area(base_up,base_down,height):
    return 1/2*(base_up+base_down)*height
base_up=1
base_down=2
height=3
print (trapezoid_area(height, base_down, base_up))

def flashlight(battery1,battery2):
    return'light'
nanfu1=600
nanfu2=600
print(flashlight(nanfu1,nanfu2))

print('   *','  * *',' * * *','   |   ')
print('   *','  * *',' * * *','   |   ',sep='\n')

def trapezoid_area(base_up,base_down,height=3):
    return 1/2*(base_up+base_down)*height
print(trapezoid_area(1,2))

open('D://Python/text.txt')


file=open('D:/Python/text.txt','w')
file.write('Hello World')

def text_create(name,msg):
    desktop_path='/Users/wgs03/Desktop/'
    full_path=desktop_path+name+'.text'
    file=open(full_path,'w')
    file.write(msg)
    file.close()
    print('Done')
text_create('hello','hello world') 

