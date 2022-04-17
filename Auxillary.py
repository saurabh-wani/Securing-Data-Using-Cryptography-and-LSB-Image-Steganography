import json
import shutil

import numpy as np
from skimage.io import imread, imshow,imsave
import RSA
import  DES
import random
import os
import math
import LSB_Steganography as lsb
import shutil as sht
import Config


def isprime(n):
    if n <= 1:
        return 0
    if n == 2:
        return 1
    if n > 2 and n & 1 == 0:
        return 0
    s = math.floor(math.sqrt(n))

    for i in range(2, s):
        if n % i == 0:
            return 0
    return 1

def splitImage(path, sections=random.randint(3, 6), save=False, dest_path=os.getcwd()):
    image = imread(fname=path)
    lis = np.split(image, sections)

    if (save):
        for i in range(sections):
            imsave(dest_path + "\\part {0}.jpg".format(i), lis[i])

    return lis


def mergeImage(lis, show=False):
    image = np.vstack(lis)
    if (show):
        imshow(image)

    return image

def splitfiles(filename, filepath, destination = os.getcwd()):
    data = []
    with open(filepath + "\\" + filename, 'r') as f:

        data.append(f.readlines())

        f.close()
    n = len(data[0])


    data = data[0]
    last = []
    final = []
    if(n <=3):

        randomno = n
        final = data


    else:
        randomno = random.randint(2,9)
        if isprime(n):

            temp =n-1
            last = data[-1]
            final = data[0:-1]
            while(temp%randomno!=0):

                randomno = random.randint(2,temp)


        else:
            final = data

            while(n%randomno!=0):

                randomno = random.randint(2,9)

    final = np.array(final)
    if(len(last)==0):
        final = np.split(final,randomno)
    else:
        final = np.split(final, randomno)
        final.append(np.array(last))

    counter = 0
    result = []

    for i in final:

        s = ""
        if(i.size>1):
            s = "".join(i)
            s = str(s)
        else:
            s  = str(i)
        result.append(s)
        name = "splitted_part_"+str(counter)+".txt"
        with open(destination+"\\" + name,'w') as f:
            f.write(s)
            f.close()
        counter+=1
    return result

def encrypt(al, data):
    dict = {}
    # print("INsise enc")
    #r = RSA.RSA(0,userid=1,no_of_bits=128)
    # des = DES.DES()
    # k = des.Generate_Key_64()
    # dict[2] = k

    counter = 0

    for d , a in zip(data,al):

        if a == 1:
            r = RSA.RSA(0, userid=1, no_of_bits=128)
            name = "encrypted_part_" + str(counter) + ".txt"
            e = []
            for i in d:
                # print("rsa , \n" ,a)
                e.append(r.encryption(1,ord(i)))
                # print("e , \n", e)
            s = ",".join(str(l) for l in e)
            with open(name,'w') as f:
                f.writelines(s)
                f.close()
            counter+=1

        elif a == 2:
            des = DES.DES()
            k = des.Generate_Key_64()
            dict[counter] = k
            c = des.DES_Encrypt(d,k)

            c = c.encode()

            # print(type(c))
            name = "encrypted_part_" + str(counter) + ".txt"
            with open(name,'wb') as f:
                f.write(c)
                f.close()
            counter+=1
    with open("al.json", 'w') as js:
        json.dump(al,js)


    return  dict


def decrypt():

    k = Getkeys()
    keycount = 0
    # desk = keys.get(2)
    # print("desk",type(desk))
    # print(desk)
    import glob
    ls = glob.glob("encrypted_part_*.txt")
    if len(ls) == 0:
        raise Exception("No Encrypted File Found")
    ls.sort(key=len)
    al = []
    with open('al.json', 'r') as f:
        al = json.load(f)
        f.close()
    count = 0
    for f,a in zip(ls,al):

        if a == 1:
            r = RSA.RSA(0,1,128)
            data = []
            with open(f) as c:
                # print("Reading Lines for file ", count)

                data = c.readlines()
                c.close()
            data =data[0]
            data = data.split(",")
            #print(data)
            s = ""
            for i in data:
                s =s + chr(r.decryption(int(i)))

            name = "decrypted_part" + str(count)  + ".txt"
            with open(name, 'w') as v:
                v.write(s)
                v.close()

        elif a== 2:
            d = ""
            #desk =  keys[count]
            desk = k[keycount: keycount+8 ]
            # print(desk)
            with open(f,'rb') as c:
                data = c.read()
                data = data.decode()
                des = DES.DES()
                d = str(des.DES_Decrypt(data,desk))
                c.close()
            d = str(d)
            name = "decrypted_part" + str(count)  + ".txt"
            with open(name, "w") as x:

                x.write(d)
                x.close()
            keycount += 8







        count += 1


    mergeFiles()











def generate_al(n):
    al = []
    for i in range(0, n):
        al.append(random.randint(1, 2))

    return  al


def Getkeys():
    k = ""
    with open("meta.txt", 'r') as f:
        m = f.readlines()
        f.close()
    rsa = RSA.RSA(0,1,128)
    l = []
    m = m[0]
    m = m.split()

    for i in m:
        l.append(rsa.decryption(int(i)))
    k = lsb.decode("stegoimg.png" , l[0],l[1],l[2])
    return k


def mergeFiles():
    import glob
    ls = glob.glob("decrypted_part*.txt")
    ls.sort(key=len)
    with open("message.txt", 'wb') as actmsg:
        for i in ls:
            with open(i ,'rb') as f:
                shutil.copyfileobj(f,actmsg)








