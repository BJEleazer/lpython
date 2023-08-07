i = 0
numbers = []
bound = int(input("Loop how many times? "))
inc = int(input("Increment by how much? "))
overshoot = False

while i < bound:
    print(f"At the top i is {i}")
    numbers.append(i)

    i = i + inc
    print("Numbers now:", numbers)
    print(f"At the bottom i is {i}")
    if i >= bound:
        overshoot = True


print("The numbers: ")

for num in numbers:
    print(num)

print(f"Looped {len(numbers)} times.")

if overshoot == True:
    print("i exceeded the bound, therefore the loop cut short.")

