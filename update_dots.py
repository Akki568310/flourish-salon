import re

file_path = r'c:\Users\Brotherx\OneDrive\Documents\BOT\test-ai-site\index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update the pagination dots CSS
dots_css_pattern = r'    \.ps-dot-indicator \{.*?    \}\n    \.ps-dot-indicator\.active \{.*?    \}'
dots_css_replacement = """    .ps-dot-indicator {
      width: 6px;
      height: 6px;
      background-color: #6a4a3a;
      border-radius: 50%;
      cursor: pointer;
      transition: all 0.3s ease;
      margin: 0 8px;
    }
    .ps-dot-indicator.active {
      width: 6px;
      height: 6px;
      background-color: #6a4a3a;
      border-radius: 50%;
      box-shadow: 0 0 0 5px #fdfcf7, 0 0 0 6px #6a4a3a;
    }"""
content = re.sub(dots_css_pattern, dots_css_replacement, content, flags=re.DOTALL)


# 2. Fix inner gap for pagination (optional, adjusting the wrapper gap so ring has space)
# The wrapper `.ps-pagination` already has `gap: 10px;`.
# So margins on the dot + gap should be plenty.


# 3. Swap Expert image URLs
# Emma Rose
content = content.replace('https://images.unsplash.com/photo-1580489944761-15a19d654956?auto=format&fit=crop&q=80&w=400', 'https://images.pexels.com/photos/3993321/pexels-photo-3993321.jpeg?auto=compress&cs=tinysrgb&w=400')
# Sophia Lane
content = content.replace('https://images.unsplash.com/photo-1534528741775-53994a69daeb?auto=format&fit=crop&q=80&w=400', 'https://images.unsplash.com/photo-1521590832167-7bfc17484d8d?auto=format&fit=crop&q=80&w=400')
# Jane Doe
content = content.replace('https://images.pexels.com/photos/415829/pexels-photo-415829.jpeg?auto=compress&cs=tinysrgb&w=400', 'https://images.pexels.com/photos/3993444/pexels-photo-3993444.jpeg?auto=compress&cs=tinysrgb&w=400')
# Olivia Tate
content = content.replace('https://images.unsplash.com/photo-1544005313-94ddf0286df2?auto=format&fit=crop&q=80&w=400', 'https://images.unsplash.com/photo-1600948836101-f9ffda59d250?auto=format&fit=crop&q=80&w=400')


with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Dots outline style and expert images updated successfully!")
