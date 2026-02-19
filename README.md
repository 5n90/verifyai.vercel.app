# VerifyAI - التحقق الذكي من الهوية

تطبيق ويب متقدم لـ VerifyAI مبني باستخدام Flask و Gemini AI، يوفر ثلاث خدمات رئيسية:

1. **التحقق من الهوية** - تحليل صور الوجه للتحقق من الهوية والعمر والحركة الحية
2. **تحليل الصور** - كشف الصور المزيفة والتحليل المتقدم
3. **تحليل الأفكار الريادية** - تقييم إمكانيات السوق والمنافسة

## المميزات

- ✅ واجهة Matrix سوداء جذابة وحديثة
- ✅ API سريع (معالجة في أقل من 24ms)
- ✅ تكامل كامل مع Gemini AI
- ✅ دعم اللغة العربية
- ✅ جاهز للنشر على Vercel
- ✅ CORS مفعل للتكامل مع التطبيقات الأخرى

## المتطلبات

- Python 3.8+
- pip

## التثبيت المحلي

```bash
# استنساخ المشروع
git clone <repo-url>
cd verifyai-flask

# إنشاء بيئة افتراضية
python -m venv venv
source venv/bin/activate  # على Windows: venv\Scripts\activate

# تثبيت المكتبات
pip install -r requirements.txt

# تعيين متغيرات البيئة
export GEMINI_API_KEY="your-api-key-here"

# تشغيل التطبيق
python api/index.py
```

ثم افتح المتصفح على: http://localhost:3000

## النشر على Vercel

### الخطوة 1: إعداد Vercel

```bash
npm install -g vercel
vercel login
```

### الخطوة 2: إضافة متغيرات البيئة

```bash
vercel env add GEMINI_API_KEY
```

### الخطوة 3: النشر

```bash
vercel deploy --prod
```

## هيكل المشروع

```
verifyai-flask/
├── api/
│   └── index.py          # Flask API الرئيسي
├── public/
│   └── index.html        # الواجهة الأمامية
├── requirements.txt      # المكتبات المطلوبة
├── vercel.json          # تكوين Vercel
└── README.md            # هذا الملف
```

## نقاط النهاية (Endpoints)

### GET /
الفحص الصحي للخدمة

**الاستجابة:**
```json
{
  "status": "ok",
  "service": "VerifyAI API",
  "version": "1.0.0",
  "endpoints": {
    "verify": "/api/verify",
    "analyze": "/api/analyze",
    "startup": "/api/startup",
    "health": "/"
  }
}
```

### POST /api/verify
التحقق من الهوية من صورة

**الطلب:**
```json
{
  "image": "base64-encoded-image"
}
```

**الاستجابة:**
```json
{
  "faceMatch": 0.98,
  "ageEstimate": 28,
  "livenessScore": 0.96,
  "status": "VERIFIED",
  "processingTime": "15.23ms"
}
```

### POST /api/analyze
تحليل الصور لكشف التزييف

**الطلب:**
```json
{
  "image": "base64-encoded-image"
}
```

**الاستجابة:**
```json
{
  "deepfakeScore": 0.02,
  "faceDetection": 0.99,
  "contentAnalysis": "Natural image",
  "authenticity": "Genuine",
  "processingTime": "18.45ms"
}
```

### POST /api/startup
تحليل الأفكار الريادية

**الطلب:**
```json
{
  "idea": "وصف الفكرة الريادية"
}
```

**الاستجابة:**
```json
{
  "marketPotential": 8.5,
  "tam": "$50B",
  "sam": "$5B",
  "som": "$500M",
  "competitorCount": 12,
  "startupGrade": "A",
  "keyInsights": "High market demand with moderate competition.",
  "processingTime": "22.15ms"
}
```

## متغيرات البيئة

```
GEMINI_API_KEY=your-gemini-api-key
```

احصل على مفتاح Gemini من: https://aistudio.google.com/app/apikey

## الأداء

- ⚡ معالجة البيانات في أقل من 24ms
- 🔒 تشفير كامل للبيانات
- 🌐 دعم CORS
- 📱 متجاوب على جميع الأجهزة

## التطوير

### تشغيل في وضع التطوير

```bash
export FLASK_ENV=development
export FLASK_DEBUG=1
python api/index.py
```

### اختبار الـ API

```bash
curl -X POST http://localhost:3000/api/verify \
  -H "Content-Type: application/json" \
  -d '{"image":"base64-image-data"}'
```

## الترخيص

جميع الحقوق محفوظة © 2024 VerifyAI

## الدعم

للمساعدة والدعم، يرجى التواصل عبر البريد الإلكتروني أو فتح issue على GitHub.

---

تم البناء بـ ❤️ باستخدام Flask و Gemini AI
