import re

html_path = "frontend/index.html"
with open(html_path, "r", encoding="utf-8") as f:
    content = f.read()

# Extract sections
section_pattern = r'(<!-- [^>]*Section -->\s*<section class="section[^"]*" id="([^"]+)">.*?</section>)'

sections = re.findall(section_pattern, content, re.DOTALL)
section_dict = {sec[1]: sec[0] for sec in sections}

# Desired sequence
desired_order = ["about", "skills", "experience", "projects", "ai-studio", "api-sandbox", "certifications", "contact"]

# Re-assemble body content
hero_part = content.split('<!-- About Section -->')[0]
footer_part = '<!-- Footer -->' + content.split('<!-- Footer -->')[1]

new_middle = "\n\n    ".join([section_dict[s_id] for s_id in desired_order if s_id in section_dict])

new_content = hero_part + new_middle + "\n\n    " + footer_part

with open(html_path, "w", encoding="utf-8") as f:
    f.write(new_content)

print("Sections successfully reordered!")
