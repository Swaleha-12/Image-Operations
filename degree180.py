def degrees180(locimage: MyImage):

    lenn = locimage.size[0]*locimage.size[1]
    for i in range((lenn//2)):
        pixel = locimage.pixels[i]
        locimage.pixels.set(i, locimage.pixels[lenn-i-1])
        locimage.pixels.set(lenn-i-1, pixel)
    locimage.save("images/degrees180.png")
    locimage.show()
