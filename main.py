class NPDA:
    def __init__(self):
        self.stack = []

    def accepts(self, input_string):
        return self._accept('q0', input_string, 0, ['Z'])

    def _accept(self, state, input_string, index, stack):
        if state == 'q_accept' and index == len(input_string) and stack == ['Z']:
            return True
        if index > len(input_string):
            return False

        symbol = input_string[index] if index < len(input_string) else ''
        transitions = []

        if state == 'q0':
            if index < len(input_string):
                transitions.append(('q0', index + 1, stack + [symbol]))
                transitions.append(('q1', index, stack))

        if state == 'q1':
            if index < len(input_string):
                if stack and stack[-1] == symbol:
                    transitions.append(('q1', index + 1, stack[:-1]))
                else:
                    return False
            elif stack == ['Z']:
                transitions.append(('q_accept', index, stack))

        if state == 'q_accept' and index == len(input_string) and stack == ['Z']:
            return True

        for new_state, new_index, new_stack in transitions:
            if self._accept(new_state, input_string, new_index, new_stack):
                return True

        return False
