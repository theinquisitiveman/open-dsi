for a in range(1, 7):
    for b in range(1, 7):
        for c in range(1, 7):
            for d in range(1, 7):
                for e in range(1, 7):
                    for f in range(1, 7):
                        if (a + (b - c) * d - e) * f == 75 and len({a, b, c, d, e, f}) == 6:
                            print(a, b, c, d, e, f)

for a in range(1, 7):
    for b in range(1, 7):
        for c in range(1, 7):
            for d in range(1, 7):
                for e in range(1, 7):
                    for f in range(1, 7):
                        if ((a + (b - c) * d - e) * f == 75 and
                        a != b and a != c and a != d and
                        a != e and a != f and b != c and
                        b != d and b != e and b != f and
                        c != d and c != e and c != f and
                        d != e and d != f and e != f):
                            print(a, b, c, d, e, f)
