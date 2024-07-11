import os
os.system("pip install diffusers")
os.system("pip install pyautogui")
os.system("pip install pyperclip")
import time
import pyautogui
import pyperclip
from PIL import Image
from tkinter import Tk


from diffusers import DiffusionPipeline

#Initialize the image generation model
pipeline = DiffusionPipeline.from_pretrained("runwayml/stable-diffusion-v1-5")
pipeline.to("mps")
pipeline.enable_attention_slicing()

pyautogui.FAILSAFE = False

#Mainloop
num_iterations = int(input("How many iterations do you want to run for?: "))
#image = input("What is the path to the image you want to use?: ")
image = "/Users/aditya/Desktop/AI Telephone/StartingPic.png"
main = Tk()
main.withdraw()
time.sleep(5)

for x in range(num_iterations):
  #Make gemini prompt]
  #Assumes a 1440x900 screen, macos, maximized window, gemini open and signed in
  #Gemini window has to be directly to the left of the python window
  pyautogui.leftClick(220,115,duration=0)
  time.sleep(1)
  pyautogui.leftClick(541,827, duration=0)
  pyautogui.typewrite("Write a detailed description of this image in such a way that another AI model will be able to recreate this image perfectly. This should be around 250 words and capture every minor detail.")
  pyautogui.leftClick(490,845,duration=0)
  time.sleep(0.2)
  pyautogui.leftClick(690,800,duration=0)
  pyautogui.hotkey("winleft", "shiftleft", "g")
  pyautogui.typewrite(image + "\n\n\n", interval= 0.1)
  time.sleep(0.1)
  pyautogui.hotkey("return")
  time.sleep(5)
  pyautogui.click(1200,845)
  time.sleep(15)
  pyautogui.scroll(1000000)
  pyautogui.moveTo(525,700)
  pyautogui.dragTo(0,0,duration=30, button="left")
  pyautogui.moveTo(525,700)
  pyautogui.dragTo(1000,850, duration=30, button="left")
  pyautogui.rightClick(533,195, duration=0)
  time.sleep(0.1)
  pyautogui.leftClick(740,240,duration=0)
  time.sleep(0.1)
  pyautogui.hotkey("winleft", "c")
  time.sleep(0.1)
  pyautogui.hotkey("winleft", "c")
  time.sleep(0.1)
  pyautogui.hotkey("winleft", "c")
  time.sleep(0.1)
  description = main.clipboard_get()#pyperclip.paste()
  text = open("Prompt.txt", "a")
  text.write(description + "\n---------------------------------\n")
  text.close()

  #Now, transfer it to the image-generator to generate the image
  image = pipeline("An image of a squirrel in Picasso style").images[0]
  image.save("ScreenShot " + str(x) + ".png", "PNG")
  image = os.path.realpath("ScreenShot " + str(x) + ".png")
  time.sleep(1)