# Study_planner
A self-host study planner website
# study.service Management Guide

This document outlines the standard commands used to manage the `study.service` systemd service.

## Prerequisites

These commands generally require root/administrator privileges. Ensure you have `sudo` access or are logged in as a root user.

## Service Control

Use these commands to manage the current state of the service:

| Action | Command |
| :--- | :--- |
| **Start** | `sudo systemctl start study.service` |
| **Stop** | `sudo systemctl stop study.service` |
| **Restart** | `sudo systemctl restart study.service` |
| **Status** | `sudo systemctl status study.service` |

## Boot Configuration

Manage whether the service starts automatically when the system boots:

| Action | Command |
| :--- | :--- |
| **Enable (Start on boot)** | `sudo systemctl enable study.service` |
| **Disable (Manual start only)** | `sudo systemctl disable study.service` |

## Maintenance & Debugging

| Action | Command |
| :--- | :--- |
| **Reload Daemon** | `sudo systemctl daemon-reload` |
| **View Logs (Follow)** | `journalctl -u study.service -f` |

---

### Best Practices
* **After Modification:** If you modify the service file (e.g., changes in `/etc/systemd/system/study.service`), always run `sudo systemctl daemon-reload` to inform systemd of the changes.
* **Logs:** Using `journalctl -u study.service -f` is the most effective way to troubleshoot startup errors or runtime issues.
