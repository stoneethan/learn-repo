# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        # 1. 创建哑节点(dummy)，作为结果链表的"虚拟头"
        dummy = ListNode(-1)
        # 2. cur 指针始终指向结果链表的最后一个节点
        cur = dummy

        # 3. 当两个链表都还有节点时，比较当前节点大小
        while list1 and list2:
            if list1.val <= list2.val:
                cur.next = list1     # 接上较小的 list1
                list1 = list1.next   # list1 指针后移
            else:
                cur.next = list2     # 接上较小的 list2
                list2 = list2.next   # list2 指针后移
            cur = cur.next           # cur 也跟着后移

        # 4. 循环结束后，某个链表可能还有剩余节点，直接接上
        cur.next = list1 if list1 else list2

        # 5. 返回哑节点的下一个节点，就是真正的头节点
        return dummy.next


# ============ 下面是测试代码 ============

def build_list(arr):
    """根据数组构建链表，返回头节点"""
    dummy = ListNode()
    cur = dummy
    for v in arr:
        cur.next = ListNode(v)
        cur = cur.next
    return dummy.next


def print_list(head):
    """打印链表，形如 1 -> 2 -> 4"""
    vals = []
    while head:
        vals.append(head.val)
        head = head.next
    print(" -> ".join(map(str, vals)) if vals else "空链表")


if __name__ == "__main__":
    s = Solution()

    # 测试 1：普通情况
    print("测试 1：普通情况")
    l1 = build_list([1, 2, 4])
    l2 = build_list([1, 3, 4])
    print("list1:", end=" "); print_list(l1)
    print("list2:", end=" "); print_list(l2)
    print("合并后:", end=" "); print_list(s.mergeTwoLists(l1, l2))
    print()

    # 测试 2：两个都为空
    print("测试 2：两个都为空")
    print("合并后:", end=" "); print_list(s.mergeTwoLists(None, None))
    print()

    # 测试 3：一个为空
    print("测试 3：list1 为空")
    print("合并后:", end=" "); print_list(s.mergeTwoLists(None, build_list([1, 2, 3])))
    print()

    print("测试 4：list2 为空")
    print("合并后:", end=" "); print_list(s.mergeTwoLists(build_list([5, 6]), None))
    print()

    # 测试 5：一个链表完全小于另一个
    print("测试 5：list1 全部小于 list2")
    print("合并后:", end=" "); print_list(s.mergeTwoLists(build_list([1, 2, 3]), build_list([4, 5, 6])))
    print()

    # 测试 6：有相等元素
    print("测试 6：有相等元素")
    print("合并后:", end=" "); print_list(s.mergeTwoLists(build_list([1, 1, 1]), build_list([1, 1])))
    print()

    # 测试 7：单个节点
    print("测试 7：各一个节点")
    print("合并后:", end=" "); print_list(s.mergeTwoLists(build_list([2]), build_list([1])))
    