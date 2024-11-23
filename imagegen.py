import replicate
import os


def generate_image(prompt, size, output_file):
    """
    Generate an image using the specified Replicate model.

    Parameters:
        prompt (str): Text prompt for the image.
        size (str): Size of the output image (e.g., '1365x1024').
        output_file (str): Path to save the generated image.

    Returns:
        bool: True if the image was successfully generated, False otherwise.
    """
    try:
        # Input schema for the model
        input_data = {
            "size": size,
            "prompt": prompt
        }

        # Call the Replicate model
        output = replicate.run(
            "recraft-ai/recraft-v3",
            input=input_data
        )

        # Save the output image
        with open(output_file, "wb") as file:
            file.write(output.read())
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False


def main():
    print("Welcome to the Image Generation Bot!")

    # Get user input for the prompt
    prompt = input(
        "Enter a prompt for the image (e.g., 'a red panda using a laptop in a snowy forest'): ")
    size = input(
        "Enter the desired image size (e.g., '1365x1024', leave empty for default): ")
    size = size.strip() or "1365x1024"  # Default size if not provided

    print("\nGenerating image, please wait...")
    output_file = "output.webp"  # File to save the image

    # Generate the image
    result = generate_image(prompt, size, output_file)

    if result:
        print(f"Image generated successfully! Saved as {output_file}")
    else:
        print("Failed to generate the image. Please check the input and try again.")


if __name__ == "__main__":
    main()
