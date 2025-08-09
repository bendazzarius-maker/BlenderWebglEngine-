"""Open the WebGL engine index.html in the default browser."""
import pathlib
import webbrowser


def main() -> None:
    index = pathlib.Path(__file__).with_name('index.html').resolve()
    webbrowser.open(index.as_uri())


if __name__ == '__main__':
    main()
