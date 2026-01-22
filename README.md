IP-LOCATOR
Introduction
IP-LOCATOR is a lightweight tool for determining the geographical location and network details of any IP address. It helps developers, security analysts, and system administrators quickly inspect IP information during debugging, monitoring, and investigation tasks. The project focuses on simplicity, fast responses, and an approachable interface for both beginners and advanced users.

Features
IP-LOCATOR offers a focused set of capabilities designed around everyday IP lookup workflows. You can use it interactively or script it into automated jobs.

Lookup geolocation data for IPv4 and IPv6 addresses
Display country, region, city, ZIP or postal code, and coordinates
Show ISP, ASN, hostname, and connection details when supported by the provider
Provide timezone and local time information for the resolved location
Use it from the command line with simple arguments and flags
Import it as a Python module in your own scripts and tools
Support batch lookups from files for repetitive investigations
Allow easy replacement of the underlying geolocation provider
Requirements
Before installing or running IP-LOCATOR, verify that your system satisfies these basic requirements. These keep the tool predictable and avoid common environment issues.

Python 3.7 or higher installed and available in your PATH
pip or another Python package manager for dependency installation
Internet connection for online geolocation lookups using APIs
Access to a supported geolocation API service or database
Operating system support for running Python scripts on your machine
If you use a provider that requires authentication, you also need a valid API key. Some providers offer free tiers with daily or monthly limits.

Installation
You install IP-LOCATOR like a typical Python-based CLI tool from source. These steps assume a standard development environment with git and Python.

Clone this repository:
git clone https://github.com/Anymshacker047/IP-LOCATOR.git
cd IP-LOCATOR
(Recommended) Create and activate a virtual environment:
python -m venv .venv
source .venv/bin/activate   # On Windows use: .venv\Scripts\activate
Install the required dependencies:
pip install -r requirements.txt
(Optional) Install the package in editable mode for easier imports:
pip install -e .
After installation, test the script once with a known public IP to confirm everything works. This also validates your network access and provider configuration.

Usage
You can use IP-LOCATOR as a command-line tool for quick checks or import it into Python scripts. Both approaches rely on the same underlying lookup logic.

Command-Line Interface
The CLI is ideal for ad‑hoc queries and shell scripting. It accepts a single IP, multiple IPs, or a file containing many IPs.

Lookup a single IP address:
python ip_locator.py 8.8.8.8
Lookup multiple IP addresses:
python ip_locator.py 8.8.8.8 1.1.1.1
Lookup multiple IP addresses from a file:
python ip_locator.py -f ip_list.txt
Show help and available options:
python ip_locator.py -h
Typical output includes IP, country, region, city, coordinates, ISP, and timezone. Exact fields depend on the configured provider and its response schema.

Python Module
The Python interface integrates IP-LOCATOR into your own automation scripts and applications. You can use it inside data pipelines, monitoring agents, or web services.

from ip_locator import locate_ip

ip = "8.8.8.8"
result = locate_ip(ip)

print("IP:", result.ip)
print("Country:", result.country)
print("City:", result.city)
print("Latitude:", result.latitude)
print("Longitude:", result.longitude)
You can also call the lookup function in loops for batch processing. In that case, consider implementing rate limiting or caching to respect provider limits.

Contributing
Contributions help keep IP-LOCATOR reliable, flexible, and up to date with provider changes. Bug reports, feature suggestions, and documentation improvements are all valuable.

To contribute code:

Fork the repository to your own GitHub account
Create a feature branch for your change
Implement your changes with clear, focused commits
Add or update tests when you change behaviour
Run tests and linters before opening a pull request
Open a pull request with a clear description and motivation
If you find issues with provider responses or edge cases, include example IPs or anonymised logs. This helps maintainers reproduce and fix problems quickly.

License
This project is licensed under the MIT License. You may use, copy, modify, merge, publish, distribute, sublicense, and sell copies of the software under the license terms.

MIT License

Copyright (c) 2026 Manas Dhingra

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "https://github.com/anymshacker047/IP-LOCATOR"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
