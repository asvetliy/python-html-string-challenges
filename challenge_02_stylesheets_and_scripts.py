html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Page</title>
    <link rel="stylesheet" href="styles.css">
    <script src="app.js"></script>
</head>
<body>
</body>
</html>"""

find_and_replace_pairs = [
    ('styles.css', 'main.min.css', ),
    ('app.js', 'bundle.js', ),
]

for pair in find_and_replace_pairs:
    pos = html.find(pair[0])
    if pos >= 0:
        html = html[:pos] + pair[1] + html[pos + len(pair[0]):]


print(html)