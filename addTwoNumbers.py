# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
    carry = 0
    head = ListNode()
    currentNode = None
    
    while l1 != None or l2 != None:
        newNode = ListNode()
        
        if l1 == None: # If 1st list doesn't have another entry
            temp = l2.val
            
            if carry > 0:   # Add carry
                temp += carry
                carry = 0
            
            if temp >= 10:    # Check if it has carry
                newNode.val = temp % 10
                carry = temp // 10
            else:
                newNode.val = temp
            
            l2 = l2.next    # Update
            
        elif l2 == None: # If 2nd list doesn't have another entry
            temp = l1.val
            
            if carry > 0:   # Add carry
                temp += carry
                carry = 0
            
            if temp >= 10:    # Check if it has carry
                newNode.val = temp % 10
                carry = temp // 10
            else:
                newNode.val = temp
            
            l1 = l1.next    # Update
            
        else:       # If it has more entries
            temp = l1.val + l2.val
            
            if carry > 0:   # Add carry
                temp += carry
                carry = 0
            
            if temp >= 10:    # Check if it has carry
                newNode.val = temp % 10
                carry = temp //10
            else:
                newNode.val = temp
            
            l1 = l1.next    # Update
            l2 = l2.next
            
        if currentNode == None:   # Add to linked list
            currentNode = newNode
            head = currentNode
        else:
            currentNode.next = newNode
            currentNode = newNode
    
    if carry > 0:   # If it still has a carry at the end
        currentNode.next = ListNode(carry)
    
    return head