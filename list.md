
create list

  LPUSH mylist 'hello' #left push
  RPUSH mylist 'world' #right push

  LRANGE mylist 0 -1

-> 1) 'hello'
-> 2) 'world'
