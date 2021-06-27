import smtplib
import time
from email.header import Header
from email.mime.text import MIMEText


class SendEmail():
    def send_email(self, new_report):
        # 读取测试报告中的内容作为邮件的内容
        with open(new_report, 'r', encoding='utf8') as f:
            mail_body = f.read()
        # 发件人地址
        send_addr = '3381350680@qq.com'
        # 收件人地址
        reciver_addr = '3381350680@qq.com'
        # 发送邮箱的服务器地址 qq邮箱是'smtp.qq.com', 136邮箱是'smtp.136.com'
        mail_server = 'smtp.qq.com'
        now = time.strftime("%Y-%m-%d %H_%M_%S")
        # 邮件标题


        subject = 'web自动化测试报告测试报告' + now
        # 发件人的邮箱及邮箱授权码
        username = '3381350680@qq.com'
        password = '***'  # 注意这里是邮箱的授权码而不是邮箱密码
        # 邮箱的内容和标题
        message = MIMEText(mail_body, 'html', 'utf8')
        message['Subject'] = Header(subject, charset='utf8')
        # 发送邮件，使用的使smtp协议
        smtp = smtplib.SMTP()
        smtp.connect(mail_server)
        smtp.login(username, password)
        smtp.sendmail(send_addr, reciver_addr.split(','), message.as_string())
        smtp.quit()
