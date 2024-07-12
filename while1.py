# range

#Start
x: int = 1;
while x < 20: # condition is tested before entering 1st cycle
    print(x, end=" ");
    x = x + 1;
    # --
print('finish\nfinish')
#Stop

#while1.diag
# input grades until got -1
#Start
# grade: int = 0;
# while not grade == -1:
#     grade = int(input("Enter grade:"))
# print('finish')
#Stop

#while2.diag
# input grades until got -1
# calculate avg.
#Start
grade: int = 0;
sum: int = 0;
count: int = 0;
grade = int(input("enter grade:"));
while grade >= 0 and grade <= 100:
    sum = sum + grade;
    count = count + 1;
    grade = int(input("enter grade:"));
    # jump to top
avg: float = sum / count
print("the average is:", avg)
print(f"the average is: {avg}")
#Stop

# input product prices from the user, float
# until the total price exceed 1000
# print the avg price of the products
# print how many products you have purchased
# print how much beyond 1000 you reached
# i.e. 1900 then print:
# 'you went 900 beyond 1000'

#while3.diag
price: int = 0;
total: int = 0;
number_of_products: int = 0;

while total <= 1000:
    price = float(input('enter product price:'));
    total = total + price;
    number_of_products = number_of_products + 1;

diff: float = total - 1_000;
avg: float = total / number_of_products;
print(f"you bought {number_of_products} products.");
print(f"the avg is: {avg}.");
print(f"you exceed the 1,000 by {diff}");

# 500
# 700
# 1,200
# 200
#for-each

#while
# input grades from a class until input -1

# while True
# run in loop until condition reached at the end