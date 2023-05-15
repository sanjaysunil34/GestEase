import ssl
import smtplib

from pynotifier import Notification, NotificationClient
from pynotifier.backends import platform, smtp

smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465, context=ssl.create_default_context())


# Create a notification object with the desired properties
notification = Notification(
    title='Hello, world!',
    description='This is a test notification',
    
    duration=5,  # Duration in seconds
)

c = NotificationClient()

c.register_backend(platform.Backend())
c.register_backend(smtp.Backend(server=smtp_server,
                                name='My Organization',
                                email='sender@organization.com',
                                password='super_password'))

# Display the notification
c.notify(notification)

print("hello")
