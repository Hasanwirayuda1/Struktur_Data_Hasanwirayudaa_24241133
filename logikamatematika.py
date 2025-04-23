#operasi logika boolean

#NOT,OR,AND,XOR

print('------NOT------')
x = False
y = not x
print('data x =',x)
print('-----------NOT')
print('data y =',y)

#(jika ada salah, maka hasilnya salah)
print("======== AND ========")
x = False
y = False
nilai = x and y
print(x, "and", y, "=", nilai)

x = False
y = True
nilai = x and y
print(x, "and", y, "=", nilai)

x = True
y = False
nilai = x and y
print(x, "and", y, "=", nilai)

x = True
y = True
nilai = x and y
print(x, "and", y, "=", nilai)

#(jika salah satu true, maka hasilnya true)
print("======== OR ========")
x = False
y = False
nilai = x or y
print(x, "or", y, "=", nilai)

x = False
y = True
nilai = x or y
print(x, "or", y, "=", nilai)

x = True
y = False
nilai = x or y
print(x, "or", y, "=", nilai)

x = True
y = True
nilai = x or y
print(x, "or", y, "=", nilai)

#(jika ada salah, maka hasilnya salah)
print("======== XOR ========")
x = False
y = False
nilai = x ^ y
print(x, "xor", y, "=", nilai)

x = False
y = True
nilai = x ^ y
print(x, "xor", y, "=", nilai)

x = True
y = False
nilai = x ^ y
print(x, "xor", y, "=", nilai)

x = True
y = True
nilai = x ^ y
print(x, "xor", y, "=", nilai)
