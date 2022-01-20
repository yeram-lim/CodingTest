ListNode = 1->2
def isPalindrom(self, head: ListNode) -> bool:
    #데크 자료형 선언
    q: Deque = collections.deque()

    if not head:
        return True

    node = head
    while node in not None:
        q.append(node.val)
        node = node.next

    while len(q) > 1:
        if q.popleft() != q.pop():
            return False
        
    return True