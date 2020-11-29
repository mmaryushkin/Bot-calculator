class Stack():

    def __init__(self, stack: list):
        self.stack = stack

    def push(self, e):
        self.stack.append(e)

    def get_last(self):
        return self.stack.pop()

    def is_empty(self):
        return len(self.stack) == 0

    def top(self):
        return self.stack[-1]
