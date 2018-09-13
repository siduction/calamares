# Author: 2017-2018 Alf Gaida <agaida@siduction.org>
# License: WTFPL-2
#  0. You just DO WHAT THE FUCK YOU WANT TO.

# Variables
# =========
# baseversion= the first part of the version no (0.x.y~)
# distribution= target distribution
# repository= your repository
# branch= your branch, if needed
# commit= your commit , if needed
# target_dir= target dir, if needed, default is snapshot
#
# Functions
# =========
# cleanup ()

baseversion=3.2.2
distribution=unstable
uploadrepo=extra

repository="https://github.com/calamares/calamares"
branch='-b v3.2.2 --single-branch --depth=1'
build="yes"
clean="yes"
gitcommit="yes"
push="yes"
upload="yes"
dryrun="no"

# cleanup function definiton
cleanup() {
    echo ""
    echo "┌───────────────────────┐"
    echo "│ Cleanup calamares ... │"
    echo "└───────────────────────┘"
    rm -f  .editorconfig
    rm -rf .git*
    rm -f  .travis.yml
    rm -rf .tx
    rm -rf hacking
    rm -f  HACKING.md
    rm -f  src/modules/testmodule.py
    rm -f  src/modules/globalStorage.yml
}
