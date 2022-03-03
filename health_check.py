#!/usr/bin/env python3

import emails
import psutil
import shutil
import socket

errors = [
    "Error - CPU usage is over 80%",
    "Error - Available disk space is less than 20%",
    "Error - Available memory is less than 500MB",
    "Error - localhost cannot be resolved to 127.0.0.1",
]

subject = None

while True:
    cpu = psutil.cpu_percent(60)
    disk_space = shutil.disk_usage("C:")
    disk_percentage = 100 - (disk_space.used / disk_space.total) * 100
    ram = psutil.virtual_memory()
    free_ram = ram.free / 1_000_000_000
    resolved = socket.gethostbyname("localhost")

    if cpu > 80:
        subject = errors[0]
    if disk_percentage < 20:
        subject = errors[1]
    if free_ram < 0.5:
        subject = errors[2]
    if resolved != "127.0.0.1":
        subject = errors[3]

    if subject is not None:
        sender = "automation@example.com"
        receiver = "username@example.com"
        body = "Please check your system and resolve the issue as soon as possible"

        message = emails.generate(sender, receiver, subject, body)
        emails.send(message)
        subject = None
