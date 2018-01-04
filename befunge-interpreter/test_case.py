from collections import namedtuple

TestCase = namedtuple('TestCase', ('name', 'code', 'result'))

test_cases = [

    TestCase('Example from description',
             '>987v>.v\n'
             'v456<  :\n'
             '>321 ^ _@',
             '123456789'),

    TestCase('Hello World!',
             '>25*"!dlroW olleH":v\n'
             '                v:,_@\n'
             '                >  ^',
             'Hello World!\n'),

    TestCase('Factorial (8! = 40320)',
             '08>:1-:v v *_$.@ \n'
             '  ^    _$>\\:^',
             '40320'),

    TestCase('Quine',
             '01->1# +# :# 0# g# ,# :# 5# 8# *# 4# +# -# _@',
             '01->1# +# :# 0# g# ,# :# 5# 8# *# 4# +# -# _@'),

    TestCase('Sieve of Eratosthenes',
             '2>:3g" "-!v\\  g30          <\n'
             ' |!`"&":+1_:.:03p>03g+:"&"`|\n'
             ' @               ^  p3\\" ":<\n'
             '2 2345678901234567890123456789012345678',
             '23571113171923293137')

]

test.describe("Testing Befunge interpreter")

test.it('Testing various code snippets')

for test_case in test_cases:
    test.it(test_case.name)
    test.assert_equals(interpret(test_case.code),
                       test_case.result,
                       'Code: <pre>' + test_case.code + '</pre>')

test.it('Testing random direction')

ones, twos, total, code = 0, 0, 2000, 'v@.<\n >1^\n>?<^\n >2^'

for _ in range(total):
    v = interpret(code)
    if v == '1':
        ones += 1
    elif v == '2':
        twos += 2
    else:
        test.expect(False, 'Code: <pre>' + code + '</pre>')

test.expect(abs(ones / float(total) - 0.5) < 0.05,
            'Code: <pre>' + code + '</pre> Did not come up with 1s between 45% and 55% of the time')
