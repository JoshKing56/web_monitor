from datetime import datetime
import difflib
from telegram_send import configure, send
from subprocess import call

send_to_telegram = True

def handle_update(url, old_page, new_page):
    # This logic probably works, but I want the script to work and I don't have an easy way of testing this
    # So commenting this out until I have a reason to use it
    # Very bad practice
    # x = 0
    # old_page = old_page.split("\n")
    # new_page = new_page.split("\n")
    # for line in zip(old_page, new_page):
    #     if line[0] != line[1]:
    #         print(f"{x} | Old: {line[0]}")
    #         print(f"{x} | New: {line[1]}")
    #         x += 1

    update_time = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
    if send_to_telegram:
        alert = f"At approximately {update_time}, there was an update to [this page]({url})"
        # Yucky code, but this is how the author of telegram_send uses his own package
        # TODO: Rewrite to actually use python commands 
        call(["telegram-send", "--format", "markdown", alert])
    else:
        print(f"There was an update to the page at approximately {update_time}")
        print("\n")
