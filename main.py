class LOL:
    def __init__(self, i):
        self.i = i


def t(ob):
    print(ob.i)

if __name__ == '__main__':
    LOL.einemaus = t
    LOL.x = 100
    l = LOL(20)
    l.einemaus()
    print(l.x)