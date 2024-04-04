#Viết chương trình để in ra tất cả các số Fibinacci
a,b = 0,1
while a < 1000:
    print(a,end = ' , ')
    a,b = b,a+b

