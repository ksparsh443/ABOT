import replicate
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the API token from the environment variable
# REPLICATE_API_TOKEN = os.getenv("REPLICATE_API_TOKEN")

# Check if the token is set
if tok is None:
    raise ValueError("REPLICATE_API_TOKEN is not set in the .env file")

# Set the API token in the environment variable
os.environ[""] = tok


def generate_video(prompt, num_frames=50):
    """
    Generate a video using the replicate model and return the URL or error message.

    Parameters:
        prompt (str): The prompt for video generation.
        num_frames (int): Number of frames to generate.

    Returns:
        str: URL of the generated video or error message.
    """
    try:
        # Define input parameters for the model
        input_data = {
            "prompt": prompt,
            "num_frames": num_frames
        }

        # Call the replicate model
        output = replicate.run(
            "cjwbw/damo-text-to-video:1e205ea73084bd17a0a3b43396e49ba0d6bc2e754e9283b2df49fad2dcf95755",
            input=input_data
        )

        # Return the output URL
        return output if output else "Model returned no output."

    except Exception as e:
        return f"Error: {str(e)}"


# Example usage
if __name__ == "__main__":
    prompt = "A panda eating bamboo on a rock."
    video_url = generate_video(prompt)

    # Check if a valid URL was returned
    if video_url and isinstance(video_url, str) and "http" in video_url:
        print(f"Generated video is available at: {video_url}")
    else:
        print(f"Failed to generate video. Response: {video_url}")
