def solve_pythogorean_triplet():
    for a in range(1, 1000//3):
        for b in range(a+1, 1000//2):
            c = 1000 - a - b
            if a**2 + b**2 == c**2:
                return a * b *c
print(solve_pythogorean_triplet())
