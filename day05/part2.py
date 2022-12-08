import re
from collections import deque
from itertools import takewhile

command_regex = re.compile(r'move (\d+) from (\d) to (\d)')


def boxes_and_instructions(path):
    with open(path, 'r') as file:
        it = iter(file.readlines())
        return takewhile(lambda x: x != '\n', it), it

def stacks(box_list):
    stack_list = ['' for _ in range(9)]
    for boxes in box_list:
        for ind, box in enumerate( boxes[1::4]):
            stack_list[ind] += box
    return [list(i[-2::-1].strip()) for i in stack_list]

def commands(commands):
    for command in commands:
        groups = command_regex.match(command.strip()).groups()
        yield int(groups[0]),int(groups[1]) -1,int(groups[2]) - 1

def move(stacks, deque_, n, source, target):
    for _ in range(n):
        deque_.appendleft(stacks[source].pop())
    while deque_:
        stacks_[target].append(deque_.popleft())
        
if __name__ == '__main__':
    PATH = 'day05/data.txt'
    boxes, instructions = boxes_and_instructions(PATH)
    stacks_ = stacks(boxes)
    deque_ = deque()
    for command in commands(instructions):
        move(stacks_, deque_, *command)
    print(''.join(i[-1] for i in stacks_))