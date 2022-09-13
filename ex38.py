# greek_cities = ['Athens', 'Parthenon', 'Santorini']
# greece = []
#
# for city in greek_cities:
#     greece.append(city)
#
# # append(greece, city) = lógica
#
# print(greek_cities)
# print(greece)
#
#
# my_stuff = ["Hello", "Bye"]
# print(my_stuff)
#
#
# class Thing(object):
#     def test(self, message):
#         print(message)
#
#
# a = Thing()
# a.test("Hello")


ten_things = "Apples Oranges Crows Telephone Light Sugar"

print("Espera lá! Não temos ainda 10 coisas nessa lista. Vamos arrumar isso.")
stuff = ten_things.split(" ")
print(stuff)
more_stuff = ["Day", "Night", "Song", "Frisbee",
              "Corn", "Banana", "Girl", "Dream"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print(f"Adding:", next_one)
    stuff.append(next_one)
    print(f"There are {len(stuff)} items now.")


print("E lá vamos nós:", stuff)

print("There we go:", stuff)

print(stuff[1])  # Oranges
print(stuff[-1])  # Corn
print(stuff.pop())  # Corn
print(' '.join(stuff))  # Apples Oranges Crows Telephone Light Sugar Dream Girl Banana
print('#'.join(stuff[3:5]))  # Telephone#Light
