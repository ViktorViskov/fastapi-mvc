#!/usr/bin/sh

help_message() {
    echo "Usage: $0 <command>"
    echo "Commands:"
    echo "  generate   Generate a new migration"
    echo "  apply      Apply the latest migration"
    echo "  revert     Downgrade the last migration"
    echo "  all        Generate and apply the latest migration"
}

generate_migration() {
    echo "Generating migration..."
    alembic revision --autogenerate
}

apply_migration() {
    echo "Applying migration..."
    alembic upgrade head
}

downgrade_migration() {
    echo "Downgrading last migration..."
    alembic downgrade -1
}

all() {
    echo "Generating and applying migration..."
    generate_migration && apply_migration
}

# Check if the script is being run with the correct arguments
if [ "$#" -ne 1 ]; then
    echo "Error: Invalid number of arguments"
    help_message
    exit 1
fi

# Check the command and call the appropriate function
case "$1" in
    generate)
        generate_migration
        ;;
    apply)
        apply_migration
        ;;
    all)
        all
        ;;
    revert)
        downgrade_migration
        ;;
    *)
        echo "Invalid command: $1"
        help_message
        ;;
esac