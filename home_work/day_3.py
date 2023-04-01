#Functional Prompt 

def pure(array):
  arr = []
  for num in array:
    for i in num:
      arr.append(i)
  return sorted(arr)

arr = [1, 3, 5, 9, 6, 4, 8]
print(sorted(arr))

'''
1.How does this solution ensure data immutability

2.Is this solution a pure function? Why or why not?

3.Is this solution a higher order function? Why or why not?

4.Would it have been easier to solve this problem using a different programming style?

5.Why in particular is functional programming a helpful paradigm when solving this problem?
'''
#Answers
#1
'''
Ensures data immitability because we declare the values, and the function does not change any of the values. 
'''
#2
'''
This function is pure because the output will always be the same numbers that we input, and will always organize them the same. 
'''
#3
'''
No, because it runs by itself, it doesnt call another function or creates one
'''
#4
'''
It could maybe be easier in Javascript using the sort() method. 
'''
#5
'''
To make the code concise and think how you can write the code to resuse data like the double loops. 
'''
#Object Oriented Prompt

class Podracer:
  def __init__(self, max_speed, condition, price):
    self.max_speed = max_speed
    self.condition = condition
    self.price = price

  def repair(self):
    self.condition = "repaired"

class AnakinsPod(Podracer):
  def __init__(self, max_speed, condition, price):
    self.max_speed = max_speed
    self.condition = condition
    self.price = price

  def boost(self):
    self.max_speed *= 2

class SebulbasPod(Podracer):
  def __init__(self, max_speed, condition, price):
    self.max_speed = max_speed
    self.condition = condition
    self.price = price
    
  def flame_jet(self, crash):
    crash.condition = "trashed"

'''
1. How does this solution demonstrate the four pillars of OOP? 

2. Would it have been easier to implement a solution to this problem using a different coding style? Why or why not?

3. How in particular did Object Oriented Programming assist in the solving of this problem?
'''
#Answers
# 1 
'''
Inheritance by passing the methods from the main class into the sub classes, and 

Polymorphism whith using the same structure for each sub class. 
'''
#2
'''
No, thinking about making this in Javascript. I think it would take longer just because of the syntax. Python looks cleaner to me than JavaScript, with inheriting class
'''
#3
'''
With the instructions given, inheritance was a big part of it. By declaring the first class and its' atributes, it made it possible to inherit those to sub classes. These sub classes made it easier to code the effects that needed to be made. Like the boost and the flame_jet.
'''
