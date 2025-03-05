import tkinter as tk
from tkvideo import tkvideo
from threading import Thread
from playsound import playsound
import random

# Global variables to store the captain's room details
captain_room = None
largest_dimension = None

# Function to play sound using playsound
def play_sound(audio_path):
    playsound(audio_path, block=False)
    print(f'Playing sound: {audio_path}')

# Function to start playing the sound in a separate thread
def start_sound_thread(audio_path):
    sound_thread = Thread(target=play_sound, args=(audio_path,))
    sound_thread.start()

# Function to update video and sound
def update_media(video_label, video_paths, audio_paths, index):
    video_label.destroy()
    video_label = tk.Label(root)
    video_label.pack()

    player = tkvideo(video_paths[index], video_label, loop=0, size=(1220, 640))
    player.play()
    start_sound_thread(audio_paths[index])
    return video_label

# Generate random dimensions for the rooms
def generate_random_dimensions():
    length = random.randint(10, 50)  # Random length between 10 and 50 meters
    breadth = random.randint(10, 50)  # Random breadth between 10 and 50 meters
    return length, breadth

# Function to find and display the captain's room based on the largest room dimensions
def find_captains_room(k):
    num_rooms = k + 1
    room_numbers = [random.randint(100, 999) for _ in range(num_rooms)]
    room_dimensions = [generate_random_dimensions() for _ in range(num_rooms)]

    room_areas = [length * breadth for length, breadth in room_dimensions]
    largest_area = max(room_areas)
    captain_room_index = room_areas.index(largest_area)
    captain_room = room_numbers[captain_room_index]
    largest_dimension = room_dimensions[captain_room_index]

    return captain_room, largest_dimension

# List of video and corresponding audio paths
video_paths = [
    r"C:\Users\PC\Downloads\ffirst.mp4",
    r"C:\Users\PC\Downloads\second.mp4",
    r"C:\Users\PC\Downloads\third.mp4",
    r"C:\Users\PC\Downloads\fourth.mp4",
    #r"C:\Users\PC\Downloads\fifth.mp4",
    r"C:\Users\PC\Downloads\sixth.mp4",
]

audio_paths = [
    r"C:\Users\PC\Downloads\first_audio.mp3",  # Page 1 audio
    r"C:\Users\PC\Downloads\secondaudio.mp3",  # Page 2 audio
    r"C:\Users\PC\Downloads\thirdaudio.mp3",  # Page 3 audio
    r"C:\Users\PC\Downloads\fourthaudio.mp3",  # Page 4 audio
    r"c:\Users\PC\Downloads\fifthaudio.mp3",  # page 5 audio
    r"C:\Users\PC\Downloads\sixthaudio.mp3",  # Page 6 audio
]

# Create the main application window
root = tk.Tk()
root.geometry("1280x720")
root.title("CAPTAIN'S ROOM")

# Initialize the current video index
current_index = 0
video_label = tk.Label(root)

# Global variable to store the number of families
k = 0

def wt1():
    global video_label
    for widget in root.winfo_children():
        widget.destroy()
    label = tk.Label(root, text="PORT")
    label.pack(pady=3)

    video_label = update_media(video_label, video_paths, audio_paths, 0)

    # Create a custom-shaped button using a canvas
    canvas = tk.Canvas(root, width=200, height=100, bg="lightblue", highlightthickness=0)
    canvas.place(x=960, y=390)  # Adjust the position of the button

    # Draw a right-facing arrow-shaped button using a polygon
    arrow_shape = [
        (20, 25), (120, 25), (120, 10), (180, 50), (120, 90), (120, 75), (20, 75)
    ]
    canvas.create_polygon(arrow_shape, fill="#FFB6C1", outline="black", width=2)

    # Add text to the button
    canvas.create_text(100, 50, text="Let's Enter The Cruise", font=("Arial", 10, "bold"), fill="black")

    # Bind the button click event
    canvas.bind("<Button-1>", lambda event: wt2())

def wt2():
    global video_label
    for widget in root.winfo_children():
        widget.destroy()
    label = tk.Label(root, text="INTRODUCTION")
    label.pack(pady=10)

    video_label = update_media(video_label, video_paths, audio_paths, 1)

    previous_button = tk.Button(root, text="Go Back", bg="yellow",font=("Arial",10,"bold") ,command=wt1)
    previous_button.place(x=75, y=652)

    next_button = tk.Button(root, text="Continue", bg="darkcyan",font=("Arial",10,"bold"), command=wt3)
    next_button.place(x=1225, y=652)

def wt3():
    global video_label, k_entry
    for widget in root.winfo_children():
        widget.destroy()
    label = tk.Label(root, text="FILLING DETAILS")
    label.pack(pady=10)

    video_label = update_media(video_label, video_paths, audio_paths, 2)

    previous_button = tk.Button(root, text="Go Back", bg="yellow",font=("Arial",10,"bold") ,command=wt2)
    previous_button.place(x=75, y=652)

    next_button = tk.Button(root, text="Continue", bg="darkcyan",font=("Arial",10,"bold"), command=wt4)
    next_button.place(x=1225, y=652)

    # Updated label and entry styles
    k_label = tk.Label(root, text="Enter the number of families (K):", bg="brown", fg="white", font=("Arial", 16))
    k_label.place(x=540, y=280)

    k_entry = tk.Entry(root, font=("Arial", 16), bg="white", fg="black", width=10)
    k_entry.place(x=540, y=310)

