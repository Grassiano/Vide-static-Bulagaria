#!/usr/bin/env python3
from pathlib import Path

# Footer HTML (adjusted paths for policies directory - need ../../ instead of ../)
footer_html = '''
    <footer-group class="footer-group block w-full"><!-- BEGIN sections: footer-group -->
<div id="shopify-section-sections--25703129907509__footer" class="shopify-section shopify-section-group-footer-group"><style data-shopify>#shopify-section-sections--25703129907509__footer {
    --section-padding-top: 60px;
    --section-padding-bottom: 96px;--color-background: 198 1 90;--color-foreground: 255 255 255;
  --color-border: var(--color-foreground)/ 0.1;
  --color-border-dark: var(--color-foreground)/ 0.4;
  --color-border-light: var(--color-foreground)/ 0.06;--color-button-background: 255 255 255;
  --color-button-border: 255 255 255;--color-button-text: 0 0 0;}</style><div class="section section--padding section--rounded" is="footer-parallax">
  <footer class="footer page-width page-width--full relative grid"><div class="footer__left flex flex-col md:flex-row gap-10"><div class="footer__accordions flex flex-wrap flex-col md:flex-row md:grow md:gap-12"><details class="footer__item--brand_information details active" is="footer-details">
      <summary class="details__summary flex items-center justify-between gap-2 cursor-pointer">
        <span class="text-base-2xl font-medium">Искате да се свържете с нас?</span><svg class="icon icon-chevron-up icon-md" viewBox="0 0 24 24" stroke="currentColor" fill="none" xmlns="http://www.w3.org/2000/svg">
      <path stroke-linecap="round" stroke-linejoin="round" d="M6 15L12 9L18 15"/>
    </svg></summary><div class="details__content">
      <div class="footer__contact flex flex-col gap-1"><p>
            <a class="link inline-block leading-tight text-left" href="https://wa.me/359896345048" is="magnet-link">
              <span class="btn-text" data-text>Пишете ни в WhatsApp</span>
            </a>
          </p><p>
            <a class="link inline-block leading-tight text-left" href="../../pages/events-form/" is="magnet-link">
              <span class="btn-text" data-text>Запитване за оферта</span>
            </a>
          </p><p>
            <a class="link inline-block leading-tight text-left" href="mailto:bgvide@gmail.com" is="magnet-link">
              <span class="btn-text" data-text>Изпрати имейл</span>
            </a>
          </p></div>
    </div>
    <style>
      @media (min-width: 1280px) {
        .footer__item--brand_information { width: calc(95% - var(--sp-12)); }
      }
    </style></details><details class="footer__item--link_list_RHz6UU details active" is="footer-details">
      <summary class="details__summary flex items-center justify-between gap-2 cursor-pointer">
        <span class="text-base-2xl font-medium">Бърза навигация</span><svg class="icon icon-chevron-up icon-md" viewBox="0 0 24 24" stroke="currentColor" fill="none" xmlns="http://www.w3.org/2000/svg">
      <path stroke-linecap="round" stroke-linejoin="round" d="M6 15L12 9L18 15"/>
    </svg></summary><div class="details__content">
      <ul class="flex flex-col gap-3"><li class="inline-flex">
            <a href="../../search/" class="block reversed-link text-sm-lg leading-tight">Търсене</a>
          </li><li class="inline-flex">
            <a href="../../pages/about-us/" class="block reversed-link text-sm-lg leading-tight">Относно</a>
          </li><li class="inline-flex">
            <a href="../../pages/events/" class="block reversed-link text-sm-lg leading-tight">Услуги</a>
          </li><li class="inline-flex">
            <a href="../../pages/contact/" class="block reversed-link text-sm-lg leading-tight">Контакт</a>
          </li><li class="inline-flex">
            <a href="../../pages/שאלות-תשובות/" class="block reversed-link text-sm-lg leading-tight">ЧЗВ</a>
          </li></ul>
    </div>
    <style>
      @media (min-width: 1280px) {
        .footer__item--link_list_RHz6UU { width: calc(50% - var(--sp-12)); }
      }
    </style></details><details class="footer__item--link_list_yfrGqh details active" is="footer-details">
      <summary class="details__summary flex items-center justify-between gap-2 cursor-pointer">
        <span class="text-base-2xl font-medium">Политики</span><svg class="icon icon-chevron-up icon-md" viewBox="0 0 24 24" stroke="currentColor" fill="none" xmlns="http://www.w3.org/2000/svg">
      <path stroke-linecap="round" stroke-linejoin="round" d="M6 15L12 9L18 15"/>
    </svg></summary><div class="details__content">
      <ul class="flex flex-col gap-3"><li class="inline-flex">
            <a href="../terms-of-service/" class="block reversed-link text-sm-lg leading-tight">Общи условия</a>
          </li><li class="inline-flex">
            <a href="../privacy-policy/" class="block reversed-link text-sm-lg leading-tight">Политика за поверителност</a>
          </li><li class="inline-flex">
            <a href="../terms-of-service/" class="block reversed-link text-sm-lg leading-tight">Условия за ползване</a>
          </li><li class="inline-flex">
            <a href="../../pages/%D7%AA%D7%A7%D7%A0%D7%95%D7%9F-%D7%94%D7%92%D7%A8%D7%9C%D7%94/" class="block reversed-link text-sm-lg leading-tight">Правила за промоции</a>
          </li></ul>
    </div>
    <style>
      @media (min-width: 1280px) {
        .footer__item--link_list_yfrGqh { width: calc(50% - var(--sp-12)); }
      }
    </style></details></div>
      </div><div class="footer__right grid gap-10"><div class="footer__socials flex justify-start md:justify-end xl:justify-start"><ul class="flex flex-wrap items-center gap-7"><li><a href="../../../../www.instagram.com/vide.events.bulgaria/" class="social_platform block relative" is="magnet-link" title="VIDE Bulgaria on Instagram"><svg class="icon icon-instagram icon-lg" viewBox="0 0 24 24" stroke="none" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
      <path d="M12 2.98C14.94 2.98 15.28 2.99 16.44 3.04C17.14 3.04 17.83 3.18 18.48 3.42C18.96 3.6 19.39 3.88 19.75 4.24C20.12 4.59 20.4 5.03 20.57 5.51C20.81 6.16 20.94 6.85 20.95 7.55C21 8.71 21.01 9.06 21.01 12C21.01 14.94 21 15.28 20.95 16.44C20.95 17.14 20.81 17.83 20.57 18.48C20.39 18.95 20.11 19.39 19.75 19.75C19.39 20.11 18.96 20.39 18.48 20.57C17.83 20.81 17.14 20.94 16.44 20.95C15.28 21 14.93 21.01 12 21.01C9.07 21.01 8.72 21 7.55 20.95C6.85 20.95 6.16 20.81 5.51 20.57C5.03 20.39 4.6 20.11 4.24 19.75C3.87 19.4 3.59 18.96 3.42 18.48C3.18 17.83 3.05 17.14 3.04 16.44C2.99 15.28 2.98 14.93 2.98 12C2.98 9.07 2.99 8.72 3.04 7.55C3.04 6.85 3.18 6.16 3.42 5.51C3.6 5.03 3.88 4.6 4.24 4.24C4.59 3.87 5.03 3.59 5.51 3.42C6.16 3.18 6.85 3.05 7.55 3.04C8.71 2.99 9.06 2.98 12 2.98ZM12 1C9.01 1 8.64 1.01 7.47 1.07C6.56 1.09 5.65 1.26 4.8 1.58C4.07 1.86 3.4 2.3 2.85 2.85C2.3 3.41 1.86 4.07 1.58 4.8C1.26 5.65 1.09 6.56 1.07 7.47C1.02 8.64 1 9.01 1 12C1 14.99 1.01 15.36 1.07 16.53C1.09 17.44 1.26 18.35 1.58 19.2C1.86 19.93 2.3 20.6 2.85 21.15C3.41 21.7 4.07 22.14 4.8 22.42C5.65 22.74 6.56 22.91 7.47 22.93C8.64 22.98 9.01 23 12 23C14.99 23 15.36 22.99 16.53 22.93C17.44 22.91 18.35 22.74 19.2 22.42C19.93 22.14 20.6 21.7 21.15 21.15C21.7 20.59 22.14 19.93 22.42 19.2C22.74 18.35 22.91 17.44 22.93 16.53C22.98 15.36 23 14.99 23 12C23 9.01 22.99 8.64 22.93 7.47C22.91 6.56 22.74 5.65 22.42 4.8C22.14 4.07 21.7 3.4 21.15 2.85C20.59 2.3 19.93 1.86 19.2 1.58C18.35 1.26 17.44 1.09 16.53 1.07C15.36 1.02 14.99 1 12 1ZM12 6.35C10.88 6.35 9.79 6.68 8.86 7.3C7.93 7.92 7.21 8.8 6.78 9.84C6.35 10.87 6.24 12.01 6.46 13.1C6.68 14.2 7.22 15.2 8.01 15.99C8.8 16.78 9.81 17.32 10.9 17.54C12 17.76 13.13 17.65 14.16 17.22C15.19 16.79 16.07 16.07 16.7 15.14C17.32 14.21 17.65 13.12 17.65 12C17.65 10.5 17.05 9.06 16 8.01C14.94 6.95 13.5 6.36 12.01 6.36L12 6.35ZM12 15.67C11.27 15.67 10.57 15.45 9.96 15.05C9.36 14.65 8.89 14.07 8.61 13.4C8.33 12.73 8.26 11.99 8.4 11.28C8.54 10.57 8.89 9.92 9.4 9.4C9.91 8.88 10.57 8.54 11.28 8.4C11.99 8.26 12.73 8.33 13.4 8.61C14.07 8.89 14.64 9.36 15.05 9.96C15.45 10.56 15.67 11.27 15.67 12C15.67 12.97 15.28 13.91 14.6 14.59C13.91 15.28 12.98 15.66 12.01 15.66L12 15.67ZM17.87 7.45C18.6 7.45 19.19 6.86 19.19 6.13C19.19 5.4 18.6 4.81 17.87 4.81C17.14 4.81 16.55 5.4 16.55 6.13C16.55 6.86 17.14 7.45 17.87 7.45Z"/>
    </svg><span class="sr-only">Instagram</span>
        </a>
      </li><li><a href="../../../../www.tiktok.com/%40vide_is_from_webapp%3D1%26sender_device%3Dpc.prints.html" class="social_platform block relative" is="magnet-link" title="VIDE Bulgaria on TikTok"><svg class="icon icon-tiktok icon-lg" viewBox="0 0 24 24" stroke="none" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
      <path d="M10.6315 8.937V13.059C10.1123 12.9221 9.56911 12.9034 9.0418 13.0044C8.5145 13.1054 8.01657 13.3234 7.58473 13.6424C7.15288 13.9613 6.79813 14.3732 6.54661 14.8475C6.2951 15.3218 6.15324 15.8466 6.13148 16.383C6.10175 16.8449 6.17125 17.3078 6.33531 17.7405C6.49938 18.1733 6.7542 18.5659 7.08266 18.892C7.41111 19.2181 7.80557 19.4701 8.23952 19.631C8.67346 19.7919 9.13684 19.8581 9.59848 19.825C10.0648 19.8608 10.5333 19.7949 10.9717 19.6319C11.41 19.4689 11.8078 19.2126 12.1374 18.8809C12.4671 18.5491 12.7208 18.1498 12.881 17.7104C13.0413 17.271 13.1042 16.8021 13.0655 16.336V0H17.1425C17.8355 4.315 19.9935 5.316 22.8825 5.778V9.913C20.8804 9.74881 18.9491 9.09645 17.2575 8.013V16.18C17.2575 19.88 15.0675 24 9.63048 24C8.61045 23.9955 7.60156 23.7875 6.66297 23.3881C5.72437 22.9886 4.87496 22.4059 4.16451 21.6739C3.45407 20.942 2.89689 20.0755 2.52563 19.1254C2.15438 18.1754 1.97652 17.1607 2.00248 16.141C2.03479 15.0794 2.29174 14.0366 2.75639 13.0815C3.22105 12.1265 3.88285 11.2807 4.69819 10.6C5.51352 9.9193 6.46387 9.41915 7.48658 9.1325C8.50929 8.84586 9.58114 8.77923 10.6315 8.937Z"/>
    </svg><span class="sr-only">TikTok</span>
        </a>
      </li></ul></div></div></footer><parallax-overlay class="footer-overlay hidden md:block z-20 absolute left-0 top-0 w-full pointer-events-none" data-target="height" data-start="100%" data-stop="0%"></parallax-overlay></div>


</div><div id="shopify-section-sections--25703129907509__scrolling_text_3waECX" class="shopify-section shopify-section-group-footer-group scrolling-text-section"><style>
  #shopify-section-sections--25703129907509__scrolling_text_3waECX {
    --section-padding-top: 4px;
    --section-padding-bottom: 4px;--color-background: 255 255 255;--color-foreground: 198 1 90;
  --color-border: var(--color-foreground)/ 0.1;
  --color-border-dark: var(--color-foreground)/ 0.4;
  --color-border-light: var(--color-foreground)/ 0.06;--section-grid-gap: 50px;
  }
</style>

<div class="section section--padding section--rounded relative">
  <div class="relative z-1"><marquee-element class="scrolling-text scrolling-text--left flex items-center" data-speed="2.5" data-direction="left" data-parallax="1.5"><div class="marquee flex items-center flex-auto whitespace-nowrap"></div></marquee-element></div>
</div>


</div>
<!-- END sections: footer-group --></footer-group>
  </div>

  <ul hidden>
    <li id="a11y-refresh-page-message">Choosing a selection results in a full page refresh.</li>
    <li id="a11y-new-window-message">Отвори в нов прозорец</li>
  </ul>
  <script>
  document.addEventListener('globo.formbuilder.form.loaded', e => {
    const {formId, form} = e.detail
    if (formId == "45693") {
      const urlParams = new URLSearchParams(window.location.search);
      const fbclid = urlParams.get('fbclid');
      
      fbclidInput = form.querySelector('input[value="fbclid"]')
      fbclidInput.value = fbclid;
    }
  })
</script>
<style> .globo-form-app .header:before {display: none !important;} </style>
</body>
</html>
'''

# Policy files to fix
policy_files = [
    Path("public/videprints.com/policies/terms-of-service/index.html"),
    Path("public/videprints.com/policies/privacy-policy/index.html"),
]

for policy_file in policy_files:
    if not policy_file.exists():
        print(f"File not found: {policy_file}")
        continue
    
    with open(policy_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if footer already exists
    if 'footer-group' in content:
        print(f"Footer already exists in {policy_file}")
        continue
    
    # Find </main> and add footer after it
    if '</main>' in content:
        content = content.replace('    </main>', '    </main>\n\n' + footer_html)
        print(f"Added footer to {policy_file}")
    else:
        print(f"Could not find </main> in {policy_file}")
        continue
    
    with open(policy_file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Done adding footers to policy pages!")
