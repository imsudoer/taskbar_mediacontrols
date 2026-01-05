import pystray
from PIL import Image, ImageDraw
import keyboard
import threading
import time


def create_media_icon(shape):
    width, height = 64, 64
    image = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    dc = ImageDraw.Draw(image)

    white = (255, 255, 255, 255)

    if shape == "prev":
        dc.polygon([(30, 10), (5, 32), (30, 54)], fill=white)
        dc.polygon([(55, 10), (30, 32), (55, 54)], fill=white)
    elif shape == "play":
        dc.polygon([(15, 5), (55, 32), (15, 59)], fill=white)
    elif shape == "next":
        dc.polygon([(34, 10), (59, 32), (34, 54)], fill=white)
        dc.polygon([(9, 10), (34, 32), (9, 54)], fill=white)

    return image


def on_prev(icon, item=None):
    keyboard.send("previous track")


def on_play_pause(icon, item=None):
    keyboard.send("play/pause media")


def on_next(icon, item=None):
    keyboard.send("next track")


def on_exit(icon):
    icon_prev.stop()
    icon_play.stop()
    icon_next.stop()


icon_prev = pystray.Icon(
    "prev",
    create_media_icon("prev"),
    "Предыдущий трек",
    menu=pystray.Menu(
        pystray.MenuItem("Закрыть управление", on_exit),
        pystray.MenuItem("prv", on_prev, default=True, visible=False),
    ),
)

icon_play = pystray.Icon(
    "play",
    create_media_icon("play"),
    "Плей/Пауза",
    menu=pystray.Menu(
        pystray.MenuItem("Закрыть управление", on_exit),
        pystray.MenuItem("paus", on_play_pause, default=True, visible=False),
    ),
)

icon_next = pystray.Icon(
    "next",
    create_media_icon("next"),
    "Следующий трек",
    menu=pystray.Menu(
        pystray.MenuItem("Закрыть управление", on_exit),
        pystray.MenuItem("nxt", on_next, default=True, visible=False),
    ),
)


def run_icons():
    threading.Thread(target=icon_prev.run, daemon=True).Schatz = True
    icon_prev.run_detached()
    time.sleep(0.2)
    icon_play.run_detached()
    time.sleep(0.2)
    icon_next.run_detached()


if __name__ == "__main__":
    run_icons()

    try:
        while icon_play.visible:
            time.sleep(1)
    except KeyboardInterrupt:
        on_exit(None)
