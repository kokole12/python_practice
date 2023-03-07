#!/usr/bin/python3

def create_stack():
    stack = []
    return stack

def check_empty(stack):
    if len(stack) == 0:

        return

def push(stack, item):
    stack.append(item)
    print('pushed item: {}'.format(item))

def pop(stack):
    if (check_empty(stack)):
        return "stack is empty"

    return stack.pop()


stack = create_stack()
push(stack, str(1))
push(stack, str(2))
push(stack, str(3))
push(stack, str(4))
print("popped item: " + pop(stack))
print("stack after popping an element: " + str(stack))
