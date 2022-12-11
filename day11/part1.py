from operator import add, mul
from collections import deque
import re
import heapq


class MonkeyBusiness:

    def __init__(self, PATH: str):
        self.monkeys = self.read_file(PATH)

    def read_file(self, PATH):
        with open(PATH, 'r') as file:

            return [Monkey.from_string(inp, self) for inp in file.read().split("\n\n")]

    def throw(self, monkey, item):
        self.monkeys[monkey].catch(item)

    def __iter__(self):
        return iter(self.monkeys)

    @property
    def level(self):
        return mul(*heapq.nlargest(2, (x.counter for x in monkey_business)))

class Monkey:
    test_pattern = re.compile(r'divisible by (\d+)')
    action_pattern = re.compile(r'throw to monkey (\d+)')
    operation_pattern = re.compile((r'new = old ([+*]) (\d+|old)'))

    def __init__(self, items: list[int], operation, test: int, true_action: int, false_action: int, game: MonkeyBusiness):
        self.items = deque(items)
        self.test_value = test
        self.counter = 0
        self.true_action = true_action
        self.false_action = false_action
        self.game = game
        self.operation = operation

    def inspect(self):
        self.counter += 1
        item = self.items.pop()
        item = self.operation(item)
        item //= 3
        return item

    def divisibility(self, item):
        if item % self.test_value:
            return self.false_action
        else:
            return self.true_action

    def catch(self, item):
        self.items.appendleft(item)

    def play(self):
        while self.items:
            item = self.inspect()
            self.game.throw(self.divisibility(item), item)

    @classmethod
    def from_string(cls, read_input, game):
        _, items, operation, test, true_action, false_action = read_input.strip().split("\n")
        items = (int(item) for item in items.split(": ")[1].split(", "))
        operation = cls.parse_operation(operation)
        test = int(cls.test_pattern.search(test.split(": ")[1]).group(1))
        true_action = int(cls.action_pattern.search(
            true_action.split(": ")[1]).group(1))
        false_action = int(cls.action_pattern.search(
            false_action.split(": ")[1]).group(1))

        return cls(items, operation, test, true_action, false_action, game)

    @classmethod
    def parse_operation(cls, operation):
        re_match = cls.operation_pattern.search(operation.split(": ")[1])
        op = re_match.group(1)
        operand = re_match.group(2)
        
        match op:
            case "*":
                f = mul
            case "+":
                f = add
        if operand == "old":
            return lambda x: f(x, x)
        else:
            return lambda x: f(x, int(operand))



if __name__ == '__main__':
    PATH = 'day11/data.txt'
    # PATH = 'day11/test.txt'
    monkey_business = MonkeyBusiness(PATH)

    for _ in range(20):
        for monkey in monkey_business:
            monkey.play()

    print(monkey_business.level)
    
