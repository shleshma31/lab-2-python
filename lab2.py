#LAB-2
#QN:1  ( without using built-in functions)
#a). 
n = int(input())
a = []
for i in range(n):
    x = int(input())
    a.append(x)
maxi = a[0]
mini = a[0]
for i in range(1, n):
    if a[i] > maxi:
        maxi = a[i]
    if a[i] < mini:
        mini = a[i]
print("Maximum:", maxi)
print("Minimum:", mini)

#b).
a = [9, 3, 7, 2, 6, 1]
n = 0
while True:
    try:
        a[n]
        n += 1
    except:
        break
i = 0
while i < n:
    j = i + 1
    while j < n:
        if a[i] > a[j]:
            temp = a[i]
            a[i] = a[j]
            a[j] = temp
        j += 1
    i += 1
print(a)

#c). 
a = [2, 4, 2, 5, 6, 4, 6, 7]
unique = []
i = 0
while i < len(a):
    j = 0
    found = False
    while j < len(unique):
        if a[i] == unique[j]:
            found = True
            break
        j += 1
    if not found:
        unique += [a[i]]
    i += 1
print(unique)

#using built-in functions)

#a). 
n = int(input())
a = [int(input()) for _ in range(n)]

print("Maximum:", max(a))
print("Minimum:", min(a))

#b). 
a = [9, 3, 7, 2, 6, 1]
a.sort()
print(a)

#c). 
a = [2, 4, 2, 5, 6, 4, 6, 7]
a = list(set(a))
print(a)


#QN:2
a = [1, 2, 3, 4, 5]
b = [4, 5, 6, 7, 8]
merged = []
i = 0
while i < len(a):
    merged += [a[i]]
    i += 1
i = 0
while i < len(b):
    merged += [b[i]]
    i += 1
result = []
i = 0
while i < len(merged):
    count = 0
    j = 0
    while j < len(merged):
        if merged[i] == merged[j]:
            count += 1
        j += 1
    if count == 1:
        result += [merged[i]]
    i += 1
print(result)


#QN:3
sentence = "My name is Shleshma Dahal."

words = sentence.split(" ")
uniq_words = set(words)
print(uniq_words)
d = {}

for word in uniq_words:
    d[word] = words.count(word)

print(d)


#QN:4
stack = []
queue = []

while True:
    print("1. Push to Stack")
    print("2. Pop from Stack")
    print("3. Enqueue to Queue")
    print("4. Dequeue from Queue")
    print("5. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        val = input("Enter value to push: ")
        stack.append(val)
        print("Stack:", stack)
    elif choice == "2":
        if stack:
            val = stack.pop()
            print("Popped:", val)
        else:
            print("Stack is empty")
        print("Stack:", stack)
    elif choice == "3":
        val = input("Enter value to enqueue: ")
        queue.append(val)
        print("Queue:", queue)
    elif choice == "4":
        if queue:
            val = queue.pop(0)
            print("Dequeued:", val)
        else:
            print("Queue is empty")
        print("Queue:", queue)
    elif choice == "5":
        break
    else:
        print("Invalid choice")



#QN:5
l = [2,3,4,5,6,7,8,9]
even_indices = range(0,len(l),2)
print(even_indices)

for index in even_indices:
    count = 0
    for i in range(1,l[index]+1):
        if (l[index]%i==0):
            count +=1
    if count==2:
        print(f"{l[index]} is prime")



#QN:6
l = (2, 3, 4, 5, 6, 7, 8, 9, 9 , 10, 10, 10, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)
# Finding average
average = sum(l)/len(l)
print(f"Average: {average:.2f}")

# Finding median:
sorted_list = sorted(l)
n = len(sorted_list)

if n % 2 == 0:
    median = (sorted_list[n//2 - 1] + sorted_list[n//2]) / 2
else:
    median = sorted_list[n//2]
print(f"Median: {median}")

# Finding mode:
mode_count = {}
for number in l:
    if number in mode_count:
        mode_count[number] += 1
    else:
        mode_count[number] = 1

print(mode_count)

max_count = 0
for num, count in mode_count.items():
    if count > max_count:
        max_count = count
        mode = num
print(f"Mode: {mode}")



#QN:7

points = []
n = int(input())
for _ in range(n):
    x, y = map(int, input().split())
    points.append((x, y))

x0, y0 = points[0]
x1, y1 = points[1]
is_line = True
for i in range(2, n):
    x, y = points[i]
    if (y1 - y0) * (x - x0) != (y - y0) * (x1 - x0):
        is_line = False
        break
print(is_line)


#QN:8
all_students = set(input().split())
cricket = set(input().split())
football = set(input().split())

print(cricket & football)
print((cricket | football) - (cricket & football))
print(all_students - (cricket | football))


#QN:9
import random
s = set()
while len(s) < 10:
    s.add(random.randint(1, 100))
s.remove(min(s))
s.remove(max(s))
print(s)


#QN:10
def get_vowels(sentence):
    vowels = "aeiouAEIOU"
    result = set()
    for ch in sentence:
        if ch in vowels:
            result.add(ch.lower())
    return result

sentence = input()
print(get_vowels(sentence))



#QN:11
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3]
l = list(set(l))
l.sort()
print("Sorted list without duplicates:", l)




#QN:12
d = {}
for _ in range(int(input())):
    name = input()
    marks = list(map(int, input().split()))
    d[name] = marks

for name in d:
    avg = sum(d[name]) / len(d[name])
    print(name, avg)

topper = ""
high = 0
for name in d:
    avg = sum(d[name]) / 3
    if avg > high:
        high = avg
        topper = name
print(topper)

name = input()
if name in d:
    d[name] = list(map(int, input().split()))
print(d)



#QN:13
text = input()
d = {}
for c in text:
    if c.isalnum():
        if c in d:
            d[c] += 1
        else:
            d[c] = 1
print(d)


#QN:14
products = {"apple": 100, "banana": 40, "milk": 80}

while True:
    print("1. Add new product")
    print("2. Update product price")
    print("3. View products")
    print("4. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter product name: ")
        if name in products:
            print("Product already exists")
        else:
            price = float(input("Enter price: "))
            products[name] = price
            print("Product added")
    elif choice == "2":
        name = input("Enter product name to update: ")
        if name in products:
            price = float(input("Enter new price: "))
            products[name] = price
            print("Price updated")
        else:
            print("Product not found")
    elif choice == "3":
        print(products)
    elif choice == "4":
        break
    else:
        print("Invalid choice")