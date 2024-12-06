from Parser import Parser
from Colors import RED, RESET

class IO_Ops:
    @staticmethod
    def print():
        from PostScriptInterpreter import operand_stack
        if operand_stack.size() >= 1:
            print(operand_stack.pop())
        else:
            print(RED + " not enough operands" + RESET)

    @staticmethod
    def eq_op():
        from PostScriptInterpreter import operand_stack
        if operand_stack.size() >= 1:
            print(operand_stack.pop())
        else:
            print(RED + " not enough operands" + RESET)
    
    @staticmethod
    def eqeq_op():
        from PostScriptInterpreter import operand_stack
        if operand_stack.size() >= 1:
            value = operand_stack.pop()
            if isinstance(value, str):
                print(f"({value})")
            elif isinstance(value, dict):
                print(f"<<{value}>>")
            elif isinstance(value, list):
                IO_Ops._print_proc_or_list(value)
            else:
                print(value)
        else:
            print(RED + " not enough operands" + RESET)
    
    @staticmethod
    def _print_proc_or_list(value):
        if isinstance(value[-1], str):
            if IO_Ops._is_proc(value):
                IO_Ops._print_proc(value)
            else:
                print(value)
        else:
            print(value)
    
    @staticmethod
    def _is_proc(value):
        from PostScriptInterpreter import dictionary_stack
        found_dict = None
        for d in reversed(dictionary_stack.items):
            if value[-1] in d:
                found_dict = d
                break
        if found_dict:
            return True
        return False
    
    @staticmethod
    def _print_proc(value):
        print("{ ", end="")
        for elem in value:
            print(elem, end=" ")
        print("}")