import datetime
import difflib
import telegram

send_to_telegram = True

def handle_update(old_page, new_page):
    update = difflib.ndiff(old_page, new_page)
        if send_to_telegram:
            alert = f"At {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}, there was an update to the page"
        else: