#!/usr/bin/env python3
import re
from pathlib import Path

# Policy files to fix
policy_files = [
    Path("public/videprints.com/policies/terms-of-service/index.html"),
    Path("public/videprints.com/policies/privacy-policy/index.html"),
]

# English content for Terms of Service
terms_english_content = """<div class="rte">
        <p><strong>Privacy Policy</strong></p>
        <p><br></p>
        <p>Dear User,</p>
        <p>** This document is written in masculine form for convenience only but refers to both men and women. We apologize for this.</p>
        <p><br></p>
        <p>Your use of the tools listed in <strong>Appendix A</strong> ("<strong>The Tools</strong>") of Rovad Hadash Ltd. (hereinafter "<strong>The Company</strong>") constitutes your agreement to the terms set forth in this document (hereinafter: "<strong>The Terms</strong>") and related/attached terms.</p>
        <p><br></p>
        <p>This document is intended to consolidate for you the terms of use and privacy policy in the tools. The Company draws your attention to the fact that any use of the tools, including the services provided through them, constitutes your agreement to the terms set forth below. The Company reserves the right to change, delete and/or add to the terms of these terms at any time and without commitment to provide prior or retroactive notice. Your use of the tools after making changes indicates your agreement to these changes, and therefore we recommend reviewing these terms from time to time.</p>
        <p><br></p>
        <p>If you do not agree to the terms of the terms, all or part of them, please refrain from continuing to use the tools or contact us so that we can assist you in alternative ways, through the details specified in section 4. These terms do not replace terms, terms of use or privacy policy of any service that may be linked or available through or through the tools and it is recommended to review them separately.</p>
        <p><br></p>
        <ol>
        <li>
        <strong>Privacy Policy, Information Collection and Storage.</strong>
        </li>
        <ol>
        <li>The Company respects your privacy and will handle information, as defined below, in accordance with the provisions of the law, including in accordance with the provisions of the Privacy Protection Law, 1981. As part of your use of the tools, information will be collected about you, including: information you provide on the registration page for the tools and information about your use of the tools. You are not obligated to provide the information, but failure to provide it will prevent us from providing you with services and/or the use of the tools.</li>
        <li>The tools use automatic tools to characterize your use of the tools and improve the browsing experience, by collecting unidentified data. These tools collect general information about you and your use of the tools. This information includes, among other things, your Internet service provider details, your Internet Protocol address (IP address) and domain name for accessing the tools, the location of the device used to access the tools, times and methods of using the tools, your browser type and additional anonymous details indicating how the tools are used.</li>
        <li>If you choose to connect to the tools through your social network account, we may have access to information about you that you choose to publish on that network or information we receive from it, subject to the terms of the relevant social network, and the settings you have adjusted on that network.</li>
        <li>In addition, the Company uses information files called "Cookies". These files help track visitor preferences and improve the user experience of the tools. For example, cookies allow you to save the details you entered in the various forms, thus saving you the time of filling in the details again on your next visit. If you do not want to receive or activate "cookies", you can block them at any time by changing the settings in the tools. Some cookie files may expire when you close the tools, and others may be saved on your device's or computer's memory. At any time, you can delete cookie files, even if they are saved with you. It is recommended to do so only if you are convinced that you do not want the tools, the content displayed in them and the services offered through them to be adapted to your preferences.</li>
        <li>The Company may collect and use information provided by you or collected about you, including during the use of the tools and/or the services offered through them (hereinafter together "<strong>The Information</strong>"), in order to improve, enrich or change (including changing the tools displayed to the user) the tools and the services offered in the tools. Also, the Company may use the information for operational, marketing and statistical purposes, and provide statistical and/or aggregate information that is not personal to third parties for these purposes.</li>
        <li>The services in the tools may require registration. As part of such registration, you will be required to provide personal information, such as your name, address, various ways of contacting you (phone, email), and in certain cases it is possible that an ID number for verification purposes only. The fields that will be required to fill in will be clearly marked. Without providing the requested data in the marked fields, you will not be able to register to perform actions that require registration.</li>
        <li>Also, registration for a certain service through the tools, including the Company's customer club or mailing lists or any other matter, available or accessible through the tools, may require your consent and approval to the terms of that service, and in this case you will be required to confirm your consent separately on the relevant page.</li>
        <li>If and to the extent that you provide personal information of any kind, this information will be stored in the Company's databases which are subject to the provisions of the law. The information will be stored for the purpose of managing and optimizing the service and contact with you, for operational, marketing or statistical needs, including processing the information and direct mailing for the purpose of realizing these goals, as well as providing service and encouraging customer loyalty of the Company and ensuring fair commercial activity according to law. Know that you are not required by law to provide information to the Company, and that the transfer of information by you to the Company is done at your own responsibility, voluntarily and with your consent, and you will not have any claim and/or claim against the Company and its representatives on this matter. Also, to the extent that you provide or upload any personal information to the Company or to the tools, you hereby declare that the information you provide and/or update in the tools is correct, reliable and accurate and that you are providing the information in your name and for yourself only, or that you are legally authorized to provide this information for another, and in any case you will be solely responsible in relation to the said information.</li>
        <li>In accordance with your consent, if accepted, the Company will be entitled to contact you from time to time with direct mailing for the purpose of receiving updates, offers for products and/or services, promotions and sales promotions, and this as long as no other notice has been received from you at any time.</li>
        <li>1.10. In case of payment for the service through the tools, you may be required to enter your ID number and credit card details. The said information will not be stored in the Company's databases and these details will be stored by third parties who provide the Company with clearing services and have a license for this, and they bear all responsibility for protecting the said information with all that implies.</li>
        <li>1.11. The Company makes sure not to transfer personally identifiable information about you to third parties, except only if one or more of the following cases exist:
        <ol>
        <li>Upon request or with your explicit consent or registration for a service that may require this, with your consent.</li>
        <li>In case of a legal dispute between you and the Company that will require the disclosure of your details and/or if you perform actions contrary to the law in the tools and/or in case a court order is received instructing this.</li>
        <li>For the purpose of conducting statistical analyzes and transferring statistical or other information to third parties. Such information will not allow your personal identification.</li>
        <li>In case it is found that you violated one or more of these terms of use and/or in cases where you perform or attempt to perform actions contrary to the terms of use or any legal instruction.</li>
        <li>According to a court order or a request from an authority authorized by law or for the purpose of preventing the commission of an offense;</li>
        <li>In any case where the Company believes that providing the information is necessary in order to prevent serious damage to a person's property and/or body, or in order to prevent other serious damage according to its sole discretion.</li>
        <li>In case the Company sells, transfers and/or merges its operations with another corporation, provided that the new recipient of the information accepts upon itself the provisions of these terms of use in full.</li>
        </ol>
        </li>
        <li>1.12. According to the Privacy Protection Law, 1981, you, or someone on your behalf with your power of attorney, are entitled to review information about you that is in the Company's database and even request from us to correct this information if it is not correct, complete or accurate and even delete it in appropriate cases. In order to exercise this right, a request must be sent to the Company through the contact page in the tools or through one of the contact details listed in section 4 below.</li>
        </ol>
        <li>
        <strong>Information Security</strong>
        </li>
        <ol>
        <li>The Company does everything in its power and uses advanced technological and organizational security measures to secure the tools and the communication channels through it and the information in its control, against accidental or intentional exploitation, loss, destruction or against access by unauthorized or authorized persons.</li>
        <li>The connection between your end device (computer, smartphone, tablet, etc.) and the computers supporting the tools is secured using accepted encryption methods, according to accepted standards. Also, the Company takes reasonable measures to protect the tools and hardware and software components related to its operation and ensures their regular updates, among other things, to protect the tools and its content from unauthorized intrusions, breaches or eavesdropping.</li>
        <li>Despite the above, the Company cannot guarantee the security and preservation of the information in an absolute manner and does not commit that the tools or their use will be completely immune from unauthorized access to information or content stored in them. Therefore, it is hereby clarified that the Company will not be responsible and will not bear any responsibility in case of intrusion or breach and/or any damage caused due to the use of the tools and/or the content displayed in them and/or the services attached to them, by the user or on his behalf in the tools.</li>
        <li>The data that will be received by the Company, including its suppliers and anyone on its behalf, through the tools, whether by you or by another factor, are stored on secure servers protected by advanced technologies. The Company does and will do its best to maintain the privacy of its customers using the tools. However, the Company cannot guarantee absolute immunity from intrusions into the servers where the information database is stored or from intrusions into the Company's computers and use of the information, its disclosure or misuse by those factors. In the event of one or more of the actions mentioned above, and as long as the Company has taken reasonable security measures, you will not have any claim, claim or demand against the Company. It is emphasized that the user must also take protective measures against virus intrusion into his mobile device.</li>
        </ol>
        <li>
        <strong>Intellectual Property</strong>
        </li>
        <ol>
        <li>Unless otherwise indicated or marked explicitly, the Company is the owner of all intellectual property rights in the tools and the content found or accessible through them, including the design, source code and binary code, trademarks, concepts, trade secrets, trademarks and service marks, copyrights, derivative works, reputation, ideas, logo, market data, methods, moral rights, graphic file, trade names, technical information and any parallel or derivative right to any of the above. Use of all of these, without prior explicit written consent from the Company, is absolutely prohibited and will constitute a violation of the Company's rights by you.</li>
        <li>Also, unless otherwise indicated or marked explicitly, the Company is the owner of all rights related to the content found in the tools, including text, images, graphics, sound files, animation files, video files and the way they are organized in the tools. It is forbidden to use, copy, duplicate, reproduce, process, distribute, display or publish content from the tools or make any use of it for commercial or private needs, by you or by another on your behalf, without prior explicit written consent from the Company.</li>
        </ol>
        <li>
        <strong>Contact</strong>
        </li>
        <ol>
        <li>In any case of a question and/or request, please contact us through one of the following means:</li>
        </ol>
        <p><strong>Contact Form on the Website</strong> at https://videprints.com/</p>
        <p><strong>By Email</strong> - Support@videprints.com</p>
        <p><strong>By WhatsApp</strong> – 054-6492267</p>
        <ol>
        <li>If you believe that your privacy has been violated in any way through the use of the tools, by any factor, please contact us through one of the means listed above.</li>
        </ol>
        <p><br></p>
        <p><strong>Terms of Use for User in the Tools</strong></p>
        <p><br></p>
        <p>The tools listed in <strong>Appendix A</strong> ("<strong>The Tools</strong>") of Rovad Hadash Ltd. (hereinafter: "<strong>The Company</strong>") are provided for use through your device and belong to the Company. Use of the tools, whether through the tools and/or any other auxiliary service for the tools, including representative support and telephone response as will be from time to time (hereinafter: "<strong>Auxiliary Services</strong>"), indicates your agreement to the terms set forth in this document or other documents linked to this document ("<strong>Terms of Use</strong>") and to the other terms appearing or that will appear when using the tools. If you do not agree to any of the terms of use and/or the additional terms (as defined below), you are requested to refrain from making any use of the tools, including the services offered through them and including through the auxiliary services (hereinafter, together - "<strong>The Services</strong>").</p>
        <p><br></p>
        <p>These terms of use will apply to any use made by you, including use of the services offered through the tools, and constitute a legally binding agreement between you and anyone on your behalf who will use these services and the Company. Certain benefits, including promotions, coupons and services offered in the tools, may be subject to additional terms ("<strong>Additional Terms</strong>") and may change from time to time. The additional terms will be linked to these terms of use and/or will appear in the tools and will be placed in the appropriate areas, including but not limited to, section 10 below. It is emphasized that the additional terms will include by way of reference to the terms of use and that any term not defined in the additional terms will have the meaning given to it in these terms of use. In any case of conflict between the provisions of the terms of use and the additional terms and/or provisions of other agreements and/or provisions of other publications regarding the tools, including the services offered through them, these terms of use will prevail, unless explicitly stated otherwise by the Company.</p>
        <p><br></p>
        <ol>
        <li>
        <strong>Changes to Use</strong>
        </li>
        <ol>
        <li>The Company may make changes to the terms of use at any time, according to its sole discretion. Changes to the terms of use that are subject to the provisions of the law will enter into force from the date of their publication in the tools, even if no prior notice was given by the Company.</li>
        <li>Your continued use of the tools and the services provided in them after making the changes to the terms of use as mentioned will indicate your agreement and acceptance of the new terms of use. If you do not agree to any of the new terms of use, you must refrain from continuing to use the tools and the services offered in them.</li>
        <li>The Company may, according to its sole discretion, at any time, in any way and for any reason, change or delete all or part of the tools and/or services, or impose charges for access to the tools and/or services (all or part of them), with or without prior notice. The Company will not be responsible towards the user and/or towards any third party due to such change or deletion. To the extent that you object to changes made or to be made by the Company, you are requested to refrain from making any use of the tools and/or services. Your use of the tools and the services offered through it, after making the changes as mentioned, will indicate your agreement to the changes.</li>
        <li>The Company may, according to its sole discretion, at any time, in any way and for any reason, immediately block your access to the tools.</li>
        <li>You hereby confirm and agree that the Company will not bear any responsibility towards you or towards a third party, due to blocking your access to the tools and/or services. Stopping your access to the tools will not change and/or cancel any liability that will arise as a result of your use of the tools and/or services, whether such commitment is towards the Company or towards third parties.</li>
        </ol>
        <li>
        <strong>License</strong>
        </li>
        <ol>
        <li>Subject to your compliance with the terms of use, the Company grants you a limited, non-transferable and non-assignable license and/or sub-licensing, to use the tools and services and install the tools on the devices according to the requirements detailed in <strong>Appendix A</strong>, and subject to your compliance with the relevant terms of use for the devices, including Apple: App Store Terms of Service and Google Play Terms of Service as applicable ("<strong>The License</strong>").</li>
        <li>The tools can be used through any computer or mobile device that meet the requirements as detailed in <strong>Appendix A</strong>. The Company is not responsible for ensuring that the services will be compatible with the computer or mobile device in your possession.</li>
        </ol>
        <li>
        <strong>General Rules of Use for User</strong>
        </li>
        <ol>
        <li>Failure to comply with the terms of this section may expose you to criminal and/or civil liability and you will be subject to the penalties prescribed by law for their violation.</li>
        <li>The Company will be entitled to block your access to the tools and/or the services offered in the tools, for a limited or unlimited period, according to its sole discretion and for any reason without the need to provide justification. Without derogating from the above, blocking your access to the tools and/or services may apply, among other things, in cases where there is a concern that you have violated the terms of use (or any other instruction that will appear in the tools) or the provisions of the law, or in case you harm or attempt to harm the proper conduct of the tools or any third party.</li>
        <li>If your access to the tools and/or services has been blocked as mentioned, you will not be entitled to re-register in the tools under another username during the restriction period, if any, except with the approval of the Company. Your attention is drawn to the fact that registration while impersonating another person constitutes a criminal offense.</li>
        <li>By using the tools and/or services, you hereby declare that you will use the tools and/or the services offered through them for yourself and for anyone on your behalf only, that the use is intended for legal purposes subject to the provisions of the terms of use and the provisions of the law, and you will refrain from any commercial use of the tools, including charging for services offered in the tools (unless approved by the Company), or any other use that is not personal, or that may harm the Company or a third party as determined according to our sole discretion.</li>
        <li>If you are a minor (under the age of 18), the use of the tools is conditional on receiving the approval of your guardian for the terms of use, including the privacy policy detailed in them. If explicit approval as mentioned has not been received, you undertake to refrain from making any use of the tools, including the services offered in it.</li>
        <li>It is clarified for the sake of removing doubt that the name of the Company, with all its derivatives and brands, as well as the names of the tools, and the domain names of the tools, are protected trademarks of the Company and in its full and exclusive ownership. The mere entry and/or use of the tools does not grant any license and/or right of any kind in them.</li>
        </ol>
        <li>
        <strong>Prohibited Uses</strong>
        </li>
        <ol>
        <li>Without receiving explicit, written permission in advance from the Company, you are not entitled to perform the following actions and/or acts:
        <ol>
        <li>4.1.1. Commercial use of the tools and/or their content and/or use of the tools and/or their content for the purpose of creating a database and/or collection;</li>
        <li>4.1.2. To copy, reproduce, modify, process, translate, perform reverse engineering, distribute, broadcast, display, perform, duplicate, publish and store the content of the tools, all or part of them;</li>
        <li>4.1.3. To operate or allow the operation of any computer application or any other means, including software of the Crawlers, Robots type and the like, for the purpose of searching, scanning, copying or automatic retrieval of the content of the tools;</li>
        <li>4.1.4. To display content from the tools within a visible or hidden frame (iframe) or to display the content of the tools in any way that changes their original design in the tools and/or omits anything;</li>
        </ol>
        </li>
        <li>Failure to comply with these limitations may lead to preventing your access to the tools and even expose you to civil and/or criminal liability according to any law.</li>
        </ol>
        <li>
        <strong>Providing Information, Registration and Payment Collection</strong>
        </li>
        <ol>
        <li>As of the date of publication of the terms of use, the use of the Company's application and website (as defined in <strong>Appendix A</strong>) for private customers (as will be defined by the Company from time to time) ("<strong>The Private Customer</strong>") does not involve payment. The Company may charge in the future for registration and/or certain use of the application and/or the website and/or the services provided through the application, and if the Company requests to do so, a notice will be published in the application and/or the website. In any case, the Company will not charge you any payment without your explicit consent to this.</li>
        <li>As of the date of publication of the terms of use, in order to use the editing software and the web system, registration is required. The Company may require registration for the rest of the tools according to its sole discretion (tools that require a registration process will be called hereinafter: "<strong>Tools Requiring Registration</strong>"). Your registration for tools that require registration is subject to additional terms and the Company's privacy policy. As part of the registration, you may be required to provide your personal information - name, phone number, email address, and if payments can be made through the tools, payment method details.</li>
        <li>You are not obligated to provide these details, but know that you will not be able to use the tools that require registration and the services offered in them without providing the required details as part of the registration process. The data you provide when registering for tools that require registration (except for data related to the payment clearing process, as detailed below) will be stored in the Company's information database. The Company's use of details about you will be subject to the Company's privacy policy.</li>
        <li>You must ensure that you provide correct details when registering for tools that require registration and update any change in details, which will be in accordance with the details in the privacy policy.</li>
        <li>The Company reserves the right to take any action as it deems appropriate and according to its sole discretion, to ensure the security of the tools, including and without limitation, requesting additional details in order to confirm transactions in which your account is linked, as well as closing your account as needed.</li>
        </ol>
        <li>
        <strong>Payment and Transaction Cancellation</strong>
        </li>
        <p>The following instructions will apply to any payment:</p>
        <ol>
        <li>Payment for the services is possible by credit card and/or in any other way according to the Company's discretion at the time of the order. After payment approval at the time of order completion, a receipt and tax invoice for the payment will be sent to the email address you provided during registration. Sending the receipt is instead of sending a receipt by physical mail.</li>
        <li>In this terms of use document, "credit card" means as stated in the Credit Cards Law, 1986, except for a direct credit card, a charged credit card and/or any other card that is charged in advance.</li>
        <li>You hereby declare and agree that: (a) sending the receipt/tax invoice to the email box as mentioned above will be considered as receiving it for all intents and purposes; (b) you will not have any claim, claim and/or demand against the Company if the receipt sent to you is classified by your email server as an offensive message and/or spam; (c) the responsibility for any result arising from providing incorrect or misleading email address details will be solely on you.</li>
        <li>The Company examines each cancellation case individually and reserves the right to change the cancellation policy individually according to its sole discretion and subject to the law.</li>
        </ol>
        <li>
        <strong>Payment Processing Service</strong>
        </li>
        <ol>
        <li>The Company uses third-party payment processing services to make the payment (hereinafter: "<strong>Payment Processing Companies</strong>" and "<strong>Payment Companies</strong>"). Making the payment through payment companies is subject to the relevant terms of use and privacy policy, including the terms of use of PayPlus Ltd.: Data Security Policy https://www.payplus.co.il/data-security and Terms of Service https://www.payplus.co.il/privacy.</li>
        <li>As part of the payment services, payment details and/or credit card details are entered by the user and/or any other detail related to the payment ("<strong>Credit Details</strong>") and reach the payment company. After the above data is entered, the Company receives from the payment company anonymous unique information (Token) that allows linking between the user and his/her credit details for payment by credit card for the services. We do not use the credit details ourselves and we do not store the credit details in our information databases.</li>
        <li>We remove all responsibility in connection with the payment services, and the use of these services is at the sole responsibility of the user.</li>
        <li>Payment companies may use credit details only for: 1) improving payment processing services (without using personal information); (2) implementing fraud prevention mechanisms or in connection with legal disputes between the payment processing company and the users and/or the Company. In addition, the payment company will be able to transfer anonymous statistical information it collects to third parties for its commercial purposes.</li>
        </ol>
        <li>
        <strong>Limitation of Liability</strong>
        </li>
        <ol>
        <li>The Company will do its best to operate the tools and the services offered in it properly, without technical failures and without interruptions. However, and since the operation of the tools depends on third parties, including cellular operators, photographers, the tools may not always be immune to interruptions and failures in their regular operation. In light of the above, you will not have any claim, demand or claim of any kind against the Company due to any failure or interruption as mentioned, including due to any damage caused, directly or indirectly, as a result of interruptions or failures as mentioned. The Company will not bear any responsibility and/or liability for any disruption, error or omission in the material found in the tools and/or the various services and/or the contents in them, and will not be responsible for any direct or indirect damage, caused due to access to the tools and/or the website and their use or due to any prevention of access or use of them.</li>
        <li>The Company, and anyone who received explicit written permission from it, may publish commercial information and advertisements through the tools using advertising spaces intended for this. The responsibility for the content of the published advertisements is solely on the advertisers. The Company has no responsibility regarding the content of the publications or their reliability. Publishing the information in the tools will not be considered as a recommendation of the Company to purchase the services included in the advertisements as mentioned, and the responsibility for purchasing the services included in the advertisements will be solely on the user.</li>
        <li>To the maximum extent permitted by law, the Company, including its suppliers and anyone on its behalf, provides the user with the tools in their condition as they are (As-Is) including all defects in them, including inaccuracies, computer failures and human errors. The Company and anyone on its behalf explicitly remove from themselves any responsibility and any condition, whether explicit, implied or by law, including but without detracting from the generality of the above, any responsibility or conditions (if any) regarding ownership, copyright infringement, suitability for commercial purpose, suitability for a specific purpose, absence of viruses, absence of negligence and suitability for description.</li>
        <li>It is hereby clarified that the Company's commitment to preserve images and videos uploaded by users who are customers of the Company will not exceed a period of two years from the date of upload (or a shorter period as this document will be updated from time to time), unless otherwise explicitly stated. Despite the above, the Company also uses tools and services of third parties as detailed in this document, and therefore it is possible that in practice the retention period will be shorter, according to the limitations and conditions of those third parties. The Company will not bear any responsibility for deletion, loss or damage to images and videos beyond the said period and/or due to third-party limitations.</li>
        </ol>
        <li>
        <strong>Coupons and Promotions</strong>
        </li>
        <ol>
        <li>Discount codes and promotions ("<strong>Coupons and Promotions</strong>") may be sent to you through one of these: email, text messages, Push messages and/or will be updated in the tools. These constitute an offer to purchase products and services from the Company at the times, prices and conditions set forth below and as mentioned in the tools ("<strong>Terms of Coupons and Promotions</strong>").</li>
        <li>The use of coupons and utilization of promotions, including purchasing products and services through them, indicates your agreement to the terms of use and the other terms appearing in the tools and/or that will appear when using. If you do not agree to any of the terms of use and/or the additional terms, you are requested to refrain from making any use of coupons and promotions, including purchasing products and services through them.</li>
        <li>The provisions of the terms of coupons and promotions will apply to any use made by you, including purchasing products and services, and they constitute a legally binding agreement between you and the Company.</li>
        <li>As mentioned, the coupons and promotions appearing in the tools may be subject to additional terms. In any case of conflict between the provisions of the terms of use and the additional terms and/or provisions of other agreements and/or provisions of other publications regarding the tools, including the services offered through them, these terms of use will prevail, unless explicitly stated otherwise.</li>
        <li>If you encounter any difficulties in utilizing the coupons and promotions, contact us through the Company's customer service via WhatsApp message to number 054-6492267 which will specify details about the relevant service and the discount code indicated on the coupon or promotion in your possession.</li>
        <li>The Company may make changes to the terms of coupons and promotions at any time, according to its sole discretion. Your continued use of coupons and promotions after making the changes to the terms of coupons and promotions as mentioned will indicate your agreement and acceptance of the new terms of coupons and promotions. If you do not agree to any of the new terms of coupons and promotions, you must refrain from continuing to use them.</li>
        <li>For your attention, that as part of improving the service and performing ongoing optimization of the Company's services, the Company may offer, from time to time, different coupons or promotions based on criteria that are determined according to the Company's sole discretion, such as (but not only) - geographical areas, peak or off-peak hours, usage patterns in the tools, seasonality in the market and the like. The Company reserves the right to apply or stop at any time, according to its sole discretion, such or other promotion policy, and this even without updating you in advance, or at all. In your use of coupons and promotions, you give your consent and waive in advance any claim and/or demand against the Company in this regard. Also, you hereby waive, explicitly and irrevocably, any claim and/or demand in the context of a class action against the Company, and you agree that you will not be entitled to raise any claim and/or demand in connection with a class action.</li>
        <li>In addition, you agree to the terms of use of coupons and promotions as follows:
        <ol>
        <li>Utilization of the coupon or promotion will be done by credit card payment only.</li>
        <li>The coupon or promotion is personal and cannot be sold, transferred and/or assigned, whether for payment or without payment.</li>
        <li>There are coupons or promotions for which a maximum utilization period is set within which they can be utilized. After the end of this period, the coupon will have no validity, and you will lose your entitlement to purchase the product or service at a discounted price, without the right to any payment and/or compensation for the coupon or promotion.</li>
        <li>If it is a coupon or promotion whose use is defined as one-time, after use, the validity of the coupon or promotion will be canceled and it will not be possible to make any additional use of it.</li>
        <li>The coupons and promotions cannot be converted to money, including for making other purchases, and it is not possible to pay past debts through the coupons. No excess or refund of any kind will be returned for a coupon that was not utilized by you, or that was partially utilized.</li>
        </ol>
        </li>
        <li>In general, there is no double promotion on purchases made through coupons and promotions unless the Company decides to have double promotions in relation to specific coupons and/or promotions. The Company may but is not obligated to notify in advance and publish a notice about this.</li>
        <li>The Company may prevent the use of coupons and promotions, including the purchase of services at a discounted price through them, whether temporarily or permanently, whether fully or partially, and this according to its sole and absolute discretion, without justification, without giving notice about this in advance and without the Company bearing any liability from this, and this, among other things, due to one or more of the following reasons:
        <ol>
        <li>Violation of the terms of coupons and promotions;</li>
        <li>The Company believes that you performed or are about to perform an illegal act or violate the provisions of the law, through the use of coupons and promotions;</li>
        <li>Use of coupons and promotions not for the purpose for which they were created and/or in order to mislead another person and/or in order to cause harm to any third parties and/or for another purpose which in the Company's opinion constitutes abuse of the coupons and promotions; and/or</li>
        <li>For any other reason, according to the Company's sole and absolute discretion.</li>
        </ol>
        </li>
        <li>For your attention, that the terms of coupons and promotions will be updated from time to time and that there may be additional terms that will apply, in addition to the terms of use on specific coupons and/or promotions, which can be seen in various relevant publications.</li>
        </ol>
        <li>
        <strong>Rates</strong>
        </li>
        <p>The Company reserves the right to update the rates of the tools and/or the accompanying services and/or the accompanying products from time to time, as will be detailed in the tools according to the Company's discretion.</p>
        <li>
        <strong>Agreement Period and Agreement Cancellation</strong>
        </li>
        <ol>
        <li>These terms of use will serve as a binding agreement valid starting, in relation to each of the tools, from their installation on the relevant devices for the tools in your possession until it is canceled at the request of either party ("<strong>Agreement Period</strong>"). If you wish to cancel the agreement, you must notify us of your wish to cancel the agreement to the Company's email address as detailed in section 16. In this case, the cancellation will enter into force after you are sent confirmation of receipt of the cancellation notice, which will be sent within a reasonable time.</li>
        <li>If the Company requests to cancel the agreement, the Company will notify you of its intention to do so and in any case will be entitled to block your access to the tools immediately. In such a case, the cancellation will enter into force immediately upon blocking your access to the tools.</li>
        <li>Upon the end of the agreement period for any reason, you are required to immediately cease using the tools and/or any services provided by the Company.</li>
        </ol>
        <li>
        <strong>Special Terms Relating to Third-Party Components</strong>
        </li>
        <ol>
        <li>The tools may use or include software, files and/or components subject to license terms including open source licenses of third parties ("<strong>Third-Party Components</strong>"). You are entitled to use third-party components as part of or in connection with the tools only subject to your compliance with the applicable and/or attached license terms of the relevant third-party components. If there is a conflict between the license terms of a third-party component and these terms, the license terms of the relevant third-party component will prevail, and this only in the context of third-party components.</li>
        <li>These terms do not apply to any third-party components attached and/or included in the tools, and the Company removes all responsibility related to this. You acknowledge that the Company is not the creator, owner or grantor of the license of third-party components, and the Company does not provide any representation or commitment of any kind, explicitly or implied, regarding the quality, capabilities, operation, performance or suitability of this or that third-party component. The tools or any part of them (except for third-party components included in them, if included) should not be seen as "open source" software.</li>
        </ol>
        <li>
        <strong>Indemnification and Compensation</strong>
        </li>
        <p>You hereby undertake to indemnify and compensate the Company or anyone on its behalf, for any damage, expense or loss, direct or indirect, including legal expenses and attorney's fees, that will be caused to it in connection with the violation of any term of the terms of use, or the performance of any other action contrary to the law in connection with the tools and services.</p>
        <li>
        <strong>Miscellaneous</strong>
        </li>
        <ol>
        <li>These terms of use (or any of the provisions in them) do not create and will not be interpreted as creating any partnership, joint venture, employer-employee relationship, agent or representative between you and the Company or anyone on its behalf in any way.</li>
        <li>The exclusive jurisdiction to hear any dispute and/or conflict in connection with the tools and services, the Company, and/or the terms of use, and/or any claim, demand and/or request arising from this use will apply only the laws of the State of Israel and the place of jurisdiction will be in the court in Tel Aviv, and the substantive and procedural law will be Israeli law. This is subject to the Company's right to take legal proceedings in the courts where the user's address and/or place of business and/or assets or part of them are located for the Company's consideration.</li>
        <li>If any term of the terms of use is found to be illegal, void or unenforceable for any reason, this term will be deleted from the terms of use and its deletion will not affect the legality and validity of the remaining terms of use.</li>
        <li>As mentioned above, this agreement will include the terms detailed in the Company's privacy policy.</li>
        </ol>
        <li>
        <strong>Contacting the Company</strong>
        </li>
        <p>For any question and/or request in connection with the tools and services provided in them and the terms of use including the privacy policy, you can contact us through one of the following means:</p>
        <p><strong>Contact Form</strong> - https://videprints.com/</p>
        <p><strong>Email</strong> - Support@videprints.com</p>
        <p><strong>WhatsApp</strong>- 054-6492267</p>
        <p><br></p>
        <p><strong>Appendix A</strong></p>
        <p><br></p>
        <p>"<strong>The Tools</strong>" means the Company's tools listed below:</p>
        <p><br></p>
        <ol>
        <li>"<strong>Editing Software</strong>" Vide Maker software.</li>
        <li>"<strong>The Application</strong>" "Vide - AR Video Prints" application, as will be called from time to time, available on the App Store at https://apps.apple.com/il/app/vide-ar-video-prints/id1605983842?l=he and on Google Play at https://play.google.com/store/apps/details?id=co.viaar.liveframe&hl=en.</li>
        <li>"<strong>Web Panel</strong>" Web system for creating Targets (images that can be identified by the application) and managing them.</li>
        <li>"<strong>Company Website</strong>" The Company's website at https://videprints.com/.</li>
        </ol>
        </ol>
        </div>
"""

