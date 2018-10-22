import pyscreenshot as ig
import pytesseract as pt
from PIL import Image

x = ig.grab()
print(pt.image_to_data(x))