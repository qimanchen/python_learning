class ManMadeError(Exception):
    def __init__(self,error_type):
        self.error_type = error_type

def trigger_manMade_error():
    num = 4

    if num == 4:
        try:
            raise ManMadeError("ManMadeError")
        except ManMadeError as error_info:
            print("error type is %s: " % error_info.error_type)

if __name__ == "__main__":
    trigger_manMade_error()
