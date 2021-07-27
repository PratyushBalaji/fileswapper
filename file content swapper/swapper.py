def swapfile():
    file1 = input("What is the 1st file's name? ")
    file2 = input("What is the 2nd file's name? ")
    with open(file1,"r") as a:
        data1 = a.read()
    with open(file2,"r") as b:
        data2 = b.read()
    with open (file1,'w') as c:
        c.write(data2)
    with open(file2,"w") as d:
        d.write(data1)
swapfile()
print()
input("The file contents have been swapped! (Press enter to exit) ")