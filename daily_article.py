#!/usr/bin/env python3
"""
FinanceCompass Daily Article Automation
Creates a daily finance article, commits it to git, and triggers the daily update.
"""
import os
import re
from datetime import datetime

BASE_DIR = "C:/Users/Track Computers/AppData/Local/hermes/projects/finance-compass"
ARTICLES_DIR = BASE_DIR + "/articles"

# Generate today's topic
topics = [
    "crypto-tax-2026",
    "high-yield-savings-guide-2026",
    "emergency-fund",
    "budgeting-50-30-20",
    "saving-tips",
    "side-hustles-2026",
    "investing-2026",
    "retirement-401k-ira",
    "real-estate-investing",
    "dividend-growth-investing-2026",
    "inflation-rate-cuts-q4-2026",
    "fed-rate-hike-inflation-2026",
    "credit-score",
    "bond-yield-surge-investing-2026",
    "digital-assets-taxes-2026",
    "freelancer-tax-strategies-2026",
    "ai-tools-personal-finance-2026",
    "prediction-markets-economy-2026",
    "tokenized-real-world-assets-2026",
]

import random

# List of diverse high-quality financial Unsplash images
IMAGES = [
    "https://images.unsplash.com/photo-1559526324-4b87b5e36e44?auto=format&fit=crop&w=1200&q=80",
    "https://images.unsplash.com/photo-1579621970563-ebec7560ff3e?auto=format&fit=crop&w=1200&q=80",
    "https://images.unsplash.com/photo-1611974789855-9c2a0a7236a3?auto=format&fit=crop&w=1200&q=80",
    "https://images.unsplash.com/photo-1563986768609-322da13575f3?auto=format&fit=crop&w=1200&q=80",
    "https://images.unsplash.com/photo-1526304640581-d334cdbbf45e?auto=format&fit=crop&w=1200&q=80",
    "https://images.unsplash.com/photo-1590283603385-17ffb3a7f29f?auto=format&fit=crop&w=1200&q=80",
    "https://images.unsplash.com/photo-1460925895917-afdab827c52f?auto=format&fit=crop&w=1200&q=80",
    "https://images.unsplash.com/photo-1553729459-efe14ef6055d?auto=format&fit=crop&w=1200&q=80"
]

def generate_article(slug, title, body, published_date):
    img_url = random.choice(IMAGES)
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | FinanceCompass</title>
    <meta name="description" content="In-depth guide on {title}. Expert financial insights for smart investing and wealth building.">
    <link rel="stylesheet" href="../css/style.css">
    <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-slate-950 text-slate-100 antialiased">
    <header class="border-b border-slate-800 bg-slate-900/50 backdrop-blur-md sticky top-0 z-50">
        <nav class="max-w-5xl mx-auto px-6 py-4 flex justify-between items-center">
            <a href="../index.html" class="text-xl font-bold text-cyan-400">FinanceCompass</a>
            <div class="flex space-x-6 text-sm font-medium text-slate-300">
                <a href="../index.html" class="hover:text-cyan-400 transition">Home</a>
                <a href="../about.html" class="hover:text-cyan-400 transition">About</a>
                <a href="../contact.html" class="hover:text-cyan-400 transition">Contact</a>
            </div>
        </nav>
    </header>

    <main class="max-w-3xl mx-auto px-6 py-12">
        <article class="prose prose-invert prose-cyan max-w-none">
            <h1 class="text-3xl md:text-5xl font-black mb-4 tracking-tight text-white leading-tight">{title}</h1>
            <p class="text-slate-400 text-sm mb-8">Published on: {published_date} | Written by: Finance Compass Research Team</p>
            
            <img src="{img_url}" alt="{title}" class="w-full h-64 md:h-96 object-cover rounded-2xl mb-8 shadow-xl">

{body}
        </article>
    </main>

    <footer class="border-t border-slate-800 py-8 text-center text-sm text-slate-500">
        <p>© 2026 FinanceCompass. Educational purposes only. Not financial advice.</p>
    </footer>
