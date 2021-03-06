# **DOS TOOLS**

Python scripts for Denial of Service Attacks

<hr>

## **DOS**


A Denial Of Service attack is a cyber attack which targets a network or machineinorder to take it down making it inaccessible for intended users.

**Working**

In this attack, mutiple web sockets are created and all these sockets send requests tothe targeted host on its specified port

**Prevention**

Supervise traffic via a firewall, monitor traffic

**How to try it out**

- Create an apache2 server listening on a particular ip and host
- On openning a browser you will see it load pretty immediately and serve the required webpage
- Now DOS this host and port
- You will observe that this network is heavily crowded and can observe the browser buffering

**USE WISELY! DO NOT DOS NETWORKS AND MACHINES YOU DO NOT HAVE CONTROL OVER!**

```
usage: python dos.py [-h] [-p PORT] [-s SOCKETS] [-t TIMEOUT] [host]

positional arguments:
  host                  Host IP to DoS attack

options:
  -h, --help            show this help message and exit
  -p PORT, --port PORT
  -s SOCKETS, --sockets SOCKETS
  -t TIMEOUT, --timeout TIMEOUT
```

<hr>

## **SLOWLORIS DOS**

A Slowloris Denial Of Service attack is a cyber attack which targets a network or machineinorder to take down another machine's web server with minimal bandwidth

**Working**

In this attack, mutiple web sockets are created and trie to keep as many ofthese connections to the target web server open as long as possible

**Prevention**

Set an absolute connection timeout,Limit the header and message body to a minimal reasonable length

**How to try it out**

- Create an apache2 server listening on a particular ip and host
- On openning a browser you will see it load pretty immediately and serve the required webpage
- Now Slowloris DOS this host and port
- You will observe that this network is heavily crowded and can observe the browser buffering

**USE WISELY! DO NOT DOS NETWORKS AND MACHINES YOU DO NOT HAVE CONTROL OVER!**

```
usage: python slowloris.py [-h] [-p PORT] [-s SOCKETS] [host]

positional arguments:
  host                  Host IP to slowloris DoS

options:
  -h, --help            show this help message and exit
  -p PORT, --port PORT
  -s SOCKETS, --sockets SOCKETS
```