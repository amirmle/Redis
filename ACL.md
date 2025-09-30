https://redis.io/docs/latest/operate/oss_and_stack/management/security/acl/

list of users

    ACL LIST
    -> 1) "user default on nopass ~* &* +@all"

set a user


    ACL SETUSER <name>
    ACL SETUESR amir
    
    ACL SETUSER amir on
    
    ACL SETUSER ><password>
    ACL SETUSER >123
    ACL GENPASS  # creates some password

login with user
    
    ACL WHOAMI
    AUTH <name> <password>


All commands are grouped into categories

    ACL CAT
    ->
     1) "keyspace"
     2) "read"
     3) "write"
     4) "set"
     5) "sortedset"
     6) "list"
     7) "hash"
     8) "string"
     9) "bitmap"
    10) "hyperloglog"
    11) "geo"
    12) "stream"
    13) "pubsub"
    14) "admin"
    15) "fast"
    16) "slow"
    17) "blocking"
    18) "dangerous"
    19) "connection"
    20) "transaction"
    21) "scripting"

get all commands in a caregory

    ACL CAT list
    ->
     1) "sort"
     2) "blmove"
     3) "rpop"
     4) "sort_ro"
     5) "lmove"
     6) "lpos"
     7) "rpoplpush"
     8) "lrange"
     9) "lpush"
    10) "rpush"
    11) "brpop"
    12) "brpoplpush"
    13) "llen"
    14) "lmpop"
    15) "linsert"
    16) "ltrim"
    17) "lrem"
    18) "rpushx"
    19) "lindex"
    20) "blpop"
    21) "blmpop"
    22) "lpop"
    23) "lset"
    24) "lpushx"    
