# Port Scanner

A fast, lightweight, and efficient multi-threaded TCP port scanner written in Python. This tool utilizes a `ThreadPoolExecutor` to concurrently scan a range of target ports on a specified host, logging the results to both the console and a local log file.

## Features

* **Multi-Threaded Performance:** Utilizes up to 100 concurrent worker threads for fast and efficient port scanning.
* **Dual Logging:** Outputs clean, timestamped logs to both the terminal and `scan_result.log`.
* **Graceful Error Handling:** Handles unknown hosts, connection timeouts, and refused connections gracefully.

## Installation

Clone the repository:

```bash
git clone https://github.com/areeeesha/Syntecxhub-Port-Scanner.git
```

Move into the project folder:

```bash
cd Port-Scanner
```

---

## Running the Program

```bash
python port_scanner.py
```

Example:

```text
Enter the host to scan: scanme.nmap.org
Enter the starting port number: 20
Enter the ending port number: 100
```

---

## Output

Example:

```text
PORT 22: OPEN
PORT 23: CLOSED
PORT 80: OPEN
PORT 81: TIMEOUT
```

A complete log is also saved to:

```text
scan_result.log
```

---

This project is intended for educational purposes and was developed as part of a cybersecurity internship project at **Syntecxhub**.
