# Number of students unable to eat lunch
'''
The school cafeteria offers circular and square sandwiches at lunch break, referred to by numbers 0 and 1 respectively.
All students stand in a queue. Each student either prefers square or circular sandwiches.
The number of sandwiches in the cafeteria is equal to the number of students. The sandwiches are placed in a stack. 
At each step:
> If the student at the front of the queue prefers the sandwich on the top of the stack, they will take it and leave the queue.
> Otherwise, they will leave it and go to the queue's end.
This continues until none of the queue students want to take the top sandwich and are thus unable to eat.
'''

# Using Frequency Count approach
# Time: O(n)
# Space: O(1)
from collection import List, Counter
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        res = len(students)
        cnt = Counter(students)

        for s in sandwiches:
            if cnt[s] > 0: # If count of sandwich(s) is greater than 0, it means the student is fed
                res -= 1
                cnt[s] -= 1
            else:
                break
        
        return res