class Calculator(object):
    def calc(self, input_str):
        string = self.infixToPostfix(input_str).split()
        numsStack = []

        for x in string:
            if x in '0123456789':
                numsStack.append(x)
            else:
                num2 = float(numsStack.pop())
                num1 = float(numsStack.pop())
                if x == "*":
                    numsStack.append(num1 * num2)
                elif x == "/":
                    numsStack.append(num1 / num2)
                elif x == "+":
                    numsStack.append(num1 + num2)
                else:
                    numStack.append(num1 - num2)
        return numsStack.pop()



    def infixToPostfix(self, str):
        order = {
            "*": 3,
            "/": 3,
            "+": 2,
            "-": 2,
            "(": 1
        }
        signs = []
        postfix = []
        strlist = str.split()

        for x in strlist:
            if x in '0123456789':
                postfix.append(x)
            elif x == '(':
                signs.append(x)
            elif x == ')':
                topsign = signs.pop()
                while topsign != '(':
                    postfix.append(topsign)
                    topsign = signs.pop()
            else:
                while len(signs) > 0 and (order[signs[len(signs)-1]] >= order[x]):
                    postfix.append(signs.pop())
                signs.append(x)

        while len(signs) > 0:
            postfix.append(signs.pop())
        return " ".join(postfix)

    def calc_with_vars(self, input_list):
        dict = {}
        answer = []
        for x in input_list:
            list = x.split(' = ')
            dict[list[0]] = list[1]
            answer.append(list[0])
        for key,value in dict.iteritems():
            expression = value.split(' ')
            for i in range(len(expression)):
                if expression[i] in dict:
                    expression[i] = dict[expression[i]]
            dict[key] = self.calc(" ".join(expression))
        for j in range (len(answer)):
            answer[j] = dict[answer[j]]
        return answer

def main():
    calculator = Calculator()

    print "First Step"
    print calculator.calc("3 + 4 * 5 / 7")

    print "\nSecond Step"
    print calculator.calc("( 3 + 4 ) * 5 / 7")

    print "\nThird Step"
    print calculator.calc_with_vars(
        ["pi = 3",
         "pizza = 9 * 9 * pi"])

main()
