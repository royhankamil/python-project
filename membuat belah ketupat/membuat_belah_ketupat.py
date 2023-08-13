panjang = int(input('masukkan panjang: '))
spasi = panjang
for i in range(panjang * 2):    
        if i %2 ==1:
            continue
        print(spasi* ' ' +'*' * (i+1 ))
        spasi -=1
a = panjang * 2 - 3    
spasi = 2    
while a > 0 :    
        print(spasi * ' ' +'*' * a)
        spasi +=1
        a-=2        
