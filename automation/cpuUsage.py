#python programm for checking memory usages and sending this as an alert 
import psutil 
import logging
import time
import smtplib
#i don't know what is this but as imported so i'm also importing it 
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


# here is the cpu config setting 
cpu_threshold = 80
memory_threshold = 75
check_interval = 300 # this are in seconds 


EMAIL_FROM = "your_email@gmail.com"
EMAIL_TO = "recipient_email@example.com"
EMAIL_PASSWORD = "your_app_password"
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587


LOG_FILE = "cpu_monitor.log"
logging.basicConfig(filename= LOG_FILE, level = logging.INFO,
        format= '%(asctime)s%(levelname)s:%(message)s')



#copy pasted this function 

def send_email(subject, body):
    try:
        msg = MIMEMultipart()
        msg['From'] = EMAIL_FROM
        msg['To'] = EMAIL_TO
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(EMAIL_FROM, EMAIL_PASSWORD)
        server.send_message(msg)
        server.quit()

        logging.info("Email alert sent.")
    except Exception as e:
        logging.error(f"Email failed: {e}")


#checking the system health 


def check_sys_resc():
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent


    logging.info(f"CPU: {cpu}%, Memory: {memory}%")

    if cpu > cpu_threshold or memory > memory_threshold:
        subject = "Server Alert: High Usage"
        body = (f" High resource usage detected!\n\n"
                f"CPU Usage: {cpu}% (Limit: {CPU_THRESHOLD}%)\n"
                f"Memory Usage: {memory}% (Limit: {MEMORY_THRESHOLD}%)")
        send_email(subject, body)


    #so here printig the general value of the cpu here 


    print(f"current cpu usage is:{cpu}, and current memory usage is:{memory}")


#so now we are out of the def loop so now tyring the infinite loop 

if __name__ == "__main__":
    logging.info("Monitoring started.")
    while True:
        check_sys_resc()
        time.sleep(check_interval)


