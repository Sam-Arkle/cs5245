import matplotlib.pyplot as plt
import numpy as np


def usgs_tiling():
    pass


def construct_file_name(lat, lon):
    """ Takes the latitude and longitude as signed integers and
    constructs the appropriate file name for the TIF file. """
    ns_card = 'n'
    ew_card = 'w'
    if lat < 0:
        ns_card = 's'
        lat = abs(lat)
    if lon < 0:
        ew_card = 'w'
        lon = abs(lon)
    file_name = f'USGS_NED_1_{ns_card}{lat:02}{ew_card}{lon:03}_IMG.tif'
    return file_name


def load_trim_image(lat, lon):
    """ Takes the latitude and longitude as signed integers and
    loads the appropriate file and trims it to 3600x3600
    removing the overlap between adjacent tiles. """
    file = construct_file_name(lat, lon)
    print(file)
    image = plt.imread(file)
    image = image[6:-6, 6:-6]
    return image


def stitch_four(lat, lon):
    """load the four images and construct the resulting image:
    # (nw_lat, nw_lon), (nw_lat, nw_lon+1)
    # (nw_lat-1, nw_lon), (nw_lat-1, nw_lon+1)"""
    north_west = load_trim_image(lat, lon)
    north_east = load_trim_image(lat, lon + 1)
    south_w = load_trim_image(lat - 1, lon)
    south_e = load_trim_image(lat - 1, lon + 1)
    top_image = np.concatenate([north_east, north_west], axis=1)
    bottom_image = np.concatenate([south_e, south_w], axis=1)
    image = np.concatenate([top_image, bottom_image], axis=0)
    return image


def get_row(lat, lon_min, num_tiles):
    """ Takes the latitude, minimum longitude, and number of tiles and
    returns an image that combines tiles along a row of different
    longitudes. """
    image = load_trim_image(lat, lon_min)
    for tiles in range(num_tiles - 1):
        lon_min += 1
        new_image = load_trim_image(lat, lon_min)
        image = np.concatenate([image, new_image], axis=1)

    return image


def get_tile_grid(lat_max, lon_min, num_lat, num_lon):
    """ Takes the northwest coordinate (maximum latitude, minimum longitude)
    and the number of tiles in each dimension (num_lat, num_lon) and
    constructs the image containing the entire range. """
    lon_list = []

    for ns_tiles in range(num_lat):
        row_image = get_row(lat_max, lon_min, num_lon)
        lat_max -= 1
        lon_list.append(row_image)
    image = lon_list[0]
    for i in range(1, len(lon_list)):
        image = np.concatenate([image, lon_list[i]], axis=0)

    return image


def get_northwest(lat, lon):
    """ Get the integer coordinates of the northwest corner of the tile
    that contains this decimal (lat, lon) coordinate. """
    nw_lat = int(np.ceil(lat))
    nw_lon = int(np.floor(lon))
    return nw_lat, nw_lon


def get_tile_grid_decimal(northwest, southeast):
    """ Construct the tiled grid of TIF images that contains these
    northwest and southeast decimal coordinates. Each corner
    is a tuple, (lat, lon). """
    n_lon, w_lat = northwest
    lat_max, lon_min = get_northwest(n_lon, w_lat)
    s_lon, e_lat = southeast
    lat_min, lon_max = get_northwest(s_lon, e_lat)
    num_lat = (lat_max - lat_min) + 1
    num_lon = (lon_max - lon_min) + 1
    print('num_lat = ', num_lat)
    print('num_lon = ', num_lon)
    image = get_tile_grid(lat_max, lon_min, num_lat, num_lon)

    return image


# Trim image tests below
# im = load_trim_image(lat=37, lon=-83)
# print(im.shape)
#
# h, w = im.shape
# print(im[h//2-5:h//2+5, w//2-5:w//2+5])
# print(im[:10, :10])
# im = plt.imread('USGS_NED_1_n36w082_IMG.tif')
# print(type(im))
# print(im.shape)
# plt.imshow(im)
# plt.show()
# plt.imshow(load_trim_image(36, 82))
# plt.show()
# im = load_trim_image(37, 83)
# print(im.shape)
# h, w = im.shape
# print(im[h // 2 - 5:h // 2 + 5, w // 2 - 5:w // 2 + 5])
# print(im[:10, :10])
# plt.imshow(im[:32 ,:32])
# plt.show()
# image1 = load_trim_image(37, 83)
# plt.imshow(image1)
# plt.show()
# image = stitch_four(37, 83)
# print(image.shape)
# plt.imshow(image)
# plt.colorbar()
# plt.show()
# im = get_row(37, 82, 3)
# plt.imshow(im)
# plt.colorbar()
# plt.show()
# im = get_tile_grid(38, -84, 2, 3)
# print(im.shape)
# plt.imshow(im)
# plt.colorbar()
# plt.show()
# nw = (37.2, -82.7)
# se = (36.6, -82.5)
# im = get_tile_grid_decimal(nw, se)
# print(im.shape)
# nw = (37.2, -83.7)
# se = (36.6, -81.5)
# im = get_tile_grid_decimal(nw, se)
# print(im.shape)
# plt.imshow(im)
# plt.show()
# nw = (37.5, -82.5)
# se = (36.5, -81.5)
# im = get_tile_grid_decimal(nw, se)
# print(im.shape)
