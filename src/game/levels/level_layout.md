# Layout of Level Files

A level file is formatted in a specific way such that the level loader can read properly read it an load the levels. For now, the level file contains three important pieces of data.

- The starting position of the player (Labeled "starting_position")
- The list of platforms in the level (Labeled "static_objects")
- The list of enemies in the level (Labeled "physics_objects")

Below is a description of each of these pieces of data.

## Naming Convention

The name of a level file should be level\_{n}.json where n is the integer number that represents that level.

## Starting Position

This piece of data consists of an array, that is expected to be of length 2.

- starting_position[0]: the starting x_coordinate of the player
- starting_position[1]: the starting y_coordinate of the player

## Static Objects

This piece of data consists of an array of any length. Each element of that array is expected to be of length 4, with the following properties:

- static_object[0]: the x_coordinate of the platform
- static_object[1]: the y_coordinate of the platform
- static_object[2]: the width of the platform
- static_object[3]: the height of the platform

## Physics Objects

This piece of data consists of an array of any length. Each element of that array is expected to be of length 3, with the following properties:

- physics_object[0]: the x_coordinate of the enemy
- physics_object[1]: the y_coordinate of the enemy
- physics_object[2]: the x_velocity of the enemy

## Goal

An Array with a length of 2, corresponding to a level's end goal (x, y) coordinate

- goal[0]: end goal x_coordinate
- goal[1]: end goal y_coordinate
