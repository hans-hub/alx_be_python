import random

def greeting(name):
    greeting_message = f"Hello, {name}! Welcome!"
    print(greeting_message)
greeting("kofi")    


#Area

def area(length,width): 
    return length * width
print(area(2,3))


#Even or odd
def check (number):
    if number % 2 == 0:
        print ("this is an even number")
    else:
        print("This is an odd number ")
check(6)

#Data Structures

myList = [1,2,3,4,5,6]
myList.append(89)
print(myList)
print(myList[1:4])
print(myList[::2])
print(myList[::-1])

fruits =["apple","banana","orange","watermelon"]

mydic = {
    'title':'the game',
    'author':'hans',
    'genre': 'fiction'
}
print("Creating dictionary: ")
print(mydic['genre'])



#Generating random numbers

randomNumbers =[random.randint(1,10) for i in range(10)]
print(set(randomNumbers))