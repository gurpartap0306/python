from sys import argv

script,filename=argv

txt = open(filename,'r+')
print("here's your file %r:"%filename)
print(txt.read())

print("we are going to erase ",filename)
print("if you don't want, hit CTRL-C(^C)")
print("press enter to continue")
input("?")

print("truncating the filw. Goodbye!")
txt.truncate()

print("now, i'm going to ask you to for three lines.")

line1=input("line 1: ")
line2=input("line 2: ")
line3=input("line 3: ")
#writing in file
txt.write(line1)
txt.write("\n")
txt.write(line2)
txt.write("\n")
txt.write(line3)
txt.write("\n")

print ("and finally, we close it.")
txt.close()

