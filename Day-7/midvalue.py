class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


def createLinkedList(arr):
    if not arr:
        return None

    head = ListNode(arr[0])
    temp = head

    for i in range(1, len(arr)):
        temp.next = ListNode(arr[i])
        temp = temp.next

    return head


def findMiddle(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow


def printList(head):
    temp = head
    while temp:
        print(temp.val, end=" -> ")
        temp = temp.next
    print("None")


arr = list(map(int, input("Enter elements: ").split()))


head = createLinkedList(arr)

print("Linked List:")
printList(head)


mid = findMiddle(head)

print("Middle:", mid.val)