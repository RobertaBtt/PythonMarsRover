## Mars Rover Kata
###### MartiX, like SpaceX we explore Marte
###### Version: 1.2, Last updated: 2020-10-26


----
Move an object in the two-dimensional space, giving to it
proper instructions.
- The object have initial and final coordinates `(x,y, direction)`
- direction can be one of the follows` [EAST,SOUTH, WEST, NORTH]`
- The instruction is a command like `F` (Move forward)
###### Requirements
 - to have installed python3.x.x
 - to have installed pip3

###### Installation

`cd martix`

`python3 -m venv .env_martix`

`source .env_martix/bin/activate`

`pip3 install -r requirements.txt`

##### Run Test Coverage
Inside the folder martix, run:
 
` python3 -m pytest tests/ -v --cov command`

It gives the percentage of covering the entities in the command folder

#### Run App
`python3 app.py`

Insert coordinates in the form `3,4,EAST`

Insert command in the form `F`
you can write as many 'F' as you want

To interrupt console: CTRL+C

###### Deactivate the virtual env

`deactivate`