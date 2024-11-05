def s(t):
    S_box=[12,5,6,11,9,0,10,13,3,14,15,8,4,7,1,2]
    return S_box[t]


def F_func_singleround(P):     
    t0=P[0:4]
    t1=P[4:8]
    t2=P[8:12]
    t3=P[12:16]
    t0=int(t0,2)
    t1=int(t1,2)
    t2=int(t2,2)
    t3=int(t3,2)
    t0new=str(bin(s(t0)^t1))[2:].zfill(4)
    t1new=str(bin(t2))[2:].zfill(4)
    t2new=str(bin(s(t2)^t3))[2:].zfill(4)
    t3new=str(bin(t0))[2:].zfill(4)
    return t0new+t1new+t2new+t3new

def F(P):    
    for i in range(6):
        P=F_func_singleround(P)
    return P

def keyschedule(K,i:int):
    K0=K[0:16]
    K1=K[16:32]
    K2=K[32:48]
    K3=K[48:64]
    K4=K[64:80]
    x=[K0,K1,K2,K3,K4]
    WK0=K0
    WK1=K1
    WK2=K3
    WK3=K4
   
    RCi="0"+format(i, '06b')+"00"+ format(i, '06b')+"0"
    RKi=str(bin(int(x[i%5],2)^int(RCi,2)))[2:].zfill(16)

    return RKi


def encryptSingleRound(K,P,i:int):
    P0=P[0:16]
    P1=P[16:32]
    P2=P[32:48]
    P3=P[48:64]
    if(i==1):
        WK0=K[0:16]
        WK1=K[16:32]
        P0=str(bin(int(P0,2)^int(WK0,2)))[2:].zfill(16)
        P2=str(bin(int(P2,2)^int(WK1,2)))[2:].zfill(16)
    RK1=keyschedule(K,2*(i-1))
    RK2=keyschedule(K,2*i-1)
    P0new=str(bin(int(P1,2)^int(F(P0),2)^int(RK1,2)))[2:].zfill (16)   
    P1new=P2
    P2new=str(bin(int(P3,2)^int(F(P2),2)^int(RK2,2)))[2:].zfill(16)
    P3new=P0    
    if(i==18):
        WK2=K[48:64]
        WK3=K[64:80] 
        P3new=str(bin(int(P3new,2)^int(WK2,2)))[2:].zfill(16)
        P1new=str(bin((int(P1new,2)^int(WK3,2))))[2:].zfill(16)
    return P0new+P1new+P2new+P3new

def encrypt(K,P):
    for i in range(1,19):
        P=encryptSingleRound(K,P,i)
    return P

def decryptSingleRound(K, C, i: int):
    C0 = C[0:16]
    C1 = C[16:32]
    C2 = C[32:48]
    C3 = C[48:64]
    
    if i == 18:  # First round of decryption (last round of encryption)
        WK2 = K[48:64]
        WK3 = K[64:80]
        C3 = str(bin(int(C3, 2) ^ int(WK2, 2)))[2:].zfill(16)
        C1 = str(bin(int(C1, 2) ^ int(WK3, 2)))[2:].zfill(16)
    
    RK1 = keyschedule(K, 2 * (i))
    RK2 = keyschedule(K, 2 * (i) + 1)
    
    C0new = C3
    C1new = str(bin(int(C0, 2) ^ int(F(C3), 2) ^ int(RK1, 2)))[2:].zfill(16)
    C2new = C1
    C3new = str(bin(int(C2, 2) ^ int(F(C1), 2) ^ int(RK2, 2)))[2:].zfill(16)
    
    if i == 1:  # Last round of decryption (first round of encryption)
        WK0 = K[0:16]
        WK1 = K[16:32]
        C0new = str(bin(int(C0new, 2) ^ int(WK0, 2)))[2:].zfill(16)
        C2new = str(bin(int(C2new, 2) ^ int(WK1, 2)))[2:].zfill(16)
    
    return C0new + C1new + C2new + C3new

def decrypt(K, ciphertext):
    # Convert hex ciphertext to binary string
    C = bin(int(ciphertext, 16))[2:].zfill(64)
    
    # Perform 18 rounds of decryption
    for i in range(18, 0, -1):
        C = decryptSingleRound(K, C, i)
    
    return C

plaintextinhex=input("Enter the plaintext in hex: ")
keyinhex=input("Enter the key in hex: ")
plaintextinstr=bin(int(plaintextinhex, 16))[2:].zfill(64)
keyinstr=bin(int(keyinhex, 16))[2:].zfill(80)
ciphertext=encrypt(keyinstr,plaintextinstr)
ciphertextinstr=bin(int(ciphertext, 2))[2:].zfill(64)
ciphertextinhex=hex(int(ciphertext, 2))[2:].zfill(16)
print("The ciphertext is: ",ciphertextinhex)
decryptedtextinstr=decrypt(keyinstr,ciphertextinhex)
print("The decrypted text is: ",hex(int(plaintextinstr,2))[2:].zfill(16))
# plaintext: 0000000000000000
# key: 00000000000000000000
# ciphertext: 6c6c2a2a5151efef


