### minecraft-opencv-bot

The idea behind this project was to develop a bot able to recognize and cut down trees using computer vision.

### WARNING :warning:

_This project is extremely experimental and far away from working flawlessly_

![Collage](/images/collage.png)

- Language:

![English](/images/us.png)


- Also available in: 

[![Spanish](/images/es.png)](README.ES.md)


## Getting Started

**Prerequisites**

First and foremost, you need a python based integrated development environment, such as [Spyder](https://www.spyder-ide.org/) or [Pycharm](https://www.jetbrains.com/es-es/pycharm/).

Then, you will need to install PyAutoGui, OpenCV and a few other libraries.

In order to do so, open up your IDE's terminal and type the next commands:

```
pip install pyautogui
```
```
pip install opencv-contrib-python
```
```
pip install pydirectinput
```
```
pip install keyboard
```

You will need, of course, a copy of [Minecraft](www.minecraft.net).

Create a new world, join and open up the configuration menu. Go to _Controls_, then _Mouse Settings_ and check the _Raw Input_ option. It must be OFF.

You need to run the game in fullscreen, otherwise the script won't work.

Now you are ready to try out this project! Enjoy!

## How does it work?

It starts by taking a screenshot of your screen. Aided by [opencv](https://opencv.org/releases/), the script detects every pixel related to the color of a tree.

If the amount of pixels/area is bigger or smaller than a certain number, many things could happen:

- The player keeps moving forward.
- The player moves to the left.
- The player moves to the left.
- The player starts cutting down a tree.

## Built With

- [PyAutoGui](https://pypi.org/project/PyAutoGUI/) - Python module for human beings. Used to programmatically control the mouse & keyboard.
- [opencv](https://opencv.org/releases/) - Computer Vision library and tools.
- [PyDirectInput](https://pypi.org/project/PyDirectInput/) - Similar to PyAutoGui.
- [Keyboard](https://pypi.org/project/keyboard/)

## Author

- Juan Manuel Díaz Arbués
