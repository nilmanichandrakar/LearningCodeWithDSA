/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* deleteMiddle(ListNode* head) {
        ListNode* newNode = new ListNode(0, head);
        ListNode* s = newNode;
        ListNode* f = head;
        while (f && f->next) {
            s = s->next;
            f = f->next->next;
        }
        s->next = s->next->next;
        return newNode->next;
    }
};
        
  
