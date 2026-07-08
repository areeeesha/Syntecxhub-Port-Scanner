import socket 
import logging
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime

# Log Creation
logging.basicConfig(
    level = logging.INFO, 
    format = "%(asctime)s - %(message)s", 
    handlers = [logging.FileHandler("scan_result.log"), logging.StreamHandler()]
)

# Port Scanner
def scan_port(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1.0)
    try:
        s.connect((host, port))
        logging.info(f'PORT {port}: OPEN')
    except ConnectionRefusedError:
        logging.info(f'PORT {port}: CLOSED')
    except socket.timeout:
        logging.info(f'PORT {port}: TIMEOUT')
    except socket.error as e:
        logging.info(f'PORT{port}: ERROR ({e})')
    finally:
        s.close()

# Main Function
def main():
    host = input("Enter the host to scan: ")
    try:
        ip = socket.gethostbyname(host)
    except socket.gaierror:
        logging.error(f'Could not resolve host: {host}')
        return
    
    start = int(input("Enter the starting port number: "))
    end = int(input("Enter the ending port number: "))

    logging.info(f"Starting scan on {host} ({ip}) — ports {start}-{end}")
    logging.info(f"Scan started at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    ports = range(start, end + 1)
    with ThreadPoolExecutor(max_workers=100) as executor:
        executor.map(lambda p: scan_port(host, p), ports)

    print("Port scanning completed.")

if __name__ == "__main__":
    main()