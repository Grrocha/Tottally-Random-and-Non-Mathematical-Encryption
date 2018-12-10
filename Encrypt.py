import random

Input = "Teste"
Output = []
Result = []
EncryptMap = {}
Chars = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ "
Step = 1024
for i in range(Step):
    Result.append(random.choice(Chars))
    
FirstSeed = "".join(Result)
Output.append(FirstSeed)
Seed = FirstSeed
random.seed(Seed)
for c in Chars:
    Result = []
    for i in range(Step):
        Result.append(random.choice(Chars))
    EncryptMap[c] = "".join(Result)
    for i in range(Step):
        Result.append(random.choice(Chars))
    Seed = "".join(Result)
    random.seed(Seed)
for c in Input:
    Output.append(EncryptMap[c])

Output = "".join(Output)
print(Output)

def Decrypt(String):
    Output = []
    String_Split = [String[i:i+Step] for i in range(0,len(String), Step)]
    print(String_Split)
    FirstSeed = String_Split[0]
    random.seed(FirstSeed)
    for c in Chars:
        Result = []
        for i in range(Step):
            Result.append(random.choice(Chars))
        EncryptMap[c] = "".join(Result)
        for i in range(Step):
            Result.append(random.choice(Chars))
        Seed = "".join(Result)
        random.seed(Seed)
    String_Split.remove(String_Split[0])
    for i in String_Split:
        Output.append(list(EncryptMap.keys())[list(EncryptMap.values()).index(i)])
    Output = "".join(Output)
    print(Output)
Decrypt(Output)