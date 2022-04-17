import random
import Auxillary as a
import DES
import RSA
import  RSA as rsa
import codecs
import binascii
import DES as d
import LSB_Steganography as lsb
# choice = int(input("1. Encryption \n2. Decryption"))
# dict = {}
# if choice == 1:
#     sd = a.splitfiles(filename= "d.txt", filepath= "F:\\Major Project\\Multiple-Encryption-Algorithms-And-LSB-Steganography\\Algorithms")
#     al = a.generate_al(len(sd))
#     print(sd)
#     print(al)
#     print("calling encr")
#     dict = a.encrypt(al, sd)
#     print("end encr")
# print(dict)
# # #------------------------------------decrypting with file start---------------------------
# r = RSA.RSA(0,1,128)
# with open("encrypted_part_.txt" , 'r') as f:
#     d = f.readlines()
#     d =d[0]
#     d = d.split(",")
#     s = ""
#     for i in d:
#         s =s + chr(r.decryption(int(i)))
#     print(s)
#------------------------------------decrypting with file end---------------------------


#r = DES.DES()
# with open("encrypted_part_.txt" , 'rb') as f:
#     d = f.read()
#     print(d)
#     d = d.decode()
#     print(d)
#
#
#     s = r.DES_Decrypt(d,"kJA(p'oe")
#     print(s)
#     print(type(s))
#
#     with open("dec.txt",'w') as k:
#         k.write(s)
#
#     with open("dec.txt", 'r') as t:
#         print(t.read())





#print(a.decrypt('xd@PFt[)'))

choice = 0
#a.decrypt("aYT,p0'j")
d = dict()
while choice < 3:
    choice = int(input("1. Encryption \n2. Decryption\n3. Exit"))

    if choice == 1:
        sd = a.splitfiles(filename= "big_file.txt", filepath= "C:\\Users\\saura\\Major Project Code\\Final Code\\Major Project Final")
        al = a.generate_al(len(sd))

        d = a.encrypt(al, sd)
        k = ""
        for i in d.keys():
            k = k+ d[i]
        s,e,r = lsb.encode("COVER_2.png", k)

        rsa = RSA.RSA(0,1,128)
        s = rsa.encryption(1,s)
        e = rsa.encryption(1, e)
        r = rsa.encryption(1, r)
        with open('meta.txt','w') as f:
            f.write(str(s) + " " + str(e)+ " " +str(r))

















    elif choice == 2:


        a.decrypt()


# for d,a in zip(sd,al):
#     if a == 1:
#         decrypt_des()
#     else if a== 2:






#-----------------------------------DES - Start -------------------------------------------------------------------
# d = d.DES()
# k = d.Generate_Key_64()
# e = []
# for i in sd:
#     e.append(d.DES_Encrypt(i,k))
# print(e)
# de = []
# for i in e:
#     de.append(d.DES_Decrypt(i,k))
# print(de)
# print(sd)
#-----------------------------------DES - end -------------------------------------------------------------------

#------------------------------------RSA optimization start---------------------------------------------------------
# r = rsa.RSA(0,1,2048)
# el = []
# pro = []
# for i in sd:
#     pro.append(i.split(" ", 100))
# print("len pro",len(pro[0]))
# print("len sd",len(sd))
# print(" pro",pro[0])
# print(" sd",sd)
# elt = []
# lent = []
# for i in pro:
#     for j in i:
#         s = j.encode('utf-8')
#         lb = len(s)
#         s = int.from_bytes(s,'big')
#         elt.append([r.encryption(1,s),lb])
#         #lent.append(lb)
# print(elt)
# s = ""
# for i in elt:
#     print("elt de: " ,i[0])
#     print("elt len: ", i[1])
#     dect = r.decryption(i[0])
#     k = dect.to_bytes(100,'big')
#     print("after dec:",k)
#     print("before replace")
#     #k = k.replace("\x00","")
#     print("before replace")
#     print("k : \n",k)
#     k = k.decode()
#     #v = codecs.decode(k)
#     s = s+ k
#     print(s)
# print(s)
#------------------------------------RSA optimization end-----------------------------------------------------------------------
#------------------------------------RSA Working start----------------------------------------------------------------------------
# print("pro \n",pro)
# print("sd \n",sd[0])
# for j in sd:
#
#     print(j)
#     print(type(j))
#     by = j.encode()
#     by = int.from_bytes(by,'big')
#     el.append(r.encryption(1,by))
#
# print(el)
# s = ""
# for i in el:
#     s = s + chr((r.decryption(i)))
# print(s)

#------------------------------------RSA Working end-----------------------