#!/usr/bin/env python3
"""
Uptime Kuma Pinger - Reports ping times to Uptime Kuma server
"""
import os
import sys
import time
import logging
import urllib.request
import urllib.error

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def main():
    uptime_kuma_url = os.getenv('UPTIME_KUMA_URL')
    ping_interval = int(os.getenv('PING_INTERVAL', '60'))
    
    if not uptime_kuma_url:
        logger.error("UPTIME_KUMA_URL environment variable is not set")
        sys.exit(1)
    
    logger.info(f"Starting Uptime Kuma Pinger")
    logger.info(f"URL: {uptime_kuma_url}")
    logger.info(f"Interval: {ping_interval}s")
    
    while True:
        try:
            start_time = time.time()
            req = urllib.request.Request(uptime_kuma_url)
            response = urllib.request.urlopen(req, timeout=10)
            elapsed_ms = int((time.time() - start_time) * 1000)
            
            if response.status == 200:
                logger.info(f"Ping successful - {elapsed_ms}ms")
            else:
                logger.warning(f"Ping returned status {response.status} - {elapsed_ms}ms")
            response.close()
                
        except urllib.error.HTTPError as e:
            elapsed_ms = int((time.time() - start_time) * 1000)
            logger.warning(f"HTTP error {e.code} - {elapsed_ms}ms")
        except urllib.error.URLError as e:
            logger.error(f"Connection error: {e.reason}")
        except Exception as e:
            logger.error(f"Error: {e}")
        
        time.sleep(ping_interval)


if __name__ == '__main__':
    main()
