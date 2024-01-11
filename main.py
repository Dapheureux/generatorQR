# main.py
from PIL import Image

def select_error_correction_level(level):
    error_correction_level = {
        'L':0, 'M':1, 'Q':2, 'H':3
    }
    return error_correction_level.get(level, 1)
def select_smallest_version(error_correction_level, mode):
    versions = {
        'L': {'numeric': 1, 'alphanumeric': 1, 'byte': 1, 'kanji': 1},
        'M': {'numeric': 1, 'alphanumeric': 1, 'byte': 1, 'kanji': 1},
        'Q': {'numeric': 1, 'alphanumeric': 1, 'byte': 1, 'kanji': 1},
        'H': {'numeric': 1, 'alphanumeric': 1, 'byte': 1, 'kanji': 1}
    }
    # Vérifiez si le mode est présent dans le dictionnaire, sinon utilisez la valeur par défaut
    return versions[error_correction_level].get(mode, 1)


def determine_encoding_mode(data):
    if any(char.isdigit() for char in data):
        return 'numeric'
    elif any(char.isalpha() for char in data):
        return 'alphanumeric'
    elif any(char.encode('utf-8') for char in data):
        return 'byte'
    elif any(ord(char) > 127 for char in data):
        return 'kanji'
    else:
        raise ValueError("Impossible de déterminer le mode pour les données fournies.")



def determine_indicator_char_count(version, mode):
    char_count_indicators = {
        1: {'numeric': '0000', 'alphanumeric': '0000', 'byte': '0000', 'kanji': '0000'},
        9: {'numeric': '0010', 'alphanumeric': '0001', 'byte': '0000', 'kanji': '0000'}
        
    }
    return char_count_indicators[version].get(mode, '0000')


def calculate_error_correction_blocks(version, error_correction_level):
    error_correction_info = {
        'L': {1: (1, 20), 2: (1, 18), },  # Ajoutez les informations pour toutes les versions nécessaires
        'M': {1: (2, 18), 2: (2, 16), },
        'Q': {1: (2, 26), 2: (2, 24), },
        'H': {1: (4, 16), 2: (4, 12), }
    }
    return error_correction_info[error_correction_level].get(version, (0, 0))
def calculate_error_correction_words(blocks, version, error_correction_level):
    # Implémentez la logique de calcul des mots de code de correction d'erreur pour chaque bloc
    # en utilisant l'algorithme de correction d'erreur de Reed-Solomon
    pass
def implement_error_correction(encoded_data, version, error_correction_level):
    # Obtenez le nombre de blocs et de mots de code de correction d'erreur
    blocks, words_per_block = calculate_error_correction_blocks(version, error_correction_level)

    # Divisez les données encodées en blocs
    data_blocks = [encoded_data[i:i + words_per_block] for i in range(0, len(encoded_data), words_per_block)]

    # Calculez et ajoutez les mots de code de correction d'erreur pour chaque bloc
    corrected_data = ""
    for block in data_blocks:
        corrected_data += calculate_error_correction_words(block, version, error_correction_level)

    return corrected_data

def encode_data(data, mode, version, error_correction_level):
    error_correction_level = select_error_correction_level(error_correction_level)
    version = select_smallest_version(error_correction_level, mode)
    indicator_mode = determine_indicator_mode(mode)
    indicator_char_count = determine_indicator_char_count(version, mode)

    encoded_data = ""
    if mode == 'numeric':
        encoded_data += encode_numeric(data, version)
    elif mode == 'alphanumeric':
        encoded_data += encode_alphanumeric(data, version)
    elif mode == 'byte':
        encoded_data += encode_byte(data, version)
    elif mode == 'kanji':
        encoded_data += encode_kanji(data, version)

    capacity = calculate_capacity(version, error_correction_level)
    encoded_data += '0000'
    while len(encoded_data) < capacity:
        encoded_data += '0'
    encoded_data = encoded_data[:capacity]
    
    corrected_data = implement_error_correction(encoded_data, version, error_correction_level)
    
    return encoded_data

def encode_qr_data(matrix, encoded_data, version, error_correction_level):
    # Placez les bits d'indicateur de mode dans la matrice QR
    indicator_mode = determine_indicator_mode(mode)
    indicator_char_count = determine_indicator_char_count(version, mode)
    indicator_bits = indicator_mode + indicator_char_count
    place_indicator_bits(matrix, indicator_bits)

    # Placez les bits de données encodées dans la matrice QR
    data_bits = convert_data_to_bits(encoded_data)
    place_data_bits(matrix, data_bits)

    # Placez les bits de correction d'erreur dans la matrice QR
    place_error_correction_bits(matrix, version, error_correction_level)

def place_indicator_bits(matrix, indicator_bits):
    # Implémentez le placement des bits d'indicateur de mode dans la matrice QR
    pass

def convert_data_to_bits(encoded_data):
    # Implémentez la conversion des données encodées en bits
    bits = ''
    for char in encoded_data:
        bits += format(ord(char), '08b')  # Convertir en binaire sur 8 bits

    return bits

def place_data_bits(matrix, data_bits):
    # Implémentez le placement des bits de données dans la matrice QR
    pass

def place_error_correction_bits(matrix, version, error_correction_level):
    # Implémentez le placement des bits de correction d'erreur dans la matrice QR
    pass

# Creation de l'image du code QR
def create_qr_matrix(version):
    matrix_size = get_matrix_size(version)
    return [[0] * matrix_size for _ in range(matrix_size)]

def create_qr_matrix_size(version):
    return 21 + 4 * (version - 1)

def place_finder_pattern(matrix):
    pass

def place_separators(matrix):
     pass
def place_alignment_pattern(matrix):
    # Cette fonction place le motif d'alignement dans la matrice du code QR
    pass

