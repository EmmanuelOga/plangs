# "Activate" the environment: create a new shell with pixi settings and project environment variables loaded.
bash --init-file <(cat <<- EOF
set -a .                           # Export all variables set by the following steps.
source ~/.bashrc                   # Load default bash settings.
eval "\$(pixi shell-hook -s bash)" # Load pixi shell settings.
source .env                        # Load project environment variables.
EOF
)