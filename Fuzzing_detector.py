import datetime


def Fuzzing_detector():
    while (True):
        month = datetime.datetime.now().strftime("%B")
        day = datetime.datetime.now().day
        detector_counter = 0
        errors = ["Bad protocol version", "kex_exchange_identification", "kex_input_kexinit", "Connection closed by"]
        log_file = open("/var/log/auth.log", "r")
        for line in log_file:
            line_list = str(line).split(" ")
            if line_list[0] == month and line_list[1] == day:
                for error in errors:
                    if error in line:
                        detector_counter += 1
                        print(line)

        if detector_counter >= 4:
            print("Fuzzing detect!!!")


if __name__ == "__main__":
    Fuzzing_detector()
