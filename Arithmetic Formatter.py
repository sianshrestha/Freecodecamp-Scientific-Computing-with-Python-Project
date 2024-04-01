def arithmetic_arranger(problems, true=None):

# THE ERRORS
    errors = []
    error1 = "Error: Too many problems."
    error2 = "Error: Numbers cannot be more than four digits."
    error3 = "Error: Operator must be '+' or '-'."
    error4 = "Error: Numbers must only contain digits."
# error 1
    if len(problems) > 5 and error1 not in errors:
        return error1

    for i in problems:
        x = i.split()
# error 2
        if (len(x[0]) > 4 or len(x[2]) > 4) and (error2 not in errors):
            return error2
        else:
            errors.append("")
# error 3
        if (i.split()[1]) not in ["+", "-"] and error3 not in errors:
            return error3
        else:
            errors.append("")
# error 4
        if not(x[0].isdigit() and x[2].isdigit()) and (error4 not in errors):
            return error4
        else:
            errors.append("")

# THE CALCULATION

# THE ARRANGEMENT
    problem = [p.split() for p in problems]
    counter = 0
    space = " "
    dash = "-"
    line1 = ""
    line2 = ""
    line3 = ""
    answer = ""
    for p in problems:
        maxoflen = max(len(problem[counter][0]), len(problem[counter][2]))
        firstline = f"{space * 2}{(maxoflen - len(problem[counter][0])) * space}{problem[counter][0]}"
        if counter < len(problems)-1:
            line1 += firstline
            line1 += space*4
        else:
            line1 += firstline

        secondline = f"{problem[counter][1]}{space}{(maxoflen - len(problem[counter][2])) * space}{problem[counter][2]}"
        if counter < len(problems)-1:
            line2 += secondline
            line2 += space*4
        else:
            line2 += secondline

        thirdline = f"{(2 + maxoflen) * dash}"
        if counter < len(problems)-1:
            line3 += thirdline
            line3 += space*4
        else:
            line3 += thirdline

        if problem[counter][1] == '+':
            ans = int(problem[counter][0]) + int(problem[counter][2])
        else:
            ans = int(problem[counter][0]) - int(problem[counter][2])
        fourthline = f"{((maxoflen+2)-len(str(ans)))*space}{ans}"
        if counter < len(problems)-1:
            answer += fourthline
            answer += space*4
        else:
            answer += fourthline
        counter += 1


    if true == True:
        arranged_problems = f"{line1}\n{line2}\n{line3}\n{answer}"
    else:
        arranged_problems = f"{line1}\n{line2}\n{line3}"

    return arranged_problems

