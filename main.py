import subprocess
import platform
import os
# Sprawdzenie systemu operacyjnego
system = platform.system()
current_directory = os.getcwd()
run_directory = os.path.join(current_directory, "utils")

if system == "Windows":
    subprocess.run(["Arcom_Deep-Live-Cam/My_media/base_faces dir"], shell=True)

elif system in ["Linux", "Darwin"]:  # Darwin to macOS

    path_base_faces = os.path.join(current_directory,"My_media","base_faces")
    if not os.path.exists(path_base_faces):
        os.makedirs(path_base_faces)

    path_base_backgrounds = os.path.join(current_directory,"My_media","base_backgrounds")
    if not os.path.exists(path_base_backgrounds):
        os.makedirs(path_base_backgrounds)

    path_output = os.path.join(current_directory,"My_media","output")
    if not os.path.exists(path_output):
        os.makedirs(path_output)


    base_faces = os.listdir(path_base_faces)
    base_backgrounds = os.listdir(path_base_backgrounds)


    for face in base_faces:
        for background in base_backgrounds:

            cmd = [
            "python", os.path.join(run_directory, "run.py"),
            "-s", os.path.join(path_base_faces, face),
            "-t", os.path.join(path_base_backgrounds, background),
            "-o", os.path.join(path_output, f"{face[:-4]}_{background[:-4]}"+".png"),
            "--frame-processor", "face_swapper", "face_enhancer"
        ]
            subprocess.run(cmd)

else:
    print("Nieznany system operacyjny")
