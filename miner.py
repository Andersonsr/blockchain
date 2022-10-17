from hashlib import sha256


class Miner:

    def check(self, hash, dificuldade):
        for i in range(dificuldade):
            if hash[i] != str(0):
                return False
        return True

    def mine(self, transactions, dificulade):
        nonce = 0
        input = ''
        for t in transactions:
            input += t.toString()

        while True:
            digest = sha256((input+str(nonce)).encode()).hexdigest()
            if self.check(digest, dificulade):
                return nonce, digest
            nonce += 1

