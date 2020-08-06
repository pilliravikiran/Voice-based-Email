import speech_recognition as sr
import smtplib
from bs4 import BeautifulSoup
import email
import imaplib
from gtts import gTTS
import pyglet
import os
import time


print ("\n\t \t \t -------------------------Welcome to Voice Based Email-------------------------\n\n\n")
say= gTTS(text=" Hi welcome to voice based email, please select your required choice \n", lang='en')
convert=("1.mp3") 
say.save(convert)
music = pyglet.media.load(convert, streaming = False)
music.play()
time.sleep(music.duration)
os.remove(convert)


print ("\t\t\t1. compose a mail. \t\t\t\t\t\t----------> (compose)\n")
say = gTTS(text="Say 'compose' to compose a mail.", lang='en')
convert=("start2.mp3") 
say.save(convert)
music = pyglet.media.load(convert, streaming = False)
music.play()    
time.sleep(music.duration)
os.remove(convert)



print ("\t\t\t2. Check your inbox. \t\t\t\t\t----------> (Check)\n")
say= gTTS(text="Say 'check' to Check your inbox", lang='en')
convert=("start2.mp3")
say.save(convert)
music = pyglet.media.load(convert, streaming = False)
music.play()
time.sleep(music.duration)
os.remove(convert)


print ("\t\t\t3. Clear Inbox. \t\t\t\t\t\t----------> (Clear)\n")
say= gTTS(text="Say 'clear' to clear your inbox", lang='en')
convert=("start2.mp3")
say.save(convert)
music = pyglet.media.load(convert, streaming = False)
music.play()
time.sleep(music.duration)
os.remove(convert)

print ("\t\t\t4. Delete recent Email. \t\t\t\t----------> (Delete)\n")
say= gTTS(text="Say 'Delete' to delete the Recent email ", lang='en')
convert=("start2.mp3")
say.save(convert)
music = pyglet.media.load(convert, streaming = False)
music.play()
time.sleep(music.duration)
os.remove(convert)

print ("\t\t\t5. remove Email from specific user. \t----------> (Remove)\n")
say= gTTS(text="Say 'remove' to remove email from specific user", lang='en')
convert=("start2.mp3")
say.save(convert)
music = pyglet.media.load(convert, streaming = False)
music.play()
time.sleep(music.duration)
os.remove(convert)



print ("\t\t\t6. Search for mail. \t\t\t\t\t---------->  (Search)\n")
say = gTTS(text="Say 'Search' to search for  a mail.", lang='en')
convert=("start2.mp3") 
say.save(convert)
music = pyglet.media.load(convert, streaming = False)
music.play()    
time.sleep(music.duration)
os.remove(convert)


say= gTTS(text=" Select your choice  ", lang='en')
convert=("start2.mp3") 
say.save(convert)
music = pyglet.media.load(convert, streaming = False)
music.play()
time.sleep(music.duration)
os.remove(convert)

speech1 = sr.Recognizer()
with sr.Microphone() as source:
    print ("\tYour choice:\n")
    speech2=speech1.listen(source)
    print ("\t\t\tCommand Accepted\n")

try:
    text=speech1.recognize_google(speech2)
    print ("\t\tYou said : "+text)
    
except sr.UnknownValueError:
    print("Can't Understand the command. Run Again")
     
except sr.RequestError as e:
    print("Could not Connect to the Internet; {0}".format(e)) 


if text == 'compose' or text == 'compoze' or text == 'compus' or text== 'kompoz':
    speech1 = sr.Recognizer() 
    with sr.Microphone() as source:
        print (" \t\tSay Your message  :\n")
        speech2=speech1.listen(source)
        print ("\t\t\tCommand Accepted\n")
    try:
        text1=speech1.recognize_google(speech2)
        print ("\tYou said :"+text1)
        msg = text1
    except sr.UnknownValueError:
        print("Can't Understand the command. Run Again.")
    except sr.RequestError as e:
        print("Could not Connect to the Internet; {0}".format(e))    



    mail = smtplib.SMTP('smtp.gmail.com',587)    
    mail.ehlo() 
    mail.starttls() 
    mail.login('voiceforproject@gmail.com','emailgoogle' ) 
    mail.sendmail('voiceforproject@gmail.com','voiceforproject@gmail.com',msg) 
    print (" \t\tYour message Has been Sent. ")
    say = gTTS(text="Your message Has been Sent", lang='en')
    convert=("3.mp3") 
    say.save(convert)
    music = pyglet.media.load(convert, streaming = False)
    music.play()
    time.sleep(music.duration)
    os.remove(convert)
    mail.close()   


    
