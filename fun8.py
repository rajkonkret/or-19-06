def allparams(a, b, /, c=42, *args, d=256, **kwargs):
    print("a, b", a, b)
    print("c, d", c, d)
    print("args", args)
    print("kwargs", kwargs)


allparams(1, 2)  # 1 2
# allparams(c=1, a=1, b=6)  # TypeError: allparams() missing 2 required positional arguments: 'a' and 'b'
allparams(1, 2, c=9)
# / - odgradza parametry pozycyjne od parametrow, ktore moga zostac podane po nazwie
allparams(1, 2, 9, 1, 2, 3, 4)  # args (1, 2, 3, 4), c, d 9 256, c musi byc podane na pozycji
allparams(1, 2, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9, d=128)
allparams(1, 2, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9, e=128)  # kwargs {'e': 128}
allparams(1, 2, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9, a=123, e=128)  # kwargs {'a': 123, 'e': 128}
