import sys


def merge_skylines(skyline1, skyline2):
    i = 0
    j = 0
    h1 = 0
    h2 = 0
    new_height = 0
    result = []

    while i < len(skyline1) and j < len(skyline2):

        prev_height = new_height

        if skyline1[i][0] < skyline2[j][0]:
            x1 = skyline1[i][0]
            h1 = skyline1[i][1]
            new_height = max(h1, h2)
            if new_height != prev_height:
                result.append((x1, new_height))
            i += 1

        else:
            x2 = skyline2[j][0]
            h2 = skyline2[j][1]
            new_height = max(h1, h2)
            if new_height != prev_height:
                result.append((x2, new_height))
            j += 1

    result.extend(skyline1[i:])
    result.extend(skyline2[j:])

    return result


def draw_skyline(buildings):
    n = len(buildings)

    if n == 1:
        b = buildings[0]
        return [(b[0], b[1]), (b[2], 0)]

    else:
        skyline_left = draw_skyline(buildings[n // 2:])
        skyline_right = draw_skyline(buildings[:n // 2])

        return merge_skylines(skyline_left, skyline_right)


if __name__ == '__main__':

    if len(sys.argv) < 2:
        print("Falta archivo de edificios")

    listaEdificios = []
    with open(sys.argv[1]) as fp:
        for line in fp:
            listaEdificios.append([int(e) for e in line.strip('\n\t').split(',')])

    contornoCiudad = draw_skyline(listaEdificios)

    print("Los edificios son " + str(listaEdificios))
    print("El contorno de la ciudad es " + str(contornoCiudad))
