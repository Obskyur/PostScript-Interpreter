from Colors import RESET, RED

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Pop from an empty stack")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("Peek from an empty stack")

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def __repr__(self):
        return str(self.items)
    
    @staticmethod
    def _exch():
        if operand_stack.size() >= 2:
            op1 = operand_stack.pop()
            op2 = operand_stack.pop()
            operand_stack.push(op1)
            operand_stack.push(op2)
        else:
            print(RED + " not enough operands" + RESET)

    @staticmethod
    def _pop():
        if operand_stack.size() >= 1:
            operand_stack.pop()
        else:
            print(RED + " not enough operands" + RESET)
    
    @staticmethod
    def _copy():
        if operand_stack.size() >= 1:
            op1 = operand_stack.peek()
            operand_stack.push(op1)
        else:
            print(RED + " not enough operands" + RESET)
    
    @staticmethod
    def _dup():
        if operand_stack.size() >= 1:
            op1 = operand_stack.peek()
            operand_stack.push(op1)
        else:
            print(RED + " not enough operands" + RESET)
    
    @staticmethod
    def _clear():
        operand_stack.items = []
    
    @staticmethod
    def _count():
        operand_stack.push(operand_stack.size())

operand_stack = Stack()
dictionary_stack = Stack()
dictionary_stack.push({})

dictionary_stack.peek()["exch"] = Stack._exch
dictionary_stack.peek()["pop"] = Stack._pop
dictionary_stack.peek()["copy"] = Stack._copy
dictionary_stack.peek()["dup"] = Stack._dup
dictionary_stack.peek()["clear"] = Stack._clear
dictionary_stack.peek()["count"] = Stack._count
