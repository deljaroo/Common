class Color:
    def colorKeyToTransparent(image_path, color_key):
        from PIL import Image
        with Image.open(image_path) as old_image:
            #old_image = Image.open(image_path)
            old_pixel_map = old_image.load()
            new_image = Image.new(old_image.mode, old_image.size)
            new_pixel_map = new_image.load()
            for i in range(new_image.size[0]):
                for j in range(new_image.size[1]):
                    old_color = old_pixel_map[i,j]
                    if old_color==color_key:
                        new_pixel_map[i, j] = (0, 0, 0, 255)
                    else:
                        new_pixel_map[i, j] = old_pixel_map[i, j]
            old_filename = image_path[image_path.rfind('\\')+1:]
            new_image.save("tkid_" + old_filename)
            new_image.close()

    def svhToRgb(sat, value, hue):
        """
        Converts SVH color wheel to RGB color
        sat: a number 0-1 that gives the ratio of the highest color to the
            lowest color
            generally thought of how vibrant a color is
            lower values will give all whites, grays and black
        value: a number 0-255 that represents the brightest color
            generally thought of as the brightness, but the brighness is more
            complicated than this
        hue: a number 0-360 that represents the distribution of colors
            it is the number of degrees in an rgb wheel from pure red heading
            in the green-wise direction (pure green is 120, pure blue is 240)
        RETURNS: a 3-length tuple of ints 0-255 representing red, green and then
            blue repectively
        """
        r = 0
        g = 0
        b = 0
        lowest = int(value * (1-sat))
        value = int(value)
        hue = hue % 360 #loops the hue to a 360-degree limit
        ratio = ( hue % 60 ) / 60
        if 0 <= hue < 60:
            return (value, int(value * ratio), lowest)
        if 60 <= hue < 120:
            return (int(value * (1-ratio)), value, lowest)
        if 120 <= hue < 180:
            return (lowest, value, int(value * ratio))
        if 180 <= hue < 240:
            return (lowest, int(value * (1 - ratio)), value)
        if 240 <= hue < 300:
            return (int(value * ratio), lowest, value)
        if 300 <= hue < 360:
            return (value, lowest, int(value * (1-ratio)))
        raise Exception("How did you get here?")