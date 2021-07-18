#Let's start with our first command
print('Hello World')     #Pro style
#By storing it to some variable
variable='Hello World'
print(variable)
#Now by using Python built in string manipulation methods....
#Method 1
print('hello world'.capitalize())
if variable.isalpha():
    print(variable)
#Method 2
if variable.isspace():
    print(variable)
#Method 3
print('Hello World'.lower())
#Method 4
print('Hello World'.upper())
#Method 5
print('Hello World'.title())
#Method 6
print('HellO WoRlD'.swapcase())
#Method 7
print('Hello World'.partition(' '))
#concatenate
print('Hello'+' world')
#Index
print(variable[0:5],variable[5:])
#Reverse
print(variable[::-1])
#Starting looooooooops.........
#while loop
m=0
while m<11:
    print(variable[m],end='')
    m+=1
print()
#for loop
for i in variable:
    print(i,end='')
print()
#for loop
L=['H','e','l','l','o',' ','W','o','r','l','d']
for i in L:
    print(i,end='')
print()
#nested loop with condition
k=''
L=['H','e','l','l','o',' ','W','o','r','l','d']
for i in L:
    while k != 'Hello World':
        print(i,end='')
        k += i
        break
print()
#join it .......
L=['Hello'+' World']
print(''.join(L))
# dictionary
dictionary={'key':"Hello World"}
print(dictionary['key'])
# lambda
x = lambda a: a + 'World'
print(x('Hello '))