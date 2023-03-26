import os


class FuncAttributes():
    name = 0
    module = 1
    line = 2
    error = 3


code_to_value = [lambda error:
                 error.__traceback__.tb_next.tb_frame.f_code.co_name,
                 lambda error:
                 os.path.basename(error.__traceback__.tb_next.tb_frame.f_code.co_filename).split(".")[0],
                 lambda error:
                 error.__traceback__.tb_next.tb_lineno,
                 lambda error:
                 error]
