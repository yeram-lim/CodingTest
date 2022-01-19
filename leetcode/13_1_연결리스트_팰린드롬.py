# import List
import os
import sys
from typing import List

# ListNode = 1->2
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def isPalindrom(self, head: ListNode) -> bool:
    q : List = []

    if not head: 
        return True
    
    node = head
    #리스트 변환
    while node is not None:
        q.append(node.val)
        node = node.next

    #팰린드롬 판별
    while len(q) > 1:
        if q.pop(0) != q.pop():
            return False

    return True

print(isPalindrom(head=[1,2,2,1]))