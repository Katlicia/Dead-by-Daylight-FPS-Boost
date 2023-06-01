import customtkinter
import os

# Set up a UI. 

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

root = customtkinter.CTk()
root.geometry("500x350")

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

# Get the file directory.

file_dir = r"{user_name}\AppData\Local\DeadByDaylight\Saved\Config\WindowsClient"
user = os.path.expanduser("~")
expanded_file_dir = file_dir.format(user_name=user)

# Continue with the UI.

label = customtkinter.CTkLabel(master=frame, text="Dead by Daylight FPS Configuration")
label.pack(pady=12, padx=10)


# Defining our functions to change the ini files.

print(expanded_file_dir)
def engineFunc():    
    engineFile = f"{expanded_file_dir}\Engine.ini"

    with open(engineFile, 'a') as file:
        file.write("\n\n[/Script/Engine.InputSettings]\nbEnableMouseSmoothing=False\nbDisableMouseAcceleration=True ")


def settingsFunc():
    settingsFile = f'{expanded_file_dir}\GameUserSettings.ini'
    key_to_update = "bUseVSync"
    new_value = "False"
    # INI dosyasını okuyun
    with open(settingsFile, 'r+') as file:
        lines = file.readlines()

        updated_lines = []
        for line in lines:
            if line.startswith(key_to_update):
                line = f"{key_to_update} = {new_value}\n"
            updated_lines.append(line)
    
    with open(settingsFile, 'w') as file:
        file.writelines(updated_lines)


# More UI stuff.       
button = customtkinter.CTkButton(master=frame, text = "Boost FPS", command=lambda: (engineFunc(), settingsFunc()))
button.pack(pady=12, padx=10)


root.title("Dead by Daylight FPS Configuration")
root.mainloop()

