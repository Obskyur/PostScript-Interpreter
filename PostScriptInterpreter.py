from Stack import Stack
from StackOps import StackOps
from MathOps import MathOps
from DictionaryOps import DictionaryOps
from StringOps import StringOps
from BoolOps import BoolOps
from BinOps import BinOps
from FlowControlOps import FlowControlOps

# Create application stacks
dictionary_stack = Stack()
operand_stack = Stack()
dictionary_stack.push({})

# Add stack operations to the dictionary
dictionary_stack.peek()["exch"] = StackOps.exch_op
dictionary_stack.peek()["pop"] = StackOps.pop_op
dictionary_stack.peek()["copy"] = StackOps.copy_op
dictionary_stack.peek()["dup"] = StackOps.dup_op
dictionary_stack.peek()["clear"] = StackOps.clear_op
dictionary_stack.peek()["count"] = StackOps.count_op

# Add flow control operations to the dictionary
dictionary_stack.peek()["if"] = FlowControlOps.if_op
dictionary_stack.peek()["ifelse"] = FlowControlOps.ifelse_op
dictionary_stack.peek()["for"] = FlowControlOps.for_op
dictionary_stack.peek()["repeat"] = FlowControlOps.repeat_op

# Add boolean operations to the dictionary
dictionary_stack.peek()["eq"] = BoolOps.eq
dictionary_stack.peek()["ne"] = BoolOps.ne
dictionary_stack.peek()["ge"] = BoolOps.ge
dictionary_stack.peek()["gt"] = BoolOps.gt
dictionary_stack.peek()["le"] = BoolOps.le
dictionary_stack.peek()["lt"] = BoolOps.lt
dictionary_stack.peek()["true"] = BoolOps.true_op
dictionary_stack.peek()["false"] = BoolOps.false_op

# Add string operations to the dictionary
dictionary_stack.peek()["length"] = StringOps._length
dictionary_stack.peek()["get"] = StringOps._get
dictionary_stack.peek()["getinterval"] = StringOps._getinterval
dictionary_stack.peek()["putinterval"] = StringOps._putinterval

# Add binary operations to the dictionary
dictionary_stack.peek()["and"] = BinOps.and_op
dictionary_stack.peek()["not"] = BinOps.not_op
dictionary_stack.peek()["or"] = BinOps.or_op

# Add dictionary operations to the dictionary
dictionary_stack.peek()["dict"] = DictionaryOps._dict
dictionary_stack.peek()["length"] = DictionaryOps._length
dictionary_stack.peek()["maxlength"] = DictionaryOps._maxlength
dictionary_stack.peek()["begin"] = DictionaryOps._begin
dictionary_stack.peek()["end"] = DictionaryOps._end
dictionary_stack.peek()["def"] = DictionaryOps._def

# Add math operations to the dictionary
dictionary_stack.peek()["add"] = MathOps.add
dictionary_stack.peek()["sub"] = MathOps.sub
dictionary_stack.peek()["mul"] = MathOps.mul
dictionary_stack.peek()["div"] = MathOps.div
dictionary_stack.peek()["idiv"] = MathOps.idiv
dictionary_stack.peek()["mod"] = MathOps.mod
dictionary_stack.peek()["abs"] = MathOps.abs
dictionary_stack.peek()["neg"] = MathOps.neg
dictionary_stack.peek()["ceiling"] = MathOps.ceiling
dictionary_stack.peek()["floor"] = MathOps.floor
dictionary_stack.peek()["round"] = MathOps.round
dictionary_stack.peek()["sqrt"] = MathOps.sqrt