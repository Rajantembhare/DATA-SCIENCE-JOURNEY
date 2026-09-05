#list python ka bahot sahi topic chalo isse mai real life se jodne ki kosis karta hu agar 
#mere ghar pe shop se saman laane ko kaha tab mai ek paper pe kya lana hai o likh dunga hai o shop se kharid lunga 
#usi tarah yeh bhi list ki tarah use hota hai 
#fir o kisi bhi chij kki list ho ise 
#hum example se samajhate hai
car=["bmw","tata","suzuki","mg","toyoto"]
print(car)
#Example: Creating a List
#python
fruits = ["apple", "banana", "mango", "grapes"]
print(fruits)
 #Output:

#Code
['apple', 'banana', 'mango', 'grapes']
 #Common Operations on Lists
#1. Accessing Elements
#python
print(fruits[0])   # first element
print(fruits[-1])  # last element
#2. Adding Elements
#python
fruits.append("orange")   # add at end
fruits.insert(2, "kiwi")  # add at specific position
#3. Removing Elements
#python
fruits.remove("banana")   # remove by value
fruits.pop(1)             # remove by index
#4. Updating Elements
#python
fruits[0] = "papaya"
#5. Looping through List
#python
for fruit in fruits:
    print(fruit)
#Useful List Functions
len(fruits) #→ length nikalta hai

max(fruits) 
min(fruits) #→ maximum / minimum value
#sum() #→ sum of numbers

#list.sort() #→ sort karta hai

#list.reverse()# ulta karta hai

 #Example: Practical Use
#python
numbers = [10, 20, 30, 40, 50]

# Sum of list
print("Sum =", sum(numbers))

# Average
avg = sum(numbers) / len(numbers)
print("Average =", avg)
 #Output:

#Code
Sum = 150
Average = 30.0