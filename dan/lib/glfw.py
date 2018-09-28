import os

glfw_folder = os.path.join(
    os.path.dirname(os.path.realpath(__file__)), "glfw-3.2.1.bin.WIN64", "lib-mingw-w64"
)

os.environ["PATH"] = glfw_folder + os.pathsep + os.environ["PATH"]
