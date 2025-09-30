in redis we mark databases with numbers
default starting database -> 0

avaible default databases 
    CONFIG GET databases
    -> 16

change data base
    SELECT index
    SELECT 4

send keys from database to another
    SWAPDB index1 index2

delete current active database
    FLUSHDB 
    -> ok

delete all databases 
    FLUSHALL 
    -> ok

number of keys in db
    DBSIZE


info about db
    INFO

last time we saved 
    LASTSAVE

monitoring
    MONITOR

clients info
    CLIENT LIST
    CLIENT SETNAME amir
