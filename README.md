# rootDDoS vX - Professional Network Stress Engine

An advanced, asynchronous Layer 7 and Direct IP stress testing utility developed for **Root404** operational security audits. This tool is designed to evaluate server resilience against high-concurrency request streams and bypass modern WAF/CDN mitigations.

## Key Features
* **Dual Operation Modes:** Support for both Domain-based (URL) and Direct IP targeting.
* **WAF/Cloudflare Bypass:** Integrated Headless Browser automation to solve JS challenges and capture valid session tokens.
* **Asynchronous Architecture:** High-performance I/O powered by `asyncio` and `aiohttp` for maximum request throughput.
* **Dynamic Proxy Injection:** Real-time proxy pool rotation to mitigate IP-based filtering.
* **Stealth Integration:** Utilizes stealth-evasion techniques to bypass anti-bot mechanisms.

## Installation
   ```bash
   git clone https://github.com/codewriter42/rootDDoS-vX.git
   cd rootDDoS-vX
   pip install -r requirements.txt
   playwright install chromium
```
Usage
Run the engine using Python:
```bash
python3 rootDDoS-vX.py
```
Select Mode 1 for URL targeting (includes Cloudflare Bypass).
Select Mode 2 for Direct IP targeting.
Paste your proxy list into the terminal and press CTRL+D (Linux/Termux) to commit.
Define the worker intensity.
*Legal Disclaimer
This tool is for educational purposes and authorized security testing only. The developers of Root404 are not responsible for any misuse or illegal activities conducted with this software.*
