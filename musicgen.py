# Abot.py

import os
import sys

# Check if the required dependencies are installed, otherwise install them
try:
    import scipy
    from transformers import pipeline, AutoProcessor, MusicgenForConditionalGeneration
    from audiocraft.models import MusicGen
    from audiocraft.data.audio import audio_write
except ImportError:
    print("Required libraries not found. Installing...")
    os.system('pip install --upgrade pip')
    os.system('pip install --upgrade transformers scipy')
    os.system('pip install git+https://github.com/facebookresearch/audiocraft.git')
    os.system('apt-get install ffmpeg')  # Ensure ffmpeg is installed
    sys.exit("Libraries installed. Please run the script again.")


def generate_music_with_transformers():
    """
    Generate music using the Hugging Face Transformers pipeline.
    """
    print("Generating music using Hugging Face Transformers...")
    try:
        # Initialize the text-to-audio synthesizer from the Hugging Face model hub
        synthesizer = pipeline(
            "text-to-audio", model="facebook/musicgen-large")

        # Generate music based on a textual description
        music = synthesizer("lo-fi music with a soothing melody",
                            forward_params={"do_sample": True})

        # Save the generated music as a .wav file
        scipy.io.wavfile.write("musicgen_out_transformers.wav",
                               rate=music["sampling_rate"], data=music["audio"])
        print("Music generated and saved as musicgen_out_transformers.wav.")
    except Exception as e:
        print(f"Error generating music with transformers: {e}")


def generate_music_with_audiocraft():
    """
    Generate music using Audiocraft's MusicGen model.
    """
    print("Generating music using Audiocraft...")
    try:
        # Load the pretrained MusicGen model from Audiocraft
        model = MusicGen.get_pretrained("large")
        model.set_generation_params(duration=8)  # Generate 8 seconds of audio

        # Create a list of descriptions for music generation
        descriptions = ["happy rock", "energetic EDM"]

        # Generate the music samples
        wav = model.generate(descriptions)  # Generates 2 audio samples

        # Save the generated audio files as WAV
        for idx, one_wav in enumerate(wav):
            audio_write(f'{idx}.wav', one_wav.cpu(),
                        model.sample_rate, strategy="loudness")

        print("Music generated and saved as .wav files.")
    except Exception as e:
        print(f"Error generating music with Audiocraft: {e}")


def main():
    """
    Main function to run the app and generate music.
    """
    print("Welcome to Abot - Your Music Generation App!")
    print("Choose an option to generate music:")
    print("1. Use Hugging Face Transformers")
    print("2. Use Audiocraft")

    choice = input("Enter choice (1 or 2): ").strip()

    if choice == "1":
        generate_music_with_transformers()
    elif choice == "2":
        generate_music_with_audiocraft()
    else:
        print("Invalid choice. Please choose 1 or 2.")


if __name__ == "__main__":
    main()


# pip install --upgrade pip
# pip install --upgrade transformers scipy
# pip install git+https://github.com/facebookresearch/audiocraft.git
# apt-get install ffmpeg  # Make sure ffmpeg is installed
