def average_calculation(*args):
    return sum(args)/len(args)


def addition_of_2_numbers(a,b):
    return a+b


def multiplication_of_2_numbers(a,b):
    return a*b

if __name__=='__main__':
    op1=average_calculation(1,2,3,4)
    op2=addition_of_2_numbers(1,2)
    op3=multiplication_of_2_numbers(1,2)
    print(op1,op2,op3)

