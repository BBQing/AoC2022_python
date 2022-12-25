def read_file(PATH):
    with open(PATH, "r") as file:
        for line in file.readlines():
            yield Snafu(line.strip())

class Snafu:

    s2d = {
        "2": 2,
        "1": 1,
        "0": 0,
        "-": -1,
        "=": -2
    }

    d2s = {
        0: "0",
        1: "1",
        2: "2",
        3: "1=",
        4: "1-",
        -1: "-",
        -2: "="
    } 

    def __init__(self, digits) -> None:
        self.digits = digits

    def to_decimal(self):
        return sum(self.s2d.get(digit) * (5 ** ind) for ind, digit in enumerate(reversed(self.digits)))

    @classmethod
    def from_decimal(cls, number):
        
        digits = []
        while True:
            digit, number = number % 5 , number // 5
            if digit > 2:
                number += 1
                digit -= 5

            if not number and not digit:
                break
            else:
                digits.append(digit)

        return cls("".join(cls.d2s.get(digit) for digit in reversed(digits)))

    def __repr__(self) -> str:
        return "".join(self.digits)
if __name__ == '__main__':
    PATH = 'day25/data.txt'
    # PATH = 'day25/test.txt'

    snafus = [snafu for snafu in read_file(PATH)]
    print(Snafu.from_decimal(sum(snafu.to_decimal() for snafu in snafus)))

    # print(Snafu.from_decimal(Snafu("2=").to_decimal()))