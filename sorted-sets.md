<img width="523" height="457" alt="image" src="https://github.com/user-attachments/assets/3162c4cb-6512-4661-b6bf-61cc1cf1900b" />

ZADD  key score member
ZADD class 12 amir 15 jack 18 bob
ZADD class 20 anna

ZRANGE key start end [WITHSCORES] # sorted by score - min to max
ZREVRANGE key start end [WITHSCORES] # sorted by score - max to min

### cardinality 
ZCARD class

### count of members that has score in certain range
ZCOUNT class 15 18 # include 15 and 18
-> 2
ZCOUNT class 15 (18 # include 15 but not 18
-> 1

### increment or decrement score of a member
ZINCRBY class 2 amir
ZINCRBY class -2 amir

### pop 
ZPOPMAX class [count]
ZPOPMIM class [count]

### a member has what rand/index
ZRANK class amir

### returns score of a member
SCORE class member

### remove member
ZREM class amir





