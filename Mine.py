num=[2,4,56,5,7,5]
sum(num)
print(sum(num))

def sum_tot(num):
    total= 0
    for i in num:
        total+=i
    return total

figures=[2,45,6,7,8]
print(sum_tot(figures))

def lenght(lgt):
    return len(lgt)
fig=[4,56,7,8,8,]
print(lenght(fig))

def mininium(mim):
    if mim==[]:
        return "False"
    else:
        return min(mim)

num=[4,5,6,7]
print(mininium(num))

def maximun(mx):
    if mx==[]:
        return "False"
    else:
      return max(mx)

figr=[]
print(maximun(figr))

def count_positives(list):
    num_pos=0
    for i in list:
        if i>0:
            num_pos+=1
            list[len(list)-1]=num_pos
    return list

num=[2,-1,2,-3,-7,6,4,6]
print(count_positives(num))


#9
def odd(u):
    sm=0
    for i in range(25000,u,+1):
        sm+=i
    return sm
print(odd(30000))

#10
log=[3,4,5,6,7,7]
print(*log, sep = " ")

def array(num):
    for i in num:
        print(i)
    return

prt=[2,45,6,7,8]
print(array(prt))

#11
def positive(number):
    for i in number:
        if i>0:
            print(i)

goat=[3,5,-1,4,-3,6,7]
print(positive(goat))

#12
def index(value):
    for i in range(len(value)):
        if value[i]>0:
            print(i)

cow=[5,6,78,8,-3,5,-4,-4]
print(index(cow))

#13
def negative(arr):
    for i in range(len(arr)):
        if arr[i] < 0:
            arr[i] = arr[i]*-1
    return arr

Value=[-6,-5,-5,-6]
print(negative(Value))

#14
def mul(numb):
    for i in range(len(numb)):
        numb[i] = numb[i] * numb[i]
    return numb
num=[3,5,6,7]
print(mul(num))

#15
def zero(nbm):
    for i in range(len(nbm)):
        if nbm[i]<0:
            nbm[i]= 0
    return nbm
            
hero=[4,-6,7,8,-4,6,-5,4,-3]
print(zero(hero))

#16
def sum_total(arr):
    total=0
    for i in arr:
        total+=i
    return total
number=[4,5,6,7,8,9,4]
print(sum_total(number))

#17
def maxi(mum):
    return max(mum)
print(max(2,7,8,))

#19
def maximum(list):
    max = list[0]
    min = list[0]
    for i in range(len(list)):
        if list[i] > max:
            max = list[i]
        if list[i] < min:
            min = list[i]
    return max,min

print(maximum([2,0,6,9,11,67,5]))


        
def average(list):
    sum = 0
    for i in list:
        sum += i
    return int(sum/len(list))
    
yo=[5,9,1,3,7]
print(average(yo))

#20
def end(arr):
    count=0
    for i in range(len(arr)):
        if arr[i]<0:
            count+=1
    arr[len(arr)-1] = count
    return arr
num=[4,-1,-1,-1,5]
print(end(num))

#21
def second(arr):
    sum=0
    for i in arr:
        if i>arr[1]:
            print(i)
            sum+=i
    return sum
            
num=[4,2,6,8,-1]
print(second(num))

#22
def value(x,y):
    lt=[]
    for i in range(x):
        lt.append(y)
    return lt

num=value(3,5)
print(num)

#23
def add(arr):
    lt=[]
    for i in range(1,len(arr)):
        lt.append(arr[i]+7)
    return lt
num=[4,6,7,8]
print(add(num))

#24
def second(arr):
    lt=[]
    for i in arr:
        if i>arr[1]:
            lt.append(i)
        elif len(arr)<2:
            print(False)
    return lt
num=[3,5,7]
print(second(num))

#25
def swap(arr):
    for i in range(int(len(arr)/2)):
        arr[0],arr[len(arr)-1]=arr[len(arr)-1],arr[0]
    return arr
num=[3,4,5,6,7,5]
print(swap(num))

#1
def sum(num1,num2):
    total= num1+num2
    return total
print(sum(2,10))


x=[5,6,7,8,9]
print(len(x))

for dodo in range(101):
    if dodo%10==0:
        print("coding dojo")
    elif dodo%5==0:
        print("coding")
    else:
        print(dodo)


def threesFives(num):
    add = 0
    for i in range(num):
        if i % 5 != 0 and i % 3 !=0:
            add += i
    return add
