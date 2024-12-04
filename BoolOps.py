from Colors import RESET, RED

class BoolOps:
    @staticmethod
    def eq():
        from PostScriptInterpreter import operand_stack
        if operand_stack.size() >= 2:
            b = operand_stack.pop()
            a = operand_stack.pop()
            res = a == b
            operand_stack.push(res)
        else:
            print(RED + " not enough operands" + RESET)
    
    @staticmethod
    def ne():
        from PostScriptInterpreter import operand_stack
        if operand_stack.size() >= 2:
            b = operand_stack.pop()
            a = operand_stack.pop()
            res = a != b
            operand_stack.push(res)
        else:
            print(RED + " not enough operands" + RESET)
    
    @staticmethod
    def ge():
        from PostScriptInterpreter import operand_stack
        if operand_stack.size() >= 2:
            b = operand_stack.pop()
            a = operand_stack.pop()
            res = a >= b
            operand_stack.push(res)
        else:
            print(RED + " not enough operands" + RESET)
    
    @staticmethod
    def gt():
        from PostScriptInterpreter import operand_stack
        if operand_stack.size() >= 2:
            b = operand_stack.pop()
            a = operand_stack.pop()
            res = a > b
            operand_stack.push(res)
        else:
            print(RED + " not enough operands" + RESET)
    
    @staticmethod
    def le():
        from PostScriptInterpreter import operand_stack
        if operand_stack.size() >= 2:
            b = operand_stack.pop()
            a = operand_stack.pop()
            res = a <= b
            operand_stack.push(res)
        else:
            print(RED + " not enough operands" + RESET)
    
    @staticmethod
    def lt():
        from PostScriptInterpreter import operand_stack
        if operand_stack.size() >= 2:
            b = operand_stack.pop()
            a = operand_stack.pop()
            res = a < b
            operand_stack.push(res)
        else:
            print(RED + " not enough operands" + RESET)
    
    @staticmethod
    def true_op():
        from PostScriptInterpreter import operand_stack
        operand_stack.push(True)
    
    @staticmethod
    def false_op():
        from PostScriptInterpreter import operand_stack
        operand_stack.push(False)
    