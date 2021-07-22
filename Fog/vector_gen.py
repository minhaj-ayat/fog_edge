import codecs
import ctypes

roundKeys = [[[int(0) for k in range(4)] for j in range(4)] for i in range(11)]

S = [
        99, 124, 119, 123, 242, 107, 111, 197, 48, 1, 103, 43, 254, 215, 171,
        118, 202, 130, 201, 125, 250, 89, 71, 240, 173, 212, 162, 175, 156, 164,
        114, 192, 183, 253, 147, 38, 54, 63, 247, 204, 52, 165, 229, 241, 113,
        216, 49, 21, 4, 199, 35, 195, 24, 150, 5, 154, 7, 18, 128, 226,
        235, 39, 178, 117, 9, 131, 44, 26, 27, 110, 90, 160, 82, 59, 214,
        179, 41, 227, 47, 132, 83, 209, 0, 237, 32, 252, 177, 91, 106, 203,
        190, 57, 74, 76, 88, 207, 208, 239, 170, 251, 67, 77, 51, 133, 69,
        249, 2, 127, 80, 60, 159, 168, 81, 163, 64, 143, 146, 157, 56, 245,
        188, 182, 218, 33, 16, 255, 243, 210, 205, 12, 19, 236, 95, 151, 68,
        23, 196, 167, 126, 61, 100, 93, 25, 115, 96, 129, 79, 220, 34, 42,
        144, 136, 70, 238, 184, 20, 222, 94, 11, 219, 224, 50, 58, 10, 73,
        6, 36, 92, 194, 211, 172, 98, 145, 149, 228, 121, 231, 200, 55, 109,
        141, 213, 78, 169, 108, 86, 244, 234, 101, 122, 174, 8, 186, 120, 37,
        46, 28, 166, 180, 198, 232, 221, 116, 31, 75, 189, 139, 138, 112, 62,
        181, 102, 72, 3, 246, 14, 97, 53, 87, 185, 134, 193, 29, 158, 225,
        248, 152, 17, 105, 217, 142, 148, 155, 30, 135, 233, 206, 85, 40, 223,
        140, 161, 137, 13, 191, 230, 66, 104, 65, 153, 45, 15, 176, 84, 187,
        22,
    ]

Xtime = [
    0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28,
    30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58,
    60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88,
    90, 92, 94, 96, 98, 100, 102, 104, 106, 108, 110, 112, 114, 116, 118,
    120, 122, 124, 126, 128, 130, 132, 134, 136, 138, 140, 142, 144, 146, 148,
    150, 152, 154, 156, 158, 160, 162, 164, 166, 168, 170, 172, 174, 176, 178,
    180, 182, 184, 186, 188, 190, 192, 194, 196, 198, 200, 202, 204, 206, 208,
    210, 212, 214, 216, 218, 220, 222, 224, 226, 228, 230, 232, 234, 236, 238,
    240, 242, 244, 246, 248, 250, 252, 254, 27, 25, 31, 29, 19, 17, 23,
    21, 11, 9, 15, 13, 3, 1, 7, 5, 59, 57, 63, 61, 51, 49,
    55, 53, 43, 41, 47, 45, 35, 33, 39, 37, 91, 89, 95, 93, 83,
    81, 87, 85, 75, 73, 79, 77, 67, 65, 71, 69, 123, 121, 127, 125,
    115, 113, 119, 117, 107, 105, 111, 109, 99, 97, 103, 101, 155, 153, 159,
    157, 147, 145, 151, 149, 139, 137, 143, 141, 131, 129, 135, 133, 187, 185,
    191, 189, 179, 177, 183, 181, 171, 169, 175, 173, 163, 161, 167, 165, 219,
    217, 223, 221, 211, 209, 215, 213, 203, 201, 207, 205, 195, 193, 199, 197,
    251, 249, 255, 253, 243, 241, 247, 245, 235, 233, 239, 237, 227, 225, 231,
    229]


def print_buffer(key):
    ret = ""
    for e in key:
        h = format(e, 'x')
        if len(h) == 1:
            h = "0" + h
        ret += h
        print(h, end="")
    print()
    return ret


def print_buffer2(key):
    ret = ""
    for e in key:
        h = format(e, 'x')
        if len(h) == 1:
            h = "0" + h
        ret += h
    return ret


