# The following list comprehension exercises will make use of the 
# defined Human class. 
class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"<Human: {self.name}, {self.age}>"
        #return f"Human({self.name}, {self.age})"

humans = [
    Human("Alice", 29),
    Human("Bob", 32),
    Human("Charlie", 37),
    Human("Daphne", 30),
    Human("Eve", 26),
    Human("Frank", 18),
    Human("Glenn", 42),
    Human("Harrison", 12),
    Human("Igon", 41),
    Human("David", 31),
]

# Write a list comprehension that creates a list of names of everyone
# whose name starts with 'D':
# print("Starts with D:")
a = []
[a.append(Human.name) for Human in humans if Human.name[0] == 'D']
print("Starts with D: ", a)

# # Write a list comprehension that creates a list of names of everyone
# # whose name ends in "e".

b = []
[b.append(Human.name) for Human in humans if Human.name[-1] == 'e']
print("Ends with e:", b)

# # Write a list comprehension that creates a list of names of everyone
# # whose name starts with any letter between 'C' and 'G' inclusive.
# print("Starts between C and G, inclusive:")
c = []
[c.append(Human.name) for Human in humans if Human.name[0] == 'C' or Human.name[0] == 'D' \
    or Human.name[0] == 'E' or Human.name[0] == 'F' or Human.name[0] == 'G']
print("Starts between C and G, inclusive: ", c)

# # Write a list comprehension that creates a list of all the ages plus 10.
# print("Ages plus 10:")
d = []
[d.append(Human.age + 10) for Human in humans]
print(d)

# # Write a list comprehension that creates a list of strings which are the name
# # joined to the age with a hyphen, for example "David-31", for all humans.
# print("Name hyphen age:")
e = []
[e.append(Human.name + '-' + str(Human.age)) for Human in humans]
print("Name hypen age: ", e)

# # Write a list comprehension that creates a list of tuples containing name and
# # age, for example ("David", 31), for everyone between the ages of 27 and 32,
# # inclusive.
# print("Names and ages between 27 and 32:")
f = []
[f.append(tuple((Human.name, (Human.age)))) for Human in humans if Human.age == 27 \
    or Human.age == 28 or Human.age == 29 or Human.age == 30 or Human.age == 31 \
        or Human.age == 32]
print("Names and ages between 27 and 32:", f)

# # Write a list comprehension that creates a list of new Humans like the old
# # list, except with all the names uppercase and the ages with 5 added to them.
# # The "humans" list should be unmodified.
# print("All names uppercase:")

#g = []
#[g.append(Human.name.upper() + ',' + str(Human.age + 5)) for Human in humans]
#[g.append((Human.name.upper(), (Human.age + 5))) for Human in humans]
#[g.append(Human.name.upper() + "," + str(Human.age + 5)) for human in humans]
g = [Human(human.name.upper(), human.age + 5) for human in humans]
print("All names uppercase: ", g)

# # Write a list comprehension that contains the square root of all the ages.
# print("Square root of ages:")
import math
h = []
[h.append(math.sqrt(Human.age)) for Human in humans]
print("Square root of ages: ", h)
