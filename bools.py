
x: bool = True;
y: bool = False;

balance: int = 100_000;
age: int = 19;

is_balance_sufficient: bool = balance * 1.98 + 2000 > 200_000
is_old_enough: bool = age > 18

if is_balance_sufficient and is_old_enough:
    print('you can join!')

if not is_balance_sufficient:
    print('not enough doe in balance')
