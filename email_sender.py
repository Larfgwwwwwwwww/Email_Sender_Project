import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import argparse

def send_email(sender_email, sender_password, receiver_email, subject, html_body, image_path):
    print("Начало функции send_email")
    """
    Отправляет email с HTML-содержимым и прикрепленным изображением.

    Args:
        sender_email (str): Email отправителя.
        sender_password (str): Пароль отправителя.
        receiver_email (str): Email получателя.
        subject (str): Тема письма.
        html_body (str): HTML-тело письма.
        image_path (str): Путь к файлу изображения.
    """

    message = MIMEMultipart("related")
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject

    # Создание HTML-части сообщения
    html_part = MIMEText(html_body, "html")
    message.attach(html_part)

    # Прикрепление изображения
    try:
        with open(image_path, 'rb') as img_file:
            print(f"Файл изображения открыт: {image_path}")
            image = MIMEImage(img_file.read())
            image.add_header('Content-ID', '<123456789>')  # Указываем Content-ID
            message.attach(image)
    except FileNotFoundError:
        print(f"Ошибка: Изображение не найдено по пути: {image_path}")
        return

    # Отправка email
    context = ssl.create_default_context()
    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:  # Используем Gmail SMTP
            server.login(sender_email, sender_password)
            server.send_message(message)
        print(f"Письмо успешно отправлено на {receiver_email}")
    except Exception as e:
        print(f"Ошибка отправки письма: {e}")


def main():
    parser = argparse.ArgumentParser(description="Отправляет email с HTML и изображением.")
    parser.add_argument("sender_email", help="Email отправителя")
    parser.add_argument("sender_password", help="Пароль отправителя")
    parser.add_argument("receiver_email", help="Email получателя")
    parser.add_argument("subject", help="Тема письма")
    parser.add_argument("html_body", help="HTML-тело письма", type=str)  # Принимаем строку html как аргумент
    parser.add_argument("image_path", help="Путь к файлу изображения")
    args = parser.parse_args()

    send_email(
        args.sender_email,
        args.sender_password,
        args.receiver_email,
        args.subject,
        args.html_body,
        args.image_path
    )


if __name__ == "__main__":
    main()#python email_sender.py email.sender.script05@gmail.com dxjp aihk mfrr croq АДРЕСС_ПОЛУЧАТЕЛЕЙ “ТЕКСТ” “$(type email_body.html)” ПУТЬ_К_ФОТОГРАФИИ”
