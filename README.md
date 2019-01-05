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
After running these commands you should see a list of files, including one named `dl-env.yaml`.
1. Update. This won't do much now, but run this before each session to pull the latest updates to your copy of the repository.
```bash
$ git pull
```

#### Anaconda 
We'll use the popular Python distribution Anaconda, and it's package manager conda to install and update the code we need. Follow the [installation instructions for your OS here](https://docs.anaconda.com/anaconda/install/). I'd also suggest [verifying your installation](https://docs.anaconda.com/anaconda/install/verify-install/) to make sure everything is working. For macOS in particular, there is a version of Python that comes preinstalled and we want to make sure that we are using the Anaconda Python.

Conda also comes with an environment manager. Using conda environments we can make sure we install exactly the same versions of Python and the various deep learning packages. This replaces the previous use of Docker! To see what will be installed in the deeplearning environment:

```bash
$ cat dl-env.yaml
> name: deeplearning
> channels:
>   - defaults
>   - conda-forge
> dependencies:
>   - python=3.6
>   - pip
>   - pip:
>     - tensorflow
>     - keras
>     - jupyter
>     - pandas
>     - numpy
>     - pillow
>     - opencv-contrib-python
>     - scikit-learn
>     - matplotlib
>     - bokeh
```

We also install some packages with pip, which is Python's package manager. Some packages work better with pip than conda, or have more recent versions.

To create the environment:
```bash
$ conda env create -f ~/dl-env.yaml
$ source activate deeplearning
```

The `source activate` command allows you to switch between environments. This doesn't changes files, but does change Python versions and installed packages. Learn more about [conda environments](https://conda.io/docs/user-guide/tasks/manage-environments.html).

Your command prompt should now start with `(deeplearning)`, to indicate which environment is active. You'll need to activate this environment each time you open a new terminal window.

#### Run Jupyter notebook
Run the following command, after which a Jupyter notebook should open in your browser.
```bash
$ jupyter notebook
```


