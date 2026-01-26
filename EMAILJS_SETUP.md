# EmailJS Setup Instructions

## שלבים להגדרת EmailJS לשליחת מיילים אוטומטית

### 1. הרשמה ל-EmailJS
1. היכנס ל-https://www.emailjs.com/
2. לחץ על "Sign Up" והרשם (חינמי עד 200 מיילים בחודש)
3. אשר את המייל שלך

### 2. יצירת Email Service
1. לאחר ההתחברות, לך ל-"Email Services" בתפריט
2. לחץ על "Add New Service"
3. בחר "Gmail" (או שירות מייל אחר)
4. התחבר לחשבון Gmail שלך (bgvide@gmail.com)
5. העתק את ה-Service ID שנוצר

### 3. יצירת Email Template
1. לך ל-"Email Templates" בתפריט
2. לחץ על "Create New Template"
3. השתמש בתבנית הבאה:

**Subject:**
```
Contact Form - VIDE Bulgaria
```

**Content:**
```
New contact form submission from VIDE Bulgaria website:

Name: {{from_name}}
Email: {{from_email}}
Phone: {{phone}}
Organizer: {{organizer}}
Number of Guests: {{guests}}
Event Location: {{location}}
Category: {{category}}

Message:
{{message}}

---
Reply to: {{reply_to}}
```

4. שמור את התבנית והעתק את ה-Template ID

### 4. קבלת Public Key
1. לך ל-"Account" > "General"
2. העתק את ה-Public Key שלך

### 5. עדכון הקוד
פתח את הקובץ `public/videprints.com/pages/contact/index.html` ומצא את השורות הבאות:

```javascript
emailjs.init("YOUR_PUBLIC_KEY"); // שורה ~977
emailjs.send('YOUR_SERVICE_ID', 'YOUR_TEMPLATE_ID', templateParams) // שורה ~1010
```

החלף:
- `YOUR_PUBLIC_KEY` - עם ה-Public Key שלך
- `YOUR_SERVICE_ID` - עם ה-Service ID שיצרת
- `YOUR_TEMPLATE_ID` - עם ה-Template ID שיצרת

### 6. בדיקה
1. שמור את הקובץ
2. שלח את הקוד ל-GitHub
3. בדוק את הטופס באתר - המייל צריך להישלח אוטומטית ל-bgvide@gmail.com

## הערות חשובות:
- EmailJS חינמי עד 200 מיילים בחודש
- המייל נשלח ישירות מבלי לפתוח את תוכנת המייל של המשתמש
- כל הנתונים מהטופס נשלחים במייל אחד מסודר
