from Stacks import dictionary_stack, operand_stack
import math

class Math:
    def __init__(self):
        pass

    @staticmethod
    def add():
        if operand_stack.size() >= 2:
            op1 = operand_stack.pop()
            op2 = operand_stack.pop()
            res = op1 + op2
            operand_stack.push(res)
        else:
            print(" not enough operands")

    @staticmethod
    def sub():
        if operand_stack.size() >= 2:
            op2 = operand_stack.pop()
            op1 = operand_stack.pop()
            res = op1 - op2
            operand_stack.push(res)
        else:
            print(" not enough operands")

    @staticmethod
    def mul():
        if operand_stack.size() >= 2:
            op1 = operand_stack.pop()
            op2 = operand_stack.pop()
            res = op1 * op2
            operand_stack.push(res)
        else:
            print(" not enough operands")

    @staticmethod
    def div():
        if operand_stack.size() >= 2:
            op2 = operand_stack.pop()
            op1 = operand_stack.pop()
            res = op1 / op2
            operand_stack.push(res)
        else:
            print(" not enough operands")

    @staticmethod
    def idiv():
        if operand_stack.size() >= 2:
            op2 = operand_stack.pop()
            op1 = operand_stack.pop()
            res = op1 // op2
            operand_stack.push(res)
        else:
            print(" not enough operands")

    @staticmethod
    def mod():
        if operand_stack.size() >= 2:
            op2 = operand_stack.pop()
            op1 = operand_stack.pop()
            res = op1 % op2
            operand_stack.push(res)
        else:
            print(" not enough operands")

    @staticmethod
    def abs():
        if operand_stack.size() >= 1:
            op = operand_stack.pop()
            res = abs(op)
            operand_stack.push(res)
        else:
            print(" not enough operands")

    @staticmethod
    def neg():
        if operand_stack.size() >= 1:
            op = operand_stack.pop()
            res = -op
            operand_stack.push(res)
        else:
            print(" not enough operands")
    
    @staticmethod
    def ceiling():
        if operand_stack.size() >= 1:
            op = operand_stack.pop()
            res = math.ceil(op)
            operand_stack.push(res)
        else:
            print(" not enough operands")
    
    @staticmethod
    def floor():
        if operand_stack.size() >= 1:
            op = operand_stack.pop()
            res = math.floor(op)
            operand_stack.push(res)
        else:
            print(" not enough operands")
    
    @staticmethod
    def round():
        if operand_stack.size() >= 1:
            op = operand_stack.pop()
            res = round(op)
            operand_stack.push(res)
        else:
            print(" not enough operands")
    
    @staticmethod
    def sqrt():
        if operand_stack.size() >= 1:
            op = operand_stack.pop()
            res = math.sqrt(op)
            operand_stack.push(res)
        else:
            print(" not enough operands")

dictionary_stack.peek()["add"] = Math.add
dictionary_stack.peek()["sub"] = Math.sub
dictionary_stack.peek()["mul"] = Math.mul
dictionary_stack.peek()["div"] = Math.div
dictionary_stack.peek()["idiv"] = Math.idiv
dictionary_stack.peek()["mod"] = Math.mod
dictionary_stack.peek()["abs"] = Math.abs
dictionary_stack.peek()["neg"] = Math.neg
dictionary_stack.peek()["ceiling"] = Math.ceiling
dictionary_stack.peek()["floor"] = Math.floor
dictionary_stack.peek()["round"] = Math.round
dictionary_stack.peek()["sqrt"] = Math.sqrt