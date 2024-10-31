def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    topParts = []
    bottomParts = []
    dashes = []
    answerParts = []

    for problem in problems:
        operatorPlus = problem.find(' + ')
        operatorMinus = problem.find(' - ')
        if operatorPlus == -1 and operatorMinus == -1:
            return "Error: Operator must be '+' or '-'."

        operatorIndex = max(operatorPlus, operatorMinus)
        left = problem[0:operatorIndex]
        right = problem[operatorIndex + 3:]
        if len(left) > 4 or len(right) > 4:
            return "Error: Numbers cannot be more than four digits."

        if left.isnumeric() == False or right.isnumeric() == False:
            return "Error: Numbers must only contain digits."

        result = int(left) + int(right)
        operatorSign = '+'
        if operatorMinus > -1:
            result = int(left) - int(right)
            operatorSign = '-'

        maxLength = max(len(left), len(right)) + 2
        topParts.append('{message: >{width}}'.format(
            message=left, width=maxLength))
        bottomParts.append(
            operatorSign + '{message: >{width}}'.format(message=right, width=maxLength - 1))
        dashes.append('{message:{fill}>{width}}'.format(
            message='', fill='-', width=maxLength))

        answerParts.append('{message: >{width}}'.format(
            message=result, width=maxLength))

        # print(left, right, result, maxLength)
        # print(topParts)
        # print(bottomParts)
        # print(dashes)
        # print(answerParts)

    # print(topParts)
    top = '    '.join(topParts)
    bottom = '    '.join(bottomParts)
    dash = '    '.join(dashes)
    answer = '    '.join(answerParts)

    if show_answers:
        return f'{top}\n{bottom}\n{dash}\n{answer}'

    return f'{top}\n{bottom}\n{dash}'

# print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')

# print(f'\n{arithmetic_arranger(["32 + 698", "32 + 698" , "32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')


print(f'\n{arithmetic_arranger(["3 + 855", "988 + 40"], True)}')
