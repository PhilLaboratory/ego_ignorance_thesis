from PIL import Image, ImageDraw

#SIZE of background = 960X540px

#load images
background = Image.open("stimuli/blank_scene.jpg")
empty_basket = Image.open("stimuli/empty_basket.png")
full_basket = Image.open("stimuli/full_basket.png")
occ = Image.open("stimuli/occ.png")
rectangle = Image.open("stimuli/rectangle.png")


#resize images
    #size of background = 960X540px
resize_ego_occ = 120 #subtracted from occ height
resize_alter_occ = 90 #subtracted from occ height
basket_height = 170
basket_width = 275
empty_basket = empty_basket.resize((basket_width, basket_height))
full_basket = full_basket.resize((basket_width, basket_height))
occ = occ.resize((960,(540-resize_alter_occ)))
ego_occ = occ.resize((960,(540-resize_ego_occ)))
rectangle_margin = 10
rectangle_rescale_x = 250
rectangle_rescale_y = 90
rectangle = rectangle.resize((basket_width + 2*rectangle_margin + rectangle_rescale_x, basket_height + 2*rectangle_margin + rectangle_rescale_y))

#set positions
basket_x = 295
baskey_y1 = 175
baskey_y2 = 420
baskey_y3 = 655
alter_occ_y = 265
ego_occ_y = 310
occ_x1 = 147
occ_x2 = 376
occ_x3 = 610
occ_offset = -10 #offset between ego and alter occluders, for perspective

#Define functions to draw images on background
def draw_baskets(a,b,c):
#position 1
    if(a==1):
        background.paste(full_basket, (baskey_y1, basket_x), full_basket)
    else:
        background.paste(empty_basket, (baskey_y1, basket_x), empty_basket)
#position 2
    if(b==1):
        background.paste(full_basket, (baskey_y2, basket_x), full_basket)
    else:
        background.paste(empty_basket, (baskey_y2, basket_x), empty_basket)
#position 3
    if(c==1):
        background.paste(full_basket, (baskey_y3, basket_x), full_basket)
    else:
        background.paste(empty_basket, (baskey_y3, basket_x), empty_basket)

def draw_ego_occluders(a,b,c):
    if (a == 1):
        background.paste(ego_occ, (occ_x1+occ_offset, ego_occ_y), ego_occ)
    else:
        pass
    # position 2
    if (b == 1):
        background.paste(ego_occ, (occ_x2+occ_offset, ego_occ_y), ego_occ)
    else:
        pass
    # position 3
    if (c == 1):
        background.paste(ego_occ, (occ_x3+occ_offset, ego_occ_y), ego_occ)
    else:
        pass
def draw_alter_occluders(a,b,c):
    if (a == 1):
        background.paste(occ, (occ_x1, alter_occ_y), occ)
    else:
        pass
    # position 2
    if (b == 1):
        background.paste(occ, (occ_x2, alter_occ_y), occ)
    else:
        pass
    # position 3
    if (c == 1):
        background.paste(occ, (occ_x3, alter_occ_y), occ)
    else:
        pass

def draw_selection(a):
    if (a==4):
        pass

    elif (a==0):
        background.paste(rectangle, (baskey_y1-rectangle_margin, basket_x-rectangle_margin), rectangle)

    elif (a==1):
        background.paste(rectangle, (baskey_y2-rectangle_margin, basket_x-rectangle_margin), rectangle)

    elif (a==2):
        background.paste(rectangle, (baskey_y3-rectangle_margin, basket_x-rectangle_margin), rectangle)




#define parent function
def draw_scene(ball, alt_a, alt_b, alt_c, eg_a, eg_b, eg_c, selection):
    #draw alter occluders
    draw_alter_occluders(alt_a, alt_b, alt_c)
    #draw baskets/ball
    if (ball==0):
        draw_baskets(1,0,0)
    elif (ball==1):
        draw_baskets(0,1,0)
    elif (ball==2):
        draw_baskets(0,0,1)

    #draw ego occluders
    draw_ego_occluders(eg_a, eg_b, eg_c)

    #draw selection if applicable

    draw_selection(selection)

#create all stimuli
#ball = 1, 2, or 3 for three positions left to right
#alt_a, alt_b, and alt_c can be 0 or 1. If 1, that position will be occluded from avatar
#eg_a, eg_b, eg_c can be 0 or 1. If 1, that position will be occluded from participant


#save every possible prompt stimulus as a jpg
for ball in range(0,3):
    for alt_a in range(0,2):
        for alt_b in range(0,2):
            for alt_c in range(0, 2):
                for eg_a in range(0, 2):
                    for eg_b in range(0, 2):
                        for eg_c in range(0, 2):
                            background = Image.open("stimuli/blank_scene.jpg")
                            draw_scene(ball, alt_a, alt_b, alt_c, eg_a, eg_b, eg_c, 4)
                            background.save("stimuli/" + str(ball) + str(alt_a) + str(alt_b) + str(alt_c) + str(eg_a) + str(eg_b) + str(eg_c)+'.jpg')

#save every possible response slide as a jpg
for ball in range(0,3):
    for alt_a in range(0,2):
        for alt_b in range(0,2):
            for alt_c in range(0, 2):
                for eg_a in range(0, 2):
                    for eg_b in range(0, 2):
                        for eg_c in range(0, 2):
                            for response in range(0,3):
                                background = Image.open("stimuli/blank_scene.jpg")
                                draw_scene(ball, alt_a, alt_b, alt_c, eg_a, eg_b, eg_c, response)
                                background.save("stimuli/" + str(ball) + str(alt_a) + str(alt_b) + str(alt_c) + str(eg_a) + str(eg_b) + str(eg_c) + str(response) + '.jpg')