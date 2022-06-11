from datetime import time
import socket, ssl
import schedule
import time
from win10toast import ToastNotifier

def send_file():
    host = '146.120.83.122'
    context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
    context.load_verify_locations('cert.pem')
    filepath = 'X:\\Технический Департамент\\Группа эксплуатации\\УЗЛЫ СЕВЕРЕНА\\БАЗА УЗЛОВ.xlsx'
    toaster = ToastNotifier()

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0) as sock:
        with context.wrap_socket(sock, server_hostname=host) as ssock:
            try:
                print('Trying connecting...')
                ssock.connect((host, 10023))
                print('Is connect')
                toaster.show_toast('Подключился к серверу!', 'Начинаю отправку файла. ')
                try:
                    with open(filepath, 'rb') as f:
                        print('Sending file...')
                        ssock.sendfile(f)
                        ssock.close()
                        print('Send complete')
                        toaster.show_toast('Обновление', 'Передача файла завершена ')
                except Exception:
                    print('File not found!')
                    toaster.show_toast('Ошибка', 'Передача не может быть выполнена, \
                    т.к. файл отсутсвует или неверный путь к файлу.')
                    ssock.close()
                    time.sleep(120)
                    send_file()
            except Exception as e:
                print(f'Not connect {e}')

if __name__ == '__main__':
    print('Запущен')
    schedule.every().day.at('18:00').do(send_file)
    while True:
        schedule.run_pending()
        time.sleep(1)