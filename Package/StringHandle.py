class BracketHandle(object):
    def __init__(self, string):
        self.string = string
        self.brackets = ('(', ')')
        self.place_holder = '#'

    def get_inner_brackets_pos(self):
        bracket_pos = [0, 0]
        for pos in range(len(self.string)):
            if self.string[pos] == self.brackets[0]:
                bracket_pos[0] = pos
            if self.string[pos] == self.brackets[1]:
                bracket_pos[1] = pos + 1
                return bracket_pos
        return False

    def return_inner_bracket(self):
        if self.get_inner_brackets_pos():
            sub_string = self.string[self.get_inner_brackets_pos()[0]: self.get_inner_brackets_pos()[1]]
            self.string = self.string.replace(sub_string, self.place_holder)
            #print(sub_string)
            return sub_string.replace(self.brackets[0], '').replace(self.brackets[1], '')
        else:
            return False

    def put_content(self, string):
        self.string = self.string.replace(self.place_holder, string)


if __name__ == '__main__':
    bh = BracketHandle('1(2(33)2)11')
    bracket = True
    while bracket:
        bracket = bh.return_inner_bracket()
        print(bracket)
        if bracket:
            t_int = 0
            for i in bracket:
                t_int += int(i)
            bh.put_content(str(t_int))
    print(bh.string)