def place_timing_pattern(matrix):
    # Cette fonction place le modèle de synchronisation dans la matrice du code QR
    pass

def place_dark_module(matrix):
    # Cette fonction place le module sombre dans la matrice du code QR
    pass

def reserve_format_and_version_info(matrix):
    # Cette fonction réserve les zones d'informations sur le format et la version dans la matrice du code QR
    pass    

# Application des masques de données
def apply_data_mask(matrix, mask_type):
    size = len(matrix)
    for i in range(size):
        for j in range(size):
            if is_data_position(i, j, size) and apply_mask_condition(i, j, mask_type):
                matrix[i][j] = not matrix[i][j]
    return matrix
def is_data_position(row, col, size):
    # Vérifie si la position (row, col) est une position de données dans la matrice QR
    return 0 <= row < size and 0 <= col < size

def apply_mask_condition(row, col, mask_type):
    # Applique la condition de masque spécifique en fonction du type de masque
    if mask_type == 0:
        return (row + col) % 2 == 0
    elif mask_type == 1:
        return row % 2 == 0
    elif mask_type == 2:
        return col % 3 == 0
    elif mask_type == 3:
        return (row + col) % 3 == 0
    elif mask_type == 4:
        return (row // 2 + col // 3) % 2 == 0
    elif mask_type == 5:
        return (row * col) % 2 + (row * col) % 3 == 0
    elif mask_type == 6:
        return ((row * col) % 2 + (row * col) % 3) % 2 == 0
    elif mask_type == 7:
        return ((row + col) % 2 + (row * col) % 3) % 2 == 0

def choose_best_mask(matrix):
    best_mask=0
    best_penalty=float('inf')
    
    for mask_type in range(8):
        mask_matrix = apply_data_mask(matrix, mask_type)
        penalty =evalute_mask(mask_matrix)
        if penalty<best_penalty:
            best_penalty=penalty
            best_mask=mask_type
    return best_mask

def evalute_mask(matrix):
    size = len(matrix)
    penalty = 0
    penalty += count_consecutive_modules(matrix)
    penalty += count_identical_2x2(matrix)
    return penalty
    # compter le nombre de modules consécutifs identiques
def count_consecutive_modules(matrix):
    count = 0
    max_count = 0

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == matrix[i][j - 1]:
                count += 1
            else:
                if count > max_count:
                    max_count = count
                count = 1

    return max_count
def count_identical_2x2(matrix):
    count = 0

    for i in range(len(matrix) - 1):
        for j in range(len(matrix[i]) - 1):
            if matrix[i][j] == matrix[i + 1][j] == matrix[i][j + 1] == matrix[i + 1][j + 1]:
                count += 1

    return count
def encode_format_and_version_info(matrix, version, error_correction_level):
    # Encodage des informations de format
    format_info_bits = generate_format_info(version, error_correction_level)
    place_format_info(matrix, format_info_bits)

    # Encodage des informations de version pour les versions 7 et supérieures
    if version >= 7:
        version_info_bits = generate_version_info(version)
        place_version_info(matrix, version_info_bits)

def generate_format_info(version, error_correction_level):
    # Implémentez la génération des bits d'information de format
     format_info = f'{version:03b}{error_correction_level:02b}'
     return format_info

def place_format_info(matrix, format_info_bits):
    # Implémentez le placement des bits d'information de format dans la matrice QR
    pass

def generate_version_info(version):
    # Implémentez la génération des bits d'information de version
   version_info = format(version, '06b')
   return version_info

def place_version_info(matrix, version_info_bits):
    # Implémentez le placement des bits d'information de version dans la matrice QR
    pass
def display_qr_code(matrix):
    # Créez une image à partir de la matrice QR
    image = create_qr_image(matrix)

    # Affichez l'image
    image.show()

def save_qr_code(matrix, filename):
    # Créez une image à partir de la matrice QR
    image = create_qr_image(matrix)

    # Sauvegardez l'image
    image.save(filename)

def create_qr_image(matrix):
    # Créez une image PIL à partir de la matrice QR
    image = Image.new('1', (len(matrix[0]), len(matrix)), 1)  # 1-bit pixels, default to white
    pixels = image.load()

    for y in range(len(matrix)):
        for x in range(len(matrix[0])):
            pixels[x, y] = matrix[y][x]

    return image

def determine_indicator_mode(mode):
    indicator_modes = {
        'numeric': '0001',
        'alphanumeric': '0010',
        'byte': '0100',
        'kanji': '1000',
    }
    return indicator_modes.get(mode, '0000')


def main():
    data = "ALLO C'EST DAPH N'ZITA"
    mode = determine_encoding_mode(data)
    error_correction_level = 'M'
    smallest_version = select_smallest_version(error_correction_level, mode)
    
    indicator_mode = determine_indicator_mode(mode)
    indicator_char_count = determine_indicator_char_count(smallest_version, mode)
    
    encoded_data, mode = encode_data(data, mode, smallest_version, error_correction_level)



    matrix = create_qr_matrix(smallest_version)

    # Placez les motifs et les informations nécessaires dans la matrice QR
    place_finder_pattern(matrix)
    place_separators(matrix)
    place_alignment_pattern(matrix)
    place_timing_pattern(matrix)
    place_dark_module(matrix)
    reserve_format_and_version_info(matrix)

    # Placez les données encodées dans la matrice QR
    encode_qr_data(matrix, encoded_data)

    # Encodez les informations de format et de version
    encode_format_and_version_info(matrix, smallest_version, error_correction_level)

    # Affichez le code QR
    display_qr_code(matrix)

    # Sauvegardez le code QR
    save_qr_code(matrix, "qr_code.png")

if __name__ == "__main__":
    main()