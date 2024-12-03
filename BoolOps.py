from Stacks import operand_stack, dictionary_stack
from Colors import RESET, RED

class BoolOps:
    @staticmethod
    def eq():
        if operand_stack.size() >= 2:
            b = operand_stack.pop()
            a = operand_stack.pop()
            res = a == b
            operand_stack.push(res)
        else:
            print(RED + " not enough operands" + RESET)
    
    @staticmethod
    def ne():
        if operand_stack.size() >= 2:
            b = operand_stack.pop()
            a = operand_stack.pop()
            res = a != b
            operand_stack.push(res)
        else:
            print(RED + " not enough operands" + RESET)
    
    @staticmethod
    def ge():
        if operand_stack.size() >= 2:
            b = operand_stack.pop()
            a = operand_stack.pop()
            res = a >= b
            operand_stack.push(res)
        else:
            print(RED + " not enough operands" + RESET)
    
    @staticmethod
    def gt():
        if operand_stack.size() >= 2:
            b = operand_stack.pop()
            a = operand_stack.pop()
            res = a > b
            operand_stack.push(res)
        else:
            print(RED + " not enough operands" + RESET)
    
    @staticmethod
    def le():
        if operand_stack.size() >= 2:
            b = operand_stack.pop()
            a = operand_stack.pop()
            res = a <= b
            operand_stack.push(res)
        else:
            print(RED + " not enough operands" + RESET)
    
    @staticmethod
    def lt():
        if operand_stack.size() >= 2:
            b = operand_stack.pop()
            a = operand_stack.pop()
            res = a < b
            operand_stack.push(res)
        else:
            print(RED + " not enough operands" + RESET)
    
    @staticmethod
    def my_true():
        operand_stack.push(True)
    
    @staticmethod
    def my_false():
        operand_stack.push(False)
    
dictionary_stack.peek()["eq"] = BoolOps.eq
dictionary_stack.peek()["ne"] = BoolOps.ne
dictionary_stack.peek()["ge"] = BoolOps.ge
dictionary_stack.peek()["gt"] = BoolOps.gt
dictionary_stack.peek()["le"] = BoolOps.le
dictionary_stack.peek()["lt"] = BoolOps.lt
dictionary_stack.peek()["true"] = BoolOps.my_true
dictionary_stack.peek()["false"] = BoolOps.my_false