
# Set Up

## Install Python Tools

**Head's up** We are using Python **3.11** for this course. If any installation instructions show an earlier version, replace with **3.11**. Later versions are fine as long as they start with **3.11**. E.g. **3.11.1** etc.

### Installation Notes

- Mac users:
  - [Install Python for Mac](https://wsvincent.com/install-python/#install-python-on-macos){:target="_blank"}
- Windows(WSL) & Ubuntu users:
  - [Install Python for Linux](https://wsvincent.com/install-python/#install-python-on-linux){:target="_blank"}
  - Once completed, also enter these commands in terminal:
    - > sudo apt install python3.11-dev python3.11-venv

- **NOTE:** Windows users should enter commands from the WSL Ubuntu terminal.

### Test Python Setup

Enter these commands in your terminal from a convenient location. E.g. in your home directory.

- > `mkdir python-fun`
- > `cd python-fun`
- > `python3.11 -m venv .venv`
- > `source .venv/bin/activate`
- > `python --version`
- > `deactivate`

You can delete `python-fun` folder now if you like.

#### Testing Steps Details

Let's do our best to avoid typing in commands we don't understand. Here's what each command is doing:

- `mkdir python-fun` is creating a new directory.
- `cd python-fun` changes your working directory to your project folder.
- `python3.11 -m venv .venv` uses the correct version of Python to create a `virtual environment` for your code.
  - This `virtual environment` can be thought of as a sandbox where you can safely manage your project without conflicting with any other Python installations used by the Operating System.
  - The `virtual environment` is created in the `.venv` folder because `.venv` was the last argument supplied to the command.
  - **NOTE:** This folder is not required to be named `.venv`, but that is a common convention and what we will use in class.
- `source .venv/bin/activate` will `activate` the virtual environment so that its version of Python becomes the current one in use.
  - **WARNING:** It's easy to forget this step. The terminal helps you out by showing a `(.venv)` at beginnng of prompt.
- `python --version` shows the currently used Python version.
  - It is no longer necessary to use full `python3.11` command because we are running inside a `virtual environment` so it can safely know what version of Python is being used.
  - You should see a version starting with `Python 3.11`
- `deactivate` will "turn off" the virtual environment. It's still there in the `.venv` folder, but won't be active until you reactivate it with `source .venv/bin/activate`
- **NOTE:** If you ever delete the projects `.venv` folder you can recreate it with `python3.11 -m venv .venv`

## Editor

PyCharm is the editor of choice for professional Python developers. 

**Heads up!** If you are a Windows user using WSL please follow the Windows link.

- [PyCharm for Windows](https://codefellows.github.io/code-401-python-guide/curriculum/prework/pycharm-windows){:target="_blank"}
- [PyCharm for Mac](https://codefellows.github.io/code-401-python-guide/curriculum/prework/pycharm-mac){:target="_blank"}
- [PyCharm for Linux](https://codefellows.github.io/code-401-python-guide/curriculum/prework/pycharm-linux){:target="_blank"}

## Install Docker

**NOTE:** Installing Docker tends to be really easy or really hard. So give it a shot and find out. If it gets hard then stop and let Code Fellows know about installation issues when class begins. Docker won't be used until second half of class so there's time to get things set up right.

- [Docker for Windows](https://docs.docker.com/desktop/install/windows-install/){:target="_blank"}
- [Docker for Mac](https://docs.docker.com/desktop/install/mac-install/){:target="_blank"}
- [Docker for Linux](https://docs.docker.com/desktop/install/linux-install/){:target="_blank"}

- If Docker Desktop launches then you're all set.
  - If not let instructor know on first day of class.
- Create free account at [DockerHub](https://hub.docker.com/){:target="_blank"}
