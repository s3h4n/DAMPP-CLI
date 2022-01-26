"""
    * @import Handler from src
"""

from .src import Handler


def __main__() -> None:
    """
        * declaring private fucntion __main__()

        * @param None

        * @return None
    """

    h = Handler()

    h.handler()


if __name__ == "__main__":

    __main__()
