#! /bin/sh
#
# run.sh
#
#

local_path="$(dirname $0)"
original_path="$(pwd)"

function check_module()
{
    local module="$1"
    local installName="$2"
    [ -z "$installName" ] && installName="$1" # if installName is not provided, use module name
    python -c "\"import $module\"" > /dev/null
    if [ "$?" != "0" ]; then # module not found
        python -m pip install $installName
    fi
}

check_module "tcod" "libtcod-cffi"
cd "$local_path/Rogue_Like"

python "Main.py"

cd "$original_path"
