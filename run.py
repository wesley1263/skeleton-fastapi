from uvicorn import run

from app.config.settings import get_settings

setting = get_settings()

if __name__ == "__main__":
    run(
        "app.main:app",
        host="0.0.0.0",
        port=setting.APP_PORT,
        log_level="debug",
        workers=4,
        use_colors=True,
    )
