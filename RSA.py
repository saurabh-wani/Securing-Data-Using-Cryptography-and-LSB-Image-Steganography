import random
import math


class RSA:

    def pw(self, base, ex, mod):
        i = 1
        while ex > 0:
            if ex & 1 == 1:
                i = (i * base) % mod
            base = (base * base) % mod
            ex >>= 1
        return i

    def isprime(self, n):
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

    def decryption(self, ciphertext):
        import json
        with open('private_key.json', 'r') as prkfile:
            pk = json.load(prkfile)

            pr = pk[str(self.userid)]

        return self.pw(ciphertext, pr[0], pr[1])

    def encryption(self, ud,data = None ):
        if data != None:
            self.data = data
        import os
        import json
        if os.path.isfile("rsa.json"):
            with open('rsa.json', ) as f:
                keys = json.load(f)

                ud = str(ud)
                if ud in keys:

                    public_key_of_recipient = keys[str(ud)]
                else:
                    raise Exception("Recipient Does Not Exist")
        else:
            raise Exception("Public key Does Not Exist")

        return self.pw(data, public_key_of_recipient[0], public_key_of_recipient[1])

    def calculate_d(self, phi, e):

        a = phi
        b = e
        t1 = 0
        t2 = 1
        r = phi % e
        while r != 0:
            q = int(phi / e)
            r = phi % e
            t = t1 - (t2 * q)
            if (r == 0):
                break
            phi = e
            e = r
            t1 = t2
            t2 = t
        if (t2 < 0):
            return abs(a + t2)
        return t2

    def calculate_e(self, phi):

        while 1:
            potential_e = random.randrange(1, phi)
            if math.gcd(potential_e, phi) == 1:
                return potential_e

    def eulersTotient(self, p, q):
        if p == q:
            raise Exception("Both Numebers Are same")
        return (p - 1) * (q - 1)

    def nBitRandom(self, n):
        return random.randrange(2 ** (n - 1) + 1, 2 ** n - 1)

    def getLowLevelPrime(self, n):
        while True:
            pc = self.nBitRandom(n)
            for divisor in self.first_primes_list:
                if pc % divisor == 0 and divisor ** 2 <= pc:
                    break
                else:
                    return pc

    def isMillerRabinPassed(self, mrc):
        maxDivisionsByTwo = 0
        ec = mrc - 1
        while ec % 2 == 0:
            ec >>= 1
            maxDivisionsByTwo += 1
        assert (2 ** maxDivisionsByTwo * ec == mrc - 1)

        def trialComposite(round_tester):
            if pow(round_tester, ec, mrc) == 1:
                return False
            for i in range(maxDivisionsByTwo):
                if pow(round_tester, 2 ** i * ec, mrc) == mrc - 1:
                    return False
            return True

        numberOfRabinTrials = 20
        for i in range(numberOfRabinTrials):
            round_tester = random.randrange(2, mrc)
            if trialComposite(round_tester):
                return False
        return True

    def generate_prime_number(self, n):
        RSA.first_primes_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29,
                                 31, 37, 41, 43, 47, 53, 59, 61, 67,
                                 71, 73, 79, 83, 89, 97, 101, 103,
                                 107, 109, 113, 127, 131, 137, 139,
                                 149, 151, 157, 163, 167, 173, 179,
                                 181, 191, 193, 197, 199, 211, 223,
                                 227, 229, 233, 239, 241, 251, 257,
                                 263, 269, 271, 277, 281, 283, 293,
                                 307, 311, 313, 317, 331, 337, 347, 349]

        while True:
            prime_candidate = self.getLowLevelPrime(n)
            if not self.isMillerRabinPassed(prime_candidate):
                continue
            else:
                return prime_candidate

    def key_generator(self):
        import json
        p = self.generate_prime_number(self.no_of_bits)
        q = self.generate_prime_number(self.no_of_bits)

        n = p * q

        phi = self.eulersTotient(p, q)

        e = self.calculate_e(phi)

        d = self.calculate_d(phi, e)
        d = int(d)

        public_key = {"1": [e, n]}

        private_key = {"1": [d, n]}

        pbk = json.dumps(public_key)
        prk = json.dumps(private_key)
        with open("rsa.json", "w") as rsafile:
            rsafile.write(pbk)
        with open("private_key.json", "w") as prfile:
            prfile.write(prk)

    def rsa_text_encryption(self,path, filename, dest):
        lines = list()
        with open(path + '\\' + filename) as f:
            lines = f.readlines()
            f.close()
        en = []
        for i in lines:
            for char in i:
                self.data = ord(char)
                en.append(self.encryption(1))
        with open("file.txt", "w") as output:
            output.write(str(en))

    def rsa_text_decryption(self, path, filename, dest):
        de = list()
        with open(path + '\\' + filename) as f:
            de = f.readlines()
            f.close()
        # print(de)
        de = de[0]
        de = str(de)
        # print(de[0])
        de = de[1:-1]
        de = de.split(",")

        # print(de)
        s = ""
        for i in de:
            s = s + chr(self.decryption(int(i)))
        return s

    def __init__(self, data, userid, no_of_bits=random.randint(1024, 2024)):
        import os
        self.data = data
        self.userid = userid
        self.no_of_bits = no_of_bits

        if not os.path.isfile("rsa.json"):
            self.key_generator()


