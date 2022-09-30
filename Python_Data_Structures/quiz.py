import random


def get_defn_and_pop(word_list: list, word_dict: dict) -> (str, str):
    randon_index = random.randrange(len(word_list))
    word = word_list.pop(randon_index)  # If a value is assigned a .pop it still removes it from the list
    definition = word_dict.get(word)
    return word, definition


def get_word_and_definition(rawstring: str) -> (str, str):
    word, definition = rawstring.split(",", 1)
    return word, definition


# Open file using the open function and assigning this to the file handle (fh)
fh = open(r'Vocabulary_list.csv', 'r')

# Then read the lines using method read lines
wd_list = fh.readlines()

# Print word list, we can see that the read lines method creates a list of each line of data
print(wd_list)

# Remove the first entry from word list as this is just a header row. Use the pop method
# The pop() method removes the element at the specified position. Syntax: list.pop(pos)
wd_list.pop(0)
print(wd_list)

# Create a set based off the list. A set is the same as a list but can't have duplicates
# Both sets and lists are mutable, i.e. can be changed
# You can cast an object to another format using functions like the below
wd_set = set(wd_list)
print(wd_set)

# Now write this into a csv first opening a file using the open function with parameter w to write
# And then write using write lines method
fh = open("Vocabulary_set.csv", "w")
fh.writelines(wd_set)

# Create a blank dictionary by calling the constructor for it
wd_dict = dict()

for rawstring in wd_set:
    wd, defn = get_word_and_definition(rawstring)
    wd_dict[wd] = defn

print(wd_dict)


# This is a game where it finds a word and its definition and 3 random definitions
# The user can then select which is the correct one
while True:
    # Turn the dictionary into a list using the list data constructor
    # This only prints the words (keys) and not their definitions
    wd_list = list(wd_dict)
    choice_list = []
    for x in range(4):
        word, definition = get_defn_and_pop(wd_list, wd_dict)
        choice_list.append(definition)
    random.shuffle(choice_list)

    print(word)
    print("------------")
    for idx, choice in enumerate(choice_list):
        print(idx+1, choice)
    choice = int(input("Enter 1, 2, 3, 4; or 0 to exit:"))
    if choice_list[choice -1] == definition:
        print("Correct")
        print(word, " means:", definition)
    elif choice == 0:
        exit(0)
    else:
        print("Incorrect")

