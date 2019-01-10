class stack:

    def __init__(self):
        self.stack = []

    def push(self, item):
        return self.stack.append(item)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return  self.stack[len(self.stack) - 1]

    def size(self):
        return len(self.stack)

    def isEmpty(self):
        return self.stack == []