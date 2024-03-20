import pytest


class Stack:
    def __init__(self):
        self.lst = []

    def size_of_stack(self) -> int:
        return len(self.lst)

    def is_empty(self) -> bool:
        return len(self.lst) == 0

    def peek(self) -> any:
        return self.lst[-1]

    def pop(self) -> any:
        return self.lst.pop()

    def push(self, element: any):
        self.lst.append(element)


def custom_func(sequence: str) -> bool:
    st1 = Stack()
    if sequence == '':
        return False
    for letter in sequence:
        if letter in "({[":
            st1.push(letter)
        elif letter in ")}]" and st1.is_empty():
            return False
        else:
            check = st1.pop()
            if check == '(' and letter == ')':
                continue
            if check == '{' and letter == '}':
                continue
            if check == '[' and letter == ']':
                continue
            return False
    return st1.is_empty()


def using_list_methods(sequence: str) -> bool:
    stack = []
    if sequence == '':
        return False
    for letter in sequence:
        if letter in "({[":
            stack.append(letter)
        elif letter in ")}]" and len(stack) == 0:
            return False
        else:
            check = stack.pop()
            if check == '(' and letter == ')':
                continue
            if check == '{' and letter == '}':
                continue
            if check == '[' and letter == ']':
                continue
            return False
    return len(stack) == 0


if __name__ == '__main__':
    pytest.main()
