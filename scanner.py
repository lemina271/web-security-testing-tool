import requests
from payloads import sql_payloads, xss_payloads

def test_sql_injection(url, param):
    print("\n[+] Testing SQL Injection...")
    vulnerable = False

    for payload in sql_payloads:
        test_url = f"{url}?{param}={payload}"
        response = requests.get(test_url)

        if "sql" in response.text.lower() or "error" in response.text.lower():
            print(f"[!] Possible SQL Injection found with payload: {payload}")
            vulnerable = True

    if not vulnerable:
        print("[-] No SQL Injection detected.")


def test_xss(url, param):
    print("\n[+] Testing XSS...")
    vulnerable = False

    for payload in xss_payloads:
        test_url = f"{url}?{param}={payload}"
        response = requests.get(test_url)

        if payload in response.text:
            print(f"[!] Possible XSS found with payload: {payload}")
            vulnerable = True

    if not vulnerable:
        print("[-] No XSS detected.")


def main():
    print("=== Web Application Security Testing Tool ===")
    url = input("Enter target URL (example: http://testphp.vulnweb.com/search.php): ")
    param = input("Enter parameter name (example: search): ")

    test_sql_injection(url, param)
    test_xss(url, param)

    print("\nScan completed!")


if __name__ == "__main__":
    main()
