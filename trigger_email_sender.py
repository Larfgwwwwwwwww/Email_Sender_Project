import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import tkinter as tk
from tkinter import messagebox
import random

def send_trigger_email(recipient_email):
    # Генерация рандомного пятизначного числа
    random_number = random.randint(10000, 99999)

    # Настройка email
    from_email = "email.sender.script05@gmail.com"  # Ваш email
    password = "0431951765"  # Ваш пароль
    subject = "Ваш код безопасности"
    body = f"Ваш код безопасности: {random_number}"

    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = recipient_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(from_email, password)
            server.send_message(msg)
        print(f"Письмо успешно отправлено на {recipient_email}")
    except Exception as e:
        print(f"Возникла ошибка: {e}")

def trigger_email():
    email = email_entry.get()
    if email:
        send_trigger_email(email)
        email_entry.delete(0, tk.END)
        messagebox.showinfo("Успех", "Письмо отправлено!")
    else:
        messagebox.showwarning("Ошибка", "Введите адрес электронной почты.")

# Настройка GUI
root = tk.Tk()
root.title("Отправка триггерного письма")

tk.Label(root, text="Введите адрес электронной почты:").pack()
email_entry = tk.Entry(root, width=30)
email_entry.pack()
tk.Button(root, text="Подтвердить", command=trigger_email).pack()

root.mainloop()
