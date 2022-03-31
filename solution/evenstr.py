#Write a script to enter five string in a list and check and print string whose length has even number of character without any string function.
l=[]
count=0
def list(l):
    for i in range(5):
        s=input("Enter any string : ")
        l.append(s)
list(l)
def evenlength(l):
    for i in l:
        count=0
        for j in i:
            count=count+1
        if(count%2==0):
            print("The list is {} and its length is {}.".format(i,count))
evenlength(l)
