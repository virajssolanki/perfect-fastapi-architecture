import logging
from datetime import datetime, timedelta
from pathlib import Path
from typing import Any, Dict, Optional

import emails
from emails.template import JinjaTemplate
from jose import jwt

from app.core.config import settings

from smtplib import SMTP
from email.message import EmailMessage

from app.core.config import get_app_settings

settings = get_app_settings()



# class Mailer:
#     @staticmethod
#     def send_message(content: str, subject: str, mail_to: str):
#         message = EmailMessage()
#         message.set_content(content)
#         message['Subject'] = subject
#         message['From'] = settings.MAIL_SENDER
#         message['To'] = mail_to
#         SMTP(settings.SMTP_SERVER).send_message(message)

#     @staticmethod
#     def send_confirmation_message(token: str, mail_to: str):
#         confirmation_url = '{}{}/auth/verify/{}'.format(settings.BASE_URL, settings.API_PREFIX, token)
#         message = '''Hi!

# Please confirm your registration: {}.'''.format(confirmation_url)
#         Mailer.send_message(
#             message,
#             'Please confirm your registration',
#             mail_to
#         )



# def send_email(
#     email_to: str,
#     subject_template: str = "",
#     html_template: str = "",
#     environment: Dict[str, Any] = {},
# ) -> None:
#     assert settings.EMAILS_ENABLED, "no provided configuration for email variables"
#     message = emails.Message(
#         subject=JinjaTemplate(subject_template),
#         html=JinjaTemplate(html_users_routertemplate),
#         mail_from=(settings.EMAILS_FROM_NAME, settings.EMAILS_FROM_EMAIL),
#     )
#     smtp_options = {"host": settings.SMTP_HOST, "port": settings.SMTP_PORT}
#     if settings.SMTP_TLS:
#         smtp_options["tls"] = True
#     if settings.SMTP_USER:
#         smtp_options["user"] = settings.SMTP_USER
#     if settings.SMTP_PASSWORD:
#         smtp_options["password"] = settings.SMTP_PASSWORD
#     response = message.send(to=email_to, render=environment, smtp=smtp_options)
#     logging.info(f"send email result: {response}")


# def send_test_email(email_to: str) -> None:
#     project_name = settings.PROJECT_NAME
#     subject = f"{project_name} - Test email"
#     with open(Path(settings.EMAIL_TEMPLATES_DIR) / "test_email.html") as f:
#         template_str = f.read()
#     send_email(
#         email_to=email_to,
#         subject_template=subject,
#         html_template=template_str,
#         environment={"project_name": settings.PROJECT_NAME, "email": email_to},
#     )


# def send_reset_password_email(email_to: str, email: str, token: str) -> None:
#     project_name = settings.PROJECT_NAME
#     subject = f"{project_name} - Password recovery for user {email}"
#     with open(Path(settings.EMAIL_TEMPLATES_DIR) / "reset_password.html") as f:
#         template_str = f.read()
#     server_host = settings.SERVER_HOST
#     link = f"{server_host}/reset-password?token={token}"
#     send_email(
#         email_to=email_to,
#         subject_template=subject,
#         html_template=template_str,
#         environment={
#             "project_name": settings.PROJECT_NAME,
#             "username": email,
#             "email": email_to,
#             "valid_hours": settings.EMAIL_RESET_TOKEN_EXPIRE_HOURS,
#             "link": link,
#         },
#     )


# def send_new_account_email(email_to: str, username: str, password: str) -> None:
#     project_name = settings.PROJECT_NAME
#     subject = f"{project_name} - New account for user {username}"
#     with open(Path(settings.EMAIL_TEMPLATES_DIR) / "new_account.html") as f:
#         template_str = f.read()
#     link = settings.SERVER_HOST
#     send_email(
#         email_to=email_to,
#         subject_template=subject,
#         html_template=template_str,
#         environment={
#             "project_name": settings.PROJECT_NAME,
#             "username": username,
#             "password": password,
#             "email": email_to,
#             "link": link,
#         },
#     )


# def generate_password_reset_token(email: str) -> str:
#     delta = timedelta(hours=settings.EMAIL_RESET_TOKEN_EXPIRE_HOURS)
#     now = datetime.utcnow()
#     expires = now + delta
#     exp = expires.timestamp()
#     encoded_jwt = jwt.encode(
#         {"exp": exp, "nbf": now, "sub": email}, settings.SECRET_KEY, algorithm="HS256",
#     )
#     return encoded_jwt


# def verify_password_reset_token(token: str) -> Optional[str]:
#     try:
#         decoded_token = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
#         return decoded_token["email"]
#     except jwt.JWTError:
#         return None
