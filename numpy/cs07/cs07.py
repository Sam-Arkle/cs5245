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
# im = load_trim_image(37, -83)
# print(im.shape)
# h, w = im.shape
# print(im[h // 2 - 5:h // 2 + 5, w // 2 - 5:w // 2 + 5])
# print(im[:10, :10])
# plt.imshow(im[:32, :32])
# plt.colorbar()
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
# =====================================================================================================================


def dec_to_dms(dec):
    """ Convert a decimal longitude or latitude into a DMS tuple
    (degrees, minutes, seconds). """
    if dec < 0:
        degrees = int(np.ceil(dec))
        minutes = int(np.floor((-dec % 1) * 60))
        seconds = int(np.round((((-dec % 1) * 60) % 1) * 60))
    else:
        degrees = int(np.floor(dec))
        minutes = int(np.floor((dec % 1) * 60))
        seconds = int(np.round((((dec % 1) * 60) % 1) * 60))
    return (degrees, minutes, seconds)


def seconds_to_index(seconds):
    """ Convert seconds into an image index. If the seconds are zero, the
    index should be zero. Otherwise, 3599 seconds should map to index 1
    and 1 second should map to 3599. """
    index = 0
    if seconds != 0:
        index = 3600 - seconds
    return index


def get_trim(northwest, southeast):
    """ Determine the number of pixels to crop based on the
    northwest and southeast corner of the region of interest (as tuples). """
    top_num, left_num = northwest
    bottom_num, right_num = southeast

    _, top_min, top_secs = dec_to_dms(top_num)
    top_secs = top_secs + (top_min * 60)
    top = seconds_to_index(top_secs)

    _, bottom_min, bottom_secs = dec_to_dms(bottom_num)
    bottom_secs = bottom_secs + (bottom_min * 60)
    bottom = 3599 - seconds_to_index(bottom_secs)

    _, left_min, left_secs = dec_to_dms(left_num)
    left_secs = left_secs + (left_min * 60)
    left = seconds_to_index(left_secs)

    _, right_min, right_secs = dec_to_dms(right_num)
    right_secs = right_secs + (right_min * 60)
    right = 3599 - seconds_to_index(right_secs)

    return left, right, bottom, top


def get_roi(center, n):
    """ Given the center (lat, lon) coordinate and a number of arc-seconds
    to either side (north, south, east, and west), return the northwest
    and southeast coordinate that define the region of interest:
    (north_latitude, west_longitude), (south_latitude, east_longitude)"""
    x_centre, y_centre = center
    x_c_deg, x_c_min, x_c_sec = dec_to_dms(x_centre)
    x_seconds = x_c_sec + 60 * x_c_min
    y_c_deg, y_c_min, y_c_sec = dec_to_dms(y_centre)
    y_seconds = y_c_sec + 60 * y_c_min

    north_latitude = x_c_deg + (x_seconds + n) / 3600
    west_longitude = y_c_deg - (y_seconds + n) / 3600
    south_latitude = x_c_deg + (x_seconds - n) / 3600
    east_longitude = y_c_deg - (y_seconds - n) / 3600

    northwest = (north_latitude, west_longitude)
    southeast = (south_latitude, east_longitude)
    return northwest, southeast


def crop(im, trim):
    """ Crop the image by the number of pixels specified in 'trim':
    trim = [left, right, bottom, top]. """
    left, right, bottom, top = trim
    image = im[top:-bottom, left:-right]
    if right == 0 & bottom == 0:
        image = im[top:, left:]
    elif bottom == 0:
        image = im[top:, left:-right]
    elif right == 0:
        image = im[top:-bottom, left:]
    return image


def get_extent(northwest, southeast):
    """ Return a 4-tuple containing the extent of the region of interest
    for the plt.imshow function: [left, right, bottom, top]."""
    top, left = northwest
    bottom, right = southeast

    return left, right, bottom, top


def zoom(center, n):
    """ Create a square image centered at (lat, lon) with 2n+1 arc-seconds (pixels)
    high and wide. Also return a list of the extent of the image
    [west_lon, east_lon, south_lat, north_lat]. """
    northwest, southeast = get_roi(center, n)
    image = get_tile_grid_decimal(northwest, southeast)
    left, right, bottom, top = get_trim(northwest, southeast)
    image = crop(image, (left, right, bottom, top))
    extent = get_extent(northwest, southeast)
    return extent, image


# Test dec to dms
# print(dec_to_dms(-81.668611))

# Test seconds to index
# print(seconds_to_index(0))
# print(seconds_to_index(1))
# print(seconds_to_index(100))
# print(seconds_to_index(3599))
#

# Testing get_trim
# nw = (36, -82)
# se = (35 + 1 / 3600, -81 - 1 / 3600)
# print(get_trim(nw, se))
# nw = (36 - 4 / 3600, -82 + 1 / 3600)
# se = (35 + 4 / 3600, -81 - 3 / 3600)
# print(get_trim(nw, se))

# Testing get_roi:
# center = (35+3601/7200, -81-3601/7200)
#
# print(get_roi(center, 1799.5))

# Test crop
# im = np.arange(64).reshape((8, 8))
# print(im)
# print(im.shape)
# im2 = crop(im, (1, 2, 3, 4))
# print(im2)
# print(im2.shape)
# im3 = crop(im, (0, 0, 0, 0))
# print(im3)
# print(im3.shape)

# Test get extent:
# nw = (36, -83)
# se = (34, -81)
# print(get_extent(nw, se))

# Test zoom:
# extent, im = zoom(center=(36.211389, -81.668611), n=100)
# plt.imshow(im, extent=extent)
# plt.colorbar()
# plt.show()
