
# to install

```
go get github.com/xtaci/kcptun/client
go get github.com/xtaci/kcptun/server
```

- instructions: https://github.com/xtaci/kcptun/blob/master/README.en.md
    - lots of params to play with

## on example server

```
server -t "localhost:9900"  -l ":4000" -mode fast2 --key '7454' --parityshard 2
```

## on example client
```
client -r 94.23.38.89:4000 -l ":9900" -mode fast2 --key '7454' --parityshard 2
```

- 94.23.38.89 is the server addr where the proxy is hosted
- 4000 is the udp port on the server (make sure no firewall is blocking it)

# here we did example of polipo proxy

- [polipo.cfg]

# to test performance

- fast.com
- http://www.speedtest.net/nl/