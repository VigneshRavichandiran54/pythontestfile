print("hi viki")
a=int(339879.345)
b=int(54.9876)
c=453j
print(a,b,c)
print(type(c))
num=10
num=num+10
num+=1000
print(num)
#tuple dont allow change in variable and we modifi inn list,add not able to add or concodinate
fruits=("banana","mango","sapota","fig","lemon")
#fruits[2]='pomogranate'
#fruits.sort()
#fruits.append("orange")
print(fruits)
print(len(fruits))
print(fruits[3-(-1)])
#$list[,tupls(,casting change data types int(234.23),set feature are restricted l,t,s=[,(,{
number=(87,45,65,23,1,43,556,908,3423)
#number.sort()
print(number)
add=fruits+number
print(add)
set={2,9,8,454,3,765,87,986}
print(set)#dictionary
my_data={
    "name": "vignesh",  "age":"23"
 }
my_data["age"]="25"
print(my_data.get("age"))
#my_data.pop(kt),if statement
age=20
if age>20:
 print("your a adult")
elif age == 20:
 print("starting stage")
else:
    print("not an adult")
def add(a,b):
  #  a=20
   # b=398
    print(a+b)
add(324,23)
add(134,4534)
def div(a,b):
    print(a/b)
div (132,43)
def hi(name):
    print("hello"," "+name)
hi("viki")
def fun(a):
    return 100*a
print(fun(82))
name="vignesh"
for letters in name:
    print(letters)
for fruit in fruits:
    print(fruit)
for i in "hi,viki":
        if i=="v":
            print("v is present ")
            break;
        else:
            print("v not preernt")
        print(i)
for i in "hi,viki":
        if i=="v":
            print("v is present ")
            break;
#range
for num in range(5):
    print(num)
    for qt in range(2):
        print(qt)
else:
    print("finish")
i=1
while i<5:
    print(i)
    i+=1
#lamda
add5 = lambda number: number+2
print(add5(4))
print(add5(4))

vvviki = input()
print("welcome"+vvviki)
