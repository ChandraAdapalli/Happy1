from pyfiglet import Figlet
# Please install in terminal " pip install pyfiglet==0.7 "
def print_stylish_message(message, font):
    f = Figlet(font=font)
    styled_message = f.renderText(message)
    print(styled_message)

message = "Happy Birthday Friend"
font = "slant"  # You can choose a different font from the available options

print_stylish_message(message, font)
