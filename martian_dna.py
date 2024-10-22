from pathlib import Path

def martian_dna_subsequence(dna):
    string = Path(dna).read_text(encoding="utf-8")
    linje = string.splitlines()
    linje = [x.replace(" ", "") for x in linje]
    NKR = list(linje[0])
    Lengde = NKR[0]
    alfabet = NKR[1]
    minkrav = int(NKR[-1])
    right_R = 0
    left_R = 0
    right_L = 0
    left_L = 0
    DNA_streng = list(linje[1])
    startl = len(DNA_streng)
    
    DNA_streng_R = DNA_streng.copy()
    DNA_streng_L = DNA_streng.copy()
    
 
    
    
    for L in (DNA_streng_R):
        for R in (DNA_streng_R):
            Rtest_R = DNA_streng_R[:-1]
            if sjekktrue(minkrav,Rtest_R,linje) == True:
                    right_R +=1
                    del DNA_streng_R[-1]
            else : break
        Ltest_R = DNA_streng_R[1:]
        if sjekktrue(minkrav,Ltest_R,linje) == True:
                del DNA_streng_R[0]
                left_R += 1
        else: break
        
    for L in (DNA_streng_L):
        for R in (DNA_streng_L):
            Rtest_L = DNA_streng_L[:-1]
            if sjekktrue(minkrav,Rtest_L,linje) == True:
                    right_L +=1
                    del DNA_streng_L[-1]
            else : break
        Ltest_L = DNA_streng_L[1:]
        if sjekktrue(minkrav,Ltest_L,linje) == True:
                del DNA_streng_L[0]
                left_L += 1
        else: break
    if min((startl - right_R - left_R),(startl - right_L - left_L)) == startl:
        return "impossible"
    
        
    
    return min((startl - right_R - left_R),(startl - right_L - left_L))
   
    
    
    
    
def sjekktrue(minkrav, DNA_streng,linje):
    copy = DNA_streng.copy()
    for i in range(int(minkrav)):
        krav = list(linje[2 + i])
        nuk = krav[0]
        antall = krav[1]
        for l in range(int(antall)):
            if nuk in copy:
                copy.remove(nuk)
            else:
                return False
    return True


print("Tester martian_dna_subsequence... ", end="")
assert(martian_dna_subsequence("martian1.txt") == 2)
assert(martian_dna_subsequence("martian2.txt") == 7)
assert(martian_dna_subsequence("martian3.txt") == "impossible")
print("OK")


    