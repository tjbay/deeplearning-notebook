# deeplearning-notebook

### Welcome to the **[SF Big Analytics](https://www.meetup.com/SF-Big-Analytics/)** Python Deep Learning guided study group hosted by **[Ask Media Group](https://www.askmediagroup.com/)**!
Why is it a study group and not a class? There are two main reasons. 1. I won't be standing in front of the class giving a two-hour lecture about deep learning. We learn best by doing it ourselves. I'm planning on spending a small amount of time at the beginning of each session to introduce important concepts as well as code samples and exercizes. Then we'll spend the spend the rest of the time working in small groups. 2. I'm not a deep learning expert. I'm a data scientist at Ask Media Group, working on a variety of NLP problems. I have occasionally used deep learning in my work but not often. This is a chance for me to expand my skill-set and teaching a subject is *really* good way to see if you really understand it.

### Prerequisites
1. Due to the limited number of seats for the class you must follow the installation steps below and send me the  results before you will be admitted to the study group. 
1. Can program in Python. We'll be using Python 3 for this class.
1. Comfortable with the [command line](https://www.codecademy.com/articles/command-line-commands).
1. Familiar machine learning and the main Python machine learning library [scikit-learn](http://scikit-learn.org/stable/).
1. A laptop (bring a charger). Although all OSs should be OK, I use OS X and Linux and will be unable to help with any Windows issues.


### What you'll learn
1. Basics of Git and Gitlab
1. Basics of Docker containers
1. Jupyter notebooks
1. Deep learning topics:
	* Feed-forward networks.
	* What does it mean to train a model?
	* Prepping data for deep learning.
	* Solving a classification problem.
	* Image classification using convolution neural networks.
	* How to do this using Keras and Tensorflow.
	* Next steps.

### Installation and Setup

#### Git and Github
We'll use Git, a version control system, along with Github, a popular online Git storage system. The code repository for this study group will live on Github and you'll get updates every class through Git/Github. We need to setup git on your machine to work with Github.

1. Make a [free account on Github](https://github.com/).

1. Install git. If you are on Mac OS X, you already have Git installed. From the command line run `git --version`. If you get a version number in return, you are good to go. If you need to install Git or want to upgrade to the latest version see [this page](https://git-scm.com/).

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

1. Authenticate. 


2. Configure your local machine to use those credentials. You can find directions [here](https://help.github.com/articles/set-up-git/). You should install/update git, 







1. Install git. If you are on Mac OS X, you already have Git installed. From the command line run `git --version`. If you get a version number in return, you are good to go. If you need to install Git or want to upgrade to the latest version see [this page](https://git-scm.com/).

```bash
$ git --version
> git version 2.19.1
```

2. Make a free account on Github. Configure local machine to use those credentials.

```bash
git config --global user.email "you@example.com"
git config --global user.name "Your Name"




3. Clone this repository by typing `git clone https://github.com/tjbay/deeplearning-notebook.git` at the command line. This will create a folder called `deeplearning-notebook` on your computer, inside whatever directory you are in when you run the command.

```bash
$ cd deeplearning-notebook
$ ls -l
```

After running these commands you should see a list of files, including one named `Dockerfile`.

```bash
git pull
```

This will update you to the most recent version of the repository. If you just installed, it won't do anything



#### Docker
Docker is one solution to a common software development issue. When developing software on different platforms we often run into **environment** issues. By that I mean that if I write code on Mac OS X in Python on a laptop and then want to run it on a production Linux machine it might not produce exactly the same results or might not even work at all due to a different OS, Python or package versions, or environment variables. With Docker, we can specify exactly what files and software we want to be copied into or installed in our container with a **Dockerfile**. Our code will be run from within the container in an identical setup to the other people in the study group.

1. Download and install the free [Docker Community Edition](https://www.docker.com/products/docker-desktop). You will have to create a free account. Follow the directions on the page.
2. After installing and starting Docker (you'll have to give it your machine password), run the following command. If you get a version number back, then Docker is installed.

```bash
$ docker --version
> Docker version 18.06.1-ce, build e68fc7a
```

#### Build 
The following command will create a Docker image by following the script in the Dockerfile. This currently inherits a lot of software from an image created by the Jupyter Project which contains packages for scientific computing with Python and adds installs the deep learning software we'll be using. See the reference [here](https://docs.docker.com/engine/reference/commandline/build/) for more information. This will take a few minutes to run, depending on your machine and internet connection.

```bash
$ docker build -t tf .
```

#### Start the container
See the documentation for the [run](https://docs.docker.com/engine/reference/commandline/run/) command. This will start a Docker container from the image we just created. Notably, it starts a Jupyter notebook with Python 3 and all the software we need.

```bash
$ docker run -p 8888:8888 tf
```

#### Open Jupyter notebook
In the output of the previous command, you'll see a token. Visit [Jupyter notebook](localhost:8888) and paste in the token.

#### Run a notebook and email the output to me.
???



