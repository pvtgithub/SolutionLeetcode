class Solution:
   def uniqueMorseRepresentations(self, words):
      morse_codes=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
      s=set()
      for word in words:
         temp=''
         for c in word:
            temp+=morse_codes[ord(c)-97]
         s.add(temp)
         print(s)
      return len(s)
ob = Solution()
print(ob.uniqueMorseRepresentations(["gin", "zen", "gig", "msg"]))