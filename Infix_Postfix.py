class InfixToPostfix():

    def __init__(self):
        pass

    def postfix(self, expression):
        dict_precedence = {    #storing the precedence of operators in a dictionary
            '+' : 1,
            '-' : 1,
            '/' : 2,
            '*' : 2
        }
        stack = []
        exp = []
        exp_arr = expression.split(' ')   # ['10' '*' '2' '+' '5']
        for char in exp_arr:
            if char[0].isdigit(): # operands are directly pushed onto a exp list
                exp.append(char)
            else:
                if stack == []:
                    stack.append(char)
                elif dict_precedence[char] >= dict_precedence[stack[len(stack)-1]]: #checking for the precedence
                    stack.append(char)
                else:
                    while dict_precedence[char] < dict_precedence[stack[len(stack)-1]]:
                        add_to_exp = stack.pop()
                        exp.append(add_to_exp)
                        stack.append(char)
        while stack:
            add = stack.pop()
            exp.append(add)
        return ' '.join(exp) # 10 2 * 5 +

obj = InfixToPostfix()
print(obj.postfix('10 * 2 + 5'))





