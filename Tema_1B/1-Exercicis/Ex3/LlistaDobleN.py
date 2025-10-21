from copy import deepcopy

class LlistaDobleN:
    class _Node:
        def __init__(self, val, prev=None, succ=None):
            self.val = val
            self.prev = prev
            self.succ = succ
        
        @property
        def val(self):
            return self._val
        @val.setter
        def val(self, n_val):
            self._val = n_val
        
        @property
        def prev(self):
            return self._prev
        @prev.setter
        def prev(self, n_prev):
            if isinstance(n_prev, LlistaDobleN._Node) or n_prev is None:
                self._prev = n_prev
            else:
                raise TypeError ("Previous pos must be an instance of the pos class or None (if head)")
        
        @property
        def succ(self):
            return self._succ
        
        @succ.setter
        def succ(self, n_succ):
            if isinstance(n_succ, LlistaDobleN._Node) or n_succ is None:
                self._succ = n_succ
            else:
                raise TypeError("Successor pos must be an instance of the pos class or None (if head)")
        def __eq__(self,other):
            if isinstance(other, LlistaDobleN._Node):
                return self._val == other._val
            else:
                return self._val == other
        def __str__(self):
            return self._val.__str__()
    
    def __init__(self, ll=None):
        self._length = 0
        self._head = None
        self._tail = None
        if isinstance(ll, list) or isinstance(ll, LlistaDobleN):
            for i, item in enumerate(ll):
                if i == 0:
                    self._head = self._Node(val=item, prev=self._tail, succ=None)
                    self._tail = self._head
                    node = self._head
                else:
                    self._tail = self._Node(val=item, prev=self._tail, succ=None)
                    node.succ = self._tail
                    node = self._tail
                self._length += 1
    
    def inserirPosicio(self,val,pos):
        if self._length == 0:
            if pos == 0 or pos == -1:
                self._head = self._Node(val=val, prev=self._tail, succ=None)
                self._tail = self._head
                self._length += 1
            else: raise IndexError
        elif pos < self._length:
            if pos < 0:
                x = self._tail
                i = -1
                in_range = i > -self._length
                while in_range:
                    if i != pos:
                        x = x.prev
                        i -= 1
                        in_range = i > -self._length
                    else:
                        in_range = False
                if pos != -1:
                    x.succ.prev = LlistaDobleN._Node(val, x, x.succ)
                    x.succ = x.succ.prev
                else:
                    self._tail = self._Node(val, x, x.succ)
                    x.succ = self._tail
            else:
                x=self._head
                i=0
                in_range = i < self._length
                while in_range:
                    if i != pos:
                        x = x.succ
                        i += 1
                        in_range = i < self._length
                    else:
                        in_range = False
                if pos != 0:
                    x.prev.succ = LlistaDobleN._Node(val, x.prev, x)
                    x.prev = x.prev.succ
                else:
                    self._head = LlistaDobleN._Node(val, x.prev, x)
                    x.prev = self._head
            self._length += 1
        else:
            raise IndexError
    
    def inserirPosicioList(self,pos, l2):
        node = self[pos]
        #        print(node)
        if node is None:
            self.__init__(l2)
        elif pos < 0:
            for value in l2:
                if node.succ is None:
                    self._tail = self._Node(val=value, prev=node, succ=node.succ)
                    node.succ = self._tail
                else:
                    node.succ.prev = self._Node(val=value, prev=node, succ=node.succ)
                    node.succ = node.succ.prev
                self._length += 1
                node = node.succ
        else:
            for value in l2:
                if node.prev is None:
                    self._head = self._Node(val=value, prev=node.prev, succ=node)
                    node.prev = self._head
                else:
                    node.prev.succ = self._Node(val=value, prev=node.prev, succ=node)
                    node.prev = node.prev.succ
                self._length += 1
            
    
    def deletePosicio(self, pos):
        if -self._length < pos < self._length:
            if pos < 0:
                x = self._tail
                for i in range(-1, pos, -1):
                    x = x.prev
            else:
                x = self._head
                for i in range(pos):
                    x = x.succ
            
            if x.prev is None:
                self._head = x.succ
            else:
                x.prev.succ = x.succ
            
            if x.succ is None:
                self._tail = x.prev
            else:
                x.succ.prev = x.succ
            
            self._length -= 1
            
        else:
            raise IndexError
    
    def delete(self, node):
        x = self._head
        while node != x and x is not None:
            x = x.succ
        if x is not None:
            if x.prev is None:
                self._head = x.succ
            else:
                x.prev.succ = x.succ
            
            if x.succ is None:
                self._tail = x.prev
            else:
                x.succ.prev = x.prev
            
            self._length -= 1
        else:
            raise ValueError
    
    def reverse(self):
        if self._length > 0:
            node = self._head.succ
            for i in range(self._length):
                if node is None:
                    self._tail.succ, self._tail.prev = self._tail.prev, self._tail.succ
                else:
                    node.prev.succ, node.prev.prev = node.prev.prev, node.prev.succ
                    node = node.succ
        self._head, self._tail = self._tail, self._head
        print(self)
    
    def append(self, val):
        self.inserirPosicio(val, -1)
    
    def __iter__(self) -> _Node:
        x=self._head
        for i in range(self._length):
            yield x
            x = x.succ
    
    def __getitem__(self, item):
        if 0 <= item < self._length:
            node = self._head
            for i in range(item):
                node = node.succ
        elif 0 > item >= -self._length:
            node=self._tail
            for i in range(-1, item, -1):
                node = node.prev
        else:
            if self._length == item:
                return None
            raise IndexError ("index not in range")
        return node
    
    def __len__(self):
        return self._length
    
    # noinspection SpellCheckingInspection
    def __eq__(self, other):
        if isinstance(other, LlistaDobleN) or isinstance(other, list):
            r = len(self) == len(other)
            if r:
                for i in range(self._length):
                    r = r and (self[i] == other[i])
            return r
        else:
            raise TypeError
    def __str__(self):
        tmp = "⟦"
        if self._head is not None:
            node = self._head
            tmp += node.__str__()
            while node.succ is not None:
                if node.succ is not None:
                    tmp += ", "
                node = node.succ
                tmp += node.__str__()
        return tmp + "⟧"

