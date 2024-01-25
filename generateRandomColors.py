import random

def generate_random_color():
    return "#{:06x}".format(random.randint(0, 0xFFFFFF))

def generate_random_colors(num_colors):
    return [generate_random_color() for _ in range(num_colors)]

def write_colors_to_file(colors, filename, mode = 'w'):
    with open(filename, mode) as file:
        for color in colors:
            file.write(color + '\n')

# Example: Generate and write num_colors random colors to a file
num_colors = 100
random_colors = generate_random_colors(num_colors)

#output_filename = f'''colors{random.randint(0, 1000)}.txt'''
output_filename = 'colors.txt'

write_colors_to_file(random_colors, output_filename, 'a')

print(f"Random colors written to {output_filename}.")