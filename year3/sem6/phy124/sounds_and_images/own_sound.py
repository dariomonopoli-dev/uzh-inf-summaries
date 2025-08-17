import numpy as np
import scipy.io.wavfile as wavfile


def note(frequency, duration, amplitude=4096, sample_rate=44100):
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    note_wave = amplitude * np.sin(2 * np.pi * frequency * t)
    return note_wave


def chord(notes, duration, amplitude=4096, sample_rate=44100):

    # Generates a chord from a list of note frequencies.

    chord_wave = sum(
        note(frequency, duration, amplitude, sample_rate) for frequency in notes
    )

    # Normalize amplitude
    max_amp = np.max(np.abs(chord_wave))
    if max_amp > 0:
        chord_wave = chord_wave / max_amp * amplitude
    return chord_wave


# C major chord
frequencies = [
    262,
    294,
    330,
    349,
    392,
    392,
    440,
    440,
    440,
    440,
    392,
    440,
    440,
    440,
    440,
    392,
    349,
    349,
    349,
    349,
    330,
    330,
    392,
    392,
    392,
    392,
    262,
]  # Hz


# sound_wave = chord(frequencies, duration=2)
def flatten(xss):
    return [x for xs in xss for x in xs]


song = [note(freq, 1) for freq in frequencies]
song = np.array(flatten(song))


# song = flatten(song)
filename = "c_major_chord.wav"
wavfile.write(filename, 44100, song.astype(np.int16))

print(f"Generated sound saved to {filename}")
