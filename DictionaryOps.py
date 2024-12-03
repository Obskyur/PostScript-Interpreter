from Stacks import dictionary_stack, operand_stack
from Colors import RESET, RED
from LimitedDict import LimitedDict

class DictionaryOps:
    @staticmethod
    def _dict():
        if operand_stack.size() >= 1:
            operand_stack.push(LimitedDict(operand_stack.pop()))
        else:
            print(RED + " not enough operands" + RESET)
    
    @staticmethod
    def _length():
        if operand_stack.size() >= 1:
            dictionary = operand_stack.peek()
            if isinstance(dictionary, LimitedDict):
                operand_stack.push(len(dictionary.dict))
            else:
                print(RED + " not a dictionary" + RESET)
        else:
            print(RED + " not enough operands" + RESET)
    
    @staticmethod
    def _maxlength():
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
        dictionary_stack.push(operand_stack.pop())
    
    @staticmethod
    def _end():
        if dictionary_stack.size() > 1:
            dictionary_stack.pop()
        else:
            print(RED + " dictionary stack cannot be empty" + RESET)
    
    @staticmethod
    def _def():
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

dictionary_stack.peek()["dict"] = DictionaryOps._dict
dictionary_stack.peek()["length"] = DictionaryOps._length
dictionary_stack.peek()["maxlength"] = DictionaryOps._maxlength
dictionary_stack.peek()["begin"] = DictionaryOps._begin
dictionary_stack.peek()["end"] = DictionaryOps._end
dictionary_stack.peek()["def"] = DictionaryOps._def