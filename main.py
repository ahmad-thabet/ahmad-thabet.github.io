import datetime

# Write content to HTML file
def write_content(html_page):
    with open("index.html", "w") as file:
        file.write(html_page)

# Read style file
def read_style_file():
    with open("style.txt") as f:
        return f.read()

# Read colors file
def read_color_file():
    with open("colors.txt") as f:
        lines = [line.rstrip() for line in f]
        return lines
    
# Generate div
def generate_divs(colors):
    divs = f""""""
    for color in colors:
        divs += f"""<div style="background-color: {color}"></div>\n"""
    return divs

# generate div from colors
def generate_divs_from_colors_file():
    divs = f"""\n"""
    with open("colors.txt") as f:
        for line in f:
            divs += f"""\t\t<div style="background-color: {line.rstrip()}"></div>\n"""
    return divs

# Generate HTML page content
def generate_html_page(body, style, date):
    html_page = f"""
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <style>
            {style}
        </style>
        <title>Pixel {date}</title>
    </head>
    <body>
    {body}
    </body>
</html>
        """
    return html_page

# Main
def main():
    page = generate_html_page(generate_divs_from_colors_file(), 
                              read_style_file(), 
                              datetime.datetime.now().strftime("%B %d, %Y"))
    write_content(page)

if __name__ == "__main__":
    main()