import colorsys

def round(num):
    num += 255
    return num % 255

def minMax(num):
    if num < 0:
        return 0
    if num > 255:
        return 255
    return num

def hsv_to_hexa(h, s, v):
    rgb = colorsys.hsv_to_rgb(h/float(255), s/float(255), v/float(255))
    hexa = '#%02x%02x%02x' % (int(rgb[0]*255), int(rgb[1]*255), int(rgb[2]*255))
    return hexa

def create_split(h, s, v, hue_change, saturation_change, value_change):
    hnew = round(h + hue_change)
    snew = minMax(s + saturation_change)
    vnew = minMax(v + value_change)
    return [hsv_to_hexa(hnew, snew, vnew), [hnew, snew, vnew]]

def process_hsv(h, s, v):
    orig_hexa = hsv_to_hexa(h, s, v)

    splits = []
    curr = create_split(h, s, v, 0, 0, 0)

    # splits
    hue_split_light = [create_split(h, s, v, -25, 0, 0), 
                       create_split(h, s, v, -25, 0, 0), 
                       curr, 
                       create_split(h, s, v, 25, 0, 0), 
                       create_split(h, s, v, 25, 0, 0)]
    splits.append(hue_split_light)

    hue_split_mid = [create_split(h, s, v, -50, 0, 0), 
                     create_split(h, s, v, -50, 0, 0), 
                     curr, 
                     create_split(h, s, v, 50, 0, 0), 
                     create_split(h, s, v, 50, 0, 0)]
    splits.append(hue_split_mid)

    hue_split_tiered = [create_split(h, s, v, -40, 0, 0), 
                        create_split(h, s, v, -30, 0, 0), 
                        create_split(h, s, v, -20, 0, 0),
                        create_split(h, s, v, -10, 0, 0),
                        curr, 
                        create_split(h, s, v, 10, 0, 0),
                        create_split(h, s, v, 20, 0, 0),
                        create_split(h, s, v, 30, 0, 0),
                        create_split(h, s, v, 40, 0, 0),
                        create_split(h, s, v, 127.5, 0, 0),
                        create_split(h, s, v, 127.5, 0, 0),
                        create_split(h, s, v, 127.5, 0, 0)]
    splits.append(hue_split_tiered)

    hue_split_tiered_hs_1 = [create_split(h, s, v, -40, -20, -20), 
                            create_split(h, s, v, -30, -20, -20), 
                            create_split(h, s, v, -20, -20, -20),
                            create_split(h, s, v, -10, -20, -20),
                            create_split(h, s, v, 0, -20, -20), 
                            create_split(h, s, v, 10, -20, -20),
                            create_split(h, s, v, 20, -20, -20),
                            create_split(h, s, v, 30, -20, -20),
                            create_split(h, s, v, 40, -20, -20),
                            create_split(h, s, v, 127.5, 20, 20),
                            create_split(h, s, v, 127.5, 20, 20),
                            create_split(h, s, v, 127.5, 20, 20)]
    splits.append(hue_split_tiered_hs_1)

    hue_split_tiered_hs_2 = [create_split(h, s, v, -40, -20, 20), 
                            create_split(h, s, v, -30, -20, 20), 
                            create_split(h, s, v, -20, -20, 20),
                            create_split(h, s, v, -10, -20, 20),
                            create_split(h, s, v, 0, -20, 20), 
                            create_split(h, s, v, 10, -20, 20),
                            create_split(h, s, v, 20, -20, 20),
                            create_split(h, s, v, 30, -20, 20),
                            create_split(h, s, v, 40, -20, 20),
                            create_split(h, s, v, 127.5, 20, -20),
                            create_split(h, s, v, 127.5, 20, -20),
                            create_split(h, s, v, 127.5, 20, -20)]
    splits.append(hue_split_tiered_hs_2)

    hue_split_tiered_hs_3 = [create_split(h, s, v, -40, 20, -20), 
                            create_split(h, s, v, -30, 20, -20), 
                            create_split(h, s, v, -20, 20, -20),
                            create_split(h, s, v, -10, 20, -20),
                            create_split(h, s, v, 0, 20, -20), 
                            create_split(h, s, v, 10, 20, -20),
                            create_split(h, s, v, 20, 20, -20),
                            create_split(h, s, v, 30, 20, -20),
                            create_split(h, s, v, 40, 20, -20),
                            create_split(h, s, v, 127.5, -20, 20),
                            create_split(h, s, v, 127.5, -20, 20),
                            create_split(h, s, v, 127.5, -20, 20)]
    splits.append(hue_split_tiered_hs_3)

    hue_split_tiered_hs_4 = [create_split(h, s, v, -40, 20, 20), 
                            create_split(h, s, v, -30, 20, 20), 
                            create_split(h, s, v, -20, 20, 20),
                            create_split(h, s, v, -10, 20, 20),
                            create_split(h, s, v, 0, 20, 20), 
                            create_split(h, s, v, 10, 20, 20),
                            create_split(h, s, v, 20, 20, 20),
                            create_split(h, s, v, 30, 20, 20),
                            create_split(h, s, v, 40, 20, 20),
                            create_split(h, s, v, 127.5, -20, -20),
                            create_split(h, s, v, 127.5, -20, -20),
                            create_split(h, s, v, 127.5, -20, -20)]
    splits.append(hue_split_tiered_hs_4)

    hue_split_triangle = [create_split(h, s, v, -85, 0, 0), 
                          create_split(h, s, v, -85, 0, 0), 
                          curr, 
                          create_split(h, s, v, 85, 0, 0), 
                          create_split(h, s, v, 85, 0, 0)]
    splits.append(hue_split_triangle)

    hue_split_saturation = [create_split(h, s, v, 0, -70, -40),
                            create_split(h, s, v, 0, -60, -30),
                            create_split(h, s, v, 0, -30, -15),
                            curr,
                            create_split(h, s, v, 0, 30, 15),
                            create_split(h, s, v, 0, 60, 30),
                            create_split(h, s, v, 0, 70, 40)]
    splits.append(hue_split_saturation)

    hue_split_saturation_rev = [create_split(h, s, v, 0, -70, 40),
                                create_split(h, s, v, 0, -60, 30),
                                create_split(h, s, v, 0, -30, 15),
                                curr,
                                create_split(h, s, v, 0, 30, -15),
                                create_split(h, s, v, 0, 60, -30),
                                create_split(h, s, v, 0, 70, -40)]
    splits.append(hue_split_saturation_rev)

    ld_1 = [create_split(h, s, v, -40, -70, 40),
            create_split(h, s, v, -30, -60, 30),
            create_split(h, s, v, -15, -30, 15),
            curr,
            create_split(h, s, v, 15, 30, -15),
            create_split(h, s, v, 30, 60, -30),
            create_split(h, s, v, 40, 70, -40)]
    splits.append(ld_1)

    ld_2 = [create_split(h, s, v, 40, -70, 40),
            create_split(h, s, v, 30, -60, 30),
            create_split(h, s, v, 15, -30, 15),
            curr,
            create_split(h, s, v, -15, 30, -15),
            create_split(h, s, v, -30, 60, -30),
            create_split(h, s, v, -40, 70, -40)]
    splits.append(ld_2)

    ld_3 = [create_split(h, s, v, -40, -70, -40),
            create_split(h, s, v, -30, -60, -30),
            create_split(h, s, v, -15, -30, -15),
            curr,
            create_split(h, s, v, 15, 30, 15),
            create_split(h, s, v, 30, 60, 30),
            create_split(h, s, v, 40, 70, 40)]
    splits.append(ld_3)

    ld_4 = [create_split(h, s, v, 40, -70, -40),
            create_split(h, s, v, 30, -60, -30),
            create_split(h, s, v, 15, -30, -15),
            curr,
            create_split(h, s, v, -15, 30, 15),
            create_split(h, s, v, -30, 60, 30),
            create_split(h, s, v, -40, 70, 40)]
    splits.append(ld_4)

    hue_split_o_half = [create_split(h, s, v, 60, 0, 0), 
                        create_split(h, s, v, 40, 0, 0),
                        create_split(h, s, v, 30, 0, 0),
                        create_split(h, s, v, 20, 0, 0),
                        create_split(h, s, v, 10, 0, 0),
                        create_split(h, s, v, 167.5, 0, 0),
                        create_split(h, s, v, 167.5, 0, 0),
                        create_split(h, s, v, 167.5, 0, 0)]
    splits.append(hue_split_o_half)

    hue_split_o_half_1 = [create_split(h, s, v, 60, -50, -50), 
                        create_split(h, s, v, 40, -40, -40),
                        create_split(h, s, v, 30, -30, -30),
                        create_split(h, s, v, 20, -20, -20),
                        create_split(h, s, v, 10, -10, -10),
                        create_split(h, s, v, 167.5, 30, 30),
                        create_split(h, s, v, 167.5, 30, 30),
                        create_split(h, s, v, 167.5, 30, 30)]
    splits.append(hue_split_o_half_1)

    hue_split_o_half_2 = [create_split(h, s, v, 60, -50, 50), 
                        create_split(h, s, v, 40, -40, 40),
                        create_split(h, s, v, 30, -30, 30),
                        create_split(h, s, v, 20, -20, 20),
                        create_split(h, s, v, 10, -10, 10),
                        create_split(h, s, v, 167.5, 30, -30),
                        create_split(h, s, v, 167.5, 30, -30),
                        create_split(h, s, v, 167.5, 30, -30)]
    splits.append(hue_split_o_half_2)

    hue_split_o_half_3 = [create_split(h, s, v, 60, 50, -50), 
                        create_split(h, s, v, 40, 40, -40),
                        create_split(h, s, v, 30, 30, -30),
                        create_split(h, s, v, 20, 20, -20),
                        create_split(h, s, v, 10, 10, -10),
                        create_split(h, s, v, 167.5, -30, 30),
                        create_split(h, s, v, 167.5, -30, 30),
                        create_split(h, s, v, 167.5, -30, 30)]
    splits.append(hue_split_o_half_3)

    hue_split_o_half_4 = [create_split(h, s, v, 60, 50, 50), 
                        create_split(h, s, v, 40, 40, 40),
                        create_split(h, s, v, 30, 30, 30),
                        create_split(h, s, v, 20, 20, 20),
                        create_split(h, s, v, 10, 10, 10),
                        create_split(h, s, v, 167.5, -30, -30),
                        create_split(h, s, v, 167.5, -30, -30),
                        create_split(h, s, v, 167.5, -30, -30)]
    splits.append(hue_split_o_half_4)

    hue_split_half = [create_split(h, s, v, -60, 0, 0), 
                      create_split(h, s, v, -40, 0, 0),
                      create_split(h, s, v, -30, 0, 0),
                      create_split(h, s, v, -20, 0, 0),
                      create_split(h, s, v, -10, 0, 0),
                      create_split(h, s, v, 87.5, 0, 0),
                      create_split(h, s, v, 87.5, 0, 0),
                      create_split(h, s, v, 87.5, 0, 0)]
    splits.append(hue_split_half)

    hue_split_half_1 = [create_split(h, s, v, -60, -50, -50), 
                      create_split(h, s, v, -40, -40, -40),
                      create_split(h, s, v, -30, -30, -30),
                      create_split(h, s, v, -20, -20, -20),
                      create_split(h, s, v, -10, -10, -10),
                      create_split(h, s, v, 87.5, 30, 30),
                      create_split(h, s, v, 87.5, 30, 30),
                      create_split(h, s, v, 87.5, 30, 30)]
    splits.append(hue_split_half_1)

    hue_split_half_2 = [create_split(h, s, v, -60, -50, 50), 
                      create_split(h, s, v, -40, -40, 40),
                      create_split(h, s, v, -30, -30, 30),
                      create_split(h, s, v, -20, -20, 20),
                      create_split(h, s, v, -10, -10, 10),
                      create_split(h, s, v, 87.5, 30, -30),
                      create_split(h, s, v, 87.5, 30, -30),
                      create_split(h, s, v, 87.5, 30, -30)]
    splits.append(hue_split_half_2)

    hue_split_half_3 = [create_split(h, s, v, -60, 50, -50), 
                      create_split(h, s, v, -40, 40, -40),
                      create_split(h, s, v, -30, 30, -30),
                      create_split(h, s, v, -20, 20, -20),
                      create_split(h, s, v, -10, 10, -10),
                      create_split(h, s, v, 87.5, -30, 30),
                      create_split(h, s, v, 87.5, -30, 30),
                      create_split(h, s, v, 87.5, -30, 30)]
    splits.append(hue_split_half_3)

    hue_split_half_4 = [create_split(h, s, v, -60, 50, 50), 
                      create_split(h, s, v, -40, 40, 40),
                      create_split(h, s, v, -30, 30, 30),
                      create_split(h, s, v, -20, 20, 20),
                      create_split(h, s, v, -10, 10, 10),
                      create_split(h, s, v, 87.5, -30, -30),
                      create_split(h, s, v, 87.5, -30, -30),
                      create_split(h, s, v, 87.5, -30, -30)]
    splits.append(hue_split_half_4)

    complementary = [create_split(h, s, v, 167.5, 0, 0),
                     create_split(h, s, v, 157.5, 0, 0),
                     create_split(h, s, v, 147.5, 0, 0),
                     create_split(h, s, v, 137.5, 0, 0),
                     create_split(h, s, v, 127.5, 0, 0),
                     create_split(h, s, v, 127.5, 0, 0),
                     create_split(h, s, v, 117.5, 0, 0),
                     create_split(h, s, v, 107.5, 0, 0),
                     create_split(h, s, v, 97.5, 0, 0),
                     create_split(h, s, v, 87.5, 0, 0),
                     curr,
                     curr,
                     curr]
    splits.append(complementary)

    complementary_1 = [create_split(h, s, v, 167.5, 20, 20),
                     create_split(h, s, v, 157.5, 20, 20),
                     create_split(h, s, v, 147.5, 20, 20),
                     create_split(h, s, v, 137.5, 20, 20),
                     create_split(h, s, v, 127.5, 20, 20),
                     create_split(h, s, v, 127.5, 20, 20),
                     create_split(h, s, v, 117.5, 20, 20),
                     create_split(h, s, v, 107.5, 20, 20),
                     create_split(h, s, v, 97.5, 20, 20),
                     create_split(h, s, v, 87.5, 20, 20),
                     create_split(h, s, v, 0, -20, -20),
                     create_split(h, s, v, 0, -20, -20),
                     create_split(h, s, v, 0, -20, -20)]
    splits.append(complementary_1)

    complementary_2 = [create_split(h, s, v, 167.5, -20, -20),
                     create_split(h, s, v, 157.5, -20, -20),
                     create_split(h, s, v, 147.5, -20, -20),
                     create_split(h, s, v, 137.5, -20, -20),
                     create_split(h, s, v, 127.5, -20, -20),
                     create_split(h, s, v, 127.5, -20, -20),
                     create_split(h, s, v, 117.5, -20, -20),
                     create_split(h, s, v, 107.5, -20, -20),
                     create_split(h, s, v, 97.5, -20, -20),
                     create_split(h, s, v, 87.5, -20, -20),
                     create_split(h, s, v, 0, 20, 20),
                     create_split(h, s, v, 0, 20, 20),
                     create_split(h, s, v, 0, 20, 20)]
    splits.append(complementary_2)

    complementary_3 = [create_split(h, s, v, 167.5, -20, 20),
                     create_split(h, s, v, 157.5, -20, 20),
                     create_split(h, s, v, 147.5, -20, 20),
                     create_split(h, s, v, 137.5, -20, 20),
                     create_split(h, s, v, 127.5, -20, 20),
                     create_split(h, s, v, 127.5, -20, 20),
                     create_split(h, s, v, 117.5, -20, 20),
                     create_split(h, s, v, 107.5, -20, 20),
                     create_split(h, s, v, 97.5, -20, 20),
                     create_split(h, s, v, 87.5, -20, 20),
                     create_split(h, s, v, 0, 20, -20),
                     create_split(h, s, v, 0, 20, -20),
                     create_split(h, s, v, 0, 20, -20)]
    splits.append(complementary_3)

    complementary_4 = [create_split(h, s, v, 167.5, 20, -20),
                     create_split(h, s, v, 157.5, 20, -20),
                     create_split(h, s, v, 147.5, 20, -20),
                     create_split(h, s, v, 137.5, 20, -20),
                     create_split(h, s, v, 127.5, 20, -20),
                     create_split(h, s, v, 127.5, 20, -20),
                     create_split(h, s, v, 117.5, 20, -20),
                     create_split(h, s, v, 107.5, 20, -20),
                     create_split(h, s, v, 97.5, 20, -20),
                     create_split(h, s, v, 87.5, 20, -20),
                     create_split(h, s, v, 0, -20, 20),
                     create_split(h, s, v, 0, -20, 20),
                     create_split(h, s, v, 0, -20, 20)]
    splits.append(complementary_4)

    return [orig_hexa, splits]