"""
Function has 2 parts, 
    1. Definition 
    2. Call

"""

"""
#Non Return type function 
def function_name(a):
    print(a)


z=function_name('Hello World !')
print(z) #Prints None because its a non return type functions output


#Return type function: 
def return_type_function(a):
    return a*5

output_from_function=return_type_function('*')
print(output_from_function)


# 2 inputs and 2 outputs

def two_inputs_two_outputs(a,b):
    return a*5,b*6

output_1,output_2=two_inputs_two_outputs(1,2)
print(output_1,output_2)

output_3=two_inputs_two_outputs(1,2)
print(output_3)
"""

"""
WAP to have a function named multiplication_table that takes 2 arguments 
multiplication_number and multiplication_upto 
display multiplication table for the multiplication number from 1 till 
multiplication_upto 

The result should be of the format 
X1 X 1 = X1
X1 X 2 = 2X2

def multipliaction_table(multiplication_number,multiplication_upto):
    # print(multiplication_number,multiplication_upto)
    for number in range(1,multiplication_upto+1):
        print(f'{multiplication_number} X {number} = {multiplication_number*number}')


multipliaction_table(13,10)
"""

"""
Write a function named even_checker which accepts 1 argument checks if its even 
if even return True else return False


def even_checker(a):
    if a%2==0:
        return True
    else: 
        return False


num=int(input('Enter number: '))
output_of_function=even_checker(num)
print(output_of_function)

"""
"""
#how to set default values in function 
def complex_function(a=1,b=2,c=3,d=4,e=5,f=6,g=7,h=8):
    print(a,b,c,d,e,f,g,h)


complex_function(a=10,h=14)
"""


#Args and Kwargs 

#Args
# def get_average(*args):
#     args=list(args)
#     print(f'Original args: {args}')
#     args=args[0]
#     print(f'Final args: {args}')
#     return sum(args)/len(args)

# all_numbers=input('Enter all numbers sepearted by comma: ')
# print(f'Original String: {all_numbers}')
# all_numbers=all_numbers.split(',')
# print(f'Converting to List: {all_numbers}')
# all_numbers=[int(i) for i in all_numbers]
# print(f'Converting to int list: {all_numbers}')
# average_number=get_average(all_numbers)
# print(f'Average Calculated as {average_number}')


#kwargs: 
def complex_function_2(**kwargs):
    print(kwargs)

complex_function_2(student_name='Siddhant',
                   student_marks=[10,20,30,40],
                   attendence=50)
