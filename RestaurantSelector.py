'''
stop==True
while stop==True:
    print('Hi')
    stop = False
print('Statement below the loop')
'''
#Amani Minaya
#CS 175L 01
#Restaurant Selector version 2 (why loop) 
vegan=False
veggie=False 
glut=False

#recieving users input
response=str(input('Is anyone in your party a vegetarian?: '))
if response=='yes':
    veggie=True
response=str(input('Is anyone in your party vegan?: '))
if response=='yes':
    vegan= True
response=str(input('is anyone in your party glutan free?: '))
if response=='yes':
    glut=True

#displaying the restaurant options   
print('Here are your restrant options: ')
if veggie==False and vegan==False and glut==False:
    print("Joe's Gourmet Burgers")
    print("Mama's Fine Italian")
    print("Main street Pizza")
if veggie==True and vegan==False and glut==False:
    print("Mama's Fine Italian")
    print("Main street Pizza")
if veggie==True and vegan==False and glut==True:
    print("Main street Pizza")
    print("Corner Cafe")
    print("Chef's Kitchen")
else:
    print("Corner Cafe")
    print("Chef's Kitchen")
    

keep_going=str(input('Would you like to run it again?: '))

while keep_going=='yes':
    #recieving users input
    response=str(input('Is anyone in your party a vegetarian?: '))
    if response=='yes':
        veggie=True
    response=str(input('Is anyone in your party vegan?: '))
    if response=='yes':
        vegan= True
    response=str(input('is anyone in your party glutan free?: '))
    if response=='yes':
        glut=True

    #displaying the restaurant options   
    print('Here are your restrant options: ')
    if veggie==False and vegan==False and glut==False:
        print("Joe's Gourmet Burgers")
        print("Mama's Fine Italian")
        print("Main street Pizza")
    if veggie==True and vegan==False and glut==False:
        print("Mama's Fine Italian")
        print("Main street Pizza")
    if veggie==True and vegan==False and glut==True:
        print("Main street Pizza")
        print("Corner Cafe")
        print("Chef's Kitchen")
    else:
        print("Corner Cafe")
        print("Chef's Kitchen")
    keep_going=str(input('Would you like to run it again?: '))
if keep_going=='no':
    print('ok hope you enjoy ur meal!')
   

