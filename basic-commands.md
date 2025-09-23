	redis-cli

connect to remote host

	redis-cli -h [ip] -p [post] -a [password]

---
	SET key value
->OK
	
	set key value EX time-to-expire
---
	GET key
->value

usefull for something like strings

	GETRANGE key start-index end-index 
	
set new value and return old value

	GETSET key value 

get by regex
	KEYS pattern

	KEYS *
	
->all keys
---
	DEL key1 key2 key3 ...
->number of deleted keys

---	
	EXIST key1 key2 key3 ...
->number of existed keys - counts same keys
---
set expire time for key

	EXPIRE key time-sec

time to live

	TTL key

undo EXPIRE

	PERSIS key 
---

	RANDOMKEY
-> random-key
---
	RENANE key newkey
->OK
---
	APPEND key value
---
decriment int

	DECR key
	DECRBY key 8
->key-8

incriment int
	
	INCR key
	INCRBY key 3
	INCRBYFLOAT key 2.95
---
get multiple values at once

	MGET key1 key2 key3 ... 

set multiple values at once

	MSET key1 value1 key2 value2 ...
---
set if not exists

	SETNX key value 
	
set key if none of them exist, unless set none of them

	MSETNX key1 value1 key2 values2 ... 
	
set key with expire time in msec

	PSETEX key time-msec  value
	
chenge value from offset

	SETRANGE key offset value  
	
	old key = abc
	key 1 dfg
	new key = adfg
---
lenght

	STRLEN key
