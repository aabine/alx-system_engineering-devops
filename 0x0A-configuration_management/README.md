# Configuration Management

In this project, I initiated my exploration of Puppet as a configuration management tool. My practice involved crafting Puppet manifest files to achieve various tasks such as file creation, package installation, and command execution.

## Project Objectives :page_with_curl:

* **0. Creating a File**
  * [0-create_a_file.pp](./0-create_a_file.pp): This Puppet manifest file is designed to generate a file named `school` within the `/tmp` directory, with the following specifications:
    * File Permissions: `0744`.
    * File Group: `www-data`.
    * File Owner: `www-data`.
    * File Content: `I love Puppet`.

* **1. Installing a Package**
  * [1-install_a_package.pp](./1-install_a_package.pp): This Puppet manifest file facilitates the installation of the `flask` package via `pip3`.

* **2. Executing a Command**
  * [2-execute_a_command.pp](./2-execute_a_command.pp): In this Puppet manifest file, a command is executed to terminate the process named `killmenow`.