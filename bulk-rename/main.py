import os

def main():
    number = 0
    path = "~/Repos/learning-python/bulk-rename/"

    for filename in os.listdir(path):
        my_dest = "img" + str(number) + ".jpg"
        my_src = path + filename
        my_dest = path + my_dest
        os.rename(my_src, my_dest)
        i += 1

if __name__ == "__main__":
    main()