if text == 'check'  :
    mail = imaplib.IMAP4_SSL('imap.gmail.com',993) 
    username = ('voiceforproject@gmail.com')  
    password = ('emailgoogle') 
    mail.login(username,password)  
    subtotal, total = mail.select('Inbox') 
    print ("\t\tTotal number of mails in your inbox :"+str(total))
    say = gTTS(text="Total  number of mails are :"+str(total), lang='en') 
    convert=("4.mp3") 
    say.save(convert)
    music = pyglet.media.load(convert, streaming = False)
    music.play()
    time.sleep(music.duration)
    os.remove(convert)
    
    
    first, data = mail.uid('search',None, "ALL")
    totalinboxdata = data[0].split()
    new = totalinboxdata[-1]
    old = totalinboxdata[0]
    second, totalemaildata = mail.uid('fetch', new, '(RFC822)') 
    original = totalemaildata[0][1].decode("utf-8") 
    line = email.message_from_string(original)
    print ("\t\tFrom: "+line['From'])
    say= gTTS(text="From: "+line['From'])
    convert=("5.mp3") 
    say.save(convert)
    music = pyglet.media.load(convert, streaming = False)
    music.play()
    time.sleep(music.duration)
    os.remove(convert)
    
  
    subtotal, total1 = mail.select('Inbox')
    subtotal, data1 = mail.fetch(total1[0], "(UID BODY[TEXT])")
    msg = data1[0][1]
    soup = BeautifulSoup(msg, "html.parser")
    matter = soup.get_text()
    print ("\t\tBody :"+matter)
    say = gTTS(text="Body: "+matter, lang='en')
    convert=("6.mp3") 
    say.save(convert)
    music = pyglet.media.load(convert, streaming = False)
    music.play()
    time.sleep(music.duration)
    os.remove(convert)
    mail.close()
    mail.logout()


if text == 'clear' or text == 'clea' or text == 'klear' or text == 'Kiya':
    mail = imaplib.IMAP4_SSL('imap.gmail.com', 993)
    mail.login("voiceforproject@gmail.com","emailgoogle")
    mail.select('Inbox')
    typ, data = mail.search(None, 'ALL')
    for num in data[0].split():
        mail.store(num, '+FLAGS', '\\Deleted')
    mail.expunge()
    print("\t\tInbox is cleared")
    mail.close()
    mail.logout()



if text == 'remove' or text == 'remov' or text == 'rimoove' or text == 'remove' or text == 'rimoove' or text == 'are moon':


    mail = imaplib.IMAP4_SSL('imap.gmail.com', 993)
    mail.login("voiceforproject@gmail.com","emailgoogle")
    mail.select('Inbox')
    typ, data = mail.search(None, 'from','mail2pravallikaregalla')
    for num in data[0].split():
        mail.store(num, '+FLAGS', '\\Deleted')
    mail.expunge()
    mail.close()
    mail.logout()


    
        

if text == 'delete' or text == 'dele' or text == 'delite' or text == 'dilit' or text == 'delight':
    mail = imaplib.IMAP4_SSL('imap.gmail.com', 993)
    mail.login("voiceforproject@gmail.com","emailgoogle")
    mail.select('Inbox')
    typ, data = mail.search(None, 'ALL')
    ids = data[0] # data is a list.
    id_list = ids.split() # ids is a space separated string
    latest_email_id = id_list[-1]
    mail.store(latest_email_id, '+FLAGS', '\\Deleted')
    mail.expunge()
    print("\t\trecent mail is Deleted")
    mail.close()
    mail.logout()


if text == 'search' or text == 'sarch' or text == 'serch':
    mail = imaplib.IMAP4_SSL('imap.gmail.com', 993)
    mail.login("voiceforproject@gmail.com","emailgoogle")
    mail.select('Inbox')    
    result, total1 = mail.search(None,'from','mail2pilliravikiran@gmail.com' )
    result, data1 = mail.fetch(total1[0], "(UID BODY[TEXT])")
    msg = data1[0][1]
    soup = BeautifulSoup(msg, "html.parser")
    matter = soup.get_text()
    print ("\t\tBody :"+matter)
    say = gTTS(text="Body: "+matter, lang='en')
    convert=("6.mp3") 
    say.save(convert)
    music = pyglet.media.load(convert, streaming = False)
    music.play()
    time.sleep(music.duration)
    os.remove(convert)
    mail.close()
    mail.logout()