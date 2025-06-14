# WGGA Queue System

This repository contains the source code, scripts, and documentation for the WGGA Eye Center Queue Management System. The project is composed of a Flask backend integrated with the Gize API, Raspberry Pi display clients, and touchscreen ticket kiosks.

## Queue Overview
1. **Ticketing (Kiosk)** – An anonymous numbered ticket is issued (e.g. `Q-101`). Options include Doctor, Refraction, or VIP. Once scanned at reception, the ticket expires.
2. **Reception Check-In** – The ticket is scanned and the patient's identity is created or matched in Gize. After this step, all queue handling is performed by name.
3. **Dashboard Management** – Nurses and reception staff call patients by name from a real-time dashboard. VIP and emergency overrides are supported.

