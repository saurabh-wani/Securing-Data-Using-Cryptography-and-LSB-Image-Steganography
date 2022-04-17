count = 0
data = []
final = []
with open("big_file.txt") as f:
    d = f.readlines()
    f.close()
#d = d[0]
print(d)
for i in d:
    final.append(str(count)+ " " + i)
    count = count+1
print(final)    
with open("big_file_with_numbers.txt", 'w') as f:
    for i in final:
        f.write(i)
    f.close()