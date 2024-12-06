from Colors import RESET, RED
from LimitedDict import LimitedDict

class DictionaryOps:
    @staticmethod
    def _dict():
        from PostScriptInterpreter import operand_stack
        if operand_stack.size() >= 1:
            operand_stack.push(LimitedDict(operand_stack.pop()))
        else:
            print(RED + " not enough operands" + RESET)
    
    @staticmethod
    def _length():
        from PostScriptInterpreter import operand_stack
        if operand_stack.size() >= 1:
            item = operand_stack.peek()
            if isinstance(item, LimitedDict):
                operand_stack.push(len(item.dict))
            elif isinstance(item, str):
                operand_stack.push(len(item))
            else:
                print(RED + " not a dictionary" + RESET)
        else:
            print(RED + " not enough operands" + RESET)
    
    @staticmethod
    def _maxlength():
        from PostScriptInterpreter import operand_stack
        if operand_stack.size() >= 1:
            dictionary = operand_stack.peek()
            if isinstance(dictionary, LimitedDict):
                operand_stack.push(dictionary.max_size)
            else:
                print(RED + " not a dictionary" + RESET)
        else:
            print(RED + " not enough operands" + RESET)
    
    @staticmethod
    def _begin():
        from PostScriptInterpreter import operand_stack, dictionary_stack
        dictionary_stack.push(operand_stack.pop())
    
    @staticmethod
    def _end():
        from PostScriptInterpreter import dictionary_stack
        if dictionary_stack.size() > 1:
            dictionary_stack.pop()
        else:
            print(RED + " dictionary stack cannot be empty" + RESET)
    
    @staticmethod
    def _def():
        from PostScriptInterpreter import operand_stack, dictionary_stack
        if operand_stack.size() >=2:
            value = operand_stack.pop()
            name = operand_stack.pop()

            if isinstance(name, str) and name.startswith("/"):
                key = name[1:]
                dictionary_stack.peek()[key] = value
            else:
                operand_stack.push(name)
                operand_stack.push(value)
        else:
            print(RED + " not enough operands" + RESET)
