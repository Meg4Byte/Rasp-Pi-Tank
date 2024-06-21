# Rasp-Pi-Tank
Rasp Pi Tank , primenjena elektronika

# Project Title
![IMG_20230911_142547](https://github.com/Meg4Byte/Rasp-Pi-Tank/assets/121357383/890a5547-031a-4c4b-86ca-ac3200c185d9)
![IMG_20230911_142553](https://github.com/Meg4Byte/Rasp-Pi-Tank/assets/121357383/10be3bdd-a0c3-4638-9220-1124b2f66e68)

Predmetni projekat iz primenjene elektronike.
Zadatak je napraviti tank / kola koja se mogu kontrolsati remotely.
U ovom projektu je koriscen tenk i raspberry pi mikroracunar.
Tenk se kontrolise putem Wifi-ja ili Bluetooth-a , konekcija je uspostavljena putem SSH-a.
U daljem izlaganju data su upustsva kako skinuti projekat , pokrenuti i modifikovati po zelji.

## Table of Contents

- [How to Download and Run](#how-to-download-and-run)
- [Prerequisites](#prerequisites)
- [Clone the Repository](#clone-the-repository)
- [Run the Project](#run-the-project)
- [Commands](#how-to-actually-drive)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)
  
## How to Download and Run

### Prerequisites

- Python (version X.X.X)
- [Optional] OpenCV , Media Pipe , VL53L0X , MPU6050

### Clone the Repository

1. Open your terminal or command prompt.

2. Navigate to the directory where you want to store the project files.

3. Run the following command to clone the repository:

   ```bash
   git clone https://github.com/Meg4Byte/Rasp-Pi-Tank.git

4. cd /Rasp-Pi-Tank

5. After this its time to run the script

### Run the Project

In order to run the project do the following :

   1. ```bash
      chmod +x new_car.py

   2. ```bash
      python3 new_car.py

After that the terminal should go black and you can start driving the tank.

## Commands


    • q 	- quit
    • t 	- turn on the engine 
    • w	  - speed up
    • s	  - slow down
    • key_up (strelica nagore)     – forward
    • key_down (strelica nadole)   – backward
    • key_left (strelica nalevo)   – turn left
    • key_right (strelica nadesno) – turn right
    • f	- rotate camera to the right
    • g	 -rotate camera to the left  

## Contributing

   If you'd like to contribute to this project, please follow these guidelines:
   
   Fork the repository on GitHub.
   Clone your forked repository to your local machine.
   Create a new branch for your feature or bug fix.
   Make your changes and commit them.
   Push your changes to your fork on GitHub.
   Create a pull request to submit your contribution.
   
## License 

This project is licensed under the MIT License. You are free to use, modify, and distribute this code at your own discretion.

## Contact

For questions or feedback, feel free to reach out at petnenadd_d@uns.ac.rs .
