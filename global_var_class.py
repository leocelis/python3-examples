a = 123


class Test:
    def __init__(self):
        return

    def get_a(self):
        global a
        return a


t = Test()
print(t.get_a())

a = 456
print(t.get_a())
