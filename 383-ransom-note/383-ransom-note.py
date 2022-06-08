class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hashMap1 = dict()
        hashMap2 = dict()
        for i in range(len(ransomNote)):
            if(ransomNote[i] in hashMap1):
                hashMap1[ransomNote[i]] = hashMap1[ransomNote[i]] + 1
            else:
                hashMap1[ransomNote[i]] = 1
        for i in range(len(magazine)):
            if(magazine[i] in hashMap2):
                hashMap2[magazine[i]] = hashMap2[magazine[i]] + 1
            else:
                hashMap2[magazine[i]] = 1
        for i in ransomNote:
            if(i not in hashMap2):
                return False
            else:
                if(hashMap2[i] < hashMap1[i]):
                    return False
        return True