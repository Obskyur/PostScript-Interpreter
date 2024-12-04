from Colors import RESET, RED
import math

class MathOps:
    def __init__(self):
        pass

    @staticmethod
    def add():
        from PostScriptInterpreter import operand_stack
        if operand_stack.size() >= 2:
            op1 = operand_stack.pop()
            op2 = operand_stack.pop()
            res = op1 + op2
            operand_stack.push(res)
        else:
            print(RED + " not enough operands" + RESET)

    @staticmethod
    def sub():
        from PostScriptInterpreter import operand_stack
        if operand_stack.size() >= 2:
            op2 = operand_stack.pop()
            op1 = operand_stack.pop()
            res = op1 - op2
            operand_stack.push(res)
        else:
            print(RED + " not enough operands" + RESET)

    @staticmethod
    def mul():
        from PostScriptInterpreter import operand_stack
        if operand_stack.size() >= 2:
            op1 = operand_stack.pop()
            op2 = operand_stack.pop()
            res = op1 * op2
            operand_stack.push(res)
        else:
            print(RED + " not enough operands" + RESET)

    @staticmethod
    def div():
        from PostScriptInterpreter import operand_stack
        if operand_stack.size() >= 2:
            op2 = operand_stack.pop()
            op1 = operand_stack.pop()
            res = op1 / op2
            operand_stack.push(res)
        else:
            print(RED + " not enough operands" + RESET)

    @staticmethod
    def idiv():
        from PostScriptInterpreter import operand_stack
        if operand_stack.size() >= 2:
            op2 = operand_stack.pop()
            op1 = operand_stack.pop()
            res = op1 // op2
            operand_stack.push(res)
        else:
            print(RED + " not enough operands" + RESET)

    @staticmethod
    def mod():
        from PostScriptInterpreter import operand_stack
        if operand_stack.size() >= 2:
            op2 = operand_stack.pop()
            op1 = operand_stack.pop()
            res = op1 % op2
            operand_stack.push(res)
        else:
            print(RED + " not enough operands" + RESET)

    @staticmethod
    def abs():
        from PostScriptInterpreter import operand_stack
        if operand_stack.size() >= 1:
            op = operand_stack.pop()
            res = abs(op)
            operand_stack.push(res)
        else:
            print(RED + " not enough operands" + RESET)

    @staticmethod
    def neg():
        from PostScriptInterpreter import operand_stack
        if operand_stack.size() >= 1:
            op = operand_stack.pop()
            res = -op
            operand_stack.push(res)
        else:
            print(RED + " not enough operands" + RESET)
    
    @staticmethod
    def ceiling():
        from PostScriptInterpreter import operand_stack
        if operand_stack.size() >= 1:
            op = operand_stack.pop()
            res = math.ceil(op)
            operand_stack.push(res)
        else:
            print(RED + " not enough operands" + RESET)
    
    @staticmethod
    def floor():
        from PostScriptInterpreter import operand_stack
        if operand_stack.size() >= 1:
            op = operand_stack.pop()
            res = math.floor(op)
            operand_stack.push(res)
        else:
            print(RED + " not enough operands" + RESET)
    
    @staticmethod
    def round():
        from PostScriptInterpreter import operand_stack
        if operand_stack.size() >= 1:
            op = operand_stack.pop()
            res = round(op)
            operand_stack.push(res)
        else:
            print(RED + " not enough operands" + RESET)
    
    @staticmethod
    def sqrt():
        from PostScriptInterpreter import operand_stack
        if operand_stack.size() >= 1:
            op = operand_stack.pop()
            res = math.sqrt(op)
            operand_stack.push(res)
        else:
            print(RED + " not enough operands" + RESET)
