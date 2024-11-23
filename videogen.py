import streamlit as st
from services.replicate_service import generate_video

st.title("AI Video Generation Bot 🎥")

# Prompt input from the user
prompt = st.text_input("Enter your creative prompt:",
                       placeholder="E.g., A futuristic cityscape at sunset")

# Submit button
if st.button("Generate Video"):
    if prompt.strip():
        st.write("Generating your video... This might take a moment.")

        # Call the video generation function
        video_url = generate_video(prompt)

        if "http" in video_url:
            st.success("Video generated successfully! 🎉")
            st.video(video_url)  # Display the video in Streamlit
        else:
            st.error(f"An error occurred: {video_url}")
    else:
        st.warning("Please enter a valid prompt.")
