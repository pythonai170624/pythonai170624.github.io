
# x: int = 1;
# while x < 20: # condition is tested before entering 1st cycle
#     print(x, end=" ");
#     x = x + 1;
#     # --

for i in range(1, 11):
    print(i, end= " ");

total: int = 0
for i in range(1, 11):#[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    price: int = int(input('enter price:'))
    total = total + price
    if total > 1000:
        break

# for-each
for c in "Hello":
    print(c, end = "")
print()
for i in range(1, 20, 2):
    print(i, end= " ");
print()
for i in range(20, 1, -1):
    print(i, end= " ");
print()
for i in range(1, 20, 1):
    print(i, end= " ");

