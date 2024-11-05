def PermutePlainText(PlainText):
    Result=""
    Result+=PlainText[1]+PlainText[4]+PlainText[0]+PlainText[2]+PlainText[7]+PlainText[3]+PlainText[6]+PlainText[5]
    return Result


def cylicalShift(In):
    Out=""
    for i in range(1,len(In)):
        Out+=In[i]
    Out+=In[0]
    return Out

def ithRoundKey(KeySpace,i):           #ith round key has size 8 bits
    C0=KeySpace[9]+KeySpace[3]+KeySpace[0]+KeySpace[4]+KeySpace[10]
    D0=KeySpace[7]+KeySpace[8]+KeySpace[2]+KeySpace[6]+KeySpace[1]
    while(i>0):
        C0=cylicalShift(C0)
        D0=cylicalShift(D0)
        i-=1
    
    temp=(C0)+(D0)
    Ki=temp[7]+temp[1]+temp[3]+temp[8]+temp[6]+temp[9]+temp[5]+temp[2]
    return Ki


def roundKeyFunction(Key,Text):
    final=""
    for i in range(len(Key)):
        if Key[i]==Text[i]:
            final+='0'
        else:
            final+='1'
    return final

def finalPermutation(S):
    cipherText=S[2]+S[0]+S[3]+S[5]+S[1]+S[7]+S[6]+S[4]
    return cipherText

plainText=input("Enter the 8 bit string of bits: ")
keyspace=input("Enter the 12 bit keyspace: ")

initialpermutation=PermutePlainText(plainText)
K1=ithRoundKey(keyspace,1)

temp=roundKeyFunction(K1,initialpermutation)
K2=ithRoundKey(keyspace,2)

temp=roundKeyFunction(K2,temp)

CipherText=finalPermutation(temp)
print("The Cipher text is: ",CipherText)









