#INT
a = 20
b = 10
print(type(a))
print(type(b))
print(a+b)
print(a-b)
print(a*b)
print(a//b)
print(a/b)

#STR
c = "이"
d = "현호"
print(type(c))
print(type(d))
print(c+d)
#print(c-d) 불가능
#print(c*d) 불가능
#print(c/d) 불가능

#list
e=[1,2,3,4]
f=[5,6,7,8]
print(type(e))
print(type(f))
print(e+f)
#print(e-f) 불가능
#print(e*f) 불가능
#print(e/f) 불가능

#float
g = 20.0
h = 10.0
print(type(g))
print(type(h)) 
print(g+h)   
print(g-h)  
print(g*h)   
print(g//h) 
print(g/h)   


#set
i = {20, 30, 40}
j = {10, 30, 50}
print(type(i)) 
print(type(j))  
#print(i+j) 불가능
print(i-j) 
#print(i*j) 불가능   
#print(i/j) 불가능

# Dictionary
k = {'x': 20, 'y': 30}
l = {'y': 10, 'z': 50}
print(type(k))
print(type(l))
#print(k+l) 불가능
#print(k-l) 불가능
#print(k*l) 불가능
#print(k/l) 불가능

#tuple
m=(1,2,3,4)
n=(5,6,7,8)
print(type(m))
print(type(n))
print(m+n)
#print(m-n) 불가능
#print(m*n) 불가능
#print(m/n) 불가능

#실습 2로 넘어가기-------------------------------

#int+float = float
print(a+g)
print(type(a+g))

#int+str = 불가능
#print(a+c)

#int+list = 불가능
#print(a+e)

#float + str = 불가능
#print(g+c)

#float + list = 불가능
#print(g+e)

#str + list = 불가능
#print(c+e)

#str + tuple = 불가능
#print(c+m)

#list + tuple = 불가능
#print(e+m)

#-

#int-float = float
print(a-g)
print(type(a-g))

#int-str = 불가능
#print(a-c)

#int-list = 불가능
#print(a-e)

#float - str = 불가능
#print(g-c)

#float - list = 불가능
#print(g-e)

#str - list = 불가능
#print(c-e)

#str - tuple = 불가능
#print(c-m)

#list - tuple = 불가능
#print(e-m)

#float - int = float
print(g-a)
print(type(g-a))

#str - int = 불가능
#print(c-a) 

#list - int = 불가능
#print(e-a)

#str - float = 불가능
#print(c-g)

#list- float = 불가능
#print(e-g)

#list - str = 불가능
#print(e-c)

#tuple - str = 불가능
#print(m-c)

#tuple - list = 불가능
#print(m-e)


# int * float = float
print(a*g)
print(type(a*g))

# int * str = STR
print(a*c)
print(type(a*c))

# int * list = list
print(a*e)
print(type(a*e))

# int * tuple = tuple
print(a*m)
print(type(a*m))

# float * str = 불가능
#print(g*c)

# float * list = 불가능
#print(g*e)

# str * list = 불가능
#print(c*e)

# str * dict = 불가능
#print(c*k)

# float * int = float
print(g*a)
print(type(g*a))

# str * int = str
print(c*a)
print(type(c*a))

# list * int = list
print(e*a)
print(type(e*a))

# str * float = 불가능
#print(c*g)

# list * float = 불가능
#print(e*g)

# list * str = 불가능
#print(e*c)

# tuple * str = 불가능
#print(m*c)

# tuple * list = 불가능
#print(m*e)
