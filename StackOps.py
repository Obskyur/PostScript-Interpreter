from Colors import RESET, RED

class StackOps:
        
    @staticmethod
    def exch_op():
        from PostScriptInterpreter import operand_stack
        if operand_stack.size() >= 2:
            op1 = operand_stack.pop()
            op2 = operand_stack.pop()
            operand_stack.push(op1)
            operand_stack.push(op2)
        else:
            print(RED + " not enough operands" + RESET)

    @staticmethod
    def pop_op():
        from PostScriptInterpreter import operand_stack
        if operand_stack.size() >= 1:
            operand_stack.pop()
        else:
            print(RED + " not enough operands" + RESET)
    
    @staticmethod
    def copy_op():
        from PostScriptInterpreter import operand_stack
        if operand_stack.size() >= 1:
            op1 = operand_stack.peek()
            operand_stack.push(op1)
        else:
            print(RED + " not enough operands" + RESET)
    
    @staticmethod
    def dup_op():
        from PostScriptInterpreter import operand_stack
        if operand_stack.size() >= 1:
            op1 = operand_stack.peek()
            operand_stack.push(op1)
        else:
            print(RED + " not enough operands" + RESET)
    
    @staticmethod
    def clear_op():
        from PostScriptInterpreter import operand_stack
        operand_stack.items = []
    
    @staticmethod
    def count_op():
        from PostScriptInterpreter import operand_stack
        operand_stack.push(operand_stack.size())