from key import bind

def map_gesture(text):
    if len(text) == 0:
        main()
    elif "play" in text.lower():
        print('plaaying')
        bind('play')
    elif "pause" in text.lower():
        print('pausing')
        bind('pause')
    elif "increase" in text.lower():
        print('increase')
        bind('increase')
    elif "present" in text.lower():
        print('present')
        bind('present')
    elif "next" in text.lower():
        print('next')
        bind('next')
    elif "previous" in text.lower():
        print('previous')
        bind('previous')
    elif "escape" in text.lower():
        print('escape')
        bind('escape')
    elif "windows" in text.lower():
        print('windows')
        bind('windows')
    # elif "powerpoint" in text.lower():
    #     print('powerpoint')
    #     bind('powerpoint')
    #     main()
    elif "ok" in text.lower():
        print('ok')
        bind('ok')
    elif "down" in text.lower():
        print('down')
        bind('down')
    elif "close" in text.lower():
        print('close')
        # bind('close')
    print('blah')
