# Interactive-2D-cloth-simulation

![WhatsApp_Video_2025-09-09_at_15 10_online-video-cutter com_online-video-cutter com](https://github.com/user-attachments/assets/3ce8041a-9917-4479-9d7c-5d86e6f42265)

This project is a 2D real time cloth simulation built in Python using Raylib. It focuses on interactive cloth creation, manipulation, and constraint based physics simulation, similar to techniques used in games and visual simulation systems.

The goal of this project is to explore how cloth physics works under the hood, with an emphasis on real time interaction, stability, and extensibility.

## Features

- Interactive drawing of points, lines, and custom polygons  
- Support for both stationary (hooked) and dynamic points  
- Custom cloth structures created by connecting points manually  
- Adjustable physical parameters including stiffness, damping, and mass  
- Real time slicing and cutting of fabric  
- Grid based cloth generation with optional triangulation  
- Real time constraint solving for stable cloth behavior  

## How It Works

The simulation is based on a point mass and constraint system. Cloth is represented as a collection of points connected by distance constraints. Each update step applies forces, integrates motion, and resolves constraints to preserve cloth structure.

Raylib is used for rendering and real time input handling, enabling interactive creation and manipulation of the cloth during simulation.

## Controls and Interaction

- Draw points and connect them with constraints  
- Mark points as fixed or movable  
- Adjust simulation parameters at runtime  
- Slice through fabric to dynamically remove constraints  
- Generate structured cloth grids for rapid prototyping  

## Future Scope

Planned and possible extensions include:

- Wind force simulation  
- Collision handling with shapes and boundaries  
- Exporting cloth meshes for use in other tools or pipelines  
- Performance optimizations for larger cloth systems  

## Motivation

This project was built as a hands on exercise in physics simulation, constraint solving, and real time systems. It provided practical insight into how cloth physics is implemented in interactive applications such as games and visual simulations.

## Tech Stack

- Python  
- Raylib  

## Status

Actively developed and open to future extensions and experimentation.
