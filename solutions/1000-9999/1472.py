# Design Browser History

'''
You have a browser of one tab where you start on the homepage 
and you can visit another url, get back in the history number 
of steps or move forward in the history number of steps.

'''

# Below approach is using Doubly Linked List
# Time: O(1) for initialization
# Time: O(1) for visit() function call
# Time: O(min(n, steps)) time for each back() and forward() function call; steps is number of steps we go forward or back
# Space: O(m*n) Where m = average length of the url , n = number of visited urls
class ListNode:
    def __init__(self, val, next=None, prev=None):
        self.val = val
        self.prev = prev
        self.next = next

class BrowserHistory:
    def __init__(self, homepage: str):
        self.cur = ListNode(homepage)

    def visit(self, url: str) -> None:
        self.cur.next = ListNode(url, prev=self.cur)
        self.cur = self.cur.next

    def back(self, steps: int) -> str:
        while self.cur.prev and steps > 0:
            self.cur = self.cur.prev
            steps =- 1
        return self.cur.val
    
    def forward(self, steps: int) -> str: 
        while self.cur.next and steps > 0:
            self.cur = self.cur.next
            steps =- 1
        return self.cur.val


# Below approach is using two stacks
# Time: O(1) for initialization
# Time: O(1) for visit() function call
# Time: O(min(n, steps)) time for each back() and forward() function call; steps is number of steps we go forward or back
# Space: O(m*n) Where m = average length of the url , n = number of visited urls

class BrowserHistory:

    def __init__(self, homepage: str):
        self.back_history = [homepage]
        self.front_history = []

    def visit(self, url: str) -> None:
        self.back_history.append(url)
        self.front_history = []

    def back(self, steps: int) -> str:
        while steps and len(self.back_history) > 1:
            self.front_history.append(self.back_history.pop())
            steps -= 1
        return self.back_history[-1]

    def forward(self, steps: int) -> str:
        while steps and self.front_history:
            self.back_history.append(self.front_history.pop())
            steps -= 1
        return self.back_history[-1]
    

# Below approach is using Dynamic Array
# Time: O(1) for initialization
# Time: O(1) for visit() function call
# Time: O(1) time for each back() and forward() function call; steps is number of steps we go forward or back
# Space: O(m*n) Where m = average length of the url , n = number of visited urls

class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = [homepage]
        self.cur = 0
        self.n = 1

    def visit(self, url: str) -> None:
        self.cur += 1
        if self.cur == len(self.history):
            self.history.append(url)
            self.n += 1
        else:
            self.history[self.cur] = url
            self.n = self.cur + 1

    def back(self, steps: int) -> str:
        self.cur = max(0, self.cur - steps)
        return self.history[self.cur]

    def forward(self, steps: int) -> str:
        self.cur = min(self.n - 1, self.cur + steps)
        return self.history[self.cur]