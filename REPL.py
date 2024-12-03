from Stacks import operand_stack, dictionary_stack
from Parser import Parser as Parse
import MathOps
import DictionaryOps

def repl():
    while True:
        user_input = input("REPL> ")
        if user_input.lower() == 'quit':
            break
        Parse.input(user_input, operand_stack, dictionary_stack)
        print(f"Operand Stack: {operand_stack}")

repl()