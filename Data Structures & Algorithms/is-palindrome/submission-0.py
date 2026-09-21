class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_nospace = re.sub(r'[^a-zA-Z0-9]', '', s)
        s_nospace = s_nospace.lower()
        head = 0
        tail = len(s_nospace) - 1
        
        while(head <= tail):
            if (s_nospace[head] != s_nospace[tail]):
                print(s_nospace[head])
                print(s_nospace[tail])
                return False
            head += 1
            tail -= 1
        
        return True