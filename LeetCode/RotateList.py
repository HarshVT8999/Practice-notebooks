def rotatelist(arr, k):
    for i in range(k):
        first = arr.pop()
        arr.insert(0, first)
    print(arr)


rotatelist([1, 2, 3], 2)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head

        length, tail = 1, head

        while(tail.next):
            tail = tail.next
            length += 1

        k = k % length if k >= length else k

        if length == 1 or k == 0:
            return head

        curr = head
        for i in range(length - k - 1):
            curr = curr.next
        newHead = curr.next
        curr.next = None
        tail.next = head

        return newHead
