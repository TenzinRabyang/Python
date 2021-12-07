# Measuring 2-DIMENSION distance with below formula.
#  d(p,q)={sqrt(q1-p1)^2+....+(qn-pn)^2} - MEASURE DISTANCE
def squared_euclidean_similarity(pref1,in1,in2):
    from math import sqrt
    import other_similarity as other
    othersi = other.others_similarity()
    
    global total, b1, b2, b3, s1, s2, l1, l2, p, input1, input2, pref
    input1, input2, pref = in1, in2, pref1
    total = 0
    b1, b2, b3 = [], [], []
    s1, s2 = " " in input1, " " in input2
    l1, l2 = len(input1), len(input2)
    
                    
    # Calculate total---------------------------------------------------------(e)
    def find_total(x,y):
        global total
        for i in range(len(x)):
            a = x[i]
            b = y[i]
            total += pow(a-b,2)
    
    # Calculating USER to USER ---------------------------------------------------------------(1)
    if l1 <= 6 and l2 <= 6:
        for i in pref[input1]:
            if i in pref[input2]:
                a = int(pref[input1][i][3]) # converting to int
                b = int(pref[input2][i][3]) # converting to int
                total = total + pow(a-b,2)
    
    # Calculating BOOK TO BOOK ---------------------------------------------------------------(2)
    elif s1==True and s2 == True:
        for k,v in pref.items():
            for k1,v1 in v.items():
                if input1 in k1:
                    b1.append(int(v1[3])) # converting to int
                elif input2 in k1:
                    b2.append(int(v1[3])) # converting to int

        othersi.list_len(b1,b2)
        find_total(b1,b2)
            
    # Calculating ISBN TO ISBN-----------------------------------------------------------------(3)
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
        find_total(b1,b2)
    
    # ISBN TO USER ------------------------------------------------------------------------------(4)
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
        find_total(b2,b1)
            
    # ISBN TO BOOKNAME---------------------------------------------------------------------------(5)
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
        find_total(b2,b3)
            
    # USERID TO ISBN-------------------------------------------------------------------------------(6)
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
        find_total(b1,b2)
            
    # USERID TO BOOK NAME-----------------------------------------------------------------------------(7)
    elif l1 <= 6 and s2 == True:
        for i in pref[input1]:
            a = int(pref[input1][i][3]) # converting to int
            b1.append(a)
        for k,v in pref.items():
            for k1,v1 in v.items():
                if input2 in k1:
                    b3.append(int(v1[3]))
        othersi.list_len(b1,b3)
        find_total(b1,b3)
    
    # BOOKNAME TO ISBN-------------------------------------------------------------------------------(8)
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
        find_total(b3,b2)
    
    # BOOKNAME TO USER--------------------------------------------------------------------------------(9)
    elif s1 == True and l2 <= 6:
        for k,v in pref.items():
            for k1,v1 in v.items():
                if input1 in k1:
                    b3.append(int(v1[3]))
        for i in pref[input2]:
            a = int(pref[input2][i][3]) # converting to int
            b1.append(a)
        othersi.list_len(b3,b1)
        find_total(b3,b1)
        
    return float(sqrt(total))
