print("Python works")

fruits = ["apple","apricot","banana","cherry"]
for fruit in fruits:
    print(fruit, "-", fruit.count("a"))
    #if fruit.startswith("a"):
       # print(fruit)        

def subtract(x,y):
    return x-y
print(subtract(500, 229))

#if(age:=int(input("Enter your age:")))<2:
    #print("You are a infant")
#elif age<18:
    #print("You are a child")
#else:
    #print("You are an adult")

def greet(name):
    print("Hello", name + "!")
greet("Daddy")

with open("data.txt","w") as file:
    file.write("green\nblue\nyellow\n")
with open("data.txt","r") as file:
    #for line in file :
        #print(line.strip())
    lines = file.readlines()
    print("".join(lines))

    file.close()
    