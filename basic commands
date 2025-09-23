redis-cli

connect to remote host
	redis-cli -h [ip] -p [post] -a [password]

SET key value
	->OK
set key value EX time-to-expire
GET key
	->value
GETRANGE key start-index end-index : usefull for something like strings
GETSET key value : set new value and return old value

DEL key1 key2 key3 ...
	->number of deleted keys
EXIST key1 key2 key3 ...
	->number of existed keys - counts same keys

EXPIRE key time-sec : set expire time for key
TTL key : time to live

KEYS regex
KEYS *
	all keys

PERSIS key : undo EXPIRE

RANDOMKEY
	-> random-key
RENANE key newkey
	->OK

APPEND key value

DECR key : decriment int
DECRBY key 8
	->key-8
INCR key
INCRBY key 3
INCRBYFLOAT key 2.95

MGET key1 key2 key3 ... : get multiple values at once
MSET key1 value1 key2 value2 ... : set multiple values at once

SETNX key value : set if not exists
MSETNX key1 value1 key2 values2 ... : set key if none of them exist, unless set none of them
PSETEX key time-msec  value : set key with expire time in msec

SETRANGE key offset value : chenge value from offset
	old key = abc
	key 1 dfg
	new key = adfg

STRLEN key
