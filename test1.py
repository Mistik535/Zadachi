class Test:
    str_ = ""

    def __init__(self, str):
        self.str_ = str

    def __iter__(self):
        return self

    def f(self):
        pass


d = [Test("1"), Test("2"), Test("3")]

its = iter(d)

# it = next(its)
# print(it.str_)
#
# it = next(its)
# # print(it.str_)
# print(type(it.str_))
#
# it = next(its)
# print(it.str_)
#
# str = ""

for it in iter(d):
    # str += it.str_ + ", "
    # print(it.str_)
    it.str_ = "="

for it in d:
    print(it.str_)
