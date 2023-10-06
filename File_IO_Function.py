# --- READING A FILE
# f=open("myfile.txt",'r')
# # print(f)

# text = f.read()
# print(text)


# --- WRITING A FILE
# f=open('myfile2.txt','w')
# f=open('myfile2.txt','a')
# f.write('Hello world!')
# f.close()

# -- file open and close automaticaly
# with open('myfile.txt','a') as f:
#     f.write("\nHow are you?")


# --- READLINE METHOD
# f = open('myfile.txt','r')
# while True:
#     # line = f.read()
#     line = f.readline()
#     if not line:
#         break
#     print(line)

# --- other methods
# f=open('myfile.txt','r')
# i=0
# while True:
#     i=i+1
#     line = f.readline()
#     if not line:
#         break
#     m1 = line.split(",")[0]
#     m2 = line.split(",")[1]
#     print(f"Marks of student {i} in Account is: {m1}")
#     print(f"Marks of student {i} in State is: {m2}")
#     print(line)

# -- Write text
# f = open('myfile2.txt','w')
# lines = ['line1\n', 'line2\n', 'line3\n']
# f.writelines(lines)
# f.close()

# f=open('myfile2.txt','w')
# lines = ['line4', 'line5', 'line6']
# for line in lines:
#     f.write(line + '\n')
# f.close()

# with open('file.txt','r') as f:
#     print(type(f))

#     # Move to the 10th byte in the file
#     f.seek(10)

#     # Read the next 5 bytes
#     current_position = f.tell()
#     print(current_position)
#     data=f.read(5)
#     print(data)

# - Create file and add and remove content , read content
with open('sample.txt','w') as f:
    f.write('Hello World!')
    f.truncate(4)

with open('sample.txt','r') as f:
    print(f.read())