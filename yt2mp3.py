# Made by Halsen

#Start
import os
os.system('cls' if os.name == 'nt' else 'clear')
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#

#Script
ans = True
while ans:
    print ("""
    
  ▄▀█ █▄░█ █▀▀ █▀  
  █▀█ █░▀█ ██▄ ▄█  

  █▄█ █▀█ █░█ ▀█▀ █░█ █▄▄ █▀▀   █▀▄ █▀█ █░█░█ █▄░█ █░░ █▀█ ▄▀█ █▀▄ █▀▀ █▀█
  ░█░ █▄█ █▄█ ░█░ █▄█ █▄█ ██▄   █▄▀ █▄█ ▀▄▀▄▀ █░▀█ █▄▄ █▄█ █▀█ █▄▀ ██▄ █▀▄

  -----------------------------
  
  1. First-time installation (Run me when first time opening)

  -----------------------------
  2. Download MP4 from YouTube
  3. Donwload MP3 from YouTube
  4. About the Program
  -----------------------------
    """)
    ans=input("What would you like to do? ") 
    if ans=="1":
      os.system('cls' if os.name == 'nt' else 'clear')
      sure=input("Are you sure you would like to install youtube-dl and FFMPEG? (y/n) ")
      if sure=="y":
        os.system('echo Windows NOT SUPPORTED, only UNIX/Linux! n00b' if os.name == 'nt' else 'brew install yt-dlp')
        os.system('echo Windows NOT SUPPORTED, only UNIX/Linux! n00b' if os.name == 'nt' else 'brew install ffmpeg')
        os.system('cls' if os.name == 'nt' else 'clear')
      elif sure=="n":
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Stopping installation!")
      elif sure !="":
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\n Oops! Not a valid choice! Going to start ;(") 
    elif ans=="2": 
      os.system('cls' if os.name == 'nt' else 'clear')
      string=input("Type in the YouTube Link/ID: ")
      os.system("yt-dlp -o 'ANES YTDownloader - %(title)s.%(ext)s' " + string)
      os.system('cls' if os.name == 'nt' else 'clear')
    elif ans=="3":
      os.system('cls' if os.name == 'nt' else 'clear')
      string=input("Type in the YouTube Link/ID: ")
      os.system("yt-dlp --extract-audio --audio-format mp3 -o 'ANES YTDownloader - %(title)s.%(ext)s' " + string)
      os.system('cls' if os.name == 'nt' else 'clear')
      
    elif ans=="4":
      print("soon")
    elif ans !="":
      os.system('cls' if os.name == 'nt' else 'clear')
      print("\n Oops! Not a valid choice! ;(") 
