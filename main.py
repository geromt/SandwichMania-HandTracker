from app.tracker import HandTracker


def main():
    tracker = HandTracker()
    tracker.capture_and_send(display_video=False)


if __name__ == "__main__":
    main()
