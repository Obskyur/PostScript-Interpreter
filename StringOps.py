from Colors import RESET, RED

class StringOps:
    @staticmethod
    def _length():
        from PostScriptInterpreter import operand_stack
        if operand_stack.size() >= 1:
            string = operand_stack.pop()
            res = len(string)
            operand_stack.push(res)
        else:
            print(RED + " not enough operands" + RESET)
    
    @staticmethod
    def _get():
        from PostScriptInterpreter import operand_stack
        if operand_stack.size() >= 2:
            index = operand_stack.pop()
            string = operand_stack.pop()
            res = string[index]
            operand_stack.push(res)
        else:
            print(RED + " not enough operands" + RESET)
    
    @staticmethod
    def _getinterval():
        from PostScriptInterpreter import operand_stack
        if operand_stack.size() >= 3:
            count = operand_stack.pop()
            index = operand_stack.pop()
            string = operand_stack.pop()
            res = string[index:index+count-1]
            operand_stack.push(res)
        else:
            print(RED + " not enough operands" + RESET)
    
    @staticmethod
    def _putinterval():
        from PostScriptInterpreter import operand_stack
        if operand_stack.size() >= 3:
            string2 = operand_stack.pop()
            index = operand_stack.pop()
            string1 = operand_stack.pop()
            res = string1[:index] + string2 + string1[index:]
            operand_stack.push(res)
        else:
            print(RED + " not enough operands" + RESET)
