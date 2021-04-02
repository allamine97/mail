import os
from imbox import Imbox # Il faut installer ce module avec : pip install imbox
import traceback
import datetime
#Il faut aussi aller sur ce lien pour enlever  les restrictions de google sinon la connéxion sera bloquée
# https://myaccount.google.com/lesssecureapps

#Pour Outlook le host c'est 'smtp-mail.outlook.com'
host = "imap.gmail.com"
#Il faut renseigner le mail et le mot de passe
username = "email"
password = 'password'
#ICI TU remplace le chemin d'un dossier de ta machine
download_folder = "C:/Users/lamine/Desktop/pyhtondev"

if not os.path.isdir(download_folder):
    os.makedirs(download_folder, exist_ok=True)
    
mail = Imbox(host, username=username, password=password, ssl=True, ssl_context=None, starttls=False)
messages = mail.messages() 
for (uid, message) in messages:
    mail.mark_seen(uid) # permet de marquer le mail à lu
    for idx, attachment in enumerate(message.attachments):
        try:
            att_fn = attachment.get('filename')
            #download_path = f"{download_folder}/{message.date)}_{message.subject}_{att_fn}"
            download_path = f"{download_folder}/{message.subject}_{att_fn}"
            print(download_path)
            with open(download_path, "wb") as fp:
                fp.write(attachment.get('content').read())
        except:
            print(traceback.print_exc())

mail.logout()

