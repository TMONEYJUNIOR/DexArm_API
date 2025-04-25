from pydexarm import Dexarm
import tkinter as tk
import threading

# Initialize the Dexarm
dexarm = Dexarm(port="COM10")

# Function to move the arm when the light is green
def move_arm(x, y, z):
    dexarm.move_to(x, y, z)  # Move arm to the specified position
    dexarm.go_home()  # Return the arm to home position

# A wrapper function to run `move_arm` in a separate thread
def move_arm_async(x, y, z):
    threading.Thread(target=move_arm, args=(x, y, z), daemon=True).start()

# Create the traffic light cycle
def cycle_lights(canvas, red_light, yellow_light, green_light):
    # Reversed order: Green → Yellow → Red
    colors = ["green", "yellow", "red"]
    durations = [4000, 2000, 5000]  # Durations in milliseconds for each light (green, yellow, red)
    current_color = 0

    # Cycle the traffic light indefinitely
    def update_lights():
        nonlocal current_color

        # Reset all lights to gray first
        canvas.itemconfig(red_light, fill="gray")
        canvas.itemconfig(yellow_light, fill="gray")
        canvas.itemconfig(green_light, fill="gray")

        # Get the current light's properties
        light_color = colors[current_color]
        duration = durations[current_color]

        # Change the light color and perform actions for each light
        if light_color == "green":
            canvas.itemconfig(green_light, fill="green")
            print("Green light: Moving arm to a green-specific position.")
            move_arm_async(10, 410, 0)  # Move the arm asynchronously during the green light
            
        elif light_color == "yellow":
            canvas.itemconfig(yellow_light, fill="yellow")
            print("Yellow light: Arm is stationary.")
            
        elif light_color == "red":
            canvas.itemconfig(red_light, fill="red")
            print("Red light: Moving arm to a red-specific position.")

        # Move to the next light
        current_color = (current_color + 1) % len(colors)

        # Schedule the next light update based on the duration
        root.after(duration, update_lights)

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