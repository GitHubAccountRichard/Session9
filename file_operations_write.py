with open("story.txt", "a") as f: # a or w to write, w overrides old versions, a you can keep adding to it without losing the old ones
    while True:
        text = input("What do you want to write (press q to exit)")
        if text == "q":
            break
        f.write(text+"\n")