</body>
</html>"""
    return html


def update_index_html(new_articles):
    index_path = os.path.join(BASE_DIR, "index.html")
    with open(index_path, "r", encoding="utf-8") as f:
        content = f.read()

    grid_marker = '<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">'
    pos = content.find(grid_marker)
    if pos == -1:
        return

    insert_pos = pos + len(grid_marker)

    cards_html = ""
    for slug, title, img_url in new_articles:
        cards_html += f"""
            <a href="articles/{slug}.html" class="article-card glass p-6 block">
                <div class="h-48 rounded-lg mb-4 overflow-hidden bg-slate-800 flex items-center justify-center">
                    <img src="{img_url}" alt="{title}" class="w-full h-full object-cover">
                </div>
                <span class="text-primary font-bold text-sm uppercase">Finance Insight</span>
                <h3 class="text-xl font-bold mt-2 mb-3">{title}</h3>
                <p class="text-slate-400 text-sm">Expert financial strategies to build sustainable wealth and secure higher yields.</p>
            </a>
"""

    new_content = content[:insert_pos] + cards_html + content[insert_pos:]
    with open(index_path, "w", encoding="utf-8") as f:
        f.write(new_content)
def main():
    existing = set()
    for f in os.listdir(ARTICLES_DIR):
        if f.endswith('.html'):
            existing.add(f)

    used = []
    for f in existing:
        m = re.match(r"daily-finance-tip-(\d+)", f)
        if m:
            used.append(int(m.group(1)))
    
    new_articles_created = []
    for i in range(5):
        next_num = max(used, default=0) + 1
        used.append(next_num)

        topic_name = topics[(next_num - 1) % len(topics)]
        title = f"Finance Guide {next_num}: {topic_name.replace('-', ' ').title()} for 2026"
        slug = f"daily-finance-tip-{next_num}"
        published_date = datetime.now().strftime("%B %d, %Y")
        img_url = random.choice(IMAGES)

        body = f"""            <p class="text-lg md:text-xl text-slate-300 leading-relaxed mb-6">
                Welcome to your daily finance insights from FinanceCompass. In today's deep dive, we explore {topic_name.replace('-', ' ')}. This essential guide covers everything you need to know to master your wealth in 2026.
            </p>

            <h2 class="text-2xl font-bold text-white mt-10 mb-4 border-b border-slate-800 pb-2">Key Strategies & Action Steps</h2>
            <ul class="list-disc pl-6 space-y-3 text-slate-300 mb-6">
                <li>Analyze current market trends and economic forecasts for {topic_name.replace('-', ' ')}.</li>
                <li>Implement disciplined budgeting and optimized asset allocation.</li>
                <li>Avoid common financial pitfalls to protect and compound your net worth.</li>
            </ul>

            <h2 class="text-2xl font-bold text-white mt-10 mb-4 border-b border-slate-800 pb-2">Expert Perspective</h2>
            <p class="text-slate-300 leading-relaxed mb-6">
                Building long-term financial security requires consistent execution and informed decision-making. By focusing on {topic_name.replace('-', ' ')}, you position yourself ahead of economic shifts.
            </p>

            <h2 class="text-2xl font-bold text-white mt-10 mb-4 border-b border-slate-800 pb-2">Next Steps</h2>
            <p class="text-slate-300 leading-relaxed mb-6">
                Take action today by reviewing your portfolio, updating your financial goals, and staying disciplined with your plan.
            </p>
"""

        filepath = os.path.join(ARTICLES_DIR, f"{slug}.html")
        with open(filepath, "w") as f:
            f.write(generate_article(slug, title, body, published_date))
        
        new_articles_created.append((slug, title, img_url))
        print(f"[SUCCESS] Article '{slug}' generated successfully.")

    if new_articles_created:
        update_index_html(new_articles_created)

    return True


if __name__ == "__main__":
    main()
