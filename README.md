# Snap2Pay

A revolutionary WhatsApp Business API bot that processes bank account images using advanced OCR and handles secure payments. Simply snap a photo of account details and send money instantly!

![Snap2Pay Screenshot](Assets/diagram.png)

## Features
- 📸 Advanced OCR extraction of bank account details from images
- 🏦 Smart bank selection (23 Nigerian banks supported)
- ✅ Real-time account validation
- 💰 Secure payment processing with PIN protection
- 🤖 Seamless WhatsApp Business API integration
- 🔒 Enterprise-grade security features

## Demo Video
Watch the bot in action: [Demo Video](Assets/demo.mp4)

## Documentation
Detailed explanation of the system: [Project Explanation PDF](Docs/Explanation.pdf)

## Quick Start

1. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt

   ```
2. **Configure Environment:**
   - Update `.env` with your WhatsApp and Paystack credentials

3. **Install Tesseract:**
   - Download from: https://github.com/UB-Mannheim/tesseract/wiki
   - Update path in `backend/config.py`

4. **Run Bot:**
   ```bash
   python whatsapp_business_bot.py
   ```

5. **Test Setup:**
   ```bash
   python start_for_testing.py
   ```

## Usage
1. Send WhatsApp message to your business number
2. Send "START" to begin
3. Send bank account image
4. Select bank if needed
5. Confirm payment amount
6. Bot processes payment via Paystack

## Files Structure
```
├── whatsapp_business_bot.py      # Main bot application
├── start_for_testing.py          # Test runner
├── .env                          # Environment variables
├── requirements.txt              # Dependencies
├── backend/
│   ├── config.py                 # Tesseract configuration
│   ├── account_extractor/
│   │   └── account_details_ocr.py # OCR processing
│   └── payment/
│       └── paystack_api.py       # Payment processing
└── account_images/               # Processed images storage
```

## Environment Variables Required
- `WHATSAPP_ACCESS_TOKEN`
- `WHATSAPP_PHONE_NUMBER_ID`
- `WHATSAPP_VERIFY_TOKEN`
- `PAYSTACK_SECRET_KEY`
- `PAYSTACK_ENVIRONMENT`