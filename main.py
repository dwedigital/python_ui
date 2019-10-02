from bullet import Bullet, colors
from progress.bar import Bar
from time import sleep


def getUserInput():
    # User options as a list for Bullet choices
    options = ['50','100','200','400']

    userChoices = Bullet(
        # Prompt for the user to see
        prompt = "Use up & down arrows to make selection",
        # List of options to choose from
        choices = options,
        # How much space to pad in from the start of the prompt 
        align = 5,
        # Spacing between the bullet and the choice
        margin = 2,
        # Space between the prompt and the list of choices
        shift = 1,
        # The foreground colour of the bullet
        bullet_color = colors.foreground["cyan"]
    )
    # The length variable will beomce the selected input
    length = userChoices.launch()

    # Convert the choice (string) to integer 
    return int(length)

def progressBar(length):
    """
    Sets up the Bar with the following settings:

    Prompt - String: what to print i.e. Processing
    Max - Integer: the max legnth the bar can be (user choice from getUserInput function)
    Suffix -  String: See documentation on the possible dynamic values

    """
    with Bar(
        "Processing", 
        max=length,
        suffix='%(index)d/%(max)d - Time Remaining: %(eta)ds'
        ) as bar:

        # i is set as 0 and increments by 1 each iteration. 
        # When it equals the Bar max value the progress bar is at its endpoint
        i=0

        # Set up the iterator
        while i < length:

            # Shift the progress bar on to the next iteration
            bar.next()

            # Sleep just used for demo to slow it down inbetween interations
            sleep(0.15)

            # Increment i by 1 so you do not get an infite loop!
            i += 1

if __name__ == "__main__":
    progressBar(getUserInput())
