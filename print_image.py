import win32print
import win32ui
from PIL import Image, ImageWin
import argparse

def get_printer_dc(printer_name):
    hprinter = win32print.OpenPrinter(printer_name)
    pdc = win32ui.CreateDC()
    pdc.CreatePrinterDC(printer_name)
    return pdc, hprinter

def resize_image(image_path, width, height):
    image = Image.open(image_path)
    return image.resize((width, height))

def print_image(image, pdc, width, height):
    dib = ImageWin.Dib(image)
    dib.draw(pdc.GetHandleOutput(), (0, 0, width, height))

def main(image_path):
    # Get the default printer
    printer_name = win32print.GetDefaultPrinter()

    # Create printer DC and get handle
    pdc, hprinter = get_printer_dc(printer_name)

    # Start document
    pdc.StartDoc('Image Print')
    pdc.StartPage()

    # Get paper size directly from printer
    width = pdc.GetDeviceCaps(110)  # HORZRES
    height = pdc.GetDeviceCaps(111)  # VERTRES

    # Resize and print image
    image = resize_image(image_path, width, height)
    print_image(image, pdc, width, height)

    # End the printing job
    pdc.EndPage()
    pdc.EndDoc()
    pdc.DeleteDC()

    # Close printer handle
    win32print.ClosePrinter(hprinter)

    print("Print job sent to printer.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Print an image using the default printer.")
    parser.add_argument('-f', '--file', required=True, help="Path to the image file.")
    args = parser.parse_args()

    main(args.file)
