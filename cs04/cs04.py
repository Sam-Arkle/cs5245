import matplotlib.pyplot as plt


def get_times(num_samples, start_time, sample_rate):
    # write your code here to create the new list of times 'x'
    time_list = [start_time + (x / sample_rate) for x in range(0, num_samples)]
    return time_list


def scale(audio_data, scale_factor):
    scaled_audio_data = [scale_factor * x for x in audio_data]
    return scaled_audio_data


def clip(audio_data):
    clipped_audio = [32767 if x > 32767 else -32768 if x < -32768 else x for x in audio_data]
    return clipped_audio


def zoom(time_list, audio_data, start_index, num_samples):
    zoomed_audio_data = audio_data[start_index:num_samples]
    zoomed_time_list = time_list[start_index:num_samples]
    return zoomed_time_list, zoomed_audio_data


def double_pitch(audio_data):
    doubled_pitch_data = audio_data[::2]
    return doubled_pitch_data


def half_pitch(audio_data):
    half_pitched_data = [x for y in zip(audio_data, audio_data) for x in y]
    return half_pitched_data


def plot_audio(time_list, audio_data, title):
    plt.plot(time_list, audio_data)
    plt.xlabel('Time (seconds)')
    plt.ylabel('Amplitude')
    plt.title(title)
    file_name = title + '.png'
    plt.savefig(file_name)
    return plt
