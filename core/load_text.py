import csv


def load_texts_from_csv():
    texts = []
    with open("text_image_mapping.csv", mode="r") as file:
        reader = csv.reader(file)
        for row in reader:
            texts.append(row[0])
    return texts
