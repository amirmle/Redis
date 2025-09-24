
# list in redis
 has order and can اhave duplicated value

    LPUSH mylist 'hello' #left push
  
    RPUSH mylist 'world' #right push

    LRANGE mylist 0 -1

-> 1) 'hello'

-> 2) 'world'

- get does not work

### push if list exists

    LOUSHX list-name 1 2 4

---
### overwrite item in certain index

    LSET mylist index value
    
### what is value in index i

    LINDEX mylist 0

->'hello'

### what is index for value x

    LPOS mylist world

-> 1

### insert item before|after certain item

    LINSERT mylist BEFORE world new 

### list lenght

    LLEN mylist

### pop first item at top|bottom

    LPOP mylist 
    RPOP mylist

### remove item

    LREM mylist i item #remove 'item', 'i' times from start
    LREM mylist -i item #remove 'item', 'i' times from end

### keep items from index i to j and remve others

    LTRIM mylist 2 5

---

### pop from one list and push to other list

    RPOPLPUSH src-list des-list

---
### pop from list, if list is empty, block and wait until something enters the list, then pop that

    BLPOP list [time-out-sec]


