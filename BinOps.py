from Colors import RESET, RED

class BinOps:
    @staticmethod
    def and_op():
        from PostScriptInterpreter import operand_stack
        if operand_stack.size() >= 2:
            op1 = operand_stack.pop()
            op2 = operand_stack.pop()
            if isinstance(op1, bool) or isinstance(op2, bool):
                res = op1 and op2
            else:
                res = op1 & op2
            operand_stack.push(res)
        else:
            print(RED + " not enough operands" + RESET)
    
    @staticmethod
    def not_op():
        from PostScriptInterpreter import operand_stack
        if operand_stack.size() >= 1:
            op = operand_stack.pop()
            if isinstance(op, bool):
                res = not op
            else:
                res = ~op
            operand_stack.push(res)
        else:
            print(RED + " not enough operands" + RESET)
    
    @staticmethod
    def or_op():
        from PostScriptInterpreter import operand_stack
        if operand_stack.size() >= 2:
            op1 = operand_stack.pop()
            op2 = operand_stack.pop()
            if isinstance(op1, bool) or isinstance(op2, bool):
                res = op1 or op2
            else:
                res = op1 | op2
            operand_stack.push(res)
        else:
            print(RED + " not enough operands" + RESET)
