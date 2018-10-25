from PIL import Image

material_colors = [
    (76, 100, 55),
    (125, 95, 44),
    (129, 85, 78),  # ※ Overwrite prohibited ※
    (80, 80, 78),
    (106, 105, 105),
    (54, 63, 50),
    (122, 105, 89),
    (129, 124, 109),
    (149, 148, 148),
    (81, 79, 70),
    (118, 101, 80),
    (75, 87, 59),
    (65, 67, 69),
    (95, 95, 70),
    (64, 53, 36),
    (66, 64, 55),
    (85, 96, 72),
    (81, 82, 81),
    (108, 110, 100),
    (122, 100, 92),
    (125, 115, 99),
    (134, 103, 59),
    (83, 82, 80),
    (124, 94, 85),
    (36, 25, 17),
    (63, 63, 56),
    (90, 106, 75),
    (74, 53, 46),
    (130, 111, 79),
    (81, 82, 81),  # ※ Overwrite prohibited ※
    (108, 110, 100),  # ※ Overwrite prohibited ※
    (76, 100, 55),  # unused
    (108, 98, 48),
    (58, 52, 48),
    (93, 67, 59),
    (55, 38, 29),
    (163, 159, 159),
    (94, 78, 34),
    (64, 56, 49),
    (39, 45, 27),
    (30, 42, 20),
    (43, 62, 22),
    (55, 67, 15),
    (85, 75, 66),
    (34, 80, 104),
    (80, 75, 61),
    (94, 87, 80),
    (107, 107, 109),
    (107, 68, 54),
    (98, 98, 98),
    (47, 46, 42),
    (47, 64, 77),
    (174, 155, 123),
    (123, 133, 139),
    (84, 98, 107),
    (59, 60, 61),
    (131, 123, 106),
    (143, 120, 104),
    (50, 84, 44),
    (135, 116, 99),
    (76, 78, 69),
    (80, 79, 63),
    (151, 141, 106),
    (129, 124, 109),  # unused
    (54, 84, 106),
    (89, 91, 91),
    (102, 96, 84),
    (45, 61, 35),
    (103, 64, 62),
    (47, 53, 31),
    (129, 85, 78),
    (176, 148, 102),
    (114, 99, 86),
    (112, 120, 114),
    (106, 70, 66),
    (98, 97, 93),
    (0, 0, 0),  # unused
    (54, 68, 31),
    (123, 111, 95),
    (90, 105, 70),
    (47, 49, 45),
    (117, 115, 106),
    (69, 63, 57),
    (96, 92, 76),
    (61, 74, 43),
    (97, 85, 47),
    (157, 123, 120),
    (33, 31, 28)
]


def generate_map(data: list, outfile: str, image_base_color=(0, 0, 0)):
    if len(data) != 65536:
        if len(data) < 65536:
            print("Error 2001: Data list is not long enough. Expected 65536 but saw {}".format(len(data)))
            exit(2001)

        print("Error 2002: Data list is too long. Expected 65536 but saw {}".format(len(data)))
        exit(2002)

    material_map_image = Image.new("RGB", (256, 256), image_base_color)

    for index in range(65536):
        x = index % 256
        y = index // 256
        color = lerp_rgb(
            material_colors[data[index].material_0_index],
            material_colors[data[index].material_1_index],
            data[index].blend_weight
        )

        material_map_image.putpixel((x, y), color)

    print("Saving {}...".format(outfile))
    material_map_image.save(outfile)


def generate_material_0_map(data: list, outfile: str, image_base_color=(0, 0, 0), color_as_value=False):
    if len(data) != 65536:
        if len(data) < 65536:
            print("Error 2001: Data list is not long enough. Expected 65536 but saw {}".format(len(data)))
            exit(2001)

        print("Error 2002: Data list is too long. Expected 65536 but saw {}".format(len(data)))
        exit(2002)

    material_map_image = Image.new("RGB", (256, 256), image_base_color)

    for index in range(65536):
        x = index % 256
        y = index // 256
        color = material_colors[data[index].material_0_index]

        if color_as_value:
            color_value = data[index].material_1_index
            color = (color_value, color_value, color_value)

        material_map_image.putpixel((x, y), color)

    print("Saving {}...".format(outfile))
    material_map_image.save(outfile)


def generate_material_1_map(data: list, outfile: str, image_base_color=(0, 0, 0), color_as_value=False):
    if len(data) != 65536:
        if len(data) < 65536:
            print("Error 2001: Data list is not long enough. Expected 65536 but saw {}".format(len(data)))
            exit(2001)

        print("Error 2002: Data list is too long. Expected 65536 but saw {}".format(len(data)))
        exit(2002)

    material_map_image = Image.new("RGB", (256, 256), image_base_color)

    for index in range(65536):
        x = index % 256
        y = index // 256
        color = material_colors[data[index].material_1_index]

        if color_as_value:
            color_value = data[index].material_1_index
            color = (color_value, color_value, color_value)

        material_map_image.putpixel((x, y), color)

    print("Saving {}...".format(outfile))
    material_map_image.save(outfile)


def lerp_rgb(color_0: tuple, color_1: tuple, weight: float) -> tuple:
    """
    Performs linear interpolation on the RGB values of two colors

    :param color_0:
    :param color_1:
    :param weight:
    :return:
    """
    return (
        (int((1 - weight) * color_0[0] + weight * color_1[0])),
        (int((1 - weight) * color_0[1] + weight * color_1[1])),
        (int((1 - weight) * color_0[2] + weight * color_1[2]))
    )
