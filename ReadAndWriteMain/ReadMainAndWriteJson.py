import hcl2
import json

def load_tf_file(filename):
    """ Read file .tf and write json. """
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            data = hcl2.load(f)
            return data
    except FileNotFoundError:
        print(f"The file {filename} not found.")
        return None
    except Exception as e:
        print(f"Error reading file {filename}: {e}")
        return None

def save_to_json(data, output_file):
    """ Save a dictionary to a JSON file. """
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        print(f"File JSON saved in '{output_file}'.")
    except Exception as e:
        print(f"Error writing to JSON file: {e}")

if __name__ == "__main__":
    # Especifica la ruta al archivo main.tf y el archivo de salida JSON
    tf_file_path = 'main.tf'  # Cambia esto a la ruta de tu archivo main.tf
    output_json_file = 'main.json'  # Nombre del archivo JSON de salida

    # Cargar el archivo main.tf
    tf_data = load_tf_file(tf_file_path)

    if tf_data is not None:
        # Guardar los datos en JSON
        save_to_json(tf_data, output_json_file)
