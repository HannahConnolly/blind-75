'''
https://leetcode.com/problems/implement-queue-using-stacks/

Notes:
Reversing a stack can act as a queue
'''

class MyQueue:

    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def push(self, x: int) -> None:
        self.in_stack.append(x)
        self.print_stacks('push')

    def pop(self) -> int:
        self.peek()
        self.print_stacks('pop')
        return self.out_stack.pop()

    def peek(self) -> int:
        i = 0
        length = len(self.in_stack)
        while i < length:
            print(i)
            self.out_stack.append(self.in_stack.pop())
            i += 1
        print(i, ' < ', length)

        self.print_stacks('peek')
        return self.out_stack[-1]

    def empty(self) -> bool:
        self.print_stacks('empty')
        return len(self.in_stack) == 0 and len(self.out_stack) == 0
        

    def print_stacks(self, funct: str):
        print('- - - - - - - - ')
        print(funct)
        print(self.in_stack)
        print(self.out_stack)

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()