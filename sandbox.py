from subprocess import call

send_string = "[this is lame](www.google.com)"
call(["telegram-send", "--format", "markdown", send_string])