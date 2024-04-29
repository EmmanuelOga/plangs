#!/bin/bash

# Define the bash configuration into a variable.
## read details:
### -r: raw mode, it doesn't allow backslashes to escape any characters.
### -d '': sets delimiter to null, so it reads the whole input.
read -r -d '' bash_config <<-'EOF'
# Load default bash settings.
source ~/.bashrc

# Use pixi beta feature: allow loading pypi packages.
export PIXI_BETA_WARNING_OFF=true

# Load pixi shell settings.
eval "$(pixi shell-hook -s bash)"

# Use folder-local installed go.
export GOPATH=$(pwd)/.go
export PATH=$PATH:$(pwd)/.go/bin

# Load project environment variables.
## Export variables defined in .env file.
set -a 
source .env
EOF

# "<()" is a process substitution, it allows to run a command and use its output as a file.
bash --init-file <(echo "$bash_config")
