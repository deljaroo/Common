import sys
try:
    def colorInput(color_name):
        while True:
            ink = input(str(color_name) + " value (0-255): ")
            try:
                ink = int(ink)
            except ValueError:
                print("Only integers are allowed")
                continue
            if ink < 0 or ink > 255:
                print("Must be between 0 and 255")
                continue
            return ink
    
    if len(sys.argv) < 2:
        input("drag a png file on to this script to have it make a transparent version of it")
        sys.exit()
    path = sys.argv[1]
    if (path[-4:] != ".png"):
        input("png files only")
        sys.exit()
    r = colorInput("red")
    g= colorInput("green")
    b = colorInput("blue")
    from color import Color
    Color.colorKeyToTransparent(path, (r, g, b))
except Exception as e:
    print(e)
    input()
    raise