blocks = int(input("Enter the number of blocks: "))
comparation = 0
indeks = 0

#
# Write your code here.
#	
while True:
    indeks +=1
    comparation += indeks

    if comparation == blocks:
        height = indeks
        break
    elif comparation > blocks:
        height = indeks - 1
        break

    
    

print("The height of the pyramid:", height)
