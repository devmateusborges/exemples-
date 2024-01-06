from smtplib import SMTP 
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from app import tpl

from app.env import MAIL_SMTP_HOST, MAIL_SMTP_PORT, MAIL_SMTP_PWD, MAIL_SMTP_USER

class email_util():

    #================================================================
    def send_mail(self,body_content,to_email,from_email,subject):
        try:
            message = MIMEMultipart()
            message['Subject'] = subject
            message['From'] = from_email
            message['To'] = to_email

            message.attach(MIMEText(body_content, "html"))
            msgBody = message.as_string()

            server = SMTP(MAIL_SMTP_HOST, MAIL_SMTP_PORT)
            server.starttls()
            server.login(MAIL_SMTP_USER, MAIL_SMTP_PWD)
            server.sendmail(from_email, to_email, msgBody)

            server.quit()
            return {"send_email":"OK"}
        except Exception as e:
           return {"send_email":"ERROR"}
    
    #================================================================
    def send_mail_template(self,to_email,from_email,subject, template_name, template_data):
        template = tpl.get_template(template_name+".html")
        template_render = template.render(data=template_data)
        result = self.send_mail(template_render,to_email,from_email,subject)    
        return result