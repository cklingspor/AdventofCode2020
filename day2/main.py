class Policy:

    def __init__(self, raw: str, char: str):
        self.max = int(raw.split('-')[1])
        self.min = int(raw.split('-')[0])
        self.positions = [self.min, self.max]
        self.char = char.replace(':', '')

    def get_min_occure(self):
        return self.min

    def get_max_occure(self):
        return self.max

    def get_char(self):
        return self.char

    def get_positions(self):
        return self.positions


class Password:

    def __init__(self, pwd):
        self.pwd = pwd.strip()

    def validate_occurance(self, policy):
        occurrance = self.pwd.count(policy.get_char())
        return True if policy.get_min_occure() <= occurrance <= \
                policy.get_max_occure() else False

    def validate_indices(self, policy):
        if (policy.get_char() == self.pwd[policy.get_positions()[0]-1]) ^ \
                (policy.get_char() == self.pwd[policy.get_positions()[1]-1]):
            return True

        return False


def read_file(unc_path: str):
    lines = []
    doc = open(unc_path)
    for line in doc:
        lines.append(line)

    doc.close()
    return lines


def part_1(candidates: list):
    print(num_of_valid_pw(candidates=candidates, criteria='part1'))


def num_of_valid_pw(candidates: list, criteria: str):
    valid_passwords: int = 0
    input_splited = split_input(input=candidates, delimiter=' ')

    for elem in input_splited:
        policy = Policy(raw=elem[0], char=elem[1])
        pwd = Password(pwd=elem[2])
        if criteria == 'part1':
            valid_passwords += 1 if pwd.validate_occurance(policy=policy) else 0
        elif criteria == 'part2':
            valid_passwords += 1 if pwd.validate_indices(policy=policy) else 0
        else:
            return 'No valid criteria used!'

    return valid_passwords


def split_input(input: list, delimiter: str):
    input_splitted = []
    for line in input:
        input_splitted.append(line.split(delimiter))

    return input_splitted


def part_2(candidates):
    print(num_of_valid_pw(candidates=candidates, criteria='part2'))


if __name__ == '__main__':

    candidates = read_file(unc_path='./input.txt')
    part_1(candidates=candidates)
    part_2(candidates=candidates)

