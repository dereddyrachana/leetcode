class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone = {
            '2' : ["a","b","c"],
            '3' : ["d","e","f"],
            '4' : ["g","h","i"],
            '5' : ["j","k","l"],
            '6' : ["m","n","o"],
            '7' : ["p","q","r","s"],
            '8' : ["t","u","v"],
            '9' : ["w","x","y","z"]
        }
        digit_list = []
        l = len(digits)
        if(l == 1):
            return phone[digits]
        for digit in digits:
            # print(phone[digit])
            digit_list.append(phone[digit])
        # print(digit_list)
        for i in range(l):
            if(len(digit_list) != 0 and len(digit_list)>=2):
                list_a = digit_list.pop(0)
                list_b = digit_list.pop(0)
            # print(list_a)
                new = []
                for a in list_a:
                    for b in list_b:
                        new.append(a+b)
                # print(new)
                if(len(digit_list) == 0):
                    return new
                else:
                    digit_list.insert(0,new)
            
            
        