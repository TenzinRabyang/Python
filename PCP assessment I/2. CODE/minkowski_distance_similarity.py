# Performing minkowski_distance_similarity function
# (k=1∑n|Xk-Yk|P)1/p -- Basic formula for the minkowski distance
def minkowski_distance_similarity(pref1,in1,in2):
    import math
    import other_similarity as other
    othersi = other.others_similarity()
    global total, b1, b2, b3, s1, s2, l1, l2, p, input1, input2, pref
    input1, input2, pref = in1, in2, pref1
    total = 0
    b1, b2, b3 = [], [], []
    s1, s2 = " " in input1, " " in input2
    l1, l2 = len(input1), len(input2)
    p = float('inf')

    
    # Calculate total---------------------------------------------------------(e)
    def find_total(x,y):
        global total
        for i in range(len(x)):
            a = x[i]
            b = y[i]
            total += pow(abs(a-b),p)
            
    # USERID to USERID-------------------------------------------------------------1
    if l1 <= 6 and l2 <= 6:
        for i in pref[input1]:
            if i in pref[input2]:
                a = int(pref[input1][i][3])
                b = int(pref[input2][i][3])
                total = total + pow(abs(a-b),p)
    # BOOK to BOOK------------------------------------------------------------------2
    elif s1 == True and s2 == True:
        for k,v in pref.items():
            for k1,v1 in v.items():
                if input1 in k1:
                    b1.append(int(v1[3])) # converting to int
                elif input2 in k1:
                    b2.append(int(v1[3])) # converting to int
        othersi.list_len(b1,b2)
        find_total(b1,b2)
        
    # ISBN TO ISBN-----------------------------------------------------------------2.1
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
            
    # ISBN TO USER --------------------------------------------------------------3
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
    
    # ISBN TO BOOKNAME ------------------------------------------------------------4
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
    # USER TO ISBN--------------------------------------------------------------5
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
    # USER TO BOOKNAME---------------------------------------------------------------6
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
    # BOOKNAME TO ISBN-------------------------------------------------------7
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
    # BOOKNAME TO USER---------------------------------------------------------------8
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
    return round(total**(1/p),3)
