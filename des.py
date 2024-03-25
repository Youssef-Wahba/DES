initial_perm = [58, 50, 42, 34, 26, 18, 10, 2,
                60, 52, 44, 36, 28, 20, 12, 4,
                62, 54, 46, 38, 30, 22, 14, 6,
                64, 56, 48, 40, 32, 24, 16, 8,
                57, 49, 41, 33, 25, 17, 9, 1,
                59, 51, 43, 35, 27, 19, 11, 3,
                61, 53, 45, 37, 29, 21, 13, 5,
                63, 55, 47, 39, 31, 23, 15, 7]

PC_1 = [1, 2, 3, 4, 5, 6, 7,
        9, 10, 11, 12, 13, 14, 15,
        17, 18, 19, 20, 21, 22, 23,
        25, 26, 27, 28, 29, 30, 31,
        33, 34, 35, 36, 37, 38, 39,
        41, 42, 43, 44, 45, 46, 47,
        49, 50, 51, 52, 53, 54, 55,
        57, 58, 59, 60, 61, 62, 63]

# Expansion Right PlainText Table
exp_r = [32, 1, 2, 3, 4, 5, 4, 5,
         6, 7, 8, 9, 8, 9, 10, 11,
         12, 13, 12, 13, 14, 15, 16, 17,
         16, 17, 18, 19, 20, 21, 20, 21,
         22, 23, 24, 25, 24, 25, 26, 27,
         28, 29, 28, 29, 30, 31, 32, 1]

# Permutation After S-Boxes
per = [16, 7, 20, 21,
       29, 12, 28, 17,
       1, 15, 23, 26,
       5, 18, 31, 10,
       2, 8, 24, 14,
       32, 27, 3, 9,
       19, 13, 30, 6,
       22, 11, 4, 25]

