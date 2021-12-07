class get_simi:
    global oi # ---Global variabla x1
    def __init__(self,oi=0):
        self.oi = oi
    # This function will print all the similarity options==================================================
    def print_options(self):
        print("Which Similarity Function you want to print: ")
        print("\t1. Squared euclidean similarity\n\t2. Minkowski distance similarity")
        print("\t3. Spearman correlation similarity\n\t4. Chebyshev similarity")
        print("\t5. Hamming distance similarity\n\t6. Cosine similarity\n\t7. Pearson Correlation\n\t8. All\n\t9. Exit")
        
    # This function will take options input from the users==============================================
    def o_input(self):
        global oi
        try:
            oi = int(input("Your option is: "))
        except:
            print("ERROR:Input isn't Integer. Try again")
            self.o_input()
        self.check_input()
            
    # This function will check/validate the input==============================================
    def check_input(self):
        import sys
        import dictload as dl
        import square_euclidean_similarity as ses
        import minkowski_distance_similarity as mds
        import spearman_correlation_similarity as scs
        import chebyshev_similarity as cs
        import hamming_distance_similarity as hds
        import cosine_similarity as css
        import pearson_correlation as pc
        global oi, x, y
        if oi == 1:
            print("Squared euclidean similarity is: ")
            print("\t\t\t",ses.squared_euclidean_similarity(dl.user_preference,x,y))
        elif oi == 2:
            print("Minkowski distance similarity is: ")
            print("\t\t\t",mds.minkowski_distance_similarity(dl.user_preference,x,y))
        elif oi == 3:
            print("Spearman correlation similarity is: ")
            print("\t\t\t",scs.spearman_correlation_similarity(dl.user_preference,x,y))
        elif oi == 4:
            print("Chebyshev similarity is: ")
            print("\t\t\t",cs.chebyshev_similarity(dl.user_preference,x,y))
        elif oi == 5:
            print("Hamming distance similarity is: ")
            print("\t\t\t",hds.hamming_distance_similarity(dl.user_preference,x,y))
        elif oi == 6:
            print("Cosine similarity is: ")
            print("\t\t\t",css.Cosine_similarity(dl.user_preference,x,y))
        elif oi == 7:
            print("Pearson Correlation is: ")
            print("\t\t\t",pc.Pearson_Correlation(dl.user_preference,x,y))
        elif oi == 8:
            print("\tSquared euclidean similarity is: ",ses.squared_euclidean_similarity(dl.user_preference,x,y))
            print("\tMinkowski distance similarity is: ",mds.minkowski_distance_similarity(dl.user_preference,x,y))
            print("\tSpearman correlation similarity is: ",scs.spearman_correlation_similarity(dl.user_preference,x,y))
            print("\tChebyshev similarity is: ",cs.chebyshev_similarity(dl.user_preference,x,y))
            print("\tHamming distance similarity is: ",hds.hamming_distance_similarity(dl.user_preference,x,y))
            print("\tCosine similarity is: ",css.Cosine_similarity(dl.user_preference,x,y))
            print("\tPearson_Correlation is: ",pc.Pearson_Correlation(dl.user_preference,x,y))
        elif oi == 9:
            sys.exit("You exited the program")
        else:
            print("ERROR:",int(oi)," option is not available. Try again")
            self.o_input()
            
    # This functions allows user to retry the similarity functions=========================
    def try_again(self):
        import sys
        ty = input("Try again: y/n \n")
        if ty == 'n':
            sys.exit("You Exited the Program")
        elif ty == 'y':
            self.user_ip()
        else:
            print("Invalid Options.\n")
            self.try_again()
    
    # This functions will take the main input on which we will find similarity========
    def user_ip(self):
        import dictload as dl
        global x, y, len1, len2, sp1, sp2, oi, w
        x = input("Enter first input: ")
        y = input("Enter second input: ")
        len1, len2 = len(x), len(y)
        sp1, sp2 = " " in x, " " in y
        w = False
        
        # Checking if both input value is same and if values are present in the database=========================
        if x != y:
            if 4<=len1<=6 and 4<=len2<=6: # user to user---
                for i in dl.user_preference:
                    if x == i:
                        for i in dl.user_preference:
                            if y == i:
                                w = True
                                self.print_options()
                                self.o_input()
                                self.try_again()
                if w == False:
                    print("\tOne of data not in the dictionary. Try again")
                    self.user_ip()
                    
            elif sp1 == True and sp2 == True: # book to book----
                for k,v in dl.user_preference.items():
                    for k1,v1 in v.items():
                        if x in k1:
                            for k,v in dl.user_preference.items():
                                for k1,v1 in v.items():
                                    if y in k1:
                                        w = True
                                        self.print_options()
                                        self.o_input()
                                        self.try_again()
                if w == False:
                    print("\tOne of data not in the dictionary. Try again.")
                    self.user_ip()
            elif len1 == 10 and len2 == 10:# ISBN TO ISBN--------
                for k,v in dl.user_preference.items():
                    for k1,v1 in v.items():
                        for i in v1:
                            if x in v1[0]:
                                for k,v in dl.user_preference.items():
                                    for k1,v1 in v.items():
                                        for i in v1:
                                            if y in v1[0]:
                                                w = True
                                                self.print_options()
                                                self.o_input()
                                                self.try_again()
                if w == False:
                    print("\tOne of data not in the dictionary. Try gain.")
                    self.user_ip()
            elif len1 == 10 and 4<=len2<=6: # ISBN TO USER--------
                for k,v in dl.user_preference.items():
                    for k1,v1 in v.items():
                        for i in v1:
                            if x in v1[0]:
                                for i in dl.user_preference:
                                    if y == i:
                                        w = True
                                        self.print_options()
                                        self.o_input()
                                        self.try_again()
                if w == False:
                    print("\tOne of the value not found. Try again.")
                    self.user_ip()
            elif len1 == 10 and sp2 == True: # ISBN TO BOOKNAME-----------
                for k,v in dl.user_preference.items():
                    for k1,v1 in v.items():
                        for i in v1:
                            if x in v1[0]:
                                for k,v in dl.user_preference.items():
                                    for k1,v1 in v.items():
                                        if y in k1:
                                            w = True
                                            self.print_options()
                                            self.o_input()
                                            self.try_again()
                if w == False:
                    print("\tOne of the value not found. Try again")
                    self.user_ip()
            elif 4<=len1<=6 and len2 == 10: # USER TO ISBN----------
                for i in dl.user_preference:
                    if x == i:
                        for k,v in dl.user_preference.items():
                            for k1,v1 in v.items():
                                for i in v1:
                                    if y in v1[0]:
                                        w = True
                                        self.print_options()
                                        self.o_input()
                                        self.try_again()
                if w == False:
                    print("\tOne of the value not found. Try again.")
                    self.user_ip()
            elif 4<=len1<=6 and sp2 == True: # USER TO BOOKNAME------------
                for i in dl.user_preference:
                    if x == i:
                        for k,v in dl.user_preference.items():
                            for k1,v1 in v.items():
                                if y in k1:
                                    w = True
                                    self.print_options()
                                    self.o_input()
                                    self.try_again()
                if w == False:
                    print("\tOne of the value not found. Try agian.")
                    self.user_ip()
            elif sp1 == True and len2 == 10: # BOOKNAME TO ISBN--------------
                for k,v in dl.user_preference.items():
                    for k1,v1 in v.items():
                        if x in k1:
                            for k,v in dl.user_preference.items():
                                for k1,v1 in v.items():
                                    for i in v1:
                                        if y in v1[0]:
                                            w = True
                                            self.print_options()
                                            self.o_input()
                                            self.try_again()
                if w == False:
                    print("\tOne of the value not found. Try again.")
                    self.user_ip()
            elif sp1 == True and 4<=len2<=6: # BOOKNAME TO USER----------------
                for k,v in dl.user_preference.items():
                    for k1,v1 in v.items():
                        if x in k1:
                            for i in dl.user_preference:
                                if y == i:
                                    w = True
                                    self.print_options()
                                    self.o_input()
                                    self.try_again()
                if w == False:
                    print("\tOne of the value not found. Try again.")
                    self.user_ip()                         
            else:
                print("\tInvalid input. Try again: ")
                self.user_ip()
            # elifhere------------------
        else:
            print("\tBoth input Can't have same value. Try again")
            self.user_ip()
