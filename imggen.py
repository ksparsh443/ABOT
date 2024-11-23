from diffusers import StableDiffusionPipeline
import torch

# Your Hugging Face API key
api_key = "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"

# Set up the pipeline using the model ID from Hugging Face
model_id = "runwayml/stable-diffusion-v1-5"
pipe = StableDiffusionPipeline.from_pretrained(
    model_id, use_auth_token=api_key, torch_dtype=torch.float16)

# Move the pipeline to GPU for faster performance (if available)
pipe = pipe.to("cuda")

# Define the prompt for the image
prompt = "a photo of an astronaut riding a horse on mars"

# Generate the image based on the prompt
image = pipe(prompt).images[0]

# Save the generated image
image.save("astronaut_rides_horse.png")
