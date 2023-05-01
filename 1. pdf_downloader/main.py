import PySimpleGUI as sg
import scraper

sg.theme("LightGray1")
url_label = sg.Text("Full URL address: ", size=[20, 1])
url_input = sg.Input(key='url')

dst_label = sg.Text("Select destination folder: ", size=[20, 1])
dst_output = sg.Input(key='folder')
dst_button = sg.FolderBrowse("Choose")

download_button = sg.Button("Download")
output_message = sg.Text(key='output', text_color="red", pad=[40, 0])

window = sg.Window("PDF Downloader", layout=[[url_label, url_input],
                                             [dst_label, dst_output, dst_button],
                                             [download_button, output_message]],
                   font=('Helvetica', 20))
while True:
    event, values = window.read()

    match event:
        case "Download":
            message = scraper.scraper(values['url'], values['folder'])
            window['output'].update(value=message)
        case sg.WIN_CLOSED:
            break

window.close()

