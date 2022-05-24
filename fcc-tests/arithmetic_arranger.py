# to dos:
# Break numerator and denominator into two lines
# Right align


from operator import contains

from numpy import True_


def arithmetic_arranger(problems):
    arranged_problems = list()
    for problem in problems:
        #Converts subtraction operator to negative denominator and removes addition operator (if you decide to do the math)
        #problem = problem.replace('- ','-')
        #problem = problem.replace('+ ','')
        problem = problem.split()
        #print(problem)
        #seeks the highest character count number for determining hspace
        longest_num = len(max(problem,key=len))

        for number in problem:
            numerator = number[0]
            denominator = number[1]
            print(numerator)
        #problem = (problem[0] + "\n" + problem[1] + " " + problem [2])
        #print(problem)
        #problem = problem.replace('+','\n+')
        #problem = (problem +  "\n" + "----")
        #print(problem)
        #print(problem_list)
        # appends each element of the list to the arranged_problems variable
        # arranged_problems.append(problem)
    return arranged_problems



print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))

