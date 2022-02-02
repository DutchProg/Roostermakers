
# function to find the longest consecutive streak of missing numbers
def longestConsecutive(a):
      
      if len(a) == 0:
          return 0

      a.sort()
      a = [x for x in range(a[0], a[-1]+1) if x not in a]
      a = set(a)
      longest = 0

      for i in a:

         if i-1 not in a:
            current = i
            streak = 0

            while i in a:
               i+=1
               streak+=1
               longest = max(longest,streak)
               
      return longest


