from Package.Vars import DEBUG


class DebugMessage(object):
    def __init__(self):
        self.debug = DEBUG

    def cout(self, foo, pos, **kwargs):
        string = f'{foo.__name__} # {pos}: ('
        for key, val in kwargs.items():
            string += f'{key}: {val}, '
        string += ')'
        print(string)


debug = DebugMessage()
a, b, c = 1, 2, 3


def t(a, b, c):
    debug.cout(t, 1, a=a, b=b, c=c)


if __name__ == '__main__':
    t(a, b, c)
