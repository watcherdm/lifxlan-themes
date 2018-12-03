#! /Users/gabriel.hernandez/.virtualenvs/better/bin/python

from lifxlan import LifxLAN
import time

aqua = (180, 94.31, 100)
orag = (37, 100, 100)
pink = (308, 81.18, 100)
max_range = 65535
hue_range = 360
sat_bri_r = 100

FPS = 60

    # dt is the time delta in seconds (float).



class LaserCatTheme():
  def __init__(self):
    self.client = LifxLAN()
    self.lights = self.client.get_lights()
    self.colors = [aqua, orag, pink]
    self.speed = 0.025

  def convert_hsb_to_65k_range(self, h, s, b):
    return ((h * max_range / hue_range), (s * max_range / sat_bri_r), (b * max_range / sat_bri_r), 3500)

  def set_theme(self, offset=0):
    for i, light in enumerate(self.lights):
      try:
        light.set_color(self.convert_hsb_to_65k_range(*self.colors[(i + offset) % len(self.colors)]))
      except:
        print('some shit went wrong yo, try and learn what. maybe...')
  def game_logic(self, dt):
    self.set_theme(int(self.speed * dt))

if __name__=="__main__":
  instance = LaserCatTheme()

  instance.set_theme()

  lastFrameTime = 0

  while True:
    currentTime = time.time()
    dt = currentTime - lastFrameTime
    lastFrameTime = currentTime
    sleepTime = 1./FPS - (currentTime - lastFrameTime)
    if sleepTime > 0:
        time.sleep(sleepTime)
    instance.game_logic(dt)
    
