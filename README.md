# ImageD
Short for Imagine Dragons. PCP project 2024.


## Installation instructions

1. Clone the repository in your console via this comamnd:

```sh
git clone https://github.com/PCP2024/ImageD.git
```

2. Create a virtual environment (.venv) in the same folder of the project and activate the virtual environment.

```sh
python3 -m venv .venv
source .venv/bin/activate
```

3. Install the required packages in the terminal (make sure you are in the right folder where requirements.txt is located):

```sh
pip install requirements.txt
```

## CLI
You can use our command-line interface with the following command:
```console
$ python ImageD_cmd.py --help
```

## GUI
Or you might choose to use GUI with advanced cell counting by running:
```console
$ python ImageD_GUI.py
```


## Docker
_Docker image has only access to the CLI interface and cannot display any images at the moment. The communication via X server protocol may be added in the future._


You can build docker image with:
```console
$ docker build -t imaged .
```
or pull one from our repository:
```console
$ docker pull mlukomski/imaged:latest
```
Now you should have `imaged` container image.
Run it in interactive mode with shell, eg.
```console
$ docker run  -it imaged bash
```
Inside the docker shell run your command, eq.
```console
# python ImageD_cmd.py dragon.png --rotate 90 -o result.png
```
now you have rotated image, great!
But it's still in a container, so you might want to copy it back to your machine using `docker cp`.
Firstly open **new terminal window** and check the name of the running container
```console
$ docker container ls
CONTAINER ID   IMAGE     COMMAND   CREATED          STATUS          PORTS     NAMES
c9649ee3b1fa   imaged    "bash"    17 minutes ago   Up 17 minutes             xenodochial_proskuriakova
```
In this example `xenodochial_proskuriakova` is container name, but yours probably gonna be different. Use this name to copy file from the container 
```console
$ docker cp xenodochial_proskuriakova:/app/result.png ./result.png
```
Congratulations! Now you should have the `result.png` file on your local machine! Use the same `docker cp` command to copy your files into the image container, process them, and copy the results back to your machine in order to process images.
