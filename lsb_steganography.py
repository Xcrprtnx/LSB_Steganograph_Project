from PIL import Image
import numpy as np

def encode_image(image_path, secret_message, output_path):
    # Resmi yükle
    image = Image.open(image_path)
    encoded_image = image.copy()
    
    # Mesajı bit dizisine çevir
    binary_message = ''.join(format(ord(char), '08b') for char in secret_message)
    binary_message += '00000000'  # Mesajın sonunu belirtmek için

    data_index = 0
    for y in range(image.height):
        for x in range(image.width):
            pixel = list(encoded_image.getpixel((x, y)))
            for i in range(3):  # R, G, B kanalları
                if data_index < len(binary_message):
                    # Pikselin LSB'sini değiştir
                    pixel[i] = (pixel[i] & ~1) | int(binary_message[data_index])
                    data_index += 1
            encoded_image.putpixel((x, y), tuple(pixel))
            if data_index >= len(binary_message):
                break
        if data_index >= len(binary_message):
            break

    encoded_image.save(output_path)
    print("Mesaj başarıyla kodlandı ve resim kaydedildi.")

if __name__ == "__main__":
    image_path = input("Kodlamak istediğiniz resmin yolunu girin: ")
    secret_message = input("Gizli mesajınızı girin: ")
    output_path = input("Çıktı resminin yolunu girin: ")

    encode_image(image_path, secret_message, output_path)
