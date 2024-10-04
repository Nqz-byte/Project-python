# sintaks stack jika menggunakan def
# Inisialisasi stack sebagai list kosong
stack = []

# Fungsi push (menambahkan elemen)
def push(item):
    stack.append(item)

# Fungsi pop (menghapus dan mengembalikan elemen teratas)
def pop():
    if not stack:
        return "Stack is empty"
    return stack.pop()

# Fungsi peek (melihat elemen teratas)
def peek():
    if not stack:
        return "Stack is empty"
    return stack[-1]

# Contoh penggunaan
push(1)
push(2)
push(3)

print(peek())   # Output: 3
print(pop())    # Output: 3
print(stack)    # Output: [1, 2]


#sintaks sederhana
# penggunaan penambahan (push)
list = ["otong", "yanto", "adam", "2", "yus"]

list.append("15")
list.append("20")
print(f"\nmenambahkan stuck : \n{list}")

# penggunaan pop (menghapus elemen teratas)
list.pop()
print(f"\nmenghapus elemen teratas yaitu, \n{list}")

# untuk melihat elemen
list[-1]
print(f"\n elemen peek : {list[-1]}")

print(f"\n2. contoh implementasi menggunakqn daftar")
stack =[]

#append(). fungsi untuk nmenambahkan elemen
#elemen di stack
stack.append("a")
stack.append("b")
stack.append("c")
print("inisial stack")
print(stack)

#pop(). fungsi untuk menghapus elemen
print("\elemen pop dari stack")
print(stack.pop())
print(stack.pop())
print(stack.pop())
print("\elemen sesudah dipqkukan pop")
print(stack)

print(f"\n 3. implementasi menggunakan collection.deque")

from collection import deque

stack = deque()

#append(). fungsi nmenambahkan
stack.append("a")
stack.append("b")
stack.append("c")
print("inisial stack")
print(stack)

#pop(). fungsi untuk menghapus elemen
print("\elemen pop dari stack")
print(stack.pop())
print(stack.pop())
print(stack.pop())
print("\elemen sesudah dilakukan pop")
print(stack)