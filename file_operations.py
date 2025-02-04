fp = open("text.txt", "r") # "r" stands for reading the file
print(fp.read()) # read() method gets the entire file content
fp.close() # this is good practice

# same thing using the context manager
# this is more pythonic
with open("text.txt", "r") as f:
    print(f.read())
#no need to close

# read the file line by line
print("now we print it line by line ")
with open("text.txt", "r") as f:
    for line in f: # f is iterable and we get each individual line
        print(line, end="")