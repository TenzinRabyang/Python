# Performing spearman_correlation_similarity measurement 
# 1-((cov(x,y))/std(x)*std(y)) -- Basic formula
def spearman_correlation_similarity(pref1,in1,in2):
    import math
    import other_similarity as other
    othersi = other.others_similarity()
    global b1, b2, b3, s1, s2, l1, l2, p, input1
    global input2, pref, cov, std1, std2
    cov, std1, std2, mx, my = 0, 0, 0, 0, 0
    input1, input2, pref = in1, in2, pref1
    b1, b2, b3 = [], [], []
    s1, s2 = " " in input1, " " in input2
    l1, l2 = len(input1), len(input2)
    
    # Calculating covariance on both list 
    def cov(x,y):
        global mx, my
        try:
            mx = sum(x)/len(x)
            my = sum(y)/len(y)
            cov = sum((a-mx)*(b-my) for (a,b) in zip(b1,b2)) / len(b1)
            return cov
        except:
            pass
        
    
    # Calculating Standard deviation for both list
    def std(x,y):
        from math import sqrt
        global std1, std2, mx, my
        try:
            std1 = sqrt(sum((i-mx)**2 for i in x)/(len(x)))
            std2 = sqrt(sum((y-mx)**2 for i in y)/(len(y)))
            return std1,std2
        except:
            pass
        
    
    # USER TO USER----------------------------------------------------------------------------1
    if l1 <= 6 and l2 <= 6:
        for i in pref[str(input1)]:
            if i in pref[str(input2)]:
                a = int(pref[input1][i][3])
                b = int(pref[input2][i][3])
                b1.append(a)
                b2.append(b)
        othersi.list_len(b1,b2)
        cov(b1,b2)
        std(b1,b2)
    # BOOK TO BOOK----------------------------------------------------------------------2
    elif s1 == True and s2 == True:
        for k,v in pref.items():
            for k1,v1 in v.items():
                if input1 in k1:
                    b1.append(int(v1[3])) # converting to int
                elif input2 in k1:
                    b2.append(int(v1[3])) # converting to int
        othersi.list_len(b1,b2)
        cov(b1,b2)
        std(b1,b2)
    # ISBN TO ISBN--------------------------------------------------------------------------------3
    elif l1 == 10 and l2 ==10:
        for k,v in pref.items():
            for k1,v1 in v.items():
                for i in v1:
                    if input1 in v1[0]:
                        b1.append(int(v1[3]))
                    if input2 in v1[0]:
                        b2.append(int(v1[3]))
                    break
        othersi.list_len(b1,b2)
        cov(b1,b2)
        std(b1,b2)
    # ISBN TO USER---------------------------------------------------------------------------4
    elif l1 == 10 and l2 <= 6:
        for k,v in pref.items():
            for k1,v1 in v.items():
                for i in v1:
                    if input1 in v1[0]:
                        b2.append(int(v1[3]))
                    break
        for i in pref[input2]:
            a = int(pref[input2][i][3]) # converting to int
            b1.append(a)
        othersi.list_len(b2,b1)
        cov(b2,b1)
        std(b2,b1)
    # ISBN TO BOOKNAME-----------------------------------------------------------------------5
    elif l1 == 10 and s2 == True:
        for k,v in pref.items():
            for k1,v1 in v.items():
                for i in v1:
                    if input1 in v1[0]:
                        b2.append(int(v1[3]))
                    break
        for k,v in pref.items():
            for k1,v1 in v.items():
                if input2 in k1:
                    b3.append(int(v1[3]))
        othersi.list_len(b2,b3)
        cov(b2,b3)
        std(b2,b3)
    # USER TO ISBN-------------------------------------------------------------------------6
    elif l1 <= 6 and l2 == 10:
        for i in pref[input1]:
            a = int(pref[input1][i][3]) # converting to int
            b1.append(a)
        
        for k,v in pref.items():
            for k1,v1 in v.items():
                for i in v1:
                    if input2 in v1[0]:
                        b2.append(int(v1[3]))
                    break
        othersi.list_len(b1,b2)
        cov(b1,b2)
        std(b1,b2)
    # USER TO BOOKNAME---------------------------------------------------------------------7
    elif l1 <= 6 and s2 == True:
        for i in pref[input1]:
            a = int(pref[input1][i][3]) # converting to int
            b1.append(a)
        for k,v in pref.items():
            for k1,v1 in v.items():
                if input2 in k1:
                    b3.append(int(v1[3]))
        othersi.list_len(b1,b3)
        cov(b1,b3)
        std(b1,b3)
    # BOOKNAME TO ISBN---------------------------------------------------------------------8
    elif s1 == True and l2 == 10:
        for k,v in pref.items():
            for k1,v1 in v.items():
                if input1 in k1:
                    b3.append(int(v1[3]))
        for k,v in pref.items():
            for k1,v1 in v.items():
                for i in v1:
                    if input2 in v1[0]:
                        b2.append(int(v1[3]))
                    break
        othersi.list_len(b3,b2)
        cov(b3,b2)
        std(b3,b2)
    # BOOKNAME TO USER-------------------------------------------------------------------9
    elif s1 == True and l2 <= 6:
        for k,v in pref.items():
            for k1,v1 in v.items():
                if input1 in k1:
                    b3.append(int(v1[3]))
        for i in pref[input2]:
            a = int(pref[input2][i][3]) # converting to int
            b1.append(a)
        othersi.list_len(b3,b1)
        cov(b3,b1)
        std(b3,b1)
        
    try:
        # denomenator
        de = std1*std2
        # nomenator
        no = cov
        # value
        val = no/de
        return val
    except:
        return "Undefine, Lack of observation"