def RijndaelKeySchedule(key):
    #print(roundKeys)
    print("RijndaelKeySchedule: K ",end=" ")
    print_buffer(key)

    for i in range(16):
        roundKeys[0][i & 0x03][i >> 2] = key[i]

    roundConst = 1
    for i in range(1, 11):
        roundKeys[i][0][0] = S[(roundKeys[i - 1][1][3])] ^ (roundKeys[i - 1][0][0]) ^ roundConst
        roundKeys[i][1][0] = S[roundKeys[i - 1][2][3]] ^ roundKeys[i - 1][1][0]
        roundKeys[i][2][0] = S[roundKeys[i - 1][3][3]] ^ roundKeys[i - 1][2][0]
        roundKeys[i][3][0] = S[roundKeys[i - 1][0][3]] ^ roundKeys[i - 1][3][0]

        for j in range(4):
            roundKeys[i][j][1] = roundKeys[i - 1][j][1] ^ roundKeys[i][j][0]
            roundKeys[i][j][2] = roundKeys[i - 1][j][2] ^ roundKeys[i][j][1]
            roundKeys[i][j][3] = roundKeys[i - 1][j][3] ^ roundKeys[i][j][2]

        roundConst = Xtime[roundConst]


def KeyAdd(state, rnd):
    for i in range(4):
        for j in range(4):
            state[i][j] ^= roundKeys[rnd][i][j]


def ByteSub(state):
    for i in range(4):
        for j in range(4):
            state[i][j] = S[state[i][j]]


def ShiftRow(state):
    temp = state[1][0]
    state[1][0] = state[1][1]
    state[1][1] = state[1][2]
    state[1][2] = state[1][3]
    state[1][3] = temp

    temp = state[2][0]
    state[2][0] = state[2][2]
    state[2][2] = temp
    temp = state[2][1]
    state[2][1] = state[2][3]
    state[2][3] = temp

    temp = state[3][0]
    state[3][0] = state[3][3]
    state[3][3] = state[3][2]
    state[3][2] = state[3][1]
    state[3][1] = temp


def MixColumn(state):
    for i in range(4):
        temp = state[0][i] ^ state[1][i] ^ state[2][i] ^ state[3][i]
        tmp0 = state[0][i]

        tmp = Xtime[state[0][i] ^ state[1][i]]
        state[0][i] ^= temp ^ tmp
        tmp = Xtime[state[1][i] ^ state[2][i]]
        state[1][i] ^= temp ^ tmp
        tmp = Xtime[state[2][i] ^ state[3][i]]
        state[2][i] ^= temp ^ tmp
        tmp = Xtime[state[3][i] ^ tmp0]
        state[3][i] ^= temp ^ tmp


def RijndaelEncrypt(input, output):
    state = [[0 for x in range(4)] for y in range(4)]

    for i in range(16):
        state[i & 0x3][i >> 2] = input[i]

    KeyAdd(state, 0)

    for r in range(1, 10):
        ByteSub(state)
        ShiftRow(state)
        MixColumn(state)
        KeyAdd(state, r)

    ByteSub(state)
    ShiftRow(state)
    KeyAdd(state, 10)

    for i in range(16):
        output[i] = state[i & 0x3][i >> 2]


def f1(k, opc, rand, sqn, amf):

    RijndaelKeySchedule(k)

    rijndaelInput = [0]*16
    temp = [0] * 16
    in1 = [0] * 16
    out1 = [0] * 16
    mac_a = [0] * 8

    for i in range(16):
        rijndaelInput[i] = rand[i] ^ opc[i]

    RijndaelEncrypt(rijndaelInput, temp)

    for i in range(6):
        in1[i]     = sqn[i]
        in1[i + 8] = sqn[i]

    for i in range(2):
        in1[i + 6]  = amf[i]
        in1[i + 14] = amf[i]

    for i in range(16):
        rijndaelInput[(i + 8) % 16] = in1[i] ^ opc[i]

    for i in range(16):
        rijndaelInput[i] ^= temp[i]

    RijndaelEncrypt(rijndaelInput, out1)

    for i in range(16):
        out1[i] ^= opc[i]

    for i in range(8):
        mac_a[i] = out1[i]

    print("\nMAC-A", end=" ")
    print_buffer(mac_a)
    return mac_a


