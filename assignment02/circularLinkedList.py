from listNode import ListNode

class CircularLinkedList:
    def __init__(self):
        self.__tail = ListNode("dummy", None)
        self.__tail.next = self.__tail
        self.__numItems = 0

    def insert(self, i:int, newItem) -> None:
        if(i >= 0 and i <= self.__numItems):
            prev = self.getNode(i - 1)
            newNode = ListNode(newItem, prev.next)
            prev.next = newNode
            if i == self.__numItems:
                self.__tail = newNode
            self.__numItems += 1
        else :
            print('index', i, ": out of bound in insert()") #필요 시 에러 처리

    def append(self, newItem) -> None:
        newNode = ListNode(newItem, self.__tail.next)
        self.__tail.next = newNode
        self.__tail = newNode
        self.__numItems += 1

    def pop(self, *args):
        #가변 파라미터. 인자가 없거나 -1이면 마지막 원소로 처리하기 위함. 파이썬 리스트 규칙 만족
        if self.isEmpty():
            return None
    #인덱스 i 결정
        if len(args) != 0 : #pop(k)과 같이 인자가 있으면 i = k 할당
            i = args[0]
        if len(args) == 0 or i == -1: #pop()에 인자가 없거나 pop(-1)이면 i에 맨 끝 인덱스 할당
            i = self.__numItems - 1
        #i번 원소 삭제 
        if (i >= 0 and i <= self.__numItems -1):
            prev = self.getNode(i-1)
            retItem = prev.next.next
            prev.next = prev.next.next
            if i == self.__numItems -1:
                self.__tail = prev
            self.__numItems -= 1 
            return retItem
        else:
            return None
        
    def remove(self,x):
        (prev, curr) = self.__findNode(x)
        if curr != None:
            prev.next = curr.next
            if curr == self.__tail:
                self.__tail = prev
            self.__numItems -= 1
            return x
        else:
            return None
        
    def get(self, *args):
    #가변파라미터. 인자가 없거나 -1이면 마지막 원소로 처리하기 위함. 파이썬 리스트 규칙 만족
        if self.isEmpty():
            return None
        # 인덱스 i 결정
        if len(args) != 0:
            i= args[0]
        if len(args) == 0 or i == -1:
            i = self.__numItems -1
        #i번 원소 리턴
        if (i>= 0 and i <= self.__numItems -1):
            return self.getNode(i).itme
        else:
            return None
        
    def index(self, x) -> int:
        cnt = 0
        for element in self:
            if element == x:
                return cnt
            cnt += 1
        return -12345
    
    def isEmpty(self) -> bool:
        return self.__numItems == 0
    
    def size(self) -> int:
        return self.__numItems
    
    def clear(self):
        self.__tail = ListNode("dummy", None)
        self.__tail.next = self.__tail
        self.__numItems = 0 

    def count(self, x) ->int:
        cnt = 0
        for element in self:
            if element == x:
                cnt += 1
        return cnt
    
    def extend(self, a): 
        for x in a:
            self.append(x)

    def copy(self) -> 'CircularLinkedList':
        a = CircularLinkedList()
        for element in self:
            a.append(element)
        return a
    
    def reverse(self) -> None:
        __head = self.__tail.next
        prev = __head; curr=prev.next; next = curr.next
        curr.next = __head; __head.next = self.__tail; self.__tail = curr
        for i in range(self.__numItems -1):
            perv = curr; curr=next; next=next.next
            curr.next = prev

    def sort(self) -> None:
        a=[]
        for element in self:
            a.append(element)
        a.sort()
        self.clear()
        for element in a:
            self.append(element)

    def __findNode(self,x):
        __head =prev = self.__tail.next
        curr = prev.next
        while curr !=__head:
            if curr.item == x:
                return (prev,curr)
            else:
                prev = curr; curr=curr.next
        return (None, None)

    def getNode(self, i:int) -> ListNode:
        curr = self.__tail.next
        for index in range(i+1):
            curr = curr.next
        return curr

    def printList(self) -> None:
        for element in self:
            print(element, end = '')
        print()

    def __iter__(self):
        return CircularLinkedListIterator(self) 
    
class CircularLinkedListIterator:
    def __init__(self,alist):
        self.__head = alist.getNode(-1)
        self.iterPosition = self.__head.next
    def __next__(self):
        if self.iterPosition == self.__head:
            raise StopIteration
        else:
            item = self.iterPosition.item
            self.iterPosition = self.iterPosition.next
            return item
        



   





