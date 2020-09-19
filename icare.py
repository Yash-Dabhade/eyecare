import time
from plyer import notification
if __name__ == '__main__':
    while True:
        notification.notify(
            message='Follow 20-20-20 Rule Now. Please follow this rule to keep your eyes in good health',
            title='Look at a faraway object for 20 sec.',
            app_icon='icon2.ico',
            timeout=10
        )
        time.sleep(60*20)