def f2345(k, opc, rand, res, ck, ik, ak):
    RijndaelKeySchedule(k)

    rijndaelInput = [0] * 16
    temp = [0] * 16
    out = [0] * 16

    for i in range(16):
        rijndaelInput[i] = rand[i] ^ opc[i]

    RijndaelEncrypt(rijndaelInput, temp)
    for i in range(16):
        rijndaelInput[i] = temp[i] ^ opc[i]

    rijndaelInput[15] ^= 1
    RijndaelEncrypt(rijndaelInput, out)

    for i in range(16):
        out[i] ^= opc[i]

    for i in range(8):
        res[i] = out[i + 8]

    for i in range(6):
        ak[i] = out[i]

    for i in range(16):
        rijndaelInput[(i + 12) % 16] = temp[i] ^ opc[i]

    rijndaelInput[15] ^= 2

    RijndaelEncrypt(rijndaelInput, out)

    for i in range(16):
        out[i] ^= opc[i]

    for i in range(16):
        ck[i] = out[i]

    for i in range(16):
        rijndaelInput[(i + 8) % 16] = temp[i] ^ opc[i]

    rijndaelInput[15] ^= 4
    RijndaelEncrypt(rijndaelInput, out)

    for i in range(16):
        out[i] ^= opc[i]

    for i in range(16):
        ik[i] = out[i]

    print("\nAK", end=" ")
    print_buffer(ak)
    print("\nCK", end=" ")
    print_buffer(ck)
    print("\nIK", end=" ")
    print_buffer(ik)
    print("\nXRES", end=" ")
    print_buffer(res)


def generate_autn(sqn, ak, amf, mac_a):
    autn = [0]*16
    for i in range(6):
        autn[i] = sqn[i] ^ ak[i]

    autn[6:8] = amf
    autn[8:16] = mac_a

    print("\nAUTN", end=" ")
    print_buffer(autn)
    return autn


def derive_kasme(ck, ik, plmn, sqn, ak, s):
    s = [0] * 14
    key = [0] * 32

    key[0:16] = ck
    key[16:32] = ik

    s[0] = 0x10

    s[1:4] = plmn[0:3]

    s[4] = 0x00
    s[5] = 0x03

    for i in range(6):
        s[6 + i] = sqn[i] ^ ak[i]

    s[12] = 0x00
    s[13] = 0x06

    return key


def generate_vector(rrand, rxres):
    key = [12, 10, 52, 96, 29, 79, 7, 103, 115, 3, 101, 44, 4, 98, 83, 91]
    rand = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    opc = [186, 5, 104, 129, 120, 227, 152, 190, 220, 16, 6, 116, 7, 16, 2, 203]

    sqn = [0, 0, 0, 0, 0, 96]

    amf = [0x80, 0x00]
    mac_a = f1(key, opc, rand, sqn, amf)

    res = [0] * 8
    ak = [0] * 6
    ck = [0] * 16
    ik = [0] * 16
    key = [12, 10, 52, 96, 29, 79, 7, 103, 115, 3, 101, 44, 4, 98, 83, 91]
    rand = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    opc = [186, 5, 104, 129, 120, 227, 152, 190, 220, 16, 6, 116, 7, 16, 2, 203]
    plmn = [35, 0, 50, 0]
    s = [0] * 14
    f2345(key, opc, rrand, rxres, ck, ik, ak)

    rautn = generate_autn(sqn, ak, amf, mac_a)
    return rautn

    '''new_key = derive_kasme(ck, ik, plmn, sqn, ak, s)
    kdf = ctypes.CDLL("kdf.so")
    kdf.kdf.argtypes = [ctypes.POINTER(ctypes.c_uint8), ctypes.c_uint16, ctypes.POINTER(ctypes.c_uint8),
                        ctypes.c_uint16, ctypes.POINTER(ctypes.c_uint8), ctypes.c_uint16]
    c_key = (ctypes.c_uint8 * len(new_key))(*new_key)
    c_s = (ctypes.c_uint8 * len(s))(*s)
    c_kasme = ctypes.POINTER(ctypes.c_uint8)()
    kdf.kdf(ctypes.byref(c_key), 32, ctypes.byref(c_s), 14, ctypes.byref(c_kasme), 32)

    print("\nKasme", end=" ")
    print_buffer(c_kasme)'''

