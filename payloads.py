# SQL Injection test payloads
sql_payloads = [
    "' OR '1'='1",
    "' OR 1=1--",
    "\" OR \"1\"=\"1"
]

# XSS test payloads
xss_payloads = [
    "<script>alert('XSS')</script>",
    "<img src=x onerror=alert(1)>"
]
