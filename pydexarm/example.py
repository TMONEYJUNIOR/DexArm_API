from pydexarm import Dexarm
import time
import tkinter as tk

# Initialize the Dexarm
dexarm = Dexarm(port="COM10")

# Function to move the arm when the light is red
def move_arm():
    dexarm.move_to(10, 410, 0)  # Move arm to the specified position
    dexarm.go_home()  # Return the arm to home position

# Create the traffic light cycle
def cycle_lights(canvas, red_light, yellow_light, green_light):
    colors = ["red", "yellow", "green"]
    current_color = 0

    # Cycle the traffic light indefinitely
    def update_lights():
        nonlocal current_color

        # Reset all lights to gray first
        canvas.itemconfig(red_light, fill="gray")
        canvas.itemconfig(yellow_light, fill="gray")
        canvas.itemconfig(green_light, fill="gray")

        # Change the color based on the current light
        if colors[current_color] == "red":
            canvas.itemconfig(red_light, fill="red")
            print("Red light: Moving arm!")
            move_arm()  # Move the arm when red
            
        elif colors[current_color] == "yellow":
            canvas.itemconfig(yellow_light, fill="yellow")
            print("Yellow light: Arm is stationary.")

        elif colors[current_color] == "green":
            canvas.itemconfig(green_light, fill="green")
            print("Green light: Arm is stationary.")
            
        # Update the light color every 3 seconds
        current_color = (current_color + 1) % len(colors)
        # Set the next update
        root.after(3000, update_lights)  # 3000ms = 3 seconds

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
# END OF PROGRAM