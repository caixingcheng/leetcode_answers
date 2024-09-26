/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
    dummy := &ListNode{} //哨兵节点
    curr := dummy
    carry := 0
    for l1 != nil || l2 != nil || carry != 0 {
        sum := 0
        if carry != 0 {
            sum += carry
        }
        if l1 != nil {
            sum += l1.Val
        } 
        if l2 != nil {
            sum += l2.Val
        }
        if sum >= 10 {
            carry = 1
            sum -= 10
        } else {
            carry = 0
        }
        curr.Next = &ListNode{sum, nil}
        curr = curr.Next
        if l1 != nil {
            l1 = l1.Next
        }
        if l2 != nil {
            l2 = l2.Next
        }
    }
    return dummy.Next
}
