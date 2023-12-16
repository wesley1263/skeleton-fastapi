from uvicorn import run

from src.config.settings import get_settings

setting = get_settings()

if __name__ == "__main__":
    run(
        "src.main:src",
        host="0.0.0.0",
        port=setting.APP_PORT,
        log_level="debug",
        workers=4,
        use_colors=True,
    )
