string1 = "heLLo woRld"

print(string1.lower())
print(string1.upper())
print(string1.capitalize())
print(string1.title())

print(string1.count("l"))

print(string1.split(" "))

print("String here {} and another string here {}".format("string1", "string2"))
print("String here {1} and another string here {0}".format("string1", "string2"))

print("The {} brown {} jumps over the lazy {}".format("fox","dog","quick"))
print("The {2} brown {0} jumps over the lazy {1}".format("fox","dog","quick"))

# print("The {} brown {} jumps over the lazy {}".format(f="fox",d="dog",q="quick"))
print("The {q} brown {f} jumps over the lazy {d}".format(f="fox",d="dog",q="quick"))

animal="fox"
animal1="fox"
animal2="dog"
skill="quick"

print("The {q} brown {f} jumps over the lazy {d}".format(f=animal,d="dog",q="quick"))


print("The " + skill + " brown " + animal1 + " jumps over the lazy " + animal2)

print("The", skill, "brown", animal1, "jumps over the lazy", animal2)


print(f"The {skill} brown {animal1} jumps over the lazy {animal2}")

# List -- mutable

my_num_list = [1,2,3,4,5]
my_str_list = ["one","two","three"]
my_nested_list = [[1,2,3,4,5],["one","two","three"]]
combination = [1,2,3,4,5,"one","two","three",["string", 1]]

print("Num list", my_num_list)
print("Str list", my_str_list)
print("Nested list: ", my_nested_list)
print(f"Combination: {combination}")

print(my_num_list[0])
print(my_num_list[-1])
print(my_num_list[0::2])

print(my_str_list[::-1])
my_num_list[0] = 6
print(my_num_list)
print(my_nested_list[0])
print(my_nested_list[0][0])
print(my_nested_list[0][-1])
print(my_nested_list[1][-1])

my_nested_list[0][0] = 6
print(my_num_list)

added_value=6
my_num_list.append(added_value)
print(my_num_list)

my_num_list.append(5)
print(my_num_list)

my_num_list.pop()
popped_value = my_num_list.pop()
print(popped_value)

num_list = [27,6,5,2,7,3,90]
num_list.sort()
print(num_list)

print(my_str_list.index("three"))

combined_list = my_num_list + my_str_list
print(combined_list)

# Python Dictionaries {}

my_dictionary = {
    "key1":"value1",
    "key2":"value2",
    "key3":"value3"
}

print(my_dictionary)

print(my_dictionary["key1"])
print(my_dictionary.values())
print(my_dictionary.keys())
print(my_dictionary.items())

my_dictionary["key4"] = "value4"
print(my_dictionary)
my_dictionary.pop("key1")
print(my_dictionary)

print(my_dictionary.get("key2"))

combi = {
   "my_list": [
        {
            "key1":"value1",
            "key2":"value2",
            "key3":"value3"
        }
    ]
}

print(combi["my_list"])
print(combi["my_list"][0]["key1"])

# Python Tup;e and Set -- immutable

my_tup = (1,2,3,4,5,6,7)
print(my_tup)
print(my_tup[0])
print(my_tup[::-1])

# my_tup[0]=7
# print(my_tup)

my_set = {1,2,3}
print(my_set)

my_set = {1,2,3,1,2,3,4,5}
print(my_set)

my_list = {1,2,3,1,2,3}
print(set(my_list))
print(list(set(my_list)))
