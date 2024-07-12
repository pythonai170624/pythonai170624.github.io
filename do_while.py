
# input 3 numbers in a loop a, b, c
# until a * 2 + b > c-1
# code
# while
#   code
a: int
b: int
c: int = 0

while True:
    a = float(input('enter a:'))
    b = float(input('enter b:'))
    c = float(input('enter c:'))
    print(f"a: {a} b: {b} c: {c}")
    if a * 2 + b <= c-1:
        break

print('finish')

price: int = 0;
total: int = 0;
number_of_products: int = 0;

while True:
    price = float(input('enter product price:'));
    total = total + price;
    number_of_products = number_of_products + 1;
    if total > 1000:
        break

diff: float = total - 1_000;
avg: float = total / number_of_products;
print(f"you bought {number_of_products} products.");
print(f"the avg is: {avg}.");
print(f"you exceed the 1,000 by {diff}");


