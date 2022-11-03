# Toy Robot Simulation

## Description

The application is a simulation of a toy robot moving on a square table top,
of dimensions `Coordinate.MAX_X` units x `Coordinate.MAX_Y` units.

Move the robot with commands:

    PLACE X,Y,F # X/Y: 0 to MAX_X/MAX_Y, F: NORTH|SOUTH|EAST|WEST
    MOVE
    LEFT
    RIGHT

Report the robot's current coordinate:

    REPORT

See `sample.txt` for sample commands usage.

## How to use

Make sure `python` (3.9 required) is installed on your machine, no setup necessary.
If it's not installed, install it with appropriate installer found here: `https://www.python.org/downloads/`

    # Check if python is installed
    $ python -V
    Pythonn 3.9.2
    
Usage:

    $ python -m app <file>

Sample:

    $ python -m app sample.txt
    2,3,NORTH
    1,3,WEST
    0,0,SOUTH
    0,1,NORTH
    2,0,EAST
    3,0,SOUTH

## Testing

This app comes with unit testing.
To run the tests, execute the command:

    $ python -m unittest 