def wt4():
    global video_label, k
    k = int(k_entry.get())
    for widget in root.winfo_children():
        widget.destroy()
    label = tk.Label(root, text="CONTINUATION")
    label.pack(pady=10)

    video_label = update_media(video_label, video_paths, audio_paths, 3)

    previous_button = tk.Button(root, text="Go Back", bg="yellow",font=("Arial",10,"bold") ,command=wt3)
    previous_button.place(x=75, y=652)

    next_button = tk.Button(root, text="Continue", bg="darkcyan",font=("Arial",10,"bold"), command=wt5)
    next_button.place(x=1225, y=652)

def wt5():
    global video_label, k, captain_room, largest_dimension
    for widget in root.winfo_children():
        widget.destroy()
    label = tk.Label(root, text="AVAILABLE ROOMS")
    label.pack(pady=10)

    # Play audio for page 5
    start_sound_thread(audio_paths[4])

    # Generate rooms and dimensions based on user input (k)
    num_rooms = k + 1  # Number of rooms is k families + 1 for the captain's room
    room_numbers = [random.randint(100, 999) for _ in range(num_rooms)]
    room_dimensions = [generate_random_dimensions() for _ in range(num_rooms)]
    room_areas = [length * breadth for length, breadth in room_dimensions]
    largest_area = max(room_areas)
    captain_room_index = room_areas.index(largest_area)
    captain_room = room_numbers[captain_room_index]
    largest_dimension = room_dimensions[captain_room_index]

    # Calculate the number of rows and columns needed to accommodate all rooms
    num_rows = (num_rooms + 9) // 10  # Each row contains up to 10 rooms
    num_columns = min(10, num_rooms)  # Maximum 10 columns

    # Create a scrollable frame
    container = tk.Frame(root)
    canvas = tk.Canvas(container, width=1280, height=620)
    scrollbar_y = tk.Scrollbar(container, orient="vertical", command=canvas.yview)
    scrollbar_x = tk.Scrollbar(container, orient="horizontal", command=canvas.xview)
    scrollable_frame = tk.Frame(canvas)

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(
            scrollregion=canvas.bbox("all")
        )
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar_y.set, xscrollcommand=scrollbar_x.set)

    container.pack(expand=True, fill="both")
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar_y.pack(side="right", fill="y")
    scrollbar_x.pack(side="bottom", fill="x")

    for i, (room_number, (width, height)) in enumerate(zip(room_numbers, room_dimensions)):
        area = width * height
        box_width = 80 + area // 20  # Adjust the width based on area
        box_height = 50 + area
        box_height = 50 + area // 40  # Adjust the height based on area

        room_frame = tk.Frame(scrollable_frame, relief="solid", borderwidth=2, bg="pink", width=box_width,
                              height=box_height)
        room_frame.pack_propagate(False)

        # Calculate grid position
        row_index = i // 10
        column_index = i % 10

        room_frame.grid(row=row_index, column=column_index, padx=2, pady=2)

        room_label = tk.Label(room_frame, text=f"Room {room_number}\n{width}x{height}\nArea: {area}", font=("Arial", 8),
                              bg="pink")
        room_label.place(relx=0.5, rely=0.5, anchor="center")

        if i == captain_room_index:
            room_frame.config(bg="lightblue")
            room_label.config(bg="lightblue")

    previous_button = tk.Button(root, text="Go Back", bg="yellow", font=("Arial", 10, "bold"), command=wt4)
    previous_button.place(x=75, y=652)

    next_button = tk.Button(root, text="Continue", bg="darkcyan", font=("Arial", 10, "bold"), command=wt6)
    next_button.place(x=1225, y=652)




def wt6():
    global video_label, captain_room, largest_dimension
    for widget in root.winfo_children():
        widget.destroy()
    label = tk.Label(root, text="ASSIGNING ROOMS")
    label.pack(pady=10)
    # Update video and audio separately for page 6
    video_label = tk.Label(root)
    video_label.pack()

    # Play video for page 6
    player = tkvideo(video_paths[4], video_label, loop=0, size=(940, 620))
    player.play()

    # Play audio for page 6
    start_sound_thread(audio_paths[5])

    # Use the captain's room and dimensions stored in global variables
    result_text = f"Captain's Room is allocated!\n"
    result_label1 = tk.Label(root, text=result_text, font=("Helvetica", 16, "bold"))
    result_label1.place(relx=0.5, rely=0.72, anchor="center")

    room_text = f"Room number is: {captain_room}\n"
    result_label2 = tk.Label(root, text=room_text, font=("Helvetica", 20, "bold"), fg="blue")
    result_label2.place(relx=0.5, rely=0.78, anchor="center")

    dimension_text = f"Largest dimension (length*breadth): {largest_dimension[0]} * {largest_dimension[1]}"
    result_label3 = tk.Label(root, text=dimension_text, font=("Helvetica", 16, "bold"))
    result_label3.place(relx=0.5, rely=0.84, anchor="center")

    # Add an exit button to go back to the code
    exit_button = tk.Button(root, text="Exit", bg="red", font=("Arial", 12, "bold"), command=root.destroy)
    exit_button.place(x=640, y=650)

    previous_button = tk.Button(root, text="Go Back", bg="yellow", font=("Arial", 11, "bold"), command=wt5)
    previous_button.place(x=90, y=600)
    next_button = tk.Button(root, text="BACK TO PORT", bg="darkcyan", font=("Arial", 11, "bold"), command=wt1)
    next_button.place(x=1155, y=600)


# Start the application with the first window
wt1()

# Run the Tkinter event loop
root.mainloop()
