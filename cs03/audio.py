from audio_helpers import load, save
import matplotlib.pyplot as plt

wav_file = input("Enter the WAV file name: ")
# rate is number of audio samples per second
# data is the audio data in a list
rate, data = load(wav_file)
number_of_samples = len(data)
print(f'There are {number_of_samples} samples.\nThe sample rate is {rate} samples/sec.\nThe file is '
      f'{number_of_samples / rate:.3f} seconds long.')
time_axis = [x / rate for x in range(0, number_of_samples)]
plt.plot(time_axis, data)
plt.xlabel('Time (seconds)')
plt.ylabel('sound pressure level')
plt.title(f'Waveform for {wav_file}')
plt.show()
