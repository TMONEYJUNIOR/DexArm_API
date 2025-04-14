from pydexarm import Dexarm
import tkinter as tk

# Initialize the Dexarm
dexarm = Dexarm(port="COM10")

# Function to move the arm when the light is red
def move_arm(x, y, z):
    dexarm.move_to(x, y, z)  # Move arm to the specified position
    dexarm.go_home()  # Return the arm to home position

# Create the traffic light cycle
def cycle_lights(canvas, red_light, yellow_light, green_light):
    # Define the colors and their respective durations
    lights = [
        {"color": "red", "duration": 5000},    # Red light for 5 seconds
        {"color": "yellow", "duration": 2000}, # Yellow light for 2 seconds
        {"color": "green", "duration": 4000},  # Green light for 4 seconds
    ]
    current_light = 0

    # Cycle the traffic light indefinitely
    def update_lights():
        nonlocal current_light

        # Reset all lights to gray first
        canvas.itemconfig(red_light, fill="gray")
        canvas.itemconfig(yellow_light, fill="gray")
        canvas.itemconfig(green_light, fill="gray")

        # Get the current light's properties
        light = lights[current_light]
        light_color = light["color"]
        light_duration = light["duration"]

        # Change the light color and perform actions for each light
        if light_color == "red":
            canvas.itemconfig(red_light, fill="red")
            print("Red light: Moving arm!")
            move_arm(10, 410, 0)  # Move the arm during the red light
        elif light_color == "yellow":
            canvas.itemconfig(yellow_light, fill="yellow")
            print("Yellow light: Arm is stationary.")
        elif light_color == "green":
            canvas.itemconfig(green_light, fill="green")
            print("Green light: Moving arm to a green-specific position.")
            move_arm(-280, 410, 0)

        # Move to the next light
        current_light = (current_light + 1) % len(lights)

        # Schedule the next light update based on the current light's duration
        root.after(light_duration, update_lights)

    # Start the update loop
    update_lights()

# Setup for the GUI to show the traffic light cycle
def setup_gui():
    global root
    root = tk.Tk()
    root.title("Traffic Light Cycle")

    # Create a canvas to draw the traffic light
    canvas = tk.Canvas(root, width=200, height=400)
    canvas.pack()

    # Draw the traffic light (a simple vertical rectangle)
    canvas.create_rectangle(50, 50, 150, 350, outline="black", width=2, fill="gold")

    # Create three circles to represent the lights (Red, Yellow, Green)
    red_light = canvas.create_oval(60, 60, 140, 140, fill="gray")  # Start with gray, will change
    yellow_light = canvas.create_oval(60, 160, 140, 240, fill="gray")
    green_light = canvas.create_oval(60, 260, 140, 340, fill="gray")

    # Call the function to start cycling the lights
    cycle_lights(canvas, red_light, yellow_light, green_light)

    root.mainloop()

# Run the GUI setup
setup_gui()

# Close the DexArm connection
dexarm.close()