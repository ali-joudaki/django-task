import logging
from dataclasses import dataclass
from datetime import datetime

from celery import shared_task

from user_management.models import Manager


@shared_task
def send_sms(message_body):
    try:
        manager_user_objects = Manager.objects.all()
        for staff in manager_user_objects:
            phone_number = staff.phone
            sms = SMS(phone_number, message_body)
            logging.info(f'Sending {message_body} to {phone_number}')
            sms.send()
            logging.info(f'Message sent successfully to: {staff.user.username}')
        logging.info(f"SMS task done in: {datetime.utcnow()}")
    except Exception as e:
        logging.error(f"Failed to send SMS due to error: {e}")


@dataclass
class SMS:
    phone_number: str
    message: str

    def send(self):
        logging.info(f'Sending {self.message} to {self.phone_number}')
