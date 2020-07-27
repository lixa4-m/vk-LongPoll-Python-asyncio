# asyncio LongPoll of VK

<p align="center">
    <img src="https://img.shields.io/github/license/lixa4-m/vk-LongPool-Python-asyncio?style=for-the-badge">
    <img src="https://img.shields.io/github/issues/lixa4-m/vk-LongPool-Python-asyncio?style=for-the-badge">
</p>

## Features



## Install 

- Install package 'aiovk':
	- `pip3 install aiovk`
	or
	- `python3.x -m pip install aiovk`

## Settings:

- Insert *VK_TOKEN* into **./config.py**
- Insert *GROUP_ID* into **./config.py**
- Insert *LONGPOOL_VERSION* into **./config.py**

## How to run?

- Run:
	- `python3.x Main.py`
	
*x - your version of python3*
## Usage

- Line 9 in `Main.py`:
    - longpool.init(api, GROUP_ID, {mode})
    
| Mode         | TODO               
| -------------|:------------------
| messages     | Returns only message info
| updates      | Returns only updates
| ts           | Returns only ts        
| None         | Clean LongPool 
    
## Links!

- [Python](python.org)

- [aiovk](https://github.com/Fahreeve/aiovk)

- [Link to this project](https://github.com/lixa4-m/vk-LongPool-Python-asyncio)

- [Author](https://vk.com/id370926160)
