from hashlib import sha256


class Miner:

    def check(self, hash, dificuldade):
        for i in range(dificuldade):
            if hash[i] != str(0):
                return False
        return True

    def mine(self, timeStamp, root, quantity, size, difficulty):
        nonce = 0
        input = timeStamp+root+str(quantity)+str(size)

        while True:
            digest = sha256((str(nonce)+input).encode()).hexdigest()
            if self.check(digest, difficulty):
                return nonce, digest
            nonce += 1

