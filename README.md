<center> <h1 align="center">EggShell Community Version</h1> </center>

![Unbenannt-1](https://user-images.githubusercontent.com/33968601/111917307-9201c000-8a7f-11eb-9a40-95f19f3507dd.png)


## About this fork
This is the official community fork for the abandoned eggshell project. The current project is updated to work for iOS 11+, but if you have issues or want to contribute to EggShell feel free to do so here, instead of the original repository.

## About EggShell
The original EggShell tool was a post exploitation surveillance tool written in Python. It gives you a command line session with extra functionality between you and a target machine. EggShell gives you the power and convenience of uploading/downloading files, tab completion, taking pictures, location tracking, shell command execution, persistence, escalating privileges, password retrieval, and much more.  This is project is a proof of concept, intended for use on machines you own.

## Getting Started
- Python 3.0 or higher

## Building
- Theos and $THEOS set
- iOS 13 SDKs in $THEOS/sdks

### macOS/Linux Installation

Using `git clone`:
```sh
git clone https://github.com/rpwnage/eggshell-community-fork eggshell && cd eggshell && python3 eggshell.py
```

Using `Wget`:
```sh
wget https://raw.githubusercontent.com/AstroOrbis/EggShell-Community-Fork/master/eggshell.py && python3 eggshell.py
```

Using the `github.com` website:

```
1. Download the project using the "Download Zip" file at the top of this page.
2. Extract it to the location of your choice, preferably somewhere easy to access, such as your desktop.
3. Open your terminal. 
4. Use "cd" to change your working directory to the eggshell folder.
5. Type "python3 eggshell.py", and you're on your way!
```

## Creating Payloads
Eggshell payloads are executed on the target machine. The payload first sends over instructions for getting and sending back device details to our server and then chooses the appropriate executable to establish a secure remote control session.

### Bash
Selecting bash from the payload menu will give us a 1 liner that establishes an eggshell session upon execution on the target machine.

### Teensy macOS (USB injection)
Teensy is a USB development board that can be programmed with the Arduino IDE. It emulates usb keyboard strokes extremely fast and can inject the EggShell payload just in a few seconds.
Selecting Teensy will give us an Arduino based payload for the Teensy board.
After uploading to the Teensy, we can plug the device into a macOS usb port. Once connected to a computer, it will automatically emulate the keystrokes needed to execute a payload.


## Usage
### Interacting with a session
After a session is established, we can execute commands on that device through the EggShell command line interface.
We can show all the available commands by typing `help`.

### Taking Pictures
Both iOS and macOS payloads have picture taking capability. The picture command lets you take a picture from the iSight on macOS as well as the front or back camera on iOS.

### Tab Completion
Similar to most command line interfaces, EggShell supports tab completion.When you start typing the path to a directory or filename, we can complete the rest of the path using the tab key.

### Multihandler
The Multihandler option lets us handle multiple sessions.  We can choose to interact with different devices while listening for new connections in the background.  
Similar to the session interface, we can type `help` to show Multihandler commands.

## Special Thanks
- Linus Yang / Ryley Angus for the iOS Python package
- AlessandroZ for LaZagne

## DISCLAMER
By using EggShell, you agree to the GNU General Public License v2.0 included in the repository. For more details at http://www.gnu.org/licenses/gpl-2.0.html. Using EggShell for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program.

## TODO
### Broken/WIP commands
#### iOS
- screenshot - needs upgrades from deprecated methods
- picture - needs upgrades from deprecated methods