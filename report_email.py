#!/usr/bin/env python3

import os
import datetime
import reports
import emails


def process_description_files(path):
    content = ""
    descriptions_list = os.listdir(path)
    for description in descriptions_list:
        with open(description, "r") as opened:
            lines = opened.readlines()
        content += " name: {} \n weight: {} \n\n".format(lines[0], lines[1])
    return content


if __name__ == "__main__":
    date = datetime.date.today()
    title = "Processed Update on {}".format(date.strftime("%B %d, %Y"))
    content = process_description_files("/supplier-data/descriptions/")
    reports.generate_report("/tmp/processed.pdf", title, content)

    sender = "automation@example.com"
    receiver = "username@example.com"
    subject = "Upload Completed - Online Fruit Store"
    body = "All fruits are uploaded to our website succesfully. A detailed list is attached to this email."
    attachment = "/tmp/processed.pdf"

    message = emails.generate_email(sender, receiver, subject, body, attachment)
    emails.send_email(message)
