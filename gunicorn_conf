import multiprocessing

workers = multiprocessing.cpu_count() * 2 + 1

CONFIG = {
    'working_dir': '/home/nastya/ask_dyudina/ask_dyudina',
    # 'python': '/usr/bin/python',
    'args': (
        '--bind=127.0.0.1:8000',
        '--workers=' + str(workers),
        '--timeout=60',
        'wsgi:app',
    ),
}
