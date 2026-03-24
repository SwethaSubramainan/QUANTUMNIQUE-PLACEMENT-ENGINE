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

def reverseList(head):
    prev = None
    curr = head

    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node

    return prev


def printList(head):
    temp = head
    while temp:
        print(temp.val, end=" -> ")
        temp = temp.next
    print("None")


arr = list(map(int, input("Enter elements: ").split()))


head = createLinkedList(arr)

print("Original:")
printList(head)

# Reverse list
head = reverseList(head)

print("Reversed:")
printList(head)
