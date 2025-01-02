import json

def write_json(data, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

def read_json(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)

def main():
    filename = 'pokemones.json'

    while True:
        try:
            read_data = read_json(filename)
            print('Data read from file:')
            print(read_data)

            new_pokemon={
                "name": {
                    "english": input("Ingrese el nombre en ingles del pokemon: "),
                    },
                "type": [
                    input("Ingrese el tipo del pokemon: ")
                    ],
                "base": {
                    "HP": int(input("Ingrese el HP del pokemon: ")),
                    "Attack": int(input("Ingrese el ataque del pokemon: ")),
                    "Defense": int(input("Ingrese la defensa del pokemon: ")),
                    "Sp. Attack": int(input("Ingrese el ataque especial del pokemon: ")),
                    "Sp. Defense": int(input("Ingrese la defensa especial del pokemon: ")),
                    "Speed": int(input("Ingrese la velocidad del pokemon: "))
                    }
            }

            read_data.append(new_pokemon)
            write_json(read_data, filename)
            print(f'Data written to {filename}')

            break

        except FileNotFoundError:
            print('File not found, creating a new file...')
            data = []       
            write_json(data, filename)

        except ValueError:
            print('Invalid value, try again')

        except:
            print('An error occurred')


if __name__ == '__main__':
    main()