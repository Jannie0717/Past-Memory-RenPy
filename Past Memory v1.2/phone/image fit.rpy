init python:
    def get_image_size(image):
        d = renpy.easy.displayable(image)
        w, h = renpy.render(d, 0, 0, 0, 0).get_size()
        w, h = int(round(w)), int(round(h))
        return w, h
    def image_fit(image, width, height, cap_size = True):
        image_width, image_height = get_image_size(image)
        if image_width < width and image_height < height and cap_size:
            return 1

        x_zoom = float(width) / float(image_width)
        y_zoom = float(height) / float(image_height)
        if y_zoom * image_width > width:
            return x_zoom
        else:
            return y_zoom

