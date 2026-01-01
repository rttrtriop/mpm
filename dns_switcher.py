from flask import Flask
import subprocess

app = Flask(__name__)

# Флаг состояния
dns_active = False

def set_dns(state):
    if state:
        # Включаем DNS (SkyDNS)
        subprocess.run(["sudo", "chattr", "-i", "/etc/resolv.conf"])
        with open("/etc/resolv.conf", "w") as f:
            f.write("nameserver 176.99.11.77\nnameserver 80.78.247.254\n")
        subprocess.run(["sudo", "chattr", "+i", "/etc/resolv.conf"])
        print("DNS Xbox ON")
    else:
        # Возвращаем стандарт (например, Google)
        subprocess.run(["sudo", "chattr", "-i", "/etc/resolv.conf"])
        with open("/etc/resolv.conf", "w") as f:
            f.write("nameserver 8.8.8.8\n")
        print("DNS Standard ON")

@app.route('/toggle')
def toggle():
    global dns_active
    dns_active = not dns_active
    set_dns(dns_active)
    return "ON" if dns_active else "OFF"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
