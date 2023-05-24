#FamilienWaechter.py

import time
from twilio.rest import Client
from plyer import NotificationListenerService
#Konfiguration deiner App hinzugefügt hast, um auf den NotificationListenerService zuzugreifen.
from plyer import notification
#Hir von der plyer erst instalieren 
def on_notification_posted(title, text):
    # Hier kannst du den Titel und Text der Benachrichtigung verarbeiten
    print("Titel:", title)
    print("Text:", text)

def listen_notifications():
    while True:
        notification.notify(
            title='Testbenachrichtigung',
            message='Dies ist eine Testbenachrichtigung.',
            timeout=5,
            callback=on_notification_posted
        )
        time.sleep(10)  # Überprüfung alle 10 Sekunden aktualisieren

# Hauptprogramm
listen_notifications()



# Watsapp -Kontodaten
account_sid = 'YOUR_ACCOUNT_SID'
auth_token = 'YOUR_AUTH_TOKEN'
client = Client(account_sid, auth_token)

def connect_numbers(from_number, to_number):
    try:
        call = client.calls.create(
            twiml='<Response><Dial>{}</Dial></Response>'.format(to_number),
            from_=from_number,
            to=from_number
        )
        print("Anruf gestartet.")
        print("SID: ", call.sid)
    except Exception as e:
        print("Fehler beim Verbinden der Nummern:", str(e))

# Hauptprogramm
from_number = 'YOUR_PHONE_NUMBER'  # Deine Telefonnummer
to_number = 'TARGET_PHONE_NUMBER'  # Die Zieltelefonnummer, zu der du verbinden möchtest

connect_numbers(from_number, to_number)



new_var = NotificationListenerService
class MyNotificationListenerService(new_var):
    def on_notification_posted(self, notification, sbn):
        if "WhatsApp" in sbn.getPackageName():
            # Hier kannst du den Inhalt der WhatsApp-Benachrichtigung analysieren und verarbeiten
            message = notification.get("android.text").toString()
            sender = notification.get("android.title").toString()
            print("android.title:", sender)
            print("android.text:", message)
def check_variable(variable):
    if variable is not None:
        return variable
    else:
        # Hier kannst du definieren, wie du mit einer undefinierten Variable umgehen möchtest
        # Zum Beispiel könntest du eine Standardwert zurückgeben oder eine Ausnahme auslösen
        return None  # Rückgabe eines Standardwerts

class MyNotificationListenerService(NotificationListenerService):
    def on_notification_posted(self, notification, sbn):
        if "WhatsApp" in sbn.getPackageName():
            # Hier kannst du den Inhalt der WhatsApp-Benachrichtigung analysieren und verarbeiten
            message = check_variable(notification.get("android.text").toString())
            sender = check_variable(notification.get("android.title").toString())
            print("android.title:", sender)
            print("android.text:", message)    # Hier könntest du die Überprüfung auf neue WhatsApp-Nachrichten implementieren
    # Verwende geeignete Methoden oder Bibliotheken, um auf die Nachrichten zuzugreifen
    # Du kannst die Anzahl der neuen Nachrichten oder die Details der Nachrichten zurückgeben
    # Beispiel:
def check_new_messages():
    # Code, um neue WhatsApp-Nachrichten zu überprüfen
    # Rückgabe der Anzahl der neuen Nachrichten oder der Nachrichtenliste

 def check_new_calls():
    # Code, um neue Anrufe zu überprüfen
    # Verwende geeignete Methoden oder Bibliotheken, um auf die Anrufe zuzugreifen
    # Du kannst die Anzahl der neuen Anrufe oder die Details der Anrufe zurückgeben

    # Beispiel: Annahme, dass die Anrufinformationen in einer Liste `call_list` gespeichert sind
    call_list = [...]  # Liste mit den Anrufinformationen

    new_calls = 0  # Anfangswert für die Anzahl der neuen Anrufe

    # Überprüfe jedes Anrufobjekt in der Liste
    for call in call_list:
        if call.is_new():
            new_calls += 1

    return new_calls

    # Code, um neue Anrufe zu überprüfen
    # Rückgabe der Anzahl der neuen Anrufe oder der Anrufdetails

 def notify_parents(new_messages, new_calls):


    # Hier könntest du Code hinzufügen, um Eltern über die neuen Nachrichten zu benachrichtigen
    if new_messages > 0:
        notification.notify(
            title='Neue WhatsApp-Nachrichten',
            message=f'Du hast {new_messages} neue WhatsApp-Nachricht(en).',
            app_icon=None,  # Pfad zum App-Symbol oder None für Standard-App-Symbol
            timeout=10  # Anzeigezeit der Benachrichtigung in Sekunden
        )

    # Hier könntest du Code hinzufügen, um Eltern über die neuen Anrufe zu benachrichtigen
    if new_calls > 0:
        notification.notify(
            title='Neue Anrufe',
            message=f'Du hast {new_calls} neue Anruf(e).',
            app_icon=None,  # Pfad zum App-Symbol oder None für Standard-App-Symbol
            timeout=10  # Anzeigezeit der Benachrichtigung in Sekunden
        )

 def run_monitoring():
    while True:
        new_messages = check_new_messages()
        new_calls = check_new_calls()
        notify_parents(new_messages, new_calls)
        time.sleep(10)  # Überwachung alle 10 Sekunden aktualisieren

# Hauptprogramm
 run_monitoring()
