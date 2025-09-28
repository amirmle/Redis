https://redis.io/docs/latest/develop/using-commands/transactions/

### list sevral commands and then do them all at one atomic command

    MULTI 
    ->OK
    
    SET name amir
    ->QUEUED
    
    SET age 20
    ->QUEUED
    
    INCR age
    ->QUEUED
    
    DECRBY 40
    ->QUEUED
    
    GET name
    ->QUEUED
    
    GET age
    ->QUEUED
    
    DEL name
    ->QUEUED
    
    DEL age
    ->QUEUED
    
    EXEC
    ->
    1) OK
    2) OK
    3) (integer) 21
    4) (integer) 17
    5) "amir"
    6) "17"
    7) (integer) 1
    8) (integer) 1

### dicard mulit
    DISCARD

### watch - isolated 
    WATCH key
    UNWATCH
    
