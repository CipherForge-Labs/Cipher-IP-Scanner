[![CodeQL](https://github.com/CipherForge-Labs/Cipher-IP-Scanner/actions/workflows/github-code-scanning/codeql/badge.svg)](https://github.com/CipherForge-Labs/Cipher-IP-Scanner/actions/workflows/github-code-scanning/codeql)
[![Dependency review](https://github.com/CipherForge-Labs/Cipher-IP-Scanner/actions/workflows/dependency-review.yml/badge.svg)](https://github.com/CipherForge-Labs/Cipher-IP-Scanner/actions/workflows/dependency-review.yml)
# CipherForge IP Scanner

## Overview

The CipherForge IP Scanner is a Python-based tool for scanning major ports of a given IP or domain. It includes features such as UDP scanning, geolocation lookup, and detailed summaries of open ports and their associated services.

---

## Features
- **Major Port Scanning**: Scans commonly used ports by default.
- **UDP Support**: Option to scan UDP ports with the `-u` flag.
- **Custom Ranges**: Specify port ranges to scan using arguments.
- **Geolocation**: Displays geolocation data for the target IP address.
- **Summarized Output**: Provides service names and open port summaries.

---

## Requirements

- **Python Version**: 3.12.*
- **Dependencies**: Install the required Python packages listed in `requirements.txt`.

---

## Installation and Usage

### 1. Clone the Repository
```bash
git clone https://github.com/CipherForge-Labs/CipherForge-IP-Scanner.git
cd CipherForge-IP-Scanner
```

### 2. Install Python 3.12.*
Make sure Python 3.12.* is installed on your system. You can download it from the official [Python website](https://www.python.org/downloads/).

### 3. Create and Activate a Virtual Environment
```bash
python3.12 -m venv .venv
source .venv/bin/activate   # On Linux/Mac
.\.venv\Scripts\activate    # On Windows
```

### 4. Install Dependencies
Run the following command to install the required libraries:
```bash
pip install -r requirements.txt
```

### 5. Run the Scanner
```bash
python main.py <target> [options]
```

---

## Examples

### Scan Default Major Ports
```bash
python main.py example.com --summary
```

### Scan with UDP Support
```bash
python main.py example.com -u --summary
```

### Scan a Custom Range
```bash
python main.py example.com -p 1-1000 --summary
```

---

## Requirements File (`requirements.txt`)

```plaintext
argparse==1.4.0
requests==2.31.0
geoip2==4.7.0
```

---

## Contributing
Contributions are welcome! Please open an issue or submit a pull request.

---

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

