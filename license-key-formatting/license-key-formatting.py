class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        #remove all the dashes
        s = s.replace("-","")
        #print(s)
        #reverse the string
        s = s[::-1]
        #print(s)
        #for every k add a dash
        if(len(s)!=0):  
            no_dash = len(s)//k
        else:
            return s
        #print(no_dash)
        index = k
        while(no_dash != 0):
            #print(index)
            s = s[:index] + '-' + s[index:]
            index = index + k + 1
            no_dash = no_dash-1
        #print(s)
        #captitalize
        s = s.upper()
        #print(s)
        #reverse it again
        s = s[::-1]
        #print(s)
        if(s[0] == '-'):
            s = s[1:]
            # s = s[1:]
        return s