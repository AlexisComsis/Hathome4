import json
import pygame
pygame.mixer.pre_init(44100, -16, 2, 2048)  #bug soundp
pygame.init()
window = pygame.display.set_mode((500,200))



class Info:

    # take the height and width needed
    with open("Assets\Data\Options.txt", "r+") as o_data:
        o_data = json.loads(o_data.read())
        w0 = o_data["Width"]
        h0 = o_data["Height"]
        volume = o_data["Volume"]

    icon = pygame.image.load("Assets\Image\Icon.png").convert_alpha()
    image0 = pygame.image.load("Assets\Image\D.png").convert_alpha()

    # Convert resolution depending on the screen
    def convert_coord(nx, ny, w=w0, h=h0):
        return [int(nx / 1600 * w), int(ny / 900 * h)]

    def convert(img, w=w0, h=h0):
        '''
        convert an image in the format of the options
        '''
        wc = int(img.get_width() / 1600 * w)
        hc = int(img.get_height() / 900 * h)
        return pygame.transform.scale(img, (wc, hc))

    def load_convert(img_path=image0, w1=32, bank=True, mult=1):
        '''
        separate different sprites
        '''
        img = pygame.image.load(img_path).convert_alpha()
        w2 = img.get_width()
        h2 = img.get_height()
        timer = int(w2/w1)
        if not bank:
            img = pygame.transform.scale(img, (int(mult*w1), int(mult*h2)))
            img = tools.convert(img)
            return img
        else:
            img_list = []
            for i in range(timer):
                img_list.append(img.subsurface(i*w1, 0, w1, h2))
                img_list[i] = pygame.transform.scale(img_list[i], (int(mult*w1), int(mult*h2)))
                img_list[i] = tools.convert(img_list[i])
        return img_list
