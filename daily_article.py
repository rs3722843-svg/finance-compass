#!/usr/bin/env python3
"""
FinanceCompass Daily Article Automation
Creates a daily finance article, commits it to git, and triggers the daily update.
"""
import os
import re
from datetime import datetime

BASE_DIR = "C:/Users/Track Computers/Desktop/finance-compass"
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

def generate_article(slug, title, body, published_date):
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
            
            <img src="https://images.unsplash.com/photo-1556761175-5973dc0f32e7?auto=format&fit=crop&w=1200&q=80" alt="{title}" class="w-full h-64 md:h-96 object-cover rounded-2xl mb-8 shadow-xl">

{body}
        </article>
    </main>

    <footer class="border-t border-slate-800 py-8 text-center text-sm text-slate-500">
        <p>© 2026 FinanceCompass. Educational purposes only. Not financial advice.</p>
    </footer>
</body>
</html>"""
    return html


def main():
    # Pick next available article
    existing = set()
    for f in os.listdir(ARTICLES_DIR):
        if f.endswith('.html'):
            existing.add(f)

    # Find next number in sequence
    used = []
    for f in existing:
        m = re.match(rf"daily-finance-tip-(\d+)", f)
        if m:
            used.append(int(m.group(1)))
    next_num = max(used, default=0) + 1

    title = f"Daily Finance Tip {next_num}: Smart Money Moves for 2026"
    slug = f"daily-finance-tip-{next_num}"
    published_date = datetime.now().strftime("%B %d, %Y")

    body = f"""            <p class="text-lg md:text-xl text-slate-300 leading-relaxed mb-6">
                Welcome to your daily dose of financial wisdom from FinanceCompass. In today's article, we explore {title}. This comprehensive guide will help you make smarter decisions with your money.
            </p>

            <h2 class="text-2xl font-bold text-white mt-10 mb-4 border-b border-slate-800 pb-2">Key Takeaways</h2>
            <ul class="list-disc pl-6 space-y-3 text-slate-300 mb-6">
                <li>Understand the core principles of personal finance success.</li>
                <li>Learn how to build wealth through disciplined saving and investing.</li>
                <li>Discover actionable strategies to grow your income in 2026.</li>
            </ul>

            <h2 class="text-2xl font-bold text-white mt-10 mb-4 border-b border-slate-800 pb-2">Why This Matters</h2>
            <p class="text-slate-300 leading-relaxed mb-6">
                Taking control of your finances is the most important decision you'll ever make. Whether you're just starting out or looking to optimize your portfolio, these tips will set you on the path to financial freedom.
            </p>

            <h2 class="text-2xl font-bold text-white mt-10 mb-4 border-b border-slate-800 pb-2">Start Today</h2>
            <p class="text-slate-300 leading-relaxed mb-6">
                Don't wait for the "perfect time" — it doesn't exist. Start implementing these strategies today and watch your financial confidence grow.
            </p>
"""

    filepath = os.path.join(ARTICLES_DIR, f"{slug}.html")
    with open(filepath, "w") as f:
        f.write(generate_article(slug, title, body, published_date))

    print(f"[SUCCESS] Article '{slug}' generated successfully.")
    return filepath


if __name__ == "__main__":
    main()
