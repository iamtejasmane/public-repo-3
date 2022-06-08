# file handling
# create a file
# overwrite content to the file
# append contents to the file
# read contents from the file
# close the file


def write_file():
    # open the file
    # windows   : c:\myfiles\myfile.txt
    # linux, mac: /home/user/myfile.txt
    # mode: w
    # - create a file if it does exist
    # - overwrite the content
    file = open('my_python_demo_file.txt', 'w')

    # perform the operation
    file.write("India is my country. I love India. All indians are my brothers and sisters.")
    # file.write("I love watching movies.")

    # close the files
    file.close()


write_file()


def append_file():
    # mode: a
    # previous content will be persisted
    file = open('my_python_demo_file.txt', 'a')

    # perform the operation
    file.write('new content written')

    # close the file
    file.close()


# append_file()


def read_file():
    # open the file in read mode
    file = open('my_python_demo_file.txt', 'r')

    # perform the operation
    data = file.read()
    print(f"data = {data}")

    # close the file
    file.close()


read_file()


