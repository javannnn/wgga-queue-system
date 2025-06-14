# wgga-queue-system

Queue management system for WGGA Eye Center

---

## 📦 Components

* **`backend/`**: Flask app (admin dashboard, Gize integration, REST API)
* **`pi-client/`**: Flask app for Raspberry Pi display screens (shows the live queue)
* **`kiosk/`**: Ticketing frontend (touch kiosk for patients)
* **`docs/`**: Proposals, workflow PDFs, project docs
* **`setup/`**: Scripts to install and run each component

---

## 🚦 System Highlights

* Real-time dashboard with **filtering** and **colored status badges**
* Pi client highlights the **first two patients (“Now Serving”)** in large text, includes a live clock
* Kiosk has big, touch-friendly buttons and dings when ticket is issued
* Works on your local network; remote access recommended via [Tailscale VPN](https://tailscale.com)

---

## 🛠️ 1. Prerequisites

* **Python 3.8+** installed on all systems
* **Git** installed to clone this repo
* (For Raspberry Pi): Raspbian OS, connected to LAN/Wi-Fi

---

## 🚀 2. Cloning the Repo

1. Open a terminal and run:

   git clone [https://github.com/javannnn/wgga-queue-system.git](https://github.com/javannnn/wgga-queue-system.git)
   cd wgga-queue-system

---

## 🖥️ 3. Backend Setup (Queue Server)

Steps (run on your main Ubuntu server):

```
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env  # configure credentials
nano .env             # fill in the real Gize API details if needed
python app.py
```

* Visit `http://<server-ip>:5000` from any browser on your LAN to see the dashboard.

---

## 🖨️ 4. Kiosk Setup (Ticketing Terminal)

On the kiosk touchscreen PC (or any other PC):

```
cd kiosk
python3 -m venv venv
source venv/bin/activate
pip install flask
python app.py
```

* Visit `http://<kiosk-ip>:7000` (use browser in full screen/touch mode).

---

## 📺 5. Raspberry Pi Display Setup

On each Raspberry Pi:

```
cd pi-client
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python main.py
```

* The Pi display will show the live queue.
* Edit `pi-client/main.py` to set your backend server’s IP if not `192.168.1.100`.

---

## 🌐 6. Enable Remote Access with Tailscale (Recommended)

Install [Tailscale](https://tailscale.com/download) on:

* The backend server
* Each Raspberry Pi
* Your laptop

Quick install:

```
curl -fsSL https://tailscale.com/install.sh | sh
sudo tailscale up
```

* Log in and now you can SSH or access dashboards securely from anywhere.

---

## 🔑 7. Configuration Notes

* **All config for Gize API** lives in `backend/.env`.
* **Firewall**: Allow ports `5000` (backend), `7000` (kiosk), `8000` (pi-client).
* **Static IPs**: Assign static LAN IPs for backend and Pis for reliability.
* **Auto-start on boot**: Use [systemd](https://www.freedesktop.org/software/systemd/man/systemd.service.html) or [pm2](https://pm2.keymetrics.io/) for production.

---

## 💡 Troubleshooting

* **Dashboard not updating?**
  Make sure backend is running and accessible from Pis/kiosks. Check logs (`backend.log`, `pi_client.log`, `kiosk.log`).
* **Can’t connect from Pi or kiosk?**
  Check firewalls and confirm you’re on the same LAN.
* **Printer not working?**
  Integrate real printer hardware in `kiosk/printer.py` (currently simulated).

---

## 👨‍💻 For Developers

* **Edit HTML/CSS** in `templates/` folders to adjust UI.
* **Test API**: Run `python -m unittest discover tests` (from project root) to run included test(s).

---

## 📝 Contact

For help, bug reports, or feature requests, open an issue on [GitHub](https://github.com/javannnn/wgga-queue-system/issues)
Or contact the Ace-Tech dev team.

---

Kick off your queue revolution—one patient at a time!
