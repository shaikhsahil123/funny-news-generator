# Fake News Headline Generator

A simple and entertaining Python project that generates randomized "breaking news" headlines using predefined subjects, 
actions, and locations. The program also includes text-to-speech output and colored terminal formatting for enhanced presentation.

# Overview
This project demonstrates the following Python concepts:

- Random data generation  
- Lists and dictionaries  
- Continuous user interaction using loops  
- Text-to-speech using the pyttsx3 library  
- ANSI color codes for styled terminal output  

The generator selects a random subject, an action, and a mapped location,
then forms a complete headline and reads it aloud.

## Features
- Generates a new headline every cycle  
- Text-to-speech announcement using pyttsx3  
- Colored terminal output for readability  
- Structured data for subjects, locations, and actions  
- Loop continues until the user chooses to exit  

---

## Requirements

Install the required library:

```bash
pip install pyttsx3

# How to Run
Run the script with:python headline_generator.py

Sample Output
LIVE FROM: Bandra West
BREAKING NEWS: Sachin Tendulkar announces a new rule about at Bandra West

Developed by Sahil.
