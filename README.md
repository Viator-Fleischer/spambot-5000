# spambot-5000
### What's it about? 
Well, it's all in the name... Making YouTube livestreams' spamming easier. 

### How does it work?
Pretty simply, thanks for asking.

### Need more info? Okay, but I'll just give the bulletpoints:

- you install the packages and other dependencies that are needed for executing the script

- you whip up your VSC (or terminal) and execute the program

- a window pops up asking for url, number of browsers, profile path, and something called "lines.txt"
  
- you insert the livestream url you want to späm
  
- you tell it how many browsers you want (hint: more browsers = more chaos, and the more browsers = need more computer power + more chances for something to go wrong on your end)

- you give it the file path where you want to create/store new profiles or from where you want to pull up pre-existing browser profiles (the script is coded to create a *separate*, and unique profile for each browsers, which is like a totally new identity for you; you can't really log into multiple YouTube account at the same time when you're using a browser like normal people do it. That is because you're using the same "browser identity". The script is meant to circumvent this issue by creating new identities, and as you begin to use these new identities it will save all the settings for each individual profile, so that when you fire up the script the second time, it will remember each browser's profile settings (like cookie settings and log in info). If it's your first time running the script, don't worry, it ought to create the profiles automatically, if you've specified the number of browsers you want. Each browser gets their own profile, so for example opening 5 browsers equals 5 profiles, y'know? Simple.
  
- and lastly, you give it the file path where you store a .txt document which hosts all the comments you want the script to be spamming/posting on the livestream. The script reads the .txt file line by line, copies the text from one of any number of lines that you happen to have written down there, and then posts it automatically onto the livestream's live comment box >>>>>AT RANDOM<<<< from any of the n amount of text lines you've written. As such, you ought to keep each comment separate from the other by a paragraph break.
  
- after all that's done, you press "Start" or "Stop", depending on what you're currently doing.

- it then begins to post the comments about every 3 seconds until you make it stop.

And that's all folks!

### How do I use it?
This was coded specifically with Chrome and Chromium in mind, so with other browsers the script might not work as it's supposed to. 

Download the script, pull up your Visual Code Studio or any equivalent and/or eliqible program for running python scripts.
Make sure you've installed the latest version of python (3.6.-3.9 is sufficient, I think?), the necessary webdrivers (selenium and undetected_chromedriver), and all that other junk.

There are better instructions available on how to set these webdrivers up elsewhere: just go see ultrafunkamsterdam's github page for starters; but the key point here is that you have to have the necessary Chrome version that is compatible with the right version of selenium, otherwise it won't work. And if none of it makes sense, just ask ChatGPT for help, lmao.

It's using undetected chromedriver, so your browsers shouldn't be able to prevent the script's intended functioning. If it reads at the top of your browsers something along the lines of "we've detected that you're using automated web browsing, yada yada yada", it means that there's something wrong with your installation of undetected webdriver, or something else, and that you won't be using the script anytime soon - that is, not until you fix it.

I used the following Python packages in my setup:

Package                   Version

altgraph                  0.17.3
attrs                     23.1.0
certifi                   2023.5.7
charset-normalizer        3.2.0
chromedriver              2.24.1
exceptiongroup            1.1.2
h11                       0.14.0
idna                      3.4
outcome                   1.2.0
packaging                 23.2
Pillow                    10.0.0
pip                       23.2.1
pyinstaller               5.13.0
pyinstaller-hooks-contrib 2023.6
pypng                     0.20220715.0
PySocks                   1.7.1
python-dotenv             1.0.0
qrcode                    7.4.2
requests                  2.31.0
selenium                  4.15.2
setuptools                65.5.0
sniffio                   1.3.0
sortedcontainers          2.4.0
tk                        0.1.0
trio                      0.22.1
trio-websocket            0.10.3
typing_extensions         4.7.1
undetected-chromedriver   3.5.4
urllib3                   2.0.3
webdriver-manager         4.0.1
websockets                11.0.3
wsproto                   1.2.0

You probably won't need all that stuff, but if you want to be lazy, just do "pip install" and copy-paste the names and that ought to take care of the package hurdle so that you can run the script, or something - listen, I'm not your mom, so figure it out yourselves!

### Is this ethical? Is this legal?
I dunno. Using it? Probably not. But if you were searching for spambots in the first place and happened to find this repository, it's pretty clear that you don't care and have no regard for rule of law, ethics, general human decency, and stuff like that. So, whatever it is you're doing, I ain't taking no responsibility over your actions. This was all just part of my research into political activism online and to prove how dangerous AI can be at the wrong hands - in case you haven't figured it out yet, this script was done with ChatGPT's assistance.

Don't be evil, obviously, and use it ONLY for noble causes.
