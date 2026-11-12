try:
    current_color = input()
except EOFError:
    current_color = ""


if current_color == "green":
    print("proceed")
elif current_color == "yellow":
    print("prepare to stop")
elif current_color == "red":
    print("stop")
else:
    print("proceed with caution")
