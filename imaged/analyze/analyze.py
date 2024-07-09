from PIL import Image
from PIL import ImageEnhance
from PIL import ImageChops
from PIL import ImageDraw, ImageFont
import numpy as np

def measure(x1,y1,x2,y2):
    """
        Measures the distance in pixels between two points.
        Args:
            x1,y1: position of first point
            x2,y2: position of second point
        Returns:
            measurement between the two points
        """
    measurement = np.round(np.sqrt(
                np.abs(x2 - x1)**2 + np.abs(y2 - y1)**2),2)
    
    return measurement

def determine_scale(len_m, len_p, units):
    """
        Changes scale from pixels to given unit
        Args:
            len_p: length in pixels (float)
            len_m: length in given units (float)
            units: string
        Returns:
            updated scale of 100 pixels, tuple (length, units)
        """
    scale = (len_m / len_p * 100,units)
    return scale
    