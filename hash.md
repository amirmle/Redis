# have key-value inside a value

    HSET user1 name amir age 20 height 180 

    HSET user1 gender man # add new field to hash

set if not exists

    HSETNX user1 user1 name ali

->0

---

### get a feild

    HGET user1 name

-> amir

### get all feilds in item

    HGETALL user1
->
1) "name"
2) "amir"
3) "age"
4) "20"
5) "height"
6) "180"

### get multiple feilds from a item

    HMGET user1 name age

->
1) "amir"
2) "20"

---

### delete field

    HDEL user1 name

---

### existance of field

    HEXISTS user age

---

### increment and decrement 

    HSET myhash field 5
    HINCRBY myhash field 1

->6

    HINCRBY myhash field -2

->4

---

### show all keys

    HKEYS user1

->
1) "name"
2) "age"
3) "height"

### show all values

    HVALS user1 

->
1) "amir"
2) "20"
3) "180"

---

### len of hash and fields

    HLEN user1

->3

    HSTRLEN user1 name 

->4

---


