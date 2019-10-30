"""
Multi
Line
Comments
"""

# Open
myFile = open('demofile.txt', 'w')

# Info
print('Name: ', myFile.name)
print('Is Closed: ', myFile.closed)
print('Opening Mode: ', myFile.mode)

# Write
print('<<<------------------- Write ----------------------------->>>\n\n')
myString = 'Input String One to file \n' \
           'Input String Two to file \n'

myFile.write(myString)
myFile.write('Input String Tree to file \n')
myFile.close()

print('<<<------------------- Appended ----------------------------->>>\n\n')
# Append
myFile = open('demofile.txt', 'a')
myFile.write('Input String Four append to file \n')
myFile.close()

# Read
print('<<<------------------- Read 1000 ----------------------------->>>\n\n')
myFile = open('demofile.txt', 'r+')
text = myFile.read(1000)
print(text)
