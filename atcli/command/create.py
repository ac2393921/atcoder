# import os

from rich.console import Console
from rich import print

console = Console()


def create():
    contest = select_contest()
    print(contest)
    # message1 = "Hello"
    # message2 = "World"


def select_contest():
    console.print("[red]コンテストの種類を選んでください。[/]\n\n\
        (a) ABC\n\
        (b) ARC\n\
        (c) AGC\n", style="bold red")
    
    choice = input("What would you like to do, (a/b/c/d)? ")
    return choice


if __name__ == "__main__":
    create()
