# Coinmarketcap To Notion
This project retrieves cryptocurrency data from the CoinMarketCap API and stores it in a Notion database. It allows users to keep track of cryptocurrency prices and other relevant information directly in their Notion workspace.

> - Fetch real-time cryptocurrency data from CoinMarketCap.
> - Store and update data in a Notion database.
> - Easy to set up and run with Python.

## How To Installing And Run Project?
1. ### Obtain CoinMarketCap API Key
   1. Go to the [CoinMarketCap API](https://coinmarketcap.com/api/) website.
   2. Sign up for an account if you don't have one.
   3. After logging in, navigate to the API section and create a new API key.
   4. Copy your API key for later use.
  
2. ### Create a Notion Integration
   1. Go to [Notion Developers](https://www.notion.so/my-integrations).
   2. Click on "New Integration".
   3. Fill in the required details (name, associated workspace, etc.).
   4. Once created, you will receive an Integration Token. Copy this token for later use.

3. ### Share Your Database with the Integration
   1. Open the Notion page that contains the database you want to integrate.
   2. Click on the "Share" button in the top right corner.
   3. In the "Invite" section, search for your integration by name and select it.
   4. Make sure to give it the necessary permissions (e.g., read, write).
4. ### Clone the Repository
  Clone the repository to your local machine:
  ```bash
git clone https://github.com/yuzaiakira/coinmarketcap-to-notion.git
cd ./coinmarketcap-to-notion/
  ```
   
6. ### Set Up Your Environment
   1. Rename a `sample.env` file to `.env` file in the root of your project.
   2. Fill the following lines to the .env file:
      ```plaintext
I_TOKEN= Notion Integration Token
DATABASE_ID= Notion Database ID

COINMARKETCAP_KEY= CoinMarketCap API Key
      ```
6. ### Install the Required Libraries
You can install the required libraries using pip:
```bash
pip install -r ./requirements.txt
```
7. ### Running the Project
Run the script to fetch cryptocurrency data and store it in your Notion database:

```bash
python main.py
```

I hope you enjoy using this project :)
