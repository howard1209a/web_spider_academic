import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from datetime import datetime
import config


def send_email(filename):
    # 邮件发件人、收件人和授权码
    sender_email = config.get_sender_email()
    receiver_email = config.get_receiver_email()
    email_authorization_code = config.get_email_authorization_code()  # QQ邮箱授权码

    # 获取当前日期
    current_date = datetime.now()

    # 将当前日期转换为字符串，格式：'YYYY-MM-DD'
    date_string = current_date.strftime('%Y-%m-%d')

    # 邮件内容
    subject = date_string + "-请查收本周文献追踪"

    # 创建邮件
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = subject

    # 添加邮件正文
    message.attach(MIMEText(subject, 'plain'))

    # 添加 DOCX 附件
    attachment = open(filename, "rb")

    # 创建 MIMEBase 对象并附加文件
    part = MIMEBase('application', 'octet-stream')
    part.set_payload(attachment.read())  # 读取文件内容
    encoders.encode_base64(part)  # 对附件进行 Base64 编码

    # 设置附件头信息
    part.add_header('Content-Disposition', f"attachment; filename={filename}")

    # 将附件附加到邮件
    message.attach(part)

    # 连接并发送邮件
    try:
        with smtplib.SMTP_SSL('smtp.qq.com', 465) as server:
            server.login(sender_email, email_authorization_code)
            server.sendmail(sender_email, receiver_email, message.as_string())
    except Exception as e:
        print(f"send email fail: {e}")
