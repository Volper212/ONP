input_string = '2+3 / 5*(2+32.23)'
tokens = []
for expression in input_string.split():
    lastIndex = 0
    for i in range(len(expression)):
        if expression[i] in ['+', '*', '(', ')', '/']:
            if expression[lastIndex:i]:
                tokens.append(float(expression[lastIndex:i]))
            lastIndex = i + 1
            tokens.append(expression[i])
    if expression[lastIndex:]:
        tokens.append(float(expression[lastIndex:]))
output = []
stack = []
priorities = {'(': 0, '+': 1, '*': 2, '/': 2}
for token in tokens:
    if type(token) is float:
        output.append(token)
    elif token == '(':
        stack.append('(')
    elif token == ')':
        if stack:
            last = stack.pop()
            while last != '(':
                output.append(last)
                last = stack.pop()
    else:
        while stack and priorities[stack[-1]] >= priorities[token]:
            output.append(stack.pop())
        stack.append(token)
output.extend(reversed(stack))
print(output)
