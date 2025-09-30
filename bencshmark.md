https://redis.io/docs/latest/operate/oss_and_stack/management/optimization/benchmarks/
## Usage     
    redis-benchmark [-h <host>] [-p <port>] [-c <clients>] [-n <requests]> [-k <boolean>]

    options:
     -h <hostname>      Server hostname (default 127.0.0.1)
     -p <port>          Server port (default 6379)
     -s <socket>        Server socket (overrides host and port)
     -a <password>      Password for Redis Auth
     --user <username>  Used to send ACL style 'AUTH username pass'. Needs -a.
     -c <clients>       Number of parallel connections (default 50)
     -n <requests>      Total number of requests (default 100000)
     -d <size>          Data size of SET/GET value in bytes (default 3)
     --dbnum <db>       SELECT the specified db number (default 0)
     --threads <num>    Enable multi-thread mode.
     --cluster          Enable cluster mode.
     --enable-tracking  Send CLIENT TRACKING on before starting benchmark.
     -k <boolean>       1=keep alive 0=reconnect (default 1)
     -r <keyspacelen>   Use random keys for SET/GET/INCR, random values for
                        SADD, random members and scores for ZADD.
                        Using this option the benchmark will expand the string
                        __rand_int__ inside an argument with a 12 digits number
                        in the specified range from 0 to keyspacelen-1. The
                        substitution changes every time a command is executed.
                        Default tests use this to hit random keys in the
                        specified range.
     -P <numreq>        Pipeline <numreq> requests. Default 1 (no pipeline).
     -e                 If server replies with errors, show them on stdout.
                        (No more than 1 error per second is displayed.)
     -q                 Quiet. Just show query/sec values
     --precision        Number of decimal places to display in latency output (default 0)
     --csv              Output in CSV format
     -l                 Loop. Run the tests forever
     -t <tests>         Only run the comma separated list of tests. The test
                        names are the same as the ones produced as output.
     -I                 Idle mode. Just open N idle connections and wait.
     --help             Output this help and exit.
     --version          Output version and exit.

## 
