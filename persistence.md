https://redis.io/docs/latest/operate/oss_and_stack/management/persistence/


## Redis Database - RDB
### where does RDB store 
    CONFIG GET dir
    -> /var/lib/redis

    # default file name : dump.rdb

### save a backup
    SAVE

### background save
    BGSAVE

### Auto backup routin


    CONFIG GET SAVE

    ->
    1) "save"
    2) "3600 1 300 100 60 10000"

- every 3600 sec if 1 key changed
- every 300 sec if 100 key changed
- every 60 sec if 10000 key changed

 #### it is also in redis config file

 ---
 ## Append only file - AOF

### is AOF active
    CONFIG GET APPENDONLY

### backup routin
    CONFIG GET appendsync
    ->
    1) appendsunc
    2) everysec

    
    
     
     
