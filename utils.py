from flask_mail import Message
import os


def populate_email(lead):
  msg = Message(
    subject = "Follow up from today's chat",
    sender = os.getenv('EMAIL_USER'),
    recipients = [lead['email']],
    body = format_body(lead['first_name'])
  )
  working_dir = os.getcwd()
  with open(working_dir + "/test-presentation.pdf", "rb") as f:    
    msg.attach(
        filename = lead['company_name'].lower().replace(" ", "") + "-presentation-name.pdf",
        disposition = "attachment",
        content_type = "application/pdf",
        data = f.read()
    )
  return msg

def format_body(first_name):
  body = f"Hi {first_name},\n\nIt was great meeting you earlier today!\n\nI've attached the presentation that we spoke about. Please take a look and let me know what you think.\n\nBest,\nEitan"
  return body