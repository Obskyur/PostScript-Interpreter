from Stacks import operand_stack, dictionary_stack
from Colors import RESET, RED

class StringOps:
    @staticmethod
    def length():
        if operand_stack.size() >= 1:
            string = operand_stack.pop()
            res = len(string)
            operand_stack.push(res)
        else:
            print(RED + " not enough operands" + RESET)
    
    @staticmethod
    def get():
        if operand_stack.size() >= 2:
            index = operand_stack.pop()
            string = operand_stack.pop()
            res = string[index]
            operand_stack.push(res)
        else:
            print(RED + " not enough operands" + RESET)
    
    @staticmethod
    def getinterval():
        if operand_stack.size() >= 3:
            count = operand_stack.pop()
            index = operand_stack.pop()
            string = operand_stack.pop()
            res = string[index:index+count-1]
            operand_stack.push(res)
        else:
            print(RED + " not enough operands" + RESET)
    
    @staticmethod
    def putinterval():
        if operand_stack.size() >= 3:
            string2 = operand_stack.pop()
            index = operand_stack.pop()
            string1 = operand_stack.pop()
            res = string1[:index] + string2 + string1[index:]
            operand_stack.push(res)
        else:
            print(RED + " not enough operands" + RESET)

dictionary_stack.peek()["length"] = StringOps.length
dictionary_stack.peek()["get"] = StringOps.get
dictionary_stack.peek()["getinterval"] = StringOps.getinterval
dictionary_stack.peek()["putinterval"] = StringOps.putinterval