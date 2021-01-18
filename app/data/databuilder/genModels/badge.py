import app.data.databuilder.utils.generator as gen


class GenBadge:
    def __init__(self):
        self.Image = gen.get_random_image_data()
        self.Name = gen.get_random_word()
        self.Description = gen.get_random_text(
            max_chars=gen.get_random_number(5, 255)
        )


if __name__ == '__main__':
    gen_badge = GenBadge()
    print(gen_badge.__dict__)
