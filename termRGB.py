import platform

def cprint(txt,colour: tuple, force=False):
    if not can_do_colour() and not force:
            exit("Error -> macOS is not supported by termRGB\n    Force Terminal is not enabled")
    opening = f"\033[38;2;{colour[0]};{colour[1]};{colour[2]}m"
    closing  = "\033[0m"
    print(f"{opening}{txt}{closing}")
    return


def coloured(txt, colour: tuple, force=False):
    if not can_do_colour() and not force:
        exit("Error -> macOS is not supported by termRGB\n    Force Terminal is not enabled")
    opening = f"\033[38;2;{colour[0]};{colour[1]};{colour[2]}m"
    closing  = "\033[0m"
    return opening+txt+closing

# haha, so basic!! like seriously, this is ALL you need to be able to colour stuff
# ill add more though ><

def can_do_colour() -> bool:
    if platform.platform().startswith("macOS"):
        return False
