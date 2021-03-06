# Demon Pentest Shell
A simple shell wrapper for superior logging capabilities. All commands are logged to daily-labeled files within the ```~/.dps/logs/``` directory with the values of:
***When, Host, Network, Who, Where, What*** The shell also has built-in configuration commands for customizations.
# The Shell
## CONFIGURATION
The `~/.dps/config/dpsrc` file contains the user-defined settings and variables. See the ![dps.ini.example](dps.ini.example) example config file for syntax. This file and all directories used by DPS are automatically generated in the effective user's home directory within `~/.dps/`.
## Autocomplete Feature
The tab-autocomplete feature is a custom implementation of those you may be familiar with from other (more)popular shells. You can hit TAB to autocomplete (the end of the entry only) file locations, binary paths, and commands in your Paths section of the `~/.dps/config/dpsrc` file.

![Screenshot of auto-complete text](images/screenshots/autocomplete.png)
## Built-In Programming Logic
![foreach() function screenshot](images/screenshots/foreach.png)
## Aliases
You can now define command aliases into the `dpsrc` file:

![DPS Aliases](images/screenshots/aliases.png)
## Shell Themes
These are set with PRMPT_STYL in the `~/.dps/config/dpsrc` file or with the `dps_config prompt (0-9)` built-in command.
### DPS Default Theme:
`PRMPT_STYL` value of `0` or `DPS` using `dps_config`
You can now easily set your theme by issuing the following command:
```bash
dps_config --show-all
```
and choosing a number listed as the theme. Restart the shell to take effect.
### Nouveau Theme:
`PROMPT_STYLE` value of `5` or `Nouveau` using `dps_config`

![DPS_theme_5](images/screenshots/nouveau-screenshot-2.png)

## LOGS
Below is example log output for DPS. All logs are located in `~/.dps/logs/` _with the date used in the file name_. Unlike other shells, which store command history in as session-like manner, DPS will show the command history of all commands issued within a current day from all terminal sessions (WIP).
```
root@demon2.9:/tmp/dps/(dps)# cat ~/.dps/logs/2020-10-18_dps_log.csv                                         
When,Host,Network,Who,Where,What
2020-10-18 11:32:32.253098,demon2.9,ens33:192.168.159.132,root,/tmp/dps,dps_config prompt 3
2020-10-18 11:32:34.377993,demon2.9,ens33:192.168.159.132,root,/tmp/dps,exit
2020-10-18 11:32:40.805349,demon2.9,ens33:192.168.159.132,root,/tmp/dps,ifconfig
root@demon2.9:/tmp/dps/(dps)#                                                                           
```
## SHINY FEATURES
Because this is built with prompt_toolkit, the shell has a lot of great built-in features.
* Use pipes for stdout, stderr just like you would in a native shell
### Keyboard Shortcuts
The following keyboard shortcuts are available,
* **CTRL+A** - move the cursor to the beginning of the line
* **CTRL+P** - enter the previous command into the temrinal
* **CTRL+C** - exit the current subprocess gracefully
* **CTRL+R** - search history
* **Command Suggestions** - These are pulled from your history (log file entries in ~/.dps/logs/)
* **Up and Down arrows** - flip through command history
### Custom Modules
The following are built-in commands,
* **dps_uid_gen** - generate a list of UIDs from a CSV file
* **dps_update** - pull the latest version from this repository - restart shell to take effect
* **dps_alias** - display all user-defined aliases in the dps.ini file
* **dps_update** - updates DPS using GitPython as defined by DPS_bin_path in dps.ini file
* **dps_wifi_mon** - set a Wi-Fi device into monitor mode
* **dps_stats** - show log stats
* **dps_which** - show which command is ran in your ~/.dps/config/dpsrc paths
* **dps_import_log** - import historical logs for CTRL+r reverse search purposes and suggestions
* **dps_config** - set configuration options, such as prompt style
* **clear** - clear the terminal
* **cd** - change current working directory
* **history** - view your command history for your current session file (ALL HISTORY)
### Other Features
* **Define a Target** - Some themes, including "Polar Mint","Bew" and "Terminator" will display the current target in the prompt for your penetation test report's screenshots.
* **Timestamps** - if the "timestamps" value is "True" under the "[Options]" section pf the `~/.dps/config/dpsrc` file, you will get a bright green timestamp in the top of the command output for your Obsidian Notes Timelines, or penetration testing report's screenshots.
## INSTALLATION
To install DPS, simply install the requirements using pip3 and clone the repository anywhere on your filesystem (root access required if installing for all users):
```
root@kali:~# git clone https://github.com/weaknetlabs/dps.git
root@kali:~# cd dps
root@kali:/dps# pip3 install -r requirements.txt
root@kali:/dps# ./dps.py
```
### Dependencies
This project requires Python3 and the following Python modules,
* **prompt_toolkit** - for TAB autocompletion of $PATH and built-in commands.
* **os** - for path object.
* **sys** - for exit.
* **re** - regular expressions.
* **ifaddr** - NIC info.
* **socket** - for hostname.
* **getpass** - for username.
* **subprocess** - executes cmds by passing them to `/bin/bash`.
* **configparser** - parses dps.ini file
* **datetime** - for dates and times.
* **GitPython** - updates the DPS using this very repository!
* **shutil** - for file copying during initial setup.

## UPDATING DPS
To update DPS, simply use the `dps_update` command and restart the shell. This will pull the latest version down to your repository that is defined in the `~/.dps/config/dpsrc` file that gets generated upon first run of the shell.

![DPS Update Screenshot](images/screenshots/dpsupdate2.PNG)

## TODO
This is a work in progress, so please check this area regularly if using this shell.
* TAB-autocomplete paths interpolated into commands - as of now, you can only tab-autocomplete paths at the end of your commands.
* Offload themes into it's own class
* Clean up code to make long vars in prompt_ui.bcolors shorter and more readable
* de-duplicate history in session (pressing up or down should only show a single instance of a command ran multiple times)
