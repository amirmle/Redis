# Sets
has no order and cant have duplicated value 

    SADD nums 1 2 3 4 5 
    SADD user2 
    SMEMBERS nums
    DEL nums

---

    SADD users amir kevin jack amir
    SMEMBERS users
->
1) keivn
2) amir
3) jack

### cardinality
    SCAED users
->  4

### is values member of a set ?
    SISMEMBER users amir
-> 1

### pop - remove and returns a random value from set
    SPOP users [count]

### return random value from a set
    SRANDMEMBER users [count]
    SRANDMEMBER users [count > len] 
- returns all value from set
    SRANDMEMBER users [count < 0]
    SRANDMEMBER users -4
->
amir
kevin
kevin
jack
- returns the number of input [count], even repeated value

### remove a value from set
    SREM users kevin

### Set A MINES Set B - value that exist in A and not exists in B
    SADD user2 amir jack ali
    SDIFF users users2
-> keivn

### A MINES B PUT in C
    SDIFFSTORE users3 users users2

### intersection 
    SINTER users users2
->
amir
jack

    SINTERSTORE users3 users users2

### union
    SUNION users users2
-> 
amir
jack
kevin
ali

    SUNIONSTORE users3 users users2

### move value from one set to another set
    SMOVE src dec member




