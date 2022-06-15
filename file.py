
#counting number of lines
count_lines = 0
f = open("file2.txt", "r")
for lines in f.readlines():
    count_lines+=1
print(f"the numbers of lines in the text file is {count_lines}")
f.close()