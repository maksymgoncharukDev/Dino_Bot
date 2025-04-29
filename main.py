import pyautogui
import time
from PIL import ImageGrab

# Function to detect obstacles in the defined screen area
def detect_obstacle():
    # Define the bounding box (left, top, right, bottom) where obstacles appear
    box = (100, 350, 300, 400)  # Adjust these coordinates according to your screen and game window
    # Capture a screenshot of the defined area and convert it to grayscale
    screen = ImageGrab.grab(box).convert("L")
    width, height = screen.size

    # Check pixels at intervals (every 5 pixels) to detect obstacles faster
    for x in range(0, width, 5):
        for y in range(0, height, 5):
            if screen.getpixel((x, y)) < 200:  # If the pixel is not white, an obstacle is detected
                return True
    return False

# Function to simulate a jump (spacebar press)
def jump():
    pyautogui.press("space")

# Main function to run the Dino bot
def main():
    print("Starting Dino Bot in 3 seconds...")
    time.sleep(3)  # Wait 3 seconds before starting

    try:
        while True:
            if detect_obstacle():
                jump()
            time.sleep(0.01)  # Small delay to reduce CPU usage
    except KeyboardInterrupt:
        print("\nBot stopped.")  # Graceful shutdown when user presses Ctrl+C

# Entry point of the script
if __name__ == "__main__":              
    main()
