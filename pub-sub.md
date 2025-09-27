https://redis.io/docs/latest/develop/pubsub/

- sub can recive a massage that has been send after subscribing that channel
- If no subscribers are in a channel, all sent messages will be lost

### send a massage to channel
    PUBLISH channel massage
    
### block a terminal to get massages from a channel
    SUBSCRIBE channel [channel ... ]
    UNSUBSCRIBE 

### regix pattern subscribe - subscribe every channel with certain pattern even if that channel hasnt created yet

    PSUBSCRIBE pattern
    PSUBSCRIBE o?n
### list of avable channels

    PUBSUB channels
