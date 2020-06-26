# ProbDice

ProbDice is an application that allows you to simulate the roll of one or more dice and view the probability distribution through a histogram. You can set the number of rolls, the number of dices roll at the same time and the number of faces of each dice, besides, you can save and load files so you can see the histogram of your own data set or a data set generated previously.

The histogram provides you a navigation bar so you can move along it and zoom (if you need it) so it is possible to represent an extensive amount of data (for example a roll of 50 dices, 2.000.000 times and each dice with 16 faces)


![alt text](https://github.com/Santixs/ProbDice/blob/master/Models/12F3D1M.png?raw=true)



The aim of this project is to learn Python and how to use some libraries such as PyQt5 (to generate the GUI), MatPlotLib (to generate the graphs), or Numpy (to work with faster arrays instead of lists). You can see the version of each library in the requirements.txt file

The Load function is designed for files that contain only numbers and placed with spaces between them (1 2 3 4), with commas (1,2,3,4), with commas and spaces (1, 2, 3, 4) or one number in each line.

The information represented in the histograms can be used to make better strategies in games which use dices, i.e. Monopoly or Catan, in these games the player roll two dices at once, the distribution of the results when throwing 2 dices at once, each one with 6 faces and 10.000.000 times is: is:


![alt text](https://github.com/Santixs/ProbDice/blob/master/Models/6faces2dicesOnce10M.png?raw=true)

Therefore, if we are playing a game that uses two dices, we can make our strategies knowing that 7 is the number that is more probable and then 6 and 8. 
Or the distribution of the results when throwing ten dices at once, each one with 12 faces and 10.000.000 times is:s:


![alt text](https://github.com/Santixs/ProbDice/blob/master/Models/12faces10dicesOnce10M.png?raw=true)



To run the application you just have to execute the __main__.py file with " python3 __main__.py " you need to have the libraries installed, if you do not have them you can install all the libraries of that project with "pip3 install -r requirements.txt" Remember you have to run these commands in the project directory
