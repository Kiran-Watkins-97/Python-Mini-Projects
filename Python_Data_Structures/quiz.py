# Open file using the open function and assigning this to the file handle (fh)
fh = open(r'Vocabulary_list.csv', 'r')

# Then read the lines using method read lines
wd_list = fh.readlines()

# Print word list, we can see that the read lines method creates a list of each line of data
print(wd_list)

