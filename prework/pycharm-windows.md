# PyCharm for Windows

- Install [PyCharm Professional](https://www.jetbrains.com/pycharm/download/#section=windows) for Windows.
  - Under Professional click download, not Toolbox App
  - Use default installation location
  - Check all Installation options
  - Use default Start Menu folder options
  - Reboot after install

- WSL configuration
  - In WSL Ubuntu terminal edit `~/.zshrc`
  - Add `alias charm="pycharm64.exe"` to bottom of file.
  - Close and relaunch WSL Ubunutu terminal
  - Can now do `charm .`
