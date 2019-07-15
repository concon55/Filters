import filters

def main():
    userInput = input("Enter file name: ")
    im = filters.load_img(userInput)
    # newImage = filters.obamicon(im)
    filters.show_img(im)
    filters.save_img(im, "newPic.jpg")

if __name__ == "__main__":
  main()
