from urllib.parse import urlparse

import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

from .setup import log, print

# Dealing with SSL Warnings
try:
    import requests.packages.urllib3
    requests.packages.urllib3.disable_warnings()
except Exception:
    pass


def requests_retry_session(
    retries=3,
    backoff_factor=0.3,
    status_forcelist=(500, 502, 504, 503, 403),
    session=None,
    proxy=None,
):
    session = session or requests.Session()
    retry = Retry(
        total=retries,
        read=retries,
        connect=retries,
        backoff_factor=backoff_factor,
        status_forcelist=status_forcelist,
    )
    adapter = HTTPAdapter(max_retries=retry)
    session.mount("http://", adapter)
    session.mount("https://", adapter)
    
    if proxy:
        session.proxies = {"http": proxy, "https": proxy}
    
    return session
