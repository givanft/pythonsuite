import re

def main():
    test_str = '<iframe width="560" height="315" src="https://www.youtube.com/embed/xvFZjo5PgG0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'
    print(parse(test_str))


def parse(html):
    matches = re.search(r'(?:src="https?:\/\/(?:www.)?youtube.com\/[a-z]+\/)(\w+)', html, re.IGNORECASE)

    if matches is None:
        return "None"

    return "https://youtu.be/" + matches.group(1)

if __name__ == "__main__":
    main()
