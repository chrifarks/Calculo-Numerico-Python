import os


def generate_report(env, voltage_ts, filename):
    filepath = "../reports/" + filename
    create_folder_structure(filepath)

    file = open(filepath, 'w')
    create_file_header(voltage_ts, file, env)
    create_file_body(voltage_ts, file, env)
    file.close()


def create_folder_structure(filepath):
    dirname = os.path.dirname(filepath)
    if not os.path.exists(dirname):
        os.makedirs(dirname)


def create_file_header(voltage_ts, file, env):
    file.write('# Time (ms)')
    for col in range(0, len(voltage_ts[0])):
        file.write(";Voltage(")
        file.write(str(env.space_step * col))
        file.write(", T)")
    file.write("\n")


def create_file_body(voltage_ts, file, env):
    for line in range(0, len(voltage_ts)):
        file.write('{:02f}'.format(env.time_step * line))
        for col in range(0, len(voltage_ts[0])):
            file.write(";")
            file.write(str(voltage_ts[line][col]))
        file.write("\n")
