def singleRound(LR,generatedKey):
    L1=LR[4]+LR[5]+LR[6]+LR[7]
    finalxor=""
    for i in range(4):
        if(L1[i]==generatedKey[i]):
            finalxor+='0'
        else:
            finalxor+='1'
    print(finalxor)
    for i in range(4):
        if(LR[i]==finalxor[i]):
            L1+='0'
        
        else:
            L1+='1'
    return L1


def FiestelSystem3RoundsEncrypt(Ptext,Key):
        LR=Ptext
        K1=""
        for i in range(4):
            if(Key[i]==Key[i+4]):
                K1+='0'
            else: 
                K1+='1'
        K2=""
        K3=""
        for i in range(4,8):
            if(Key[i]==Key[i+4]):
                K2+='0'
            else: 
                K2+='1'

        for i in range(8,12):
            if(Key[i]==Key[i-8]):
                K3+='0'
            else: 
                K3+='1'
        LR1=singleRound(LR,K1)
        LR2=singleRound(LR1,K2)
        LR3=singleRound(LR2,K3)

        final=LR3[4]+LR3[5]+LR3[6]+LR3[7]+LR3[0]+LR3[1]+LR3[2]+LR3[3]
        return final

Ptext:str=input("Enter the 8 bit Plain text: ")
SystemKey:str=input("Enter the 12 bit Key: ")
Ctext=FiestelSystem3RoundsEncrypt(Ptext,SystemKey)
print("The ciphered text is ",Ctext)
