import os, sys

def removeLeadingZeros(dir):
    for filename in os.listdir(dir):
        src = filename
        dst = filename.lstrip("0") + ".png"
        print(src)
        print(dst)
        os.rename(os.path.join(dir, src), os.path.join(dir, dst))



if __name__ == '__main__':
    # Calling main() function
    inputPath = input("Path: ")
    assert os.path.exists(inputPath), "I did not find the directory, " + str(inputPath)
    removeLeadingZeros(inputPath)

    print("All leading zeros removed")