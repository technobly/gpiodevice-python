def get_name():
    try:
        model = open("/proc/device-tree/model", "r").read()
        if model.startswith("Particle Tachyon"):
            return model
    except IOError:
        pass

    return None


def get_gpiochip_labels():
    if get_name() is not None:
        return (
            "f000000.pinctrl",
            # Should match /dev/gpiochip0 (f000000.pinctrl)
        )

    return None
