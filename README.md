# deeplearning-notebook

## Welcome to the **[SF Big Analytics](https://www.meetup.com/SF-Big-Analytics/)** Deep Learning guided study group.
This repo contains setup and installation instructions and (eventually) code for the examples presented in class. For more details see the Meetup [website](https://www.meetup.com/SF-Big-Analytics/). The workshop is limited to 20 attendees.

## Installation and Setup
Estimated time of 1-2 hours.

#### Git and Github
I'll use Git, a version control system, along with Github, a popular online Git storage system, to send you the class materials. The code repository for this study group will live on Github and you'll get updates before every class through Git/Github. We also need to setup git on your machine to work with Github.

1. Make a [free account on Github](https://github.com/).
1. Install git. If you are using Mac OS X, you already have Git installed. From the command line run `git --version`. If you get a version number in return, you are good to go. If you need to install Git or want to upgrade to the latest version see [this page](https://git-scm.com/).
```bash
$ git --version
> git version 2.19.1
```
1. Set up git to use your Github credentials.
```bash
$ git config --global user.name "Your Name"
$ git config --global user.name
> "Your Name"
$ git config --global user.email "you@example.com"
$ git config --global user.email 
> "you@example.com"
```
Then follow either the [HTTPS or the SSH method to authenticate with Github](https://help.github.com/articles/set-up-git/#next-steps-authenticating-with-github-from-git).

1. Clone this repository by running `git clone https://github.com/tjbay/deeplearning-notebook.git` from the command line. This will create a folder called `deeplearning-notebook` in your current directory and download the workshop files into the directory.
```bash
$ cd deeplearning-notebook
$ ls -l
```
After running these commands you should see a list of files, including one named `Dockerfile`.
1. Update. This won't do much now, but run this before each session to get all the changes and updates to the Github repo.
```bash
$ git pull
```

#### Docker
Docker is one solution to a common software development issue. When developing software on different platforms we often run into **environment** issues. By that I mean that if I write code on Mac OS X in Python on a laptop and then want to run it on a production Linux machine it might not produce exactly the same results or might not even work at all due to a different OS, Python or package versions, or environment variables. With Docker, we can specify exactly what files and software we want to be copied into or installed in our container with a **Dockerfile**. Our code will be run from within the container in an identical setup to the other people in the study group.

1. Download and install the free [Docker Community Edition](https://www.docker.com/products/docker-desktop). You will have to create a free account. 
1. After installing and starting Docker (you'll have to give it your machine password), run the following from the command line.
```bash
$ docker --version
> Docker version 18.06.1-ce, build e68fc7a
```
#### Set up persistent storage
1. One weakness of Docker is that changes in a running container are ephemeral. We'll need to set up an [external volume](https://docs.docker.com/engine/reference/commandline/volume/) that will save your work.  

```bash
$ docker volume create deeplearning
$ docker volume inspect deeplearning
> [
>    {
>        "CreatedAt": "2018-10-14T16:48:02Z",
>        "Driver": "local",
>        "Labels": {},
>        "Mountpoint": "/var/lib/docker/volumes/deeplearning/_data",
>        "Name": "deeplearning",
>        "Options": {},
>        "Scope": "local"
>    }
> ]
```

#### Build 
The following command will create a Docker image by following the script in the Dockerfile. This currently inherits a lot of software from an image created by the Jupyter Project which contains packages for scientific computing with Python and adds the deep learning software we'll be using. See the reference [here](https://docs.docker.com/engine/reference/commandline/build/) for more information. This will take a few minutes to run, depending on your machine and internet connection.

```bash
$ docker build -t tf .
```

#### Start the container
See the documentation for the [run](https://docs.docker.com/engine/reference/commandline/run/) command. This will start a Docker container from the image we just created. Notably, it starts a Jupyter notebook with Python 3 and all the software we need. This command mounts the volume we create above and it will be the `saved` directory in your notebook. Your work and data should be saved here.
```bash
$ docker run -p 8888:8888 --mount source=deeplearning,target=/home/jovyan/saved/  tf
```

#### Run Jupyter notebook
In the output of the previous command, you'll see a token. Open the [Jupyter notebook](http://localhost:8888) in your browser and paste in the token.

In the `notebooks` directory, open the `0.-deep-learning-test-notebook.ipynb` file. Run the notebook. If it's error-free, you are ready for the class. 

I've gotten feedback from a few people that sometimes the Jupyter notebook will fail to run even if everything has been installed correctly. I haven't been able to repreduce or diagnose the issue. Please try to restart the kernel by clicking `Kernel` and then selecting `Restart and run all`.

The last cell will display an image of a 4 digit number. Email the number to tj.bay@ask.com to reserve a spot in the class. Once you are finished you can type `control-c` in the terminal window to stop the Docker container.




