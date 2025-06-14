# wgga-queue-system

Queue management system for WGGA Eye Center

## Components

- `backend/`: Flask app with dashboard, Gize integration, REST API
- `pi-client/`: Flask app for Raspberry Pi display screens (fetches live queue)
- `kiosk/`: Ticketing frontend (kiosk) for patient arrival
- `docs/`: Proposals, workflow PDFs
- `setup/`: Scripts for install and deployment

## Quick Start (Dev)

### Backend
```bash
cd backend
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env  # configure credentials
python app.py
```

### Pi Client
```bash
cd pi-client
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
python main.py
```

### Kiosk
```bash
cd kiosk
python3 -m venv venv && source venv/bin/activate
pip install flask
python app.py
```

### Gize API Integration
Configure `backend/.env` with the correct endpoint and credentials.

Tailscale is recommended for remote admin access.

System auto-updates queue displays and dashboard every 5 seconds.
