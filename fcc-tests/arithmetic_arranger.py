# This takes a provided list of equations and converts them to a format that matches the way basic arithmetic is taught. Will optionally solve the equations with the second argument

def arithmetic_arranger(problems,solve):
    numerator = ""
    denominator = ""
    line = ""
    total = ""
    # validate there are no more than five problems supplied.
    if len(problems) > 5:
            return "Error: Too Many Problems."
    for problem in problems:
        problem = problem.split()
        # separate out elements of each formula
        numerators = problem[0]
        denominators = problem[2]
        operators =  problem[1]

        # Validate only addition/subtraction operators are in use
        if '+' not in operators and '-' not in operators:
            return "Error: Operator must be '+' or '-'."

        #Validates that only digits are provided
        if not numerators.isdigit() or not denominators.isdigit():
            return "Error: Numbers must only contain digits."

        # Validates that no more than four digits are provided
        if len(numerators) > 4 or len(denominators) > 4:
            return "Error: Numbers cannot be more than four digits."

        # Calculating answer to equation, if a solve argument is provided.
        if solve is True:
            topnums = int(numerators)
            bottomnums = int(denominators)
            if operators == '+':
                answers = topnums + bottomnums
            else: 
                answers = topnums - bottomnums
        else:
            answers = ""
        #length - determine the max length of each problem
        length = max(len(numerators),len(denominators)) + 2

        # set top and bottom of equation to justify based on max length
        top = numerators.rjust(length)
        bottom = denominators.rjust(length - 2)
        answer = str(answers).rjust(length)
        # determine dashed line length
        x = ""
        while len(x) < length: 
            x = (x + "-")

        # combine the each iteration of the loop to build each row of the final string of equations
        numerator += top + "    "
        denominator += operators + " " + bottom + "    "
        line += x + "    "
        total += answer + "    "

        # Assemble all rows into a single string
        arranged_problems = (numerator + "\n" + denominator + "\n" + line + "\n" + total)


    return arranged_problems
    


print(arithmetic_arranger(["22 + 98", "380 - 213", "4555 - 43", "123 + 49","5 + 6"],True))