# English content for Privacy Policy (same structure, just different title)
privacy_english_content = terms_english_content.replace('<strong>Privacy Policy</strong>', '<strong>Privacy Policy</strong>', 1)

def fix_policy_page(file_path, english_content):
    """Fix a policy page to be in English"""
    if not file_path.exists():
        print(f"File not found: {file_path}")
        return
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Fix lang and dir attributes
    content = content.replace('lang="en" dir="rtl"', 'lang="en" dir="ltr"')
    
    # Fix meta descriptions
    content = re.sub(
        r'<meta property="og:description" content="[^"]*">',
        '<meta property="og:description" content="Terms of service and privacy policy for VIDE Bulgaria">',
        content
    )
    content = re.sub(
        r'<meta name="twitter:description" content="[^"]*">',
        '<meta name="twitter:description" content="Terms of service and privacy policy for VIDE Bulgaria">',
        content
    )
    
    # Find and replace the main content body
    # Look for the shopify-policy__body div
    pattern = r'(<div class="shopify-policy__body">\s*<div class="rte">).*?(</div>\s*</div>\s*</div>\s*</main>)'
    
    match = re.search(pattern, content, re.DOTALL)
    if match:
        content = content[:match.start()] + match.group(1) + '\n' + english_content + '\n        ' + match.group(2)
        print(f"Replaced content in {file_path}")
    else:
        print(f"Could not find content section in {file_path}")
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

# Fix both policy pages
fix_policy_page(policy_files[0], terms_english_content)
fix_policy_page(policy_files[1], privacy_english_content)

print("Done fixing policy pages!")
