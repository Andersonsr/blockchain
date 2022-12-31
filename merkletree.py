from hashlib import sha256


# referencia: https://stackoverflow.com/questions/57025836/how-to-check-if-a-given-number-is-a-power-of-two
def isPow2(n):
    return (n != 0) and (n & (n-1) == 0)


def merkleRecStep(hashes):
    n = int(len(hashes)/2)
    # print(hashes)
    if n > 1:
        newHashes = []
        for i in range(n):
            temp = hashes[i*2]+hashes[i*2+1]
            newHashes.append(sha256(temp.encode()).hexdigest())

        return merkleRecStep(newHashes)

    else:
        temp = hashes[0]+hashes[1]
        # print('raiz merkle: {}'.format(sha256(temp.encode()).hexdigest()))
        return sha256(temp.encode()).hexdigest()


def merkle(transactions):
    if isPow2(len(transactions)):
        n = len(transactions)
        hashes = []
        for i in range(n):
            digest = sha256(transactions[i].toString().encode()).hexdigest()
            hashes.append(digest)

        return merkleRecStep(hashes)
