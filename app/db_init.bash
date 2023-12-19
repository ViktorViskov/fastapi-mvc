set -a
[ -f ../.env ] && . ../.env
set +a

python db_init.py