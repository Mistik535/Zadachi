def foo(*args):
    print(args)

    for a in args:
        print(a)


def bar(**kwargs):
    print(kwargs)

    for a in kwargs:
        print(a, kwargs[a])


l_list = {"0": {"1": "2"}, "3": {"4": "5"}}

for root in l_list:
    print(root)
    for child in l_list[root]:
        print(child, l_list[root][child], "\n")

print(l_list["0"]["1"])
# foo(1, 2, 3)

# bar(name='one', age=27)

# print("Hello", "World", "!!!", "123123")

def test(s: str, n: int):
    pass

test("a", 123)