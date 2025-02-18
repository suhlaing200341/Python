import os

tmp_dir = "tmp/"
if not os.path.exists(tmp_dir):
    os.makedirs(tmp_dir)
    
test_file_path = f"{tmp_dir}test.wav"
    
with open("test_files/conversation.mp3", "rb") as mp3file:
    with open(test_file_path, "wb") as textfile:
        textfile.write(mp3file.read())