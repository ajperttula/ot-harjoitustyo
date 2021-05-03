import pygame


class Event:
    """Class responsible for handling user events.

    Tracks user events like mouse motion, clicks and key presses.
    """
    def get(self):
        """Gets events from eventqueue.

        Returns:
            Eventlist: User events occured since last get function call.
        """
        return pygame.event.get()
