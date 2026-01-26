#!/usr/bin/env python3
import re
from pathlib import Path

faq_file = Path("public/videprints.com/pages/שאלות-תשובות/index.html")

# Bulgarian translations
translations = {
    "heading": "Добри въпроси, които зададохте",
    "description": "<p>Между другото, ако не намерихте отговора на вашия въпрос, нашите представители ще се радват да отговорят на всичко.</p><p>Чувствайте се свободни да се свържете с нас.</p>",
    "questions": [
        {
            "title": "<strong>Как работи процесът на поръчка?</strong>",
            "text": "<p>Извършвате покупката в сайта и получавате връзка за качване на снимките и видеоклиповете.</p>"
        },
        {
            "title": "<strong>Какво е необходимо за създаване на VIDE снимка?</strong>",
            "text": "<p>Това е много просто, всичко, от което се нуждаете, е видеоклип и снимка</p>"
        },
        {
            "title": "<strong>Възможно ли е да вмъкнете повече от един видеоклип във всяка снимка?</strong>",
            "text": "<p>Разбира се, че е възможно, предлагаме услуга за редактиране на видеоклипове и можете също да редактирате сами и да ни изпратите готов видеоклип.</p>"
        },
        {
            "title": "<strong>Има ли ограничение за продължителността на видеоклипа?</strong>",
            "text": "<p>Препоръчителната продължителност на видеоклипа е до една минута</p>"
        },
        {
            "title": "<strong>Какви са сроковете за доставка?</strong>",
            "text": "<p>Сроковете за обработка на поръчките могат временно да се удължат и могат да продължат до <strong>14 работни дни.</strong><br/><br/>Правим максимум усилия да осигурим най-добрата услуга и благодарим за търпението ви. </p>"
        },
        {
            "title": "<strong>Има ли възможност за самопредаване?</strong>",
            "text": "<p>Разбира се, можете да маркирате опцията в процеса на покупка и ще получите адрес за самопредаване в централния район.</p>"
        },
        {
            "title": "<strong>Как се гледа видеоклипът?</strong>",
            "text": "<p>С помощта на нашето приложение можете да сканирате снимката и да се насладите на изключително изживяване.</p>"
        },
        {
            "title": "<strong>Използването на приложението струва ли пари?</strong>",
            "text": "<p>Не, използването на приложението е безплатно.</p>"
        }
    ],
    "not_found_heading": "Не намерихте отговора?",
    "not_found_text": "<p>Изпратете ни съобщение или оставете данни и ще се радваме да ви помогнем с всеки въпрос, който възникне!</p>"
}

# Plus icon SVG
plus_icon = '''<svg class="icon icon-plus-alt icon-xs flex-auto" viewBox="0 0 24 24" stroke="currentColor" fill="none" xmlns="http://www.w3.org/2000/svg">
      <path stroke-linecap="round" stroke-linejoin="round" d="M12 4v16m8-8H4"/>
    </svg>'''

if faq_file.exists():
    with open(faq_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find the main content section
    main_start = content.find('<main class="main-content')
    main_end = content.find('</main>', main_start) + len('</main>')
    
    # Build the new FAQ section
    faq_html = f'''      <div id="shopify-section-faq" class="shopify-section"><style data-shopify>#shopify-section-faq {{
    --section-padding-top: 72px;
    --section-padding-bottom: 72px;
    --color-text: 198 1 90;
    --color-background: 255 255 255;
  }}</style>
<div class="section section--padding">
  <div class="page-width page-width--narrow relative">
    <div class="title-wrapper leading-none grid gap-4 text-center md:items-center">
      <h2 class="heading font-bold title-md">
        <split-words class="split-words flex flex-wrap" data-animate="fade-up-large">{translations["heading"]}</split-words>
      </h2>
      <div class="page-width--narrow rte leading-normal text-sm xl:text-base">
        {translations["description"]}
      </div>
    </div>
    <div class="faqs with-border flex flex-col lg:flex-row relative z-1">
      <div class="grow grid gap-8 md:gap-12">
        <div class="faq">
'''
    
    # Add all questions
    for q in translations["questions"]:
        faq_html += f'''          <div class="accordion">
            <details class="details" is="accordion-details">
              <summary class="details__summary flex items-center justify-between gap-2 cursor-pointer">
                <span class="text-base lg:text-lg xl:text-xl font-medium leading-tight">
                  {q["title"]}
                </span>
                {plus_icon}
              </summary>
              <div class="details__content text-base rte">
                {q["text"]}
              </div>
            </details>
          </div>
'''
    
    faq_html += '''        </div>
      </div>
    </div>
  </div>
</div>
</div>
      <div id="shopify-section-images-with-text-overlay" class="shopify-section"><style data-shopify>#shopify-section-images-with-text-overlay {
    --section-padding-top: 0px;
    --section-padding-bottom: 0px;
    --color-text: 255 255 255;
    --color-background: 23 23 23;
  }</style>
<div class="section section--padding" style="padding-top: 0; padding-bottom: 0;">
  <div class="page-width page-width--full relative">
    <div class="images-with-text-overlay relative" style="min-height: 650px;">
      <div class="absolute inset-0 z-0">
        <img src="//videprints.com/cdn/shop/files/vide-09619_873573a2-61fa-4473-83ba-239603046efa.jpg" alt="" class="w-full h-full object-cover" style="min-height: 650px;" is="lazy-image">
      </div>
      <div class="relative z-1 flex items-center justify-center" style="min-height: 650px; padding: 64px 20px;">
        <div class="page-width--small text-center">
          <h2 class="heading title-lg tracking-heading font-bold leading-none">
            <split-words class="split-words flex flex-wrap" data-animate="fade-up-large">{translations["not_found_heading"]}</split-words>
          </h2>
          <div class="rte text-sm" style="max-width: 32rem; margin: 0 auto; margin-top: 16px;">
            {translations["not_found_text"]}
          </div>
        </div>
      </div>
    </div>
  </div>
</div>
</div>'''
    
    # Replace the main content
    new_content = content[:main_start] + '<main class="main-content relative" id="MainContent" role="main">\n\n' + faq_html + '\n    </main>' + content[main_end:]
    
    with open(faq_file, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"Replaced FAQ section in {faq_file}")
