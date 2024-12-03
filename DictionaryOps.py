from Stacks import dictionary_stack, operand_stack
from LimitedDict import LimitedDict

class DictionaryOps:
    @staticmethod
    def dict():
        if operand_stack.size() >= 1:
            operand_stack.push(LimitedDict(operand_stack.pop()))
        else:
            print(" not enough operands")
    
    @staticmethod
    def length():
        if operand_stack.size() >= 1:
            dictionary = operand_stack.peek()
            if isinstance(dictionary, LimitedDict):
                operand_stack.push(len(dictionary.dict))
            else:
                print(" not a dictionary")
        else:
            print(" not enough operands")
    
    @staticmethod
    def maxlength():
        if operand_stack.size() >= 1:
            dictionary = operand_stack.peek()
            if isinstance(dictionary, LimitedDict):
                operand_stack.push(dictionary.max_size)
            else:
                print(" not a dictionary")
        else:
            print(" not enough operands")
    
    @staticmethod
    def begin():
        dictionary_stack.push(operand_stack.pop())
    
    @staticmethod
    def end():
        if dictionary_stack.size() > 1:
            dictionary_stack.pop()
        else:
            print("dictionary stack cannot be empty")
    
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
            print(" not enough operands")

dictionary_stack.peek()["dict"] = DictionaryOps.dict
dictionary_stack.peek()["length"] = DictionaryOps.length
dictionary_stack.peek()["maxlength"] = DictionaryOps.maxlength
dictionary_stack.peek()["begin"] = DictionaryOps.begin
dictionary_stack.peek()["end"] = DictionaryOps.end
dictionary_stack.peek()["def"] = DictionaryOps._def