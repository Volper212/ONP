expression = '2 3 5 / 2 32.23 + * +'
stack = []
for token in expression.split():
    try:
        stack.append(float(token))
    except ValueError:
        b = stack.pop()
        if len(stack) == 0:
            if token == '-':
                stack.append(-b)
            elif token == '+':
                stack.append(b)
            else:
                raise Exception('Unexpected token')
        else:
            a = stack.pop()
            if token == '*':
                stack.append(a * b)
            elif token == '/':
                stack.append(a / b)
            elif token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            else:
                raise Exception('Unexpected token')
print(stack.pop())
