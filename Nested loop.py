for i in range(1,5):
    for j in range(1,3):
        print(i,j)



##shirt-pant combinatio
upper = ["Shirt","Panjabi","Fatua"]
lower = ["Jeans", "Baggy", "Shorts"]

for i in upper:
    for j in lower:
        print(i,j) #(Shirt-Jeans, Shirt-Baggy,....)

print("Donee")


## another combo(Jeans-Shirt,Jeans-Panjabi,Jeans-Fatua, Baggy-Shirt,..)
for i in lower:
    for j in upper:
        print(i,j)

## another combination(Jeans-Shirt, Baggy-shirt, Shorts-shirt, Jeans-panjabi,...)
print("Donee1")
for i in upper:
    for j in lower:
        print(j,i)