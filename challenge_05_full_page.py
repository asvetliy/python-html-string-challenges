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

# Step 1 — Metadata
html = html.replace('lang="en"', 'lang="es"', 1)
html = html.replace("My Page", "Full Page Challenge", 1)

# Step 2 — Assets via slicing
pos = html.find("styles.css")
html = html[:pos] + "app.min.css" + html[pos + len("styles.css"):]

pos = html.find("app.js")
html = html[:pos] + "main.bundle.js" + html[pos + len("app.js"):]

# Step 3 — Validation
print("--- Asset Validation ---")
if html.count("styles.css") == 0:
    print(" ✅ styles.css replaced")
else:
    print(" ❌ styles.css still present")

if html.count("app.js") == 0:
    print(" ✅ app.js replaced")
else:
    print(" ❌ app.js still present")

# Step 4 — Headings
h1 = "Welcome to the Full Page"
h2 = "Built with Python Strings"
h3 = "No Parsers Allowed"

body_content = (
    f"    <h1>{h1}</h1>\n"
    f"    <h2>{h2}</h2>\n"
    f"    <h3>{h3}</h3>\n"
)

parts = html.split("<body>", 1)
html = parts[0] + "<body>\n" + body_content + parts[1]

# Step 5 — Paragraph + Image after last heading
p1 = "This page was generated via pure string manipulation."
img_src = "builder.png"
img_alt = "HTML builder illustration"

p_tag = f"    <p>{p1}</p>\n"
img_tag = f'    <img src="{img_src}" alt="{img_alt}">'

pos_h1 = html.rfind("</h1>")
pos_h2 = html.rfind("</h2>")
pos_h3 = html.rfind("</h3>")
last_pos = max(pos_h1, pos_h2, pos_h3)

line_end = html.find("\n", last_pos)
insert_pos = line_end + 1

html = html[:insert_pos] + p_tag + img_tag + html[insert_pos:]

# Step 6 — Second paragraph before </body>
title_start = html.find("<title>") + len("<title>")
title_end = html.find("</title>")
title_text = html[title_start:title_end]

p2 = f"    <p>This page title is: {title_text}</p>\n"

body_close = html.find("</body>")
html = html[:body_close] + p2 + html[body_close:]

# Step 7 — Final Validation
print("\n--- Validation Report ---")

print(" ✅ <title> is correct" if html.count("<title>Full Page Challenge</title>") == 1 else " ❌ title incorrect")
print(" ✅ <h1> found" if html.count("<h1>") == 1 else " ❌ h1 missing")
print(" ✅ <h2> found" if html.count("<h2>") == 1 else " ❌ h2 missing")
print(" ✅ <h3> found" if html.count("<h3>") == 1 else " ❌ h3 missing")
print(" ✅ <img> appears exactly once" if html.count("<img") == 1 else " ❌ img count wrong")
print(" ✅ <p> appears exactly twice" if html.count("<p>") == 2 else " ❌ p count wrong")
print(" ✅ Starts with <!DOCTYPE html>" if html.startswith("<!DOCTYPE html>") else " ❌ doctype missing")
print(" ✅ Ends with </html>" if html.strip().endswith("</html>") else " ❌ html end missing")

print("-------------------------\n")

# Step 8 — Final HTML
print(html)