#!/bin/bash

# Author: Alf Gaida <agaida@siduction.org>
# License: WTFPL-2
#  0. You just DO WHAT THE FUCK YOU WANT TO.

# Variables
# =========
# repository= your repository
# branch= your branch, if needed
# commit= your commit , if needed
# target_dir= target dir, if needed, default is snapshot
#
# Functions
# =========
# cleanup ()

repository="https://github.com/calamares/calamares"
commit=ec86922839eae9794ccb95 # working
# commit=be2338ff08b2ea9ae6e7fb81 # broken


# cleanup function definiton
cleanup() {
    echo ""
    echo "┌─────────────┐"
    echo "│ Cleanup ... │"
    echo "└─────────────┘"
    rm -rf .git*
}



