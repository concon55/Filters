from PIL import Image

def load_img(filename):
    im = Image.open(filename)
    return im

def show_img(imageObject):
    imageObject.show()

def save_img(imageObject, filename):
    imageObject.save(filename)

def obamicon(im):
  # Load the pixel data from im.
  pixels = im.getdata()
  # Create a list to hold the new image pixel data.
  new_pixels = []

  # Define color constants to use for recoloring.
  darkBlue = (0, 51, 76)
  red = (217, 26, 33)
  lightBlue = (112, 150, 158)
  yellow = (252, 227, 166)

  # Process the pixels in the image.
  for p in pixels:
    # Pixel intensity = R value + G value + B value
    intensity = p[0] + p[1] + p[2]

    if intensity < 182:
      new_pixels.append(darkBlue)

    elif intensity >= 182 and intensity < 364:
      new_pixels.append(red)

    elif intensity >= 364 and intensity < 546:
      new_pixels.append(lightBlue)

    elif intensity >=546:
      new_pixels.append(yellow)

  # Save the filtered pixels as a new image
  newim = Image.new("RGB", im.size)
  newim.putdata(new_pixels)
  return newim
