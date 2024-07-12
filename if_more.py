
# question ? Yes = everything , No = 0, None
number: int = 1# int(input("Please enter a number: "));
if number != 0:#beginer
    print("Number different than 0")

if number:#pro
    print("Number different than 0")


if 0:
    print("never happens")
if 1:
    print("always happens")

if not number % 7:
    print('number divided by 7 no sheerit')

if "":
    print('never happens')
if "a":
    print('always happens')
if 1:
    print("always happens")

num: int = int(input("Please enter a number: "));
# if num % 7 == 0:
#     print("    seven boom");
# else:
#     print("not seven boom");

# if not num % 7 == 0:
#     print("NOT", end=" ")
# print("seven boom");

# if not num % 7 == 0:
#     print("NOT", end=" ")

print(("NOT " if not num % 7 == 0 else "") + "seven boom");
print(f"{'NOT ' if not num % 7 == 0 else ''}seven boom");
print(f"{'NOT ' if num % 7 else ''}seven boom");
print(f"{2+2}")

y: int = 1
if y > 3:
    x = 2
else:
    x = 5
x: int = 2 if y > 3 else 5

# 7 % 7 = if 0


# Exercise 5
# num: int = int(input("Please enter a number: "));
# if num % 5 == 0 and num % 3 == 0:
#     print("Fizz Buzz");
# elif num % 3 == 0:
#     print("Buzz");
# elif num % 5 == 0:
#     print("Fizz");
# else:
#     print("not divisible by 3 or 5 or both");

if num % 5:
    print("Fizz", end=" ")
if num % 3 == 0:
    print("Buzz")


