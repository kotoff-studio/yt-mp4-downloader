import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QFileDialog
from pytube import YouTube

class YoutubeDownloaderApp(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('YouTube Video Downloader')
        self.setGeometry(100, 100, 400, 200)

        layout = QVBoxLayout()

        self.url_label = QLabel('Enter YouTube URL:')
        self.url_input = QLineEdit()
        self.download_button = QPushButton('Download Video')
        self.download_button.clicked.connect(self.download_video)

        layout.addWidget(self.url_label)
        layout.addWidget(self.url_input)
        layout.addWidget(self.download_button)

        self.setLayout(layout)

    def download_video(self):
        url = self.url_input.text()
        if url:
            try:
                yt = YouTube(url)
                video = yt.streams.filter(file_extension='mp4', progressive=True).first()

                save_path, _ = QFileDialog.getSaveFileName(self, "Save Video", f"{yt.title}.mp4", "Video Files (*.mp4);;All Files (*)")

                if save_path:
                    video.download(save_path)
                    QMessageBox.information(self, 'Success', 'Video downloaded successfully!')
                else:
                    QMessageBox.warning(self, 'Error', 'Invalid file path.')

            except Exception as e:
                QMessageBox.warning(self, 'Error', f'An error occurred: {str(e)}')
        else:
            QMessageBox.warning(self, 'Error', 'Please enter a valid YouTube URL.')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = YoutubeDownloaderApp()
    window.show()
    sys.exit(app.exec_())