
ARRAY = [9, 3, 1, 1, 3]
ARRAY1 = []

for i in ARRAY:
    if i not in ARRAY1:
        ARRAY1.append(i)

for element in ARRAY1:
    count = 0
    for i in ARRAY:
        if i == element:
            count += 1
    print(f"Element {element} occurs {count} times")
