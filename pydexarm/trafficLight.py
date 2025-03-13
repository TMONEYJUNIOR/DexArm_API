from pydexarm import Dexarm
import time
import tkinter as tk

# Initialize the Dexarm
dexarm = Dexarm(port="COM10")

# Function to move the arm when the light is red
def move_arm():
    dexarm.move_to(-150, 235, -50)  # Move arm to the specified position
    dexarm.go_home()  # Return the arm to home position

# Create the traffic light cycle
def traffic_light_cycle(canvas, light_label):
    # Colors for traffic light
    colors = ["red", "yellow", "green"]
    current_color = 0

    while True:
        # Red light
        if colors[current_color] == "red":
            canvas.itemconfig(light_label, fill="red")
            print("Red light: Moving arm!")
            move_arm()

        # Yellow light
        elif colors[current_color] == "yellow":
            canvas.itemconfig(light_label, fill="yellow")
            print("Yellow light: Arm is stationary.")
        
        # Green light
        elif colors[current_color] == "green":
            canvas.itemconfig(light_label, fill="green")
            print("Green light: Arm is stationary.")
        
        # Cycle to next color
        current_color = (current_color + 1) % len(colors)
        time.sleep(3)  # Wait for 3 seconds before switching to the next color
        canvas.after(0)  # Update the canvas

# Setup for the GUI to show the traffic light cycle
def setup_gui():
    root = tk.Tk()
    root.title("Traffic Light Cycle")

    # Create a canvas to draw the traffic light
    canvas = tk.Canvas(root, width=200, height=400)
    canvas.pack()

    # Draw the traffic light (a simple vertical rectangle)
    canvas.create_rectangle(50, 50, 150, 350, outline="black", width=2)
    
    # Create three circles to represent the lights (Red, Yellow, Green)
    red_light = canvas.create_oval(60, 60, 140, 140, fill="gray")  # Start with gray, will change
    yellow_light = canvas.create_oval(60, 160, 140, 240, fill="gray")
    green_light = canvas.create_oval(60, 260, 140, 340, fill="gray")

    # Function to cycle the lights
    def cycle_lights():
        # Red
        canvas.itemconfig(red_light, fill="red")
        canvas.itemconfig(yellow_light, fill="gray")
        canvas.itemconfig(green_light, fill="gray")
        move_arm()  # Move the arm when red
        time.sleep(3)
        
        # Yellow
        canvas.itemconfig(red_light, fill="gray")
        canvas.itemconfig(yellow_light, fill="yellow")
        canvas.itemconfig(green_light, fill="gray")
        print("Yellow light: Arm is stationary.")
        time.sleep(2)
        
        # Green
        canvas.itemconfig(red_light, fill="gray")
        canvas.itemconfig(yellow_light, fill="gray")
        canvas.itemconfig(green_light, fill="green")
        print("Green light: Arm is stationary.")
        time.sleep(3)
        
        # Loop back to Red
        cycle_lights()

    # Run the traffic light cycle in the background
    root.after(0, cycle_lights)
    
    root.mainloop()

# Run the GUI setup
setup_gui()

# Close the DexArm connection
dexarm.close()