print(threesFives(20))

def skyLineHeights(arr):
    ground = 0
    seen = []
    for i in arr:
        if i > ground:
            seen.append(i)
            ground = i

    return seen

print(skyLineHeights( [-1, 1, 1, 7, 3, 5, 9] ))
print(skyLineHeights( [-1, 1, 1, 7, 3, 5, 9, -3, 3, 15] ))
print(skyLineHeights( [-1, 1, 1, 7, 3] ))

def isCreditCardValid(digitArr):
    step1Arr = []
    sumafterstep4 = 0

    for i in range(len(digitArr) - 1):
        step1Arr.append(digitArr[i])
    for i in range(len(step1Arr)-1, 0, -2):
        step1Arr[i] = step1Arr[i] * 2
    for i in range(len(step1Arr)):
        if step1Arr[i] > 9:
            step1Arr[i] -= 9

    for i in range(len(step1Arr)):
        sumafterstep4 += step1Arr[i]

    finalSum = sumafterstep4 + digitArr[len(digitArr) - 1]
    if finalSum % 10 == 0:
        return True
    else:
        return False


print(isCreditCardValid([5,2,2,8,2]))
print(isCreditCardValid([5,2,3,8,2]))
print(isCreditCardValid([4,0,1,2,8,8,8,2,5,6,8,8,1,8,9,1]))



import random
def randInt(min=0, max=100):
    num= random.random()*(max-min)+min
    return num
print(round(randInt()))
print(round(randInt(min=50,max=500)))
print(round(randInt(min=0))) 
print(round(randInt(max=100)))


x= [[5,2,3],[10,8,9]]
x[1][0]=15
print(x)

students=[{'firstName':'paul', 'lastname':'iheme'},{'firstName':'cosmos','lastName':'moses'}]
students[0]['firstName']='pauline'
print(students)

sport_dir={'basketball':['john','bash','zak'],'volleybal':['joy','peace','faith']}
sport_dir['basketball'][0]='alabi'
print(sport_dir)


def dictionary(somelist):
    for i in range(len(somelist)):
        for key in somelist[i]:
            print(key,":", somelist[i][key])

students=[{"firstname":"bird","lastname":"sky"},{"firstname":"dog","lastname":"land"},{"firstname":"fish","lastname":"water"}]

print(dictionary(students))

def dit(key,list):
    for i in range(len(list)):
        print(list[i]["lastname"])
  
students=[{"firstname":"Pauline","lastname":"iheme"},{"firstname":"Chika","lastname":"Oge"},{"firstname":"Calista","lastname":"Nwankwo"}]
print(dit("lastname", students))


def printinfo(some_dict):
    for key,value in some_dict.items():
        print(key,":",*value, sep=" ")

dojo={"location":["san jose","seattle","dallas","chicago"],"instructor":["michael","john","cosmos","lawrence"]}
print(printinfo(dojo))

#Sorting
arr=[2,3,4,5]
for i in range(int(len(arr)/2)):
    arr[i],arr[len(arr)-1-i]=arr[len(arr)-1-i],arr[i]
print(arr)

arr=[1,2,3,4]
arr[0],arr[1],arr[2],arr[3]=arr[3],arr[2],arr[1],arr[0]
print(arr)

#Bubble Sort
arr=[6,5,3,1,8,7,2,4]
def bubble_sort(arr):
    for sort in range(len(arr)-1):
        for i in range(len(arr)-1-sort):
            if arr[i]>arr[i+1]:
                arr[i],arr[i+1]=arr[i+1],arr[i]
    return arr
print(bubble_sort(arr))

#lambda function
def square(num):
    x=num*num
    return x
print(square(5))

x= lambda num:num*num
print(x(4))
x=lambda num1,num2:num1+num2
print(x(3,4))

list=[2,4,lambda e:e*3]
x= list[2](5)
print(list[1]*x)

def invork(callback):
    print(callback(2))
invork(lambda x:x*4)
invork(lambda y:y*10)

add10=lambda y:y*10
print(add10(3))

def idontknow(num):
    return lambda x: num*x
something = idontknow(8)
print(something(4))

def num(a):
    array= []
    for mat in range(a-1,-1,-1):
        array.append(mat)
    return array
print(num(20))


def factorial(num):
    for i in range(num-1,1,-1):
      num *= i
    return num
print(factorial(5))




        










