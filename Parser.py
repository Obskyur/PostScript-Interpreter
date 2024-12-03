class Parser:
    @staticmethod
    def _bool(value):
        if value == "true":
            return (True, True)
        elif value == "false":
            return (True, False)
        else:
            return False

    @staticmethod
    def _number(value):
        try:
            float_value = float(value)
            if float_value.is_integer():
                return (True, int(float_value))
            else:
                return (True, float_value)
        except ValueError:
            return False

    @staticmethod
    def _code_block(value):
        if len(value) >= 2 and value.startswith("{") and value.endswith("}"):
            return (True, value[1:-1].strip().split())

    @staticmethod
    def _name_constant(value):
        if value.startswith("/"):
            return (True, value)
    
    @staticmethod
    def _constants(input):
        res = Parser._bool(input)
        res = res or Parser._number(input)
        res = res or Parser._code_block(input)
        res = res or Parser._name_constant(input)
        return res

    @staticmethod
    def input(input, operand_stack, dictionary_stack):
        result = Parser._constants(input)
        if result:
            operand_stack.push(result[1])
        else:
            Parser._lookup_in_dictionary(input, operand_stack, dictionary_stack)

    @staticmethod
    def _lookup_in_dictionary(input, operand_stack, dictionary_stack):
        # search in the dictionary stack for the input, starting from the top
        for d in reversed(dictionary_stack.items):
            if input in d:
                found_dict = d
                break
        if found_dict:
            value = found_dict[input]
            if callable(value):
                value()
            elif isinstance(value, list):
                for item in value:
                    Parser.input(item, operand_stack, dictionary_stack)
            else:
                operand_stack.push(value)
        else:
            print(" not in dictionary ") #TODO: : implement lexical scoping