import subprocess

# Define YOLOv5 command
command = [
    "python", "detect.py",
    "--source", "0",
    "--weights", "best.pt",
    "--img", "320",
    "--conf", "0.9"
]

# Run the command
subprocess.run(command)