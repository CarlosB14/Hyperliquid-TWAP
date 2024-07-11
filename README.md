# **Hyperliquid TWAP Monitoring Bot**

## **Project Description**

The **Hyperliquid TWAP Monitoring Bot** is an automated solution designed to monitor and analyze Time-Weighted Average Price (TWAP) orders on the Hyperliquid exchange. This bot fetches market data, calculates significant TWAP values, and sends notifications to a specified Telegram channel, ensuring that users stay informed about critical market movements.

## **Features**

- **Automated TWAP Monitoring**: The bot continuously checks for new TWAP orders across multiple tokens, ensuring real-time updates.
- **Market Data Integration**: Integrates with the Hyperliquid API to fetch real-time market data, including token prices and circulating supply.
- **Condition-Based Alerts**: Utilizes user-defined conditions to filter significant TWAP orders based on market capitalization and order size.
- **Telegram Notifications**: Sends detailed notifications to a Telegram channel, summarizing TWAP orders and their impact on the market.
- **Robust Error Handling**: Implements comprehensive error handling to manage API requests and data parsing efficiently.

## **Technical Details**

- **Programming Language**: Python
- **APIs Used**: Hyperliquid API for market data and TWAP orders, Telegram Bot API for notifications
- **Environment Variables**: Securely stores API tokens and chat IDs using environment variables to prevent sensitive data exposure.

## **Installation**

```sh
# Clone the repository
git clone git@github.com:CarlosB14/Hyperliquid-TWAP.git

# Navigate to the project directory
cd Hyperliquid-TWAP

# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

# Install the required dependencies
pip install -r requirements.txt

# Create a .env file in the root directory and add your environment variables
TELEGRAM_BOT_TOKEN=your_telegram_bot_token
TELEGRAM_CHAT_ID=your_telegram_chat_id

# Run the main script to start monitoring
python main.py

# The bot will periodically check for new TWAP orders and send notifications to the specified Telegram channel.

Contributions
Contributions are welcome! Please fork the repository and submit a pull request with your improvements.

License
This project is licensed under the MIT License. See the LICENSE file for more details.

Contact
For any inquiries or issues, please contact Carlos at [carlos.beltra.lopez@gmail.com].
