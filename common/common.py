import signal

def signal_handler():
    import warnings
    warnings.filterwarnings("ignore", category=DeprecationWarning)

    def receive_signal(signum, stack):
        exit(-1)
    signal.signal(signal.SIGQUIT, receive_signal)
    signal.signal(signal.SIGINT, receive_signal)
    signal.signal(signal.SIGTERM, receive_signal)
    signal.signal(signal.SIGABRT, receive_signal)
    signal.signal(signal.SIGSEGV, receive_signal)