from scipy.io.wavfile import read
from numpy import array
from scipy.io.wavfile import write


def load(file_name):
    rate, data = read(file_name)
    data = list(data)
    return rate, data


def save(file_name, rate, data):
    data = array(data, dtype='int16')
    write(file_name, rate, data)