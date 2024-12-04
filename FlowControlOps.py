from Colors import RESET, RED
from Parser import Parser as Parse

class FlowControlOps:
    @staticmethod
    def if_op():
        from PostScriptInterpreter import operand_stack, dictionary_stack
        if operand_stack.size() >= 2:
            proc = operand_stack.pop()
            condition = operand_stack.pop()
            if condition:
                # If it's a list, it's a code block
                if isinstance(proc, list):
                    for token in proc:
                        Parse.input(token, operand_stack, dictionary_stack)
                # If it's a string, it's a name
                else:
                    Parse.input(proc[1:], operand_stack, dictionary_stack)
        else:
            print(RED + " not enough operands" + RESET)
    
    @staticmethod
    def ifelse_op():
        from PostScriptInterpreter import operand_stack, dictionary_stack
        if operand_stack.size() >= 3:
            else_proc = operand_stack.pop()
            if_proc = operand_stack.pop()
            condition = operand_stack.pop()
            if condition:
                # If it's a list, it's a code block
                if isinstance(proc, list):
                    for token in proc:
                        Parse.input(token, operand_stack, dictionary_stack)
                # If it's a string, it's a name
                else:
                    Parse.input(proc[1:], operand_stack, dictionary_stack)
            else:
                for token in else_proc:
                    Parse.input(token, operand_stack, dictionary_stack)
        else:
            print(RED + " not enough operands" + RESET)
    
    @staticmethod
    def for_op():
        from PostScriptInterpreter import operand_stack, dictionary_stack
        if operand_stack.size() >= 4:
            proc = operand_stack.pop()
            end = operand_stack.pop()
            step = operand_stack.pop()
            start = operand_stack.pop()
            for i in range(start, end, step):
                # If it's a list, it's a code block
                if isinstance(proc, list):
                    for token in proc:
                        Parse.input(token, operand_stack, dictionary_stack)
                # If it's a string, it's a name
                else:
                    Parse.input(proc[1:], operand_stack, dictionary_stack)
        else:
            print(RED + " not enough operands" + RESET)
    
    @staticmethod
    def repeat_op():
        from PostScriptInterpreter import operand_stack, dictionary_stack
        if operand_stack.size() >= 2:
            proc = operand_stack.pop()
            n = operand_stack.pop()
            for i in range(n):
                # If it's a list, it's a code block
                if isinstance(proc, list):
                    for token in proc:
                        Parse.input(token, operand_stack, dictionary_stack)
                # If it's a string, it's a name
                else:
                    Parse.input(proc[1:], operand_stack, dictionary_stack)
        else:
            print(RED + " not enough operands" + RESET)
