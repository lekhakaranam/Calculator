class ExpressionEvaluator():

    def __init__(self):
        pass

    @staticmethod
    def operate(num1, num2, operation):
        if operation == '+':
            return num1 + num2
        elif operation == '-':
            return num1 - num2
        elif operation == '*':
            return num1 * num2
        else:
            return num1 / float(num2)

    #22 2 +
    def evaluate_expression(self, expression: str):
        stack = []
        expression_array = expression.split(' ')         #['22', '2', '+']
        for elem in expression_array:
            if elem[0].isdigit():
                stack.append(int(elem))
            else:
                x = stack.pop()
                y = stack.pop()
                stack.append(ExpressionEvaluator.operate(y, x, elem))
        return stack.pop()

obj = ExpressionEvaluator()
print(obj.evaluate_expression('2 3 1 * + 9 -'))









