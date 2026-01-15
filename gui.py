import tkinter as tk
from tkinter import messagebox, scrolledtext
import requests
from payloads import sql_payloads, xss_payloads

def save_report(content):
    with open("security_report.txt", "w") as file:
        file.write(content)


# ------------------------
# Security Testing Logic
# ------------------------

def test_sql_injection(url, param, output_box):
    output_box.insert(tk.END, "\n[+] Testing SQL Injection...\n")
    vulnerable = False

    for payload in sql_payloads:
        test_url = f"{url}?{param}={payload}"
        try:
            response = requests.get(test_url, timeout=5)
            if "sql" in response.text.lower() or "error" in response.text.lower():
                output_box.insert(tk.END, f"[!] Possible SQL Injection with payload: {payload}\n")
                vulnerable = True
        except:
            output_box.insert(tk.END, "[!] Connection error while testing SQL Injection\n")

    if not vulnerable:
        output_box.insert(tk.END, "[-] No SQL Injection detected.\n")


def test_xss(url, param, output_box):
    output_box.insert(tk.END, "\n[+] Testing XSS...\n")
    vulnerable = False

    for payload in xss_payloads:
        test_url = f"{url}?{param}={payload}"
        try:
            response = requests.get(test_url, timeout=5)
            if payload in response.text:
                output_box.insert(tk.END, f"[!] Possible XSS with payload: {payload}\n")
                vulnerable = True
        except:
            output_box.insert(tk.END, "[!] Connection error while testing XSS\n")

    if not vulnerable:
        output_box.insert(tk.END, "[-] No XSS detected.\n")


# ------------------------
# Button Click Function
# ------------------------

def start_scan():
    url = entry_url.get()
    param = entry_param.get()

    if not url or not param:
        messagebox.showerror("Error", "Please enter both URL and Parameter")
        return

    output_box.delete("1.0", tk.END)
    output_box.insert(tk.END, "=== Web Application Security Testing Tool ===\n")
    output_box.insert(tk.END, f"Target: {url}\nParameter: {param}\n\n")

    test_sql_injection(url, param, output_box)
    test_xss(url, param, output_box)

    output_box.insert(tk.END, "\nScan completed!\n")

    # ----------------
    # Save report
    # ----------------
    report_content = output_box.get("1.0", tk.END)
    save_report(report_content)

    messagebox.showinfo("Report Saved", "Security report saved as security_report.txt")



# ------------------------
# GUI Layout
# ------------------------

app = tk.Tk()
app.title("Web Security Testing Tool")
app.geometry("700x500")

# Labels
tk.Label(app, text="Target URL").pack()
entry_url = tk.Entry(app, width=80)
entry_url.pack()

tk.Label(app, text="Parameter Name").pack()
entry_param = tk.Entry(app, width=40)
entry_param.pack()

# Button
tk.Button(app, text="Start Scan", command=start_scan).pack(pady=10)

# Output Box
output_box = scrolledtext.ScrolledText(app, width=85, height=20)
output_box.pack()

# Run App
app.mainloop()
