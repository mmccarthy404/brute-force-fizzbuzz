with open('brute_force_fizzbuzz.py', 'w') as f:
    print('import argparse', file=f)
    print('', file=f)

    print('parser = argparse.ArgumentParser(description="Brute-force Fizzbuzz")', file=f)
    print('parser.add_argument("--int", type=int, required=True, help="Integer to run through brute-force Fizzbuzz", dest="int")', file=f)
    print('args = parser.parse_args()', file=f)
    print('', file=f)

    for i in range(9000):
        print(f'if args.int == {i}:', file=f)
        output = ''
        if i % 3 == 0:
            output += 'Fizz'
        if i % 5 == 0:
            output += 'Buzz'
        if i % 3 != 0 and i % 5 != 0:
            output += str(i)
        print(f'\tprint("{output}")', file=f)
    print('', file=f)

    print('#TODO: Over 9000', file=f)