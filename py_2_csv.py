# Make sure you have the CSV file created first, and it is not open.
file = open('test1.csv', 'w')

# Data in '' Are the headers 
line1 = file.write('Mask,Turtle,Weapons\n') #only one item in '' with write

# Data in '' is a row 
line2 = file.writelines([
    'blue,Leo,Sword\n',
    'red,Raph,Sai\n',
    'purple,Don,Bo\n', 
    'orange,Mike,nunchucks\n'
    ])

file.close()