# devika_arrays.py - Munnabhai teaches Devika array operations

# Static array (fixed size 5)
family = [None] * 5
size = 0  # Current number of elements

# Insert function
def insert(value, pos):
    global size
    if size >= len(family):
        print("Array full, bhai! No space!")
        return
    if pos < 0 or pos > size:
        print("Wrong position, Devika!")
        return
    for i in range(size, pos, -1):
        family[i] = family[i - 1]  # Shift right
    family[pos] = value
    size += 1
    print("Inserted:", family)

# Delete function
def delete(pos):
    global size
    if size == 0:
        print("Array empty, kya delete karu?")
        return
    if pos < 0 or pos >= size:
        print("Wrong position, bhai!")
        return
    for i in range(pos, size - 1):
        family[i] = family[i + 1]  # Shift left
    family[size - 1] = None
    size -= 1
    print("Deleted:", family)

# Traverse function
def traverse():
    if size == 0:
        print("Array khali hai, Devika!")
        return
    print("Family list:", end=" ")
    for i in range(size):
        print(family[i], end=" ")
    print()

# Test it
insert("Aarush", 0)    # [Aarush, None, None, None, None]
insert("Devika", 1)    # [Aarush, Devika, None, None, None]
insert("Bob", 1)       # [Aarush, Bob, Devika, None, None]
traverse()             # Aarush Bob Devika
delete(1)              # [Aarush, Devika, None, None, None]
traverse()             # Aarush Devika