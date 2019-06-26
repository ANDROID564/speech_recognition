# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 20:51:51 2018

@author: TANVEER_MUSTAFA
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 20:36:22 2018

@author: TANVEER_MUSTAFA
"""

import speech_recognition as sr     # import the library
 
r = sr.Recognizer()                 # initialize recognizer
with sr.Microphone() as source:     # mention source it will be either Microphone or audio files.
    print("Speak Anything :")
    audio = r.listen(source)        # listen to the source
    try:
        text = r.recognize_google(audio)    # use recognizer to convert our audio into text part.
        print("You said : {}".format(text))
        
        #here the audio file is stored        
        if str is bytes: 
            result = u"{}".format(text).encode("utf-8")

        else: 
            result = "{}".format(text)

        with open("outputs.txt","a") as f:
            f.write(result)
            print(result)
        
    except:
        print("Sorry could not recognize your voice")    # In case of voice not recognized  clearly
