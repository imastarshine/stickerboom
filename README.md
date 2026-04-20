# stickerboom

Telegram bot-based tool to download sticker packs by names listed in a file.

## Setup

### Using Poetry (recommended)

```bash
poetry install
```

### Manual setup

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
# or
venv\Scripts\activate    # Windows

pip install -r requirements.txt
```

> **Note**: Create `requirements.txt` from `pyproject.toml` if needed:
> ```bash
> poetry export -f requirements.txt --output requirements.txt
> ```

## Configuration

Create `.env` file with your bot token:

```env
BOT_TOKEN=your_telegram_bot_token_here
# Optional: SOCKS5 proxy
SOCKS5_PROXY_URL=socks5://user:pass@host:port
```

## Usage

1. Create `stickers_list.txt` with sticker pack names, one per line:
   ```
tea_stickers
cool_stickers_pack
```

2. Run the script:
   ```bash
python main.py
```

3. Outputs:
   - `downloads/` - downloaded sticker files
   - `metadata.jsonl` - metadata for each downloaded pack (one JSON per line)
   - `downloaded.txt` - list of successfully downloaded pack names

The script skips packs already listed in `downloaded.txt`.
