from interface import Interface
import time

backgroundImagePath = r"C:\Users\Usuario\Desktop\pokemon\generic_battle\images\background.png"
pokemon1Path = r"C:\Users\Usuario\Desktop\pokemon\generic_battle\images\arceus.png"
pokemon2Path = r"C:\Users\Usuario\Desktop\pokemon\generic_battle\images\arceus.png"

interface = Interface (800, 600)
interface.init_graphic_interface_fully (backgroundImagePath, pokemon1Path, pokemon2Path)

while True:
    interface.update_graphic_interface ()
