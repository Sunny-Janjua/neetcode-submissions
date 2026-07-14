class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s)!=len(t):
            return False
        # return Counter(s)==Counter(t)

        counter_variable=[0]*26

        for first_string in s:
            counter_variable[ord(first_string)-ord("a")]+=1

        for second_string in t:
            counter_variable[ord(second_string)-ord("a")]-=1
        

        for cnt in counter_variable:
            if cnt!=0:
                return False
        return True

