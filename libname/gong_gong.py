def gong_gong():

    # Import the gong gong files
    import random
    from playsound import playsound

    # Picks an gong gong iamge and sound (7 is danger lel)
    gong_gong_rand_int =  random.randint(1,7)
    gong_gong_image_pick = 'gong_gong_image_lib/gong_' + str(gong_gong_rand_int) + '.txt'
    gong_gong_gong_pick = 'gong_gong_gong_lib/gong_' + str(gong_gong_rand_int) + '.wav'

    # Opens the gong gong image
    f = open(gong_gong_image_pick, 'r')
    lines = f.readlines()

    # Displays the gong gong image
    count = 0
    for line in lines:
        count += 1
        print("{}".format(line.strip()))

    # Plays the gong gong gong
    playsound(gong_gong_gong_pick)