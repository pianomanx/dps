# Now we get the DPS resource file and instantiate it:
import os
import configparser
from shutil import copyfile # for copying files, etc.
import sys

class DPSrc:
    def __init__(self,dps_install_dir):
        sys.path.append(dps_install_dir+"/classes/")
        import dps_prompt_ui as prompt_ui
        prompt_ui = prompt_ui.prompt_ui()
        OKGREEN=prompt_ui.bcolors['OKGREEN'] # "ON DA GWEEN!"
        FAIL=prompt_ui.bcolors['FAIL']
        WARN=prompt_ui.bcolors['WARN']
        ENDC=prompt_ui.bcolors['ENDC']
        self.dps_config_file = os.path.expanduser("~")+"/.dps/config/dpsrc"
        if not os.path.exists(self.dps_config_file):
            try:
                if not os.path.exists(os.path.expanduser("~")+"/.dps/"):
                    os.mkdir(os.path.expanduser("~")+"/.dps")
                if not os.path.exists(os.path.expanduser("~")+"/.dps/config"):
                    os.mkdir(os.path.expanduser("~")+"/.dps/config")
                if not os.path.exists(os.path.expanduser("~")+"/.dps/logs"):
                    os.mkdir(os.path.expanduser("~")+"/.dps/logs")
            except:
                print(f"{FAIL}Could not write directories in {os.path.expanduser('~')}{ENDC}")
                exit(1)
            # copy the dpsrc.example file into ~/.dps/config/
            copyfile(dps_install_dir+"/examples/dpsrc.example",os.path.expanduser("~")+"/.dps/config/dpsrc")
            self.configparser=configparser.ConfigParser()
            self.configparser.read(os.path.expanduser("~")+"/.dps/config/dpsrc") # read the file
            self.configparser.sections() # get all sections of the config
            self.configparser.set('Paths','dps_bin_path',dps_install_dir) # TODO int() ?
            with open(self.dps_config_file, 'w') as config_file:
                self.configparser.write(config_file)
            print(f"{OKGREEN}Configuration file generated. Please restart shell.{ENDC}")
            exit(0)
        else:
            self.configparser=configparser.ConfigParser()
            self.configparser.read(self.dps_config_file) # read the file
            self.configparser.sections() # get all sections of the config
            self.mypaths = [] # custom mypaths defined in dpsrc
            self.warn_dupes = False # show duplicates binaries? Set in dpsrc to True if so.
            self.paths = [] # all good paths (exists, no symlinks, etc)
            self.prompt_theme = 0 # prompt_theme
            ###
            ## Timestamps?
            ###
            if 'Options' in self.configparser:
                self.options = self.configparser['Options']
                for option in self.options:
                    if option == "timestamps":
                        if self.options['timestamps']=="True":
                            self.timestamps = True
                        else:
                            self.timestamps = False
            try: self.timestamps # it was not defined in [Options]
            except:
                self.timestamps=False
            ###
            ## PATHS definition: (from dpsrc)
            ###
            if 'Paths' in self.configparser:
                self.mypaths = self.configparser['Paths']['mypaths'].split(":") # Array of all paths defined in dpsrc
                # check if symlinks in paths. Also, remove dupes:
                for path in self.mypaths:
                    if path not in self.paths: # not in good paths list:
                        if os.path.islink(path): # was it a symlink?
                            if "/"+os.readlink(path) not in self.paths:
                                self.paths.append("/"+os.readlink(path))
                        else:
                            self.paths.append(path)
                try:
                    self.warn_dupes = self.configparser['Paths']['warn_dupes']
                except:
                    print(f"{WARN}item missing from dpsrc: \"warn_dupes\" in [Paths] section. Default is \"False\"{ENDC}")
                # DPS installation directory defined?
                self.dpsbinpath = self.configparser['Paths']['dps_bin_path']
                # check all paths and issue warning:
                for path in self.paths:
                    if not os.path.isdir(path):
                        print(f"{FAIL}Path defined ({path}) in [Paths] section of dpsrc file does not exist! {ENDC}")
                        exit(1)
                #print(self.paths)
            else:
                print(f"{FAIL} Error in config file: Add [Paths] section to {self.dps_config_file}{ENDC}")
                exit() # die

            if 'Style' in self.configparser:
                self.prompt_theme = int(self.configparser['Style']['prompt_theme']) # grab the value of the style
            else:
                print(f"{FAIL}Error in config file: Add [Style] section to {self.CONFIG_FILENAME}{ENDC}")
                exit() # die

            # check for aliases:
            if 'Aliases' in self.configparser:
                self.aliases = self.configparser['Aliases']
            else:
                print(f"{WARN} No aliases section found in dpsrc config file.{ENDC}\n")
            self.dpsbinpath = self.configparser['Paths']['dps_bin_path']
