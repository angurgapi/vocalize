import datetime
from gtts import gTTS
from langdetect import detect


theText = input('Type your text or insert path to txt file: ')
if theText.endswith('.txt'):
    infile = theText
    f = open(infile, 'r')
    theText = f.read()
    f.close()

today = datetime.datetime.today()
   
lang = detect(theText)    
tts = gTTS(text=theText, lang=lang)
tts.save(today.strftime("%Y-%m-%d-%H.%M.%S")+'.mp3')

