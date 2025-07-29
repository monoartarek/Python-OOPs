class AddNumbers:
    def add(self, *args):
        return sum(args)

calc = AddNumbers()

print(calc.add(2, 3))         # Output: 5
print(calc.add(1, 2, 3,9,6,7,8,9,1))      # Output: 46
print(calc.add(5))            # Output: 5
print(calc.add())             # Output: 0
