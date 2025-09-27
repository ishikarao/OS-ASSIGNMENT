# OS Lab Python Scripts

This repository contains Python scripts that demonstrate core process management concepts using the `os` module and related techniques in Python. These scripts correspond to university-level Operating Systems lab assignments.

---

## Scripts Overview

- **Process Creation Utility:**  
  Creates N child processes, printing each child’s PID, parent PID, and a custom message. The parent waits for each child to finish.

- **Linux Command Execution in Child:**  
  Each child process runs a specified Linux command (like `ls`, `date`, `ps`) using `os.execvp` or `subprocess.run`, illustrating exec-based process replacement.

- **Zombie and Orphan Processes:**  
  Demonstrates zombies (parent skips `wait()`) and orphans (parent exits before child). Observing system processes using `ps -el | grep defunct` is shown.

- **Process Information Inspector:**  
  For any given PID, prints process name, state, memory usage, executable path, and open file descriptors using data from the `/proc` filesystem.

- **Process Prioritization:**  
  Spawns several CPU-bound child processes with differing `nice` values to illustrate Linux scheduling and process priorities.

---

## Requirements

- Python 3.x
- Linux OS (for process-related features and `/proc` access)
- Only standard Python library modules used

---

## How To Run

1. **Clone the repository**

2. **Run scripts as needed**

Each script will prompt for inputs such as the number of processes, PID to inspect, or the Linux command to execute.

---