# S-box Table
sbox = [[[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
         [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
         [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
         [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]],

        [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
         [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
         [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
         [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]],

        [[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
         [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
         [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
         [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]],

        [[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
         [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
         [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
         [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]],

        [[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
         [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
         [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
         [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]],

        [[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
         [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
         [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
         [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]],

        [[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
         [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
         [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
         [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]],

        [[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
         [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
         [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
         [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]]]

# Final Permutation Table
final_perm = [40, 8, 48, 16, 56, 24, 64, 32,
              39, 7, 47, 15, 55, 23, 63, 31,
              38, 6, 46, 14, 54, 22, 62, 30,
              37, 5, 45, 13, 53, 21, 61, 29,
              36, 4, 44, 12, 52, 20, 60, 28,
              35, 3, 43, 11, 51, 19, 59, 27,
              34, 2, 42, 10, 50, 18, 58, 26,
              33, 1, 41, 9, 49, 17, 57, 25]

PC_2 = [14, 17, 11, 24, 1, 5,
        3, 28, 15, 6, 21, 10,
        23, 19, 12, 4, 26, 8,
        16, 7, 27, 20, 13, 2,
        41, 52, 31, 37, 47, 55,
        30, 40, 51, 45, 33, 48,
        44, 49, 39, 56, 34, 53,
        46, 42, 50, 36, 29, 32]


def xor(x, y):
    if x == y:
        return '0'
    else:
        return '1'


def permute(k, arr, n):
    permutation = ""
    for i in range(0, n):
        permutation += k[arr[i] - 1]
    return permutation


def f_function(right, keyBinary):
    right = permute(right, exp_r, 48)
    result = ""
    sboxResult = ""
    for i in range(0, 48):
        result += xor(keyBinary[i], right[i])
    for j in range(0, 8):
        row = int(result[j * 6] + result[j * 6 + 5], 2)
        col = int(result[j * 6 + 1] + result[j * 6 + 2] + result[j * 6 + 3] + result[j * 6 + 4], 2)
        val = sbox[j][row][col]
        sboxResult += bin(val)[2:].zfill(4)
    sboxResult = permute(sboxResult, per, 32)
    return sboxResult


def shiftLeft(keyBinary):
    c = keyBinary[1:28] + keyBinary[0]
    d =  keyBinary[29:] + keyBinary[28]
    newstr = c + d
    return newstr


def shiftRight(keyBinary):
    c = keyBinary[27] + keyBinary[:27]
    d = keyBinary[55] + keyBinary[28:55]
    newstr = c + d
    return newstr

def encrypt(plainBinary, keyBinary):
    plainBinary = permute(plainBinary, initial_perm, 64)
    left = plainBinary[0:32]
    right = plainBinary[32:]
    keyBinary = permute(keyBinary, PC_1, 56)
    for i in range(1, 17):
        tempRight = right
        if i == 1 or i == 2 or i == 9 or i == 16:
            keyBinary = shiftLeft(keyBinary)
        else:
            keyBinary = shiftLeft(keyBinary)
            keyBinary = shiftLeft(keyBinary)
        keyPC = permute(keyBinary, PC_2, 48)
        fresult = f_function(right, keyPC)
        right = ""
        for j in range(0, 32):
            right += xor(left[j], fresult[j])
        left = tempRight
    cipherBinary = right + left
    cipherText = ""
    cipherBinary = permute(cipherBinary , final_perm , 64)
    for i in range(0, 64, 8):
        cipherText += chr(int(cipherBinary[i:i+8] , 2))
    return cipherText


def decrypt(cipherText , keyBinary):
    cipherBinary = ""
    for i in cipherText:
        cipherBinary += bin(ord(i))[2:].zfill(8)
    cipherBinary = permute(cipherBinary, initial_perm, 64)
    left = cipherBinary[0:32]
    right = cipherBinary[32:]
    keyBinary = permute(keyBinary, PC_1, 56)
    for i in range(1, 17):
        tempRight = right
        if i == 2 or i == 9 or i == 16:
            keyBinary = shiftRight(keyBinary)
        elif i != 1:
            keyBinary = shiftRight(keyBinary)
            keyBinary = shiftRight(keyBinary)
        keyPC = permute(keyBinary, PC_2, 48)
        fresult = f_function(right, keyPC)
        right = ""
        for j in range(0, 32):
            right += xor(left[j], fresult[j])
        left = tempRight
    plainBinary = right + left
    plainText = ""
    plainBinary = permute(plainBinary, final_perm, 64)
    for i in range(0, 64, 8):
        if chr(int(plainBinary[i:i + 8], 2)) != '@':
            plainText += chr(int(plainBinary[i:i + 8], 2))
    return plainText



plainText = input("Write the plaiText: ")
plainBinary = ""
blocksToEncrypt = []
blocksToDeccrypt = []
cipherText = ""
dePlainText = ""
for i in plainText:
    plainBinary += bin(ord(i))[2:].zfill(8)
if len(plainBinary) < 64:
    plainBinary += bin(ord('@'))[2:].zfill(8) * (8 - len(plainText))
    blocksToEncrypt.append(plainBinary)
elif len(plainBinary) > 64:
    words = int(len(plainBinary) / 64)
    if len(plainBinary) % 64 != 0:
        words += 1
    for i in range(0, words):
        if 64 * (i + 1) > len(plainBinary):
            blocksToEncrypt.append(
                plainBinary[0 + (i * 64):len(plainBinary)] + bin(ord('@'))[2:].zfill(8) * (8 - len(plainText) % 8))
        else:
            blocksToEncrypt.append(plainBinary[0 + (i * 64):64 + (i * 64)])
else:
    blocksToEncrypt.append(plainBinary)

while (True):
    key = input("Write the key: ")
    if len(key) != 8:
        print("The key must be 8 characters")
    else:
        break
keyBinary = ""
for i in key:
    keyBinary += bin(ord(i))[2:].zfill(8)

for i in range(0 , len(blocksToEncrypt)):
    blocksToDeccrypt.append(encrypt(blocksToEncrypt[i] , keyBinary))
    cipherText += blocksToDeccrypt[i]

print("The encrypted message is: " + cipherText)
for i in range(0 , len(blocksToDeccrypt)):
    dePlainText += decrypt(blocksToDeccrypt[i] , keyBinary)

print("The decrypted message is: " + dePlainText)