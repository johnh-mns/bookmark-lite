
import commands

def print_options(options):
    for shortcut, option in options.items():
        print(f'({shortcut}) {option}'
    print()

def option_choice_is_valid(choice, options):
    return choice in options or choice.upper() in options

def get_option_choice(options):
    choice = input('Choose an option: ')
    while not option_choice_is_valid(choice, options):
        print('Invalid choice')
        choice = input('Choose an option: ')

    return options[choice.upper()]

# repeating prompt
def get_user_input(label, required = True):
    value = input(f'{label}: ') or None
    while required and not value:
        value  = input(f'{label}: ') or None
    return value

# get info for adding/deleting a bookmark



if __name__ == '__main__':
    print('Welcome to Bark!')
    commands.CreateBookmarksTableCommand().execute()

    options = {
        'A':Option('Add a bookmark', commands.AddBookmarkCommand()),
        'B':Option('List bookmarks by date', commands.ListBookmarksCommand()),
        'T':Option('List bookmarks by title', commands.ListBookmarksCommand(order_by = 'title')),
        'D':Option('Delete a bookmark', commands.DeleteBookmarkCommand()),
        'Q':Option('Quit', commands.QuitCommand()),
    }
    print_options(options)

    chosen_option = get_option_choice(options)
    chosen_option.choose()   # <- ?????


class Option:
""" 
print key for user to enter to choose opiton
print option text
check if user input matches an option, choose option
"""
    def __init__(self, name, command, prep_call = None):
        self.name = name
        self.command = command
        self.prep_call = prep_call  #optional prep step before executing command

    def choose(self):
        data = self.prep_call() if self.prep_call else None
        message = self.command.execute(data) if data else self.command.execute()
        print(message)


    def __str__(self):
        return self.name


