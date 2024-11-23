import os
import replicate
import streamlit as st


def generate_video(prompt):
    """
    Generate a video using Replicate's model.

    Parameters:
        prompt (str): The creative prompt for the video.

    Returns:
        str: The URL of the generated video or an error message.
    """
    try:
        # Set the Replicate API token
        replicate.api_token = os.getenv("REPLICATE_API_TOKEN")  # Fetch from environment variable

        if not replicate.api_token:
            return "Error: Replicate API token not found. Please set the REPLICATE_API_TOKEN environment variable."

        # Input schema for the video generation model
        input_data = {
            "prompt": prompt,
            "fps": 24,  # Frames per second
            "duration": 10,  # Duration in seconds
        }

        # Call the Replicate model
        video_url = replicate.run("your-replicate-model/video-generator", input=input_data)

        return video_url  # The URL of the generated video
    except Exception as e:
        return f"Error: {str(e)}"


# Streamlit app
st.title("AI Video Generation Bot 🎥")

# Prompt input from the user
prompt = st.text_input(
    "Enter your creative prompt:",
    placeholder="E.g., A futuristic cityscape at sunset"
)

# Submit button
if st.button("Generate Video"):
    if prompt.strip():
        st.write("Generating your video... This might take a moment. 🚀")

        # Call the video generation function
        video_url = generate_video(prompt)

        if "http" in video_url:
            st.success("Video generated successfully! 🎉")
            st.video(video_url)  # Display the video in Streamlit
        else:
            st.error(f"An error occurred: {video_url}")
    else:
        st.warning("Please enter a valid prompt.")
