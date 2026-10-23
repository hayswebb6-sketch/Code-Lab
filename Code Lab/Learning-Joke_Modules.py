import sys


MENU = """
=== Joke & Fun Tools ===
1. xkcd      - Open the xkcd comic in your browser
2. pyjokes   - Get a random programming joke
3. cowsay    - Make a cow say something
4. pyfiglet  - Make big text art
5. asciiart  - Convert text to ASCII art

0. Quit
"""


def xkcd():
    """Opens the classic xkcd antigravity comic."""
    try:
        import antigravity
        antigravity.fly() if hasattr(antigravity, "fly") else antigravity.geohash(37.7749, -122.4194)
        print("\nOpening xkcd... Check your browser!")
    except Exception as e:
        print(f"Oops, couldn't run xkcd: {e}")


def pyjokes():
    """Tells a random programming joke."""
    try:
        import pyjokes
    except ImportError:
        print("\n[Missing] 'pyjokes' isn't installed.")
        print("Install it with: pip install pyjokes")
        return
    try:
        print("\n" + pyjokes.get_joke())
    except Exception as e:
        print(f"Oops, couldn't get a joke: {e}")


def cowsay():
    """Makes a cow say whatever you type."""
    try:
        import cowsay
    except ImportError:
        print("\n[Missing] 'cowsay' isn't installed.")
        print("Install it with: pip install cowsay")
        return
    try:
        text = input("\nWhat would you like the cow to say? ").strip()
        if not text:
            print("Nothing to say!")
            return
        print(cowsay.get_output_string('cow', text))
    except Exception as e:
        print(f"Oops, couldn't run cowsay: {e}")


def pyfiglet():
    """Creates big ASCII text art."""
    try:
        import pyfiglet
    except ImportError:
        print("\n[Missing] 'pyfiglet' isn't installed.")
        print("Install it with: pip install pyfiglet")
        return
    try:
        text = input("\nEnter text to make big: ").strip()
        if not text:
            print("Nothing to convert!")
            return
        print(pyfiglet.figlet_format(text))
    except Exception as e:
        print(f"Oops, couldn't run pyfiglet: {e}")


def asciiart():
    """Converts text to ASCII art using ASCII Magic."""
    try:
        import ascii_magic
    except ImportError:
        print("\n[Missing] 'ascii-magic' isn't installed.")
        print("Install it with: pip install ascii-magic")
        return
    try:
        text = input("\nEnter text to convert: ").strip()
        if not text:
            print("Nothing to convert!")
            return
        art = ascii_magic.from_text(text)
        ascii_magic.to_terminal(art)
    except Exception as e:
        print(f"Oops, couldn't run asciiart: {e}")


def main():
    while True:
        print(MENU)
        choice = input("Pick a number or name: ").strip().lower()
        
        if choice in ("0", "quit", "exit"):
            print("\nBye!")
            break
        elif choice in ("1", "xkcd"):
            xkcd()
        elif choice in ("2", "pyjokes"):
            pyjokes()
        elif choice in ("3", "cowsay"):
            cowsay()
        elif choice in ("4", "pyfiglet"):
            pyfiglet()
        elif choice in ("5", "asciiart"):
            asciiart()
        else:
            print("\nInvalid choice. Try again.")
        
        try:
            input("\nPress Enter to continue...")
        except (KeyboardInterrupt, EOFError):
            print("\n\nBye!")
            break


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nBye!")
        sys.exit(0)
