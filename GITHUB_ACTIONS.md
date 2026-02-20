# GitHub Actions Setup - VerifyAI

## 🤖 تفعيل النشر التلقائي عبر GitHub Actions

### الخطوة 1: إضافة Secrets إلى GitHub

في المستودع على GitHub:
1. اذهب إلى "Settings" → "Secrets and variables" → "Actions"
2. أضف الـ Secrets التالية:

```
VERCEL_TOKEN = (من Vercel Account Settings)
VERCEL_ORG_ID = (معرّف المنظمة)
VERCEL_PROJECT_ID = (معرّف المشروع)
GEMINI_API_KEY = AIzaSyANg93fYEK5HuDWbyVXW7B1CeHHCL3bQaE
SLACK_WEBHOOK = (اختياري - لإشعارات Slack)
```

### الخطوة 2: الحصول على Vercel Tokens

#### الحصول على VERCEL_TOKEN:
1. اذهب إلى: https://vercel.com/account/tokens
2. انقر "Create"
3. اختر "Full Access"
4. انسخ الـ Token

#### الحصول على VERCEL_ORG_ID:
1. اذهب إلى: https://vercel.com/account/general
2. ابحث عن "Team ID"
3. انسخه

#### الحصول على VERCEL_PROJECT_ID:
1. اذهب إلى مشروعك على Vercel
2. اذهب إلى "Settings"
3. ابحث عن "Project ID"
4. انسخه

### الخطوة 3: تفعيل Workflow

الملف `.github/workflows/deploy.yml` موجود بالفعل ويتضمن:

✅ اختبار الكود  
✅ فحص الأمان  
✅ النشر على Vercel  
✅ إشعارات Slack  

### الخطوة 4: اختبار الـ Workflow

```bash
# اجعل تغيير بسيط
echo "# Test" >> README.md

# ادفعه
git add README.md
git commit -m "test: trigger GitHub Actions"
git push origin main
```

ثم اذهب إلى "Actions" في المستودع لمراقبة التنفيذ.

---

## 📋 ملف الـ Workflow

### المسار:
```
.github/workflows/deploy.yml
```

### الخطوات:
1. **Checkout** - سحب الكود
2. **Setup Python** - تثبيت Python 3.11
3. **Install Dependencies** - تثبيت المكتبات
4. **Run Linting** - فحص الكود
5. **Run Tests** - تشغيل الاختبارات
6. **Deploy to Vercel** - النشر
7. **Comment PR** - تعليق على PR
8. **Notify Slack** - إرسال إشعار

---

## ✅ التحقق من الـ Workflow

### في GitHub:
1. اذهب إلى "Actions"
2. اختر آخر workflow
3. تحقق من الحالة (✅ أو ❌)
4. اعرض السجلات

### السجلات المتوقعة:
```
✅ Checkout code
✅ Setup Python 3.11
✅ Install dependencies
✅ Run linting
✅ Run tests
✅ Deploy to Vercel
✅ Deployment successful
```

---

## 🔄 التشغيل اليدوي

يمكنك تشغيل الـ Workflow يدويًا:

1. اذهب إلى "Actions"
2. اختر "Deploy to Vercel"
3. انقر "Run workflow"
4. اختر الفرع
5. انقر "Run workflow"

---

## 📊 المراقبة

### في GitHub:
- اذهب إلى "Actions" لمراقبة التنفيذ
- اعرض السجلات التفصيلية
- تحقق من الأخطاء

### في Vercel:
- اذهب إلى "Deployments"
- اعرض حالة النشر
- تحقق من الأداء

---

## 🚨 استكشاف الأخطاء

### المشكلة: فشل الـ Workflow
```
الحل:
1. اعرض السجلات في GitHub
2. تحقق من Secrets
3. تحقق من vercel.json
4. أعد المحاولة
```

### المشكلة: فشل النشر على Vercel
```
الحل:
1. تحقق من VERCEL_TOKEN
2. تحقق من VERCEL_ORG_ID
3. تحقق من VERCEL_PROJECT_ID
4. تحقق من متغيرات البيئة
```

### المشكلة: عدم إرسال إشعارات Slack
```
الحل:
1. تحقق من SLACK_WEBHOOK
2. تأكد من أنه صحيح
3. تحقق من إذن Slack
```

---

## 🎯 أفضل الممارسات

### 1. استخدم Branch Protection
```
Settings → Branches → Add rule
- Require pull request reviews
- Require status checks to pass
- Require branches to be up to date
```

### 2. استخدم Environment Protection
```
Settings → Environments → Add environment
- اسم: production
- Deployment branches: main
```

### 3. استخدم Secrets بحذر
```
✅ لا تشارك الـ Secrets
✅ أعد تعيينها بانتظام
✅ استخدم Secrets Rotation
```

---

## 📈 الأداء المتوقع

| المرحلة | الوقت |
|--------|-------|
| Checkout | 5s |
| Setup Python | 10s |
| Install Dependencies | 30s |
| Run Linting | 5s |
| Run Tests | 10s |
| Deploy to Vercel | 60s |
| **الإجمالي** | **~120s** |

---

## ✅ قائمة التحقق

- [ ] إضافة VERCEL_TOKEN
- [ ] إضافة VERCEL_ORG_ID
- [ ] إضافة VERCEL_PROJECT_ID
- [ ] إضافة GEMINI_API_KEY
- [ ] اختبار الـ Workflow
- [ ] مراقبة السجلات
- [ ] تفعيل Branch Protection

---

**تم الإنشاء:** 2026-02-20  
**الحالة:** ✅ جاهز للتفعيل
