Def train_one(save_path, config, log_file_dir, index, logfile_level, console_level, device):
    “””
    Train an agent
    :param save_path: the path to save the tensorflow model (.ckpt) , could be None
    :param config: the Jain configuration file
    :param log_file_dir: the directory to save the tensorboard logging file, could be a one
    :param index: identifier of this train, which is also the sub directory in the train_package, If it is 0. Nothing would be saved into the summary file.
    :param logfile_level: logging level of the file
    :param console_level: logging level of the console :param device 0 or 1 to show which gpu to use, if 0 means use cpu instead, of gpu
    :return : the Result namedtuple
    “””
    if log_file_dir:
        Logging.basicConfig(filename=log_file_dir.replace(“tensorboard” , “programlog”),
                            Level=logfile_level)
        Console = logging.StreamHandler()
        Console = setLevel(console_level)
        Logging.getLogger().addHandler(console)
