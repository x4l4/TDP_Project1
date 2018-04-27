from Collections.Node import Node


class MyList:
    # _head = None
    # _tail = None

    def __init__(self, *args):
        self._head = self._tail = None
        if args is not ():
            for index in range(len(args)):
                if type(args[index]).__name__ == 'list' or 'tuple':
                    try:
                        for k in range(len(args[index])):
                            self.append(args[index][k])
                    except TypeError:
                            self.append(args[index])

    def append(self, x):
        """Add an item to the end of the list."""
        _node = Node(x, None, None)
        if self._head is not None:  # if the head is not None the previously of new node become the tail and the
            #  next one None
            _node._prev = self._tail  # previously of new node linked to tail
            _node._next = None  # the next of new new node linked to None
            self._tail._next = _node  # the tail's next linked to new node
            self._tail = _node  # new node become the tail
        else:  # if the head is None there aren't node, so the new node is tail and the head
            self._head = self._tail = _node

    def clear(self):
        """Remove all items from the list"""
        self.__init__()

    def isEmpty(self):
        if self.__bool__():
            return False
        else:
            return True

    def count(self, x):
        count = 0
        curr_node = self._head
        """Return the number of times x appears in the list."""
        for i in range(0, self.__len__()):
            if curr_node._value == x:
                count += 1
            curr_node = curr_node._next
        return count

    def extend(self, iterable):
        """Extend the list by appending all the items from the iterable. Equivalent to a[len(a):] = iterable."""
        for value in iterable:
            self.append(value)

    def copy(self):
        return self.__add__()

    def insert(self, i, x):
        new_node = Node(x, None, None)
        curr_node = self._head
        if i > self.__len__():
            return 'index out of range'
        # list is empty
        if self.isEmpty():
            self._head = new_node
            self._head._prev = self._head
        else:
            if i == 0:
                new_node._next = self._head
                self._head._prev = new_node
                self._head = new_node
                if self.__len__() == 0:
                    self._tail = new_node
                return
            elif i == self.__len__():
                self.append(new_node._value)
                return
            else:
                self.insertbeforenode(x, self.__getitem__(i-1))

    def insertbeforenode(self, data, value_search):
            new_node = Node(data,None,None)
            curr_node = self._head
            while curr_node:
                if curr_node._value == value_search._value:
                    new_node._prev = curr_node._prev
                    new_node._next = curr_node
                    curr_node._prev = new_node
                    new_node._prev._next = new_node  # <--
                    break  # find node and quit loop
                else:
                    curr_node = curr_node._next

    """def _insertToMiddle(self, value, left, right):
        # Iterate double linked list
        while True:
            # Test for intersection
            if left._next is right:
                print('sono qua')
                node = Node(value, left, right)
                left._next = node
                right._prev = node
                return
            elif left is right:
                print('no sono qua')
                node = Node(value, left._prev, right._next)
                left._next = node
                right._next._prev = node
                return
            # Next iteration node
            left = left._next
            right = right._prev
            if not left or not right:
                return"""

    def remove(self, x):
        """Remove the first item from the list whose value is x. It is an error if there is no such item."""
        curr_node = self._head
        k = 0
        while curr_node is not None:
            if curr_node._value == x:
                return self.pop(k)
            k += 1
            curr_node = curr_node._next
        else:
            return 'No such ' + str(x)

    def index(self, x, start=None, end=None):
        """Return zero-based index in the list of the first item whose value is x. Raises a ValueError if there is no such item.
            The optional arguments start and end are interpreted as in the slice notation and are used to limit
             the search to a particular subsequence of the list. The returned index is computed relative to the beginning
              of the full sequence rather than the start argument."""
        if (start and end) is not None:
            not_found = True
            curr_node = self.__getitem__(start)
            while start < end and not_found:
                if curr_node._value == x:
                    k = start
                    not_found = False
                curr_node = curr_node._next
                start += 1
            if not_found:
                raise ValueError
        elif (start and end) is None:
            curr_node = self._head
            for i in range(0, self.__len__()):
                if curr_node._value == x:
                    k = i
                    break
                curr_node = curr_node._next
            if i == self.__len__() - 1:
                raise ValueError
        return k

    def reverse(self):
        """Reverse the elements of the list in place."""
        temp = None
        curr_node = self._head
        self._tail = curr_node
        # Swap next and prev for all nodes of
        # doubly linked list
        while curr_node is not None:
            temp = curr_node._prev
            curr_node._prev = curr_node._next  # the previously is the next of the current node
            curr_node._next = temp  # the next will be the previously of current before swap
            curr_node = curr_node._prev  # update current node to previously
        # Before changing head, check for the cases like
        # empty list and list with only one node
        if temp is not None:
            self._head = temp._prev

    def pop(self, i=None):
        """Remove the item at the given position in the list, and return it. If no index is specified,
        a.pop() removes and returns the last item in the list. (The square brackets around the i in the method
        signature denote that the parameter is optional, not that you should type square brackets at that position. """
        result = None
        if i is None:
            ris = self._tail
            self._tail = ris._prev
            self._tail._next = None
            return ris._value
        else:
            curr_node = self._head
            k = 0
            try:
                if i == 0:
                    self._head = curr_node._next
                    self._head._prev = None
                    return curr_node._value
                elif i == self.__len__() - 1:
                    result = self._tail
                    self._tail = result._prev
                    self._tail._next = None
                    return result._value
                elif i >= self.__len__():
                    raise AttributeError
                while k < self.__len__():
                    if k == i:
                        result = curr_node
                        curr_node._prev._next = curr_node._next
                        curr_node._next._prev = curr_node._prev
                        break;
                    k += 1
                    curr_node = curr_node._next
            except AttributeError:
                return 'out of range'
            return result._value

    def __len__(self):
        i = 1
        node_iter = self._head
        while node_iter._next is not None:
            i += 1
            node_iter = node_iter._next
        return i

    def stamp(self):
        current = self._head
        to_print = []
        while current:
            to_print.append(current._value)
            current = current._next
        return "(HEAD) {items} (TAIL)".format(items=" <--> ".join(map(str, to_print)))

    def __str__(self):
        result = ""
        curr_node = self._head
        while curr_node is not None:
            result += '{0},'.format(str(curr_node._value))
            curr_node = curr_node._next
        return '[' + result[:-1] + ']'

    def __bool__(self):
        if self._head:
            return True
        else:
            return False

    def __getitem__(self, i):
        curr_node = self._head
        if i >= self.__len__():
            raise IndexError
        elif i == 0:
            return self._head
        for k in range(0, self.__len__()):
            if k == i:
                return curr_node
            curr_node = curr_node._next

    def __contains__(self, element):
        return True if self.count(element) != 0 else False

    def __add__(self, other=None):
        """adds a an iterable data structure to the double linked list"""
        ret_my_list = MyList()
        for item in self:
            ret_my_list.append(item._value)
        if other is not None:
            for item in other:
                ret_my_list.append(item)
        return ret_my_list

    def __iadd__(self, other=None):
        if other is not None:
            for item in other:
                self.append(item)
        return self

    def __eq__(self, other):
        is_MyList = str(other.__class__).__contains__('MyList')
        if len(self) != len(other):
            return False
        curr_node = self._head
        are_equals = True
        for item in other:
            if is_MyList:
                if item._value not in self:
                    are_equals = False
                    break
                curr_node = curr_node._next
            else:
                if item not in self:
                    are_equals = False
                    break
                curr_node = curr_node._next
        return are_equals

    def __ne__(self, other):
        if len(self) != len(other):
            return True
        is_MyList = str(other.__class__).__contains__('MyList')
        curr_node = self._head
        are_nequals = False
        for item in other:
            if is_MyList:
                if item._value not in self:
                    are_nequals = True
                    break
                curr_node = curr_node._next
            else:
                if item not in self:
                    are_nequals = True
                    break
                curr_node = curr_node._next
        return are_nequals

    def __setitem__(self, index, element):
        """Sets the item at a given index to a new element."""
        self.pop(index)
        self.insert(index, element)

    def __delitem__(self, key):
        """Delete the item at a given index."""
        self.pop(self.index(key))

    def __le__(self, other):
        is_MyList = str(other.__class__).__contains__('MyList')
        curr_node = self._head
        are_lequals = False
        for item in other:
            if is_MyList:
                if curr_node._value < item._value:
                    are_lequals = True
                    break
                curr_node = curr_node._next
            else:
                if curr_node._value < item:
                    are_lequals = True
                    break
                curr_node = curr_node._next
        return are_lequals

    def __ge__(self, other):
        is_MyList = str(other.__class__).__contains__('MyList')
        curr_node = self._head
        are_gequals = False
        for item in other:
            if is_MyList:
                if curr_node._value >= item._value:
                    are_gequals = True
                    break
                curr_node = curr_node._next
            else:
                if curr_node._value >= item:
                    are_gequals = True
                    break
                curr_node = curr_node._next
        return are_gequals

    def __gt__(self, other):
        is_MyList = str(other.__class__).__contains__('MyList')
        curr_node = self._head
        are_gtequals = False
        for item in other:
            if is_MyList:
                if curr_node._value > item._value:
                    are_gtequals = True
                    break
                curr_node = curr_node._next
            else:
                if curr_node._value > item:
                    are_gtequals = True
                    break
                curr_node = curr_node._next
        return are_gtequals

    def _suffix_rec(self,node,s, r):
        if node is not None:
            r += '[' + s[:-1]+ '], '
            s = "{0},".format(str(node._value)) + s
        else:
            r += '[' + s[:-1]+ ']'
            return r

        node = node._prev
        return self._suffix_rec(node,s, r)

    def suffix_rec(self):
        return self._suffix_rec(self._tail,s="", r="")


    def suffix(self):
        curr_node = self._tail
        list = ""
        s="[], "
        while curr_node:
            list = str(curr_node._value) + list
            if(curr_node != self._head):
                s = s + "[" + list + "]" + ", "
                list = "," + list
            else:
                s = s + "[" + list + "]"
            curr_node = curr_node._prev
        return s

    def sort(self,key = None,reverse = None):
        """Sort the items of the list in place
        the arguments can be used for sort customization"""
        if reverse is not None:
            self._sortFast()
            self.reverse()
        else:
            self._sortFast()

    def _sortFast(self):
          if self._head and self._head._next:
            i = self._head
            while i._next:
                selected = i
                j = i._next
                while j:
                    if j._value < selected._value:
                        selected = j
                    j = j._next
                if not selected==i:
                    i._value, selected._value = selected._value, i._value
                i = i._next
