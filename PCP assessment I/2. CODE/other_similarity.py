# Semilarity class and its methods
class others_similarity:
    import math
    
    # Creating inner function to make list of equal length
    def list_len(self,x,y): # ----------------------------------------------------(a)
        if len(x) < len(y):
            for i in range(len(x),len(y)):
                x.append(0)
        elif len(x)>len(y): 
            for i in range(len(y),len(x)):
                y.append(0)
        return x, y
            
            

