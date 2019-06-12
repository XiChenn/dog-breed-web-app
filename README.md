# dog-breed-web-app
A web application to identify dog breeds

### port forward (80 -> 8888)
``` bash
iptables -t nat -A PREROUTING -p tcp --dport 80 -j REDIRECT --to-port 8888
```

### run with nohup
``` bash
nohub flask run --port=8888 host=0.0.0.0 &
```
