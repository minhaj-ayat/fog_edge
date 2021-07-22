import binascii
import codecs
from vector_gen import RijndaelKeySchedule, f1, f2345, generate_autn, derive_kasme,print_buffer
import ctypes

def atob(c):
    if '0' <= c <= '9':
        return ord(c)-ord('0')
    else:
        if 'a' <= c <= 'f':
            return ord(c)-ord('a')+10
        else:
            if 'A' <= c <= 'F':
                return ord(c)-ord('A')+10
            else:
                return 0


def catob(src):
    d = [0]*len(src)
    for i in range(len(src)):
        d[i] = (atob(src[i << 1]) << 4) | atob(src[(i << 1) + 1])
    return d


key = b"0c0a34601d4f07677303652c0462535b"
ans = codecs.decode(key,'hex')
print(ans)
k2 = b"\x0c\n4`\x1dO\x07gs\x03e,\x04bS["
ans = codecs.encode(k2,'hex')
print("Key: " + ans.decode())

key = b"2683b376d1056746de3b254012908e0e"
ans = codecs.decode(key,'hex')
print(ans)
k2 = b"&\x83\xb3v\xd1\x05gF\xde;%@\x12\x90\x8e\x0e"
ans = codecs.encode(k2,'hex')
print("Rand: " + ans.decode())


key = [12, 10, 52, 96, 29, 79, 7, 103, 115, 3, 101, 44, 4, 98, 83, 91]
rand = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ]
opc = [186, 5, 104, 129, 120, 227, 152, 190, 220, 16, 6, 116, 7, 16, 2, 203]

sqn =[0,0,0,0,0,96]

amf = [0x80, 0x00]
mac_a = f1(key,opc,rand,sqn,amf)

res = [0]*8
ak = [0]*6
ck = [0]*16
ik = [0]*16
key = [12, 10, 52, 96, 29, 79, 7, 103, 115, 3, 101, 44, 4, 98, 83, 91]
rand = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ]
opc = [186, 5, 104, 129, 120, 227, 152, 190, 220, 16, 6, 116, 7, 16, 2, 203]
plmn = [35,0,50,0]
s = [0]*14
f2345(key,opc,rand,res,ck,ik,ak)

generate_autn(sqn, ak, amf, mac_a)


new_key = derive_kasme(ck,ik,plmn,sqn,ak,s)
kdf = ctypes.CDLL("kdf.so")
kdf.kdf.argtypes = [ctypes.POINTER(ctypes.c_uint8), ctypes.c_uint16, ctypes.POINTER(ctypes.c_uint8), ctypes.c_uint16, ctypes.POINTER(ctypes.c_uint8), ctypes.c_uint16]
c_key = (ctypes.c_uint8 * len(new_key))(*new_key)
c_s = (ctypes.c_uint8 * len(s))(*s)
c_kasme = ctypes.POINTER(ctypes.c_uint8)()
kdf.kdf(ctypes.byref(c_key),32, ctypes.byref(c_s),14, ctypes.byref(c_kasme),32)

print("\nKasme", end=" ")
print_buffer(c_kasme)

