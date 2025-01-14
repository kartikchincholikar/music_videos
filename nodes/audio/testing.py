import torchaudio
import numpy as np

def get_wav_duration(wav_path):
    """
    Get the duration of a WAV file in seconds using torchaudio.
    
    Args:
        wav_path (str): Path to the WAV file
        
    Returns:
        float: Duration in seconds
    """
    # Load the audio file - returns tuple of (tensor, sample_rate)
    waveform, sample_rate = torchaudio.load(wav_path)
    
    # Get number of frames (first dimension of waveform tensor)
    n_frames = waveform.shape[1]
    
    # Calculate duration
    duration = n_frames / float(sample_rate)
    return duration

def load_timestamps(timestamps_path):
    """
    Load timestamps from a text file.
    
    Args:
        timestamps_path (str): Path to the timestamps file
        
    Returns:
        numpy.ndarray: Array of timestamp values
    """
    # Load timestamps using numpy
    # The file has tab-separated values, and we only need the first column
    timestamps = np.loadtxt(timestamps_path, usecols=0)
    return timestamps

def process_audio_timestamps(wav_path, timestamps_path):
    """
    Process both WAV file and timestamps.
    
    Args:
        wav_path (str): Path to the WAV file
        timestamps_path (str): Path to the timestamps file
        
    Returns:
        tuple: (wav_duration, timestamps)
    """
    # Get WAV duration
    duration = get_wav_duration(wav_path)
    
    # Load timestamps
    timestamps = load_timestamps(timestamps_path)
    print(duration)
    print(timestamps)
    return duration, timestamps

process_audio_timestamps("C:\\Users\\intro\\OneDrive\\Desktop\\audio_lifeitsef.wav","C:\\Users\\intro\\OneDrive\\Desktop\\lifeitself.txt")