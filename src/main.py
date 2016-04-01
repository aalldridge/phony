import logging
import gobject
import base.classlogger
import bluetooth.profiles
import bluetooth.control
import bluetooth.adapters

def main_loop():
  return gobject.MainLoop()

if __name__ == '__main__':
  base.classlogger.send_to_stdout()

  bluez4 = bluetooth.adapters.Bluez4("hci1")
  control = bluetooth.control.Controller(bluez4)

  control.enable_visibility()

  with bluetooth.profiles.HandsFree() as hfp:
    hfp.start()
    main_loop().run()