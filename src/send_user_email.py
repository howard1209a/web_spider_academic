import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from datetime import datetime
import config


def send_email(filename):
    sender_email = config.get_sender_email()  # 发件邮箱
    receiver_email = config.get_receiver_email()  # 收件邮箱
    email_authorization_code = config.get_email_authorization_code()  # 发件邮箱授权码

    current_date = datetime.now()
    subject = current_date.strftime('%Y-%m-%d') + "-请查收本周文献追踪"

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
