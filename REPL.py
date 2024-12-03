from Stacks import operand_stack, dictionary_stack
from Colors import RESET, CYAN
from Parser import Parser as Parse
import MathOps
import DictionaryOps
import StringOps

def repl():
    while True:
        user_input = input(CYAN + "REPL> " + RESET)
        if user_input.lower() == 'quit':
            break
        Parse.input(user_input, operand_stack, dictionary_stack)
        print(f"Operand Stack: {operand_stack}")

repl()