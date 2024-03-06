# File-set-up-plug-in-for-blender
A plug-in for blender that streamlines the file set-up process for compositing artist



# Blender Compositing Setup Plugin

## Introduction

This Blender plugin is designed to streamline the file setup process for compositing artists. It automates several tasks, including importing images as planes, scaling the planes correctly, creating lightboxes, and setting up preset cameras at correct angles. This plugin aims to enhance user workflow and ensure consistency in file setup across various projects.

## Features

1. **Import Images as Planes**: Easily import images as planes into the Blender scene.
2. **Correct Scaling**: Automatically scale imported planes to the correct dimensions.
3. **Lightbox Creation**: Generate lightboxes to improve scene lighting and aesthetics.
4. **Preset Cameras**: Automatically add three preset cameras at optimal angles for compositing.

## Installation

1. Download the plugin file (`compositing_setup_plugin.py`).
2. Open Blender and go to `Edit` > `Preferences`.
3. In the Preferences window, click on the `Add-ons` tab.
4. Click `Install...` and select the downloaded plugin file.
5. Enable the plugin by checking the box next to its name.

## Usage

1. Ensure you have Blender open and the plugin enabled.
2. Locate the plugin in the `Object` tab of the `Tool Shelf`.
3. Enter the file paths for the images you want to import.
4. Adjust the settings for lightbox location and size if needed.
5. Click `Setup Scene` to execute the plugin and automate the setup process.

## Challenges Faced

1. **Operator Availability**: Some operators used in the plugin were not available by default in Blender. This required additional research to find suitable alternatives or enable the necessary add-ons.
2. **User Interface Design**: Designing a user-friendly interface that accommodates all necessary settings without overwhelming the user was a challenge. Iterative testing and feedback helped refine the UI.
3. **Error Handling**: Ensuring the plugin gracefully handles errors, such as missing image files or incorrect settings, requires careful consideration and implementation to maintain user confidence and prevent crashes.

## Resources Used

- [Blender API Documentation](https://docs.blender.org/api/current/)
- [YouTube Tutorials](https://www.youtube.com/)
- [GitHub Repositories](https://github.com/)

## Conclusion

The Blender Compositing Setup Plugin aims to simplify the file setup process for compositing artists by automating common tasks. With its intuitive interface and robust functionality, it improves workflow efficiency and ensures consistent results across projects.

---

**Author**: Your Name  
**Date**: March 5, 2024

