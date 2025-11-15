#!/usr/bin/env python3
"""
Start WhatsApp bot for testing with ngrok
"""

import os
from dotenv import load_dotenv
from whatsapp_business_bot import WhatsAppBusinessBot

def main():
    load_dotenv()
    
    print("💫 Starting Snap2Pay for Testing")
    print("=" * 50)
    print("📱 Your Snap2Pay Details:")
    print(f"   Phone Number: {os.getenv('WHATSAPP_TEST_NUMBER')}")
    print(f"   Phone Number ID: {os.getenv('WHATSAPP_PHONE_NUMBER_ID')}")
    print(f"   Verify Token: {os.getenv('WHATSAPP_VERIFY_TOKEN')}")
    print()
    print("🌐 Server starting on http://localhost:8000")
    print("📱 Test webhook: http://localhost:8000/webhook")
    print("📱 After ngrok setup, your webhook will be: https://your-ngrok-url.com/webhook")
    print()
    print("Next steps:")
    print("1. Keep this running")
    print("2. Test locally: http://localhost:8000/webhook?hub.mode=subscribe&hub.verify_token=whatsapp_payment_bot_verify_2024&hub.challenge=12345")
    print("3. In another terminal: ngrok http 8000")
    print("4. Copy the https URL from ngrok")
    print("5. Set it as webhook in Facebook Developer Console")
    print("6. Add your phone number to allowed recipients")
    print("7. Message your bot!")
    print()
    print("Press Ctrl+C to stop")
    print("=" * 50)
    
    try:
        bot = WhatsAppBusinessBot()
        # Bind to localhost for Windows, but allow external connections
        bot.run(host="127.0.0.1", port=8000)
    except KeyboardInterrupt:
        print("\n✅ Bot stopped")

if __name__ == "__main__":
    main()