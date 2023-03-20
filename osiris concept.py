import random
import pystyle
from pystyle import *
import os

ascii = r'''


      .▄▄ · ▪  ▄▄▄  ▪  .▄▄ ·     
▪     ▐█ ▀. ██ ▀▄ █·██ ▐█ ▀.     
 ▄█▀▄ ▄▀▀▀█▄▐█·▐▀▀▄ ▐█·▄▀▀▀█▄    
▐█▌.▐▌▐█▄▪▐█▐█▌▐█•█▌▐█▌▐█▄▪▐█    
 ▀█▄▀▪ ▀▀▀▀ ▀▀▀.▀  ▀▀▀▀ ▀▀▀▀   

  https://github.com/Vega863

  '''


banner = r"""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⡇⠀⢠⣾⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⡇⢠⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⡇⢸⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⡀⠙⠛⠃⠘⠻⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠐⠚⣛⣛⣁⡀⠹⣿⣿⣶⣶⣤⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣠⣴⠶⠿⠛⠛⠛⠛⠛⠀⢻⣿⣿⣤⣀⣙⣷⣀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⣈⣁⣤⣴⣶⠶⠿⠿⠿⠿⠇⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣦⣤⡄⠀
⠀⠀⠐⠛⢉⣉⣠⣤⣤⣶⣶⣶⣶⣦⠀⣿⣿⣿⣿⣿⣿⣿⡿⠿⠿⠿⠛⠉⠀⠀
⠀⠀⡾⠛⠉⠉⠉⠙⠻⢿⣿⣿⣿⣿⡀⢹⡿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⡇⠘⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢸⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⡇⠀⣾⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠃⠀⢿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⠀⠀⠸⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠙⠀⠀⠀⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
"""
banner = Add.Add(ascii, banner, center=True)
white = Col.white
blue = Col.StaticMIX((Col.blue, Col.black))
legacypurple = Col.StaticMIX((Col.purple, Col.pink, blue))
whitepurple = Col.StaticMIX((Col.purple, blue, Col.white))
col1 = Col.StaticMIX((Col.red, Col.purple))
col2 = Col.StaticMIX((Col.pink, Col.purple, Col.dark_red))
col3 = Col.StaticMIX((Col.light_blue, Col.blue))
col4 = Col.StaticMIX((Col.red, Col.light_red, Col.pink))
col5 = Col.StaticMIX((Col.red, Col.light_red))
col6 = Col.StaticMIX((Col.green, Col.dark_green))


def encrypt(s):
    key = input("Put a key encrypt maximum (1114046):")
    key = int(key) # the maximum key is 1114046
    return ''.join(chr(ord(c) + key) for c in s), key

def decrypt(s, key):
    return ''.join(chr(ord(c) - key) for c in s)

def init():
  os.system("cls")
  colors = [legacypurple, whitepurple, blue, col1, col2, col3, col4, col5, col6]
  rdmcolors = random.choice(colors)
  print(Colorate.Diagonal(Col.DynamicMIX(
    (Col.white, rdmcolors)), Center.XCenter(banner)))
  texte = input("Type something: ")
  obfuscated_text, key = encrypt(texte)
  print("Encrypted text:", obfuscated_text)
  print("Using key:", key)
  deobfuscated_text = decrypt(obfuscated_text, key)
  print("Decrypted text:", deobfuscated_text)
  a = input("retry ? (y/n)")
  if a == ("y" or "yes"):
     init()
  else:
     exit()

if __name__ == "__main__":
    init()
