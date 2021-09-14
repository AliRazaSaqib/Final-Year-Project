import check.image_object
from pathlib import Path


def detect(input_path, output_path, block_size):
    input_path = Path(input_path)
    filename = input_path.name
    output_path_string = output_path.replace("//", "")
    output_length = len(output_path_string)
    output_path = Path(output_path)

    if not input_path.exists():
        print("Error: Source Directory did not exist.")
        exit(1)
    elif not output_path.exists():
        print("Error: Output Directory did not exist.")
        exit(1)

    single_image = check.image_object.ImageObject(input_path, filename, output_path, block_size)
    image_result_path = single_image.run()
    result_path = str(image_result_path)
    result_path_string = result_path.replace("\\", "")
    image_path = result_path_string[output_length:]
    store_msg= "Done Process completed"
    print(store_msg)
    return image_path
