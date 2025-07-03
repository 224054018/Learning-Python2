#Exception handling : allows a programmer to deal withrun time errors or an Exception
#EXCEPTION is a event that occurs during the execution of the programm disrupting the- 
# normal flow of a programm's execution
try:
    print(x)
    '''
except: NameError:
    print("Variable x is not defined")
'''

except NameError:
    print("Variable x is not defined")
else:
    print("Everhing went wrong")
    
x = -1

if x <0:
    raise Exception("Sorry no numbers below 0")