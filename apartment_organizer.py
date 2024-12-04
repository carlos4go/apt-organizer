import tkinter as tk

# Conversion factor: 1 foot = 24 pixels (1/4 inch = 1 foot)
scale_factor = 24

def create_room():
    try:
        # Check if width and height are provided, otherwise calculate from square footage
        if entry_width.get() and entry_height.get():
            width_ft = float(entry_width.get())
            height_ft = float(entry_height.get())
        else:
            area_sqft = float(entry_area.get())
            aspect_ratio = 3 / 2  # 3:2 width-to-height ratio as a fallback
            width_ft = (area_sqft * aspect_ratio) ** 0.5
            height_ft = width_ft / aspect_ratio
        
        width_px = width_ft * scale_factor
        height_px = height_ft * scale_factor
        
        canvas.delete("all")
        canvas.create_rectangle(50, 50, 50 + width_px, 50 + height_px, outline="black", width=2)
        
        enable_object_inputs()
    except ValueError:
        error_label.config(text="Please enter valid numbers for dimensions or area.")

def enable_object_inputs():
    for widget in object_widgets:
        widget.config(state="normal")

def create_objects():
    draw_object("Sofa", sofa_width.get(), sofa_height.get(), sofa_x.get(), sofa_y.get())
    draw_object("Desk", desk_width.get(), desk_height.get(), desk_x.get(), desk_y.get())
    draw_object("TV", tv_width.get(), tv_height.get(), tv_x.get(), tv_y.get())
    draw_object("TV Console", console_width.get(), console_height.get(), console_x.get(), console_y.get())

def draw_object(name, width, height, x, y):
    try:
        width_px = float(width) * scale_factor
        height_px = float(height) * scale_factor
        x_px = float(x) * scale_factor + 50
        y_px = float(y) * scale_factor + 50
        canvas.create_rectangle(x_px, y_px, x_px + width_px, y_px + height_px, outline="blue", width=2)
        canvas.create_text(x_px + width_px / 2, y_px + height_px / 2, text=name, fill="black")
    except ValueError:
        error_label.config(text=f"Invalid input for {name} dimensions or position.")

root = tk.Tk()
root.title("Apartment Layout Organizer")

# Frame for room dimensions input
room_frame = tk.Frame(root)
room_frame.pack(pady=5)

label_area = tk.Label(room_frame, text="Room Size (sqft, optional):")
label_area.grid(row=0, column=0)
entry_area = tk.Entry(room_frame)
entry_area.grid(row=0, column=1)

label_width = tk.Label(room_frame, text="Room Width (ft):")
label_width.grid(row=1, column=0)
entry_width = tk.Entry(room_frame)
entry_width.grid(row=1, column=1)

label_height = tk.Label(room_frame, text="Room Height (ft):")
label_height.grid(row=2, column=0)
entry_height = tk.Entry(room_frame)
entry_height.grid(row=2, column=1)

button_create_room = tk.Button(room_frame, text="Create Room", command=create_room)
button_create_room.grid(row=3, column=0, columnspan=2, pady=5)

error_label = tk.Label(room_frame, text="", fg="red")
error_label.grid(row=4, column=0, columnspan=2)

# Canvas for drawing
canvas = tk.Canvas(root, width=800, height=400)
canvas.pack(pady=10)

# Frame for object input fields
object_frame = tk.Frame(root)
object_frame.pack(pady=5)

# Sofa inputs
sofa_label = tk.Label(object_frame, text="Sofa (W, H, X, Y ft):")
sofa_label.grid(row=0, column=0)
sofa_width = tk.Entry(object_frame, state="disabled", width=5)
sofa_width.grid(row=0, column=1)
sofa_height = tk.Entry(object_frame, state="disabled", width=5)
sofa_height.grid(row=0, column=2)
sofa_x = tk.Entry(object_frame, state="disabled", width=5)
sofa_x.grid(row=0, column=3)
sofa_y = tk.Entry(object_frame, state="disabled", width=5)
sofa_y.grid(row=0, column=4)

# Desk inputs
desk_label = tk.Label(object_frame, text="Desk (W, H, X, Y ft):")
desk_label.grid(row=1, column=0)
desk_width = tk.Entry(object_frame, state="disabled", width=5)
desk_width.grid(row=1, column=1)
desk_height = tk.Entry(object_frame, state="disabled", width=5)
desk_height.grid(row=1, column=2)
desk_x = tk.Entry(object_frame, state="disabled", width=5)
desk_x.grid(row=1, column=3)
desk_y = tk.Entry(object_frame, state="disabled", width=5)
desk_y.grid(row=1, column=4)

# TV inputs
tv_label = tk.Label(object_frame, text="TV (W, H, X, Y ft):")
tv_label.grid(row=2, column=0)
tv_width = tk.Entry(object_frame, state="disabled", width=5)
tv_width.grid(row=2, column=1)
tv_height = tk.Entry(object_frame, state="disabled", width=5)
tv_height.grid(row=2, column=2)
tv_x = tk.Entry(object_frame, state="disabled", width=5)
tv_x.grid(row=2, column=3)
tv_y = tk.Entry(object_frame, state="disabled", width=5)
tv_y.grid(row=2, column=4)

# TV Console inputs
console_label = tk.Label(object_frame, text="TV Console (W, H, X, Y ft):")
console_label.grid(row=3, column=0)
console_width = tk.Entry(object_frame, state="disabled", width=5)
console_width.grid(row=3, column=1)
console_height = tk.Entry(object_frame, state="disabled", width=5)
console_height.grid(row=3, column=2)
console_x = tk.Entry(object_frame, state="disabled", width=5)
console_x.grid(row=3, column=3)
console_y = tk.Entry(object_frame, state="disabled", width=5)
console_y.grid(row=3, column=4)

button_create_objects = tk.Button(root, text="Add Objects", command=create_objects, state="disabled")
button_create_objects.pack(pady=10)

object_widgets = [
    sofa_width, sofa_height, sofa_x, sofa_y,
    desk_width, desk_height, desk_x, desk_y,
    tv_width, tv_height, tv_x, tv_y,
    console_width, console_height, console_x, console_y,
    button_create_objects
]

root.mainloop()