import pytest


def size(lst: list) -> int:
    return len(lst)


def is_empty(lst: list) -> bool:
    return len(lst) == 0


def peek(lst: list) -> any:
    return lst[-1]


def pop(lst: list) -> any:
    return lst.pop()


def push(element: any, sequence: list):
    sequence.append(element)


def custom_func(sequence: str) -> bool:
    stack = []
    if sequence == '':
        return False
    for letter in sequence:
        if letter in "({[":
            push(letter, stack)
        elif letter in ")}]" and is_empty(stack):
            return False
        else:
            check = pop(stack)
            if check == '(' and letter == ')':
                continue
            if check == '{' and letter == '}':
                continue
            if check == '[' and letter == ']':
                continue
            return False
    return is_empty(stack)


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
