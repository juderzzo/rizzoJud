import random
f = open("image.ppm", "w")

##true randomness
f.write("P3\n500 500\n255\n")
for a in range(500):
    for b in range(500):
        f.write(str(random.randint(0, 256)) + ' ' + str(random.randint(0, 256))+ ' '+str(random.randint(0, 256)))
        f.write("\n")
f.close()
