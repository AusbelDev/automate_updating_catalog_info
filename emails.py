#!/usr/bin/env python3

import email.message
from fileinput import filename
import mimetypes
import os.path
import smtplib
import ssl
import getpass

PORT = 465
CONTEXT = ssl.create_default_context()


def generate(sender, recipient, subject, body, attachment_path):
    """Creates an email with an attachment"""
    # * Basic Email formatting
    message = email.message.EmailMessage()
    message["From"] = sender
    message["To"] = recipient
    message["Subject"] = subject
    message.set_content(body)

    # * Process the attachment and add it to the email
    attachment_filename = os.path.basename(attachment_path)
    mime_type, _ = mimetypes.guess_type(attachment_path)
    mime_type, mime_subtype = mime_type.split("/", 1)

    with open(attachment_path, "rb") as ap:
        message.add_attachment(
            ap.read(),
            maintype=mime_type,
            subtype=mime_subtype,
            filename=attachment_filename,
        )

    return message


def send(message):
    """Sends the message to the configures SMTP server"""
    mail_server = smtplib.SMTP_SSL("smtp.gmail.com", port=PORT, context=CONTEXT)
    password = getpass.getpass("Introduce your password: ")
    mail_server.login("examplegmail.com", password)
    mail_server.send_message(message)
    mail_server.quit()
