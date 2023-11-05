import dearpygui.dearpygui as dpg
import base64

dpg.create_context()


def encode_text(text, count):
    if not text:
        return None
    if not count:
        count = 1

    # Encode the text count times
    encoded_text = text.encode('utf-8')
    for _ in range(count):
        encoded_text = base64.b64encode(encoded_text)

    return encoded_text.decode('utf-8')


def decode_text(text, count):
    if not text:
        return None
    if not count:
        count = 1

    # Decode the text count times
    decoded_text = text.encode('utf-8')
    for _ in range(count):
        try:
            decoded_text = base64.b64decode(decoded_text)
        except base64.binascii.Error:
            print("Error: Unable to decode the text. The input may not be valid Base64.")
            return None

    return decoded_text.decode('utf-8')


with dpg.window(tag="Coder window"):
    def encode():
        text = dpg.get_value("text")
        count = int(dpg.get_value("count"))
        encoded_text = encode_text(text, count)
        dpg.set_value("output", encoded_text)

    def decode():
        text = dpg.get_value("text")
        count = int(dpg.get_value("count"))
        decoded_text = decode_text(text, count)
        dpg.set_value("output", decoded_text)

    dpg.add_input_text(label="Text", tag="text")
    with dpg.popup(dpg.last_item()):
        dpg.add_text("Text to process")
    dpg.add_input_text(label="Count", tag="count")
    with dpg.popup(dpg.last_item()):
        dpg.add_text("Number of times to process")

    dpg.add_input_text(label="Output", tag="output", readonly=True, multiline=True)
    dpg.add_button(label="Encode", callback=encode, width=100)
    dpg.add_button(label="Decode", callback=decode, width=100)

dpg.create_viewport(title='Advanced Base64 UTF-8 encoder/decoder by Bt08s', width=500, height=300)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("Coder window", True)
dpg.start_dearpygui()
dpg.destroy_context()
