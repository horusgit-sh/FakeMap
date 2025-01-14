import socket
import argparse
import ipaddress
from concurrent.futures import ThreadPoolExecutor

class Scan:
    def port_scanner(target, portR):
        try:
            s = socket.socket()
            s.settimeout(0.5)
            s.connect((target, portR))
            print(f"{portR} - open")
        except:
            pass
        finally:
            s.close()

    def OnePortScanner(target, port):
        try:
            s = socket.socket()
            s.settimeout(0.5)
            s.connect((target, port))

            print(f"{port} - open ")
        except:
            print(f"{port} - close")
        finally:
            s.close()

    def BasicPorts(target):
        ports = [80, 23, 443, 21, 22, 25, 3389, 110, 445, 139, 143, 53, 135, 3306, 8080, 1723, 111, 995, 993, 5900, 1025, 587, 8888, 199, 1720, 465, 548, 113, 81, 6001, 10000, 514, 5060, 179, 1026, 2000, 8443, 8000, 32768, 554, 26, 1433, 49152, 2001, 515, 8008, 49154, 1027, 5666, 646, 5000, 5631, 631, 49153, 8081, 2049, 88, 79, 5800, 106, 2121, 1110, 49155, 6000, 513, 990, 5357, 427, 49156, 543, 544, 5101, 144, 7, 389, 8009, 3128, 444, 9999, 5009, 7070, 5190, 3000, 5432, 1900, 3986, 13, 1029, 9, 5051, 6646, 49157, 1028, 873, 1755, 2717, 4899, 9100, 119, 37]
        for port in ports:
          try:
              s = socket.socket()
              s.settimeout(0.5)
              s.connect((target, port))

              print(f"{port} - open ")


          except:
              pass
          finally:
              s.close()

    def threaded(target, port_range, max_threads=1000):
        start, end = port_range
        with ThreadPoolExecutor(max_threads) as executor:
            for port in range(start, end + 1):
                executor.submit(Scan.port_scanner, target, port)

    def is_valid_ip(target):
        try:
            ipaddress.ip_address(target)
            return True
        except ValueError:
            return False


## timeouts


def main():

    def printWelcome():
        print("\033[1;32m")
        print(""" 
       _____     _        __  __             
      |  ___|_ _| | _____|  \/  | __ _ _ __  
      | |_ / _` | |/ / _ \ |\/| |/ _` | '_ \ 
      |  _| (_| |   <  __/ |  | | (_| | |_) |
      |_|  \__,_|_|\_\___|_|  |_|\__,_| .__/ 
                                      |_|   
     """)
        print("***************************************************")
        print("*                 Welcome to FakeMap              *")
        print("*    Enter a IP address to enumerate open ports   *")
        print("*         Type --help for see all features        *")
        print("***************************************************")

    printWelcome()


    parser = argparse.ArgumentParser(description="Discover open ports")
    parser.add_argument('-t', '--target', type=str, help="Set target IP address")
    parser.add_argument('-p', '--port', type=int, help="Set one port for scanning (e.g. 8080)")
    parser.add_argument('-r', '--portrange',nargs=2, type=int, help="Set range for scanning (e.g. 1,1024)")
    parser.add_argument('-b', '--basic', action="store_true", help="Perform scan with basic ports (21, 22, 80 etc.)")

    args = parser.parse_args()

    target = args.target
    portRangeInput = args.portrange
    port1 = args.port


    if not target:
        print("Error! Target IP address is required. Use --help for usage.")
        return


    if not Scan.is_valid_ip(target):
        print("Your IP address is invalid!")
        return


    if args.portrange:
        start, end = args.portrange
        if start > end or start < 1:
            print("Invalid port range!")
            return
        print(f"Scanning ports from {start} to {end} on {target}...")
        Scan.threaded(target, (start, end))


    if args.basic:
        print(f"Scanning {target} in basic port range: ")
        Scan.BasicPorts(target)

    if args.port:
        print(f"Scanning port {port1} state...")
        Scan.OnePortScanner(target, port1)




if __name__ == "__main__":
    main()






