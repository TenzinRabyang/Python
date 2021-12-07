# Performing Cosine_similarity function
# Cosine similarity measures the similarity between two vectors by calculating the cosine of the angle between the two vectors.
# formula A*B/(||A||*||B||)
def Cosine_similarity(pref1,in1,in2):
    from math import sqrt
    import other_similarity as other
    othersi = other.others_similarity()
    
    global row1, row2, b1, b2, b3, s1, s2, l1, l2, input1, input2, pref, a1, b4, no, a, b
    input1, input2, pref = in1, in2, pref1
    row1, row2, b1, b2, b3 = [], [], [], [], []
    s1, s2 = " " in input1, " " in input2
    l1, l2 = len(input1), len(input2)
    a1, b4, no, a, b = 0, 0, 0, 0, 0
    
    
    def find_total(x,y):
        global no, a1, b4
        for i in range(len(x)):
            no += x[i]*y[i]
            a1 += pow(x[i],2)
            b4 += pow(y[i],2)
        return no, a1, b4
    
    # USER TO USER---------------------------------------------------------------------------------1
    if l1 <= 6 and l2 <= 6:
        for i in pref[input1]:
            if i in pref[input2]:
                a = int(pref[input1][i][3])
                b = int(pref[input2][i][3])
                no += a*b
                a1 += pow(a,2)
                b4 += pow(b,2)
    # BOOK TO BOOK----------------------------------------------------------------------------2
    elif s1 == True and s2 ==  True:
        for k,v in pref.items():
            for k1,v1 in v.items():
                if input1 in k1:
                    a = int(v1[3]) # converting to int
                elif input2 in k1:
                    b = int(v1[3]) # converting to int
                no += a*b
                a1 += pow(a,2)
                b4 += pow(b,2)
                break
    # ISBN TO ISBN------------------------------------------------------------------------3
    elif l1 ==10 and l2 == 10:
        for k,v in pref.items():
            for k1,v1 in v.items():
                for i in v1:
                    if input1 in v1[0]:
                        a = int(v1[3])
                    if input2 in v1[0]:
                        b = int(v1[3])
                    no += a*b
                    a1 += pow(a,2)
                    b4 += pow(b,2)
                    break
    # ISBN TO USER---------------------------------------------------------------------4
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
    # ISBN TO BOOKNAME------------------------------------------------------------5
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
    # USER TO ISBN --------------------------------------------------------6
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
    # USER TO BOOKNAME-------------------------------------------------7
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
    # BOOKNAME TO ISBN----------------------------------------------8
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
    # BOOKNAME TO USER----------------------------------------9
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
        
    try:
        deno1 = sqrt(a1)
        deno2 = sqrt(b1)
        return no/(deno1*deno2)
    except:
        return "Undefine, Lack of observation"
