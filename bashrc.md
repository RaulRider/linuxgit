# FUNCTION .bashrc file

The command below combines mkdir and cd. 
Typing md folder_name creates a directory named “folder_name” in your working directory 
and navigates into it immediately.
The $1 you see in the function represents the first argument, which is the text you type 
immediately after the function name.

```
md () { mkdir -p $1 cd $1 }
```

Another mre refined version
```
md () { [ $# = 1 ] && mkdir -p "$@" && cd "$@" || echo "Error - no directory passed!"; }
```

# MY-IP FUNCTION .bashrc file
```
function my_ip() # Get IP adress on ethernet.
{
    MY_IP=$(/sbin/ifconfig eth0 | awk '/inet/ { print $2 } ' |
      sed -e s/addr://)
    echo ${MY_IP:-"Not connected"}
}

```

# ALIASES .bashrc file
You can also write aliases in  a separate .bash_aliases
including this in .bashrc:
```
if [ -f ~/.bash_aliases ]; then
    . ~/.bash_aliases
fi
```
.bash_aliases
```
# EJEMPLO DE .bash_aliases
alias ll="ls -lha"
alias q=’exit’
alias c=’clear’

alias home='cd ~'
alias root='cd /'

#xdg-open opens files and url in browser!!!!
alias o=xdg-open
```

See here
https://unix.stackexchange.com/questions/129143/what-is-the-purpose-of-bashrc-and-how-does-it-work

a a complete sample:
https://www.tldp.org/LDP/abs/html/sample-bashrc.html



# VARIABLES .bashrc file
To set variable only for current shell:
```VARNAME="my value"```

To set it for current shell and all processes started from current shell:
```export VARNAME="my value"      # shorter, less portable version```

To set it permanently for all future bash sessions add such line to your .bashrc file in your $HOME directory.
To set it permanently, and system wide (all users, all processes) add set variable in /etc/environment:
```sudo -H gedit /etc/environment```

This file only accepts variable assignments like:
```VARNAME="my value"```

Do not use the export keyword here.

