# دليل النشر على Vercel

## المتطلبات
- حساب GitHub
- حساب Vercel
- مفتاح Gemini API

---

## الخطوة 1: إعداد مستودع GitHub

### 1.1 إنشاء مستودع جديد على GitHub
```bash
# اذهب إلى https://github.com/new
# أنشئ مستودع باسم "verifyai"
```

### 1.2 ربط المستودع المحلي
```bash
cd /home/ubuntu/verifyai-flask

# إضافة مستودع بعيد
git remote add origin https://github.com/YOUR_USERNAME/verifyai.git

# تعيين الفرع الرئيسي
git branch -M main

# دفع الكود
git push -u origin main
```

---

## الخطوة 2: ربط Vercel بـ GitHub

### 2.1 تسجيل الدخول إلى Vercel
1. اذهب إلى https://vercel.com
2. اختر "Sign Up" أو "Sign In"
3. اختر "Continue with GitHub"

### 2.2 استيراد المشروع
1. اضغط على "Add New" → "Project"
2. اختر "Import Git Repository"
3. ابحث عن "verifyai" واختره
4. اضغط "Import"

---

## الخطوة 3: تكوين متغيرات البيئة

### 3.1 إضافة متغيرات البيئة في Vercel
في لوحة تحكم Vercel:
1. اذهب إلى "Settings" → "Environment Variables"
2. أضف المتغيرات التالية:

```
GEMINI_API_KEY = YOUR_GEMINI_API_KEY
```

### 3.2 إضافة Secrets في GitHub (للنشر التلقائي)
في إعدادات المستودع:
1. اذهب إلى "Settings" → "Secrets and variables" → "Actions"
2. أضف الـ Secrets التالية:

```
VERCEL_TOKEN        = (احصل عليه من Vercel Account Settings)
VERCEL_ORG_ID       = (معرّف المنظمة في Vercel)
VERCEL_PROJECT_ID   = (معرّف المشروع في Vercel)
GEMINI_API_KEY      = YOUR_GEMINI_API_KEY
SLACK_WEBHOOK       = (اختياري - لإشعارات Slack)
```

---

## الخطوة 4: النشر

### 4.1 النشر التلقائي
بعد ربط GitHub و Vercel:
- كل `push` إلى فرع `main` سيؤدي إلى نشر تلقائي
- كل `pull request` سيحصل على preview URL

### 4.2 النشر اليدوي
```bash
# تثبيت Vercel CLI
npm i -g vercel

# تسجيل الدخول
vercel login

# النشر
vercel --prod
```

---

## الخطوة 5: التحقق من النشر

### 5.1 التحقق من الرابط
بعد النشر الناجح، ستحصل على رابط مثل:
```
https://verifyai.vercel.app
```

### 5.2 اختبار API
```bash
# اختبار نقطة النهاية الصحية
curl https://verifyai.vercel.app/api/health

# اختبار التحقق من الهوية
curl -X POST https://verifyai.vercel.app/api/verify \
  -H "Content-Type: application/json" \
  -d '{"image_url": "https://example.com/image.jpg"}'
```

---

## استكشاف الأخطاء

### المشكلة: فشل البناء
```bash
# تحقق من السجلات في Vercel Dashboard
# تأكد من أن جميع المتطلبات موجودة في requirements.txt
# تأكد من أن ملف vercel.json صحيح
```

### المشكلة: خطأ في متغيرات البيئة
```bash
# تأكد من إضافة GEMINI_API_KEY في Vercel Settings
# تأكد من أن المفتاح صحيح وفعال
```

### المشكلة: timeout في API
```bash
# زيادة maxDuration في vercel.json
# تحسين أداء الكود
# استخدام caching للنتائج
```

---

## الخطوات التالية

1. ✅ ربط GitHub و Vercel
2. ✅ إضافة متغيرات البيئة
3. ✅ النشر التلقائي
4. ✅ مراقبة الأداء
5. ✅ إضافة Custom Domain (اختياري)

---

## موارد إضافية

- [Vercel Documentation](https://vercel.com/docs)
- [Vercel Python Runtime](https://vercel.com/docs/concepts/functions/serverless-functions/runtimes/python)
- [GitHub Actions](https://docs.github.com/en/actions)
- [Gemini API Documentation](https://ai.google.dev/docs)

---

**تم إنشاء هذا الدليل بواسطة VerifyAI Development Team**
