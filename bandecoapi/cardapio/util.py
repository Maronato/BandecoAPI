def format_string(text):
    def remove_excess_spaces(text):
        return ' '.join(text.strip().split()).strip()

    def capitalize_after_period(text):
        return '. '.join([word.strip().capitalize() for word in text.split('.')]).strip()

    def capitalize_after_two(text):
        return ': '.join([(word.strip()[0].capitalize() + word.strip()[1:]) if len(word) > 1 else '' for word in text.split(':')]).strip()

    return [remove_excess_spaces(capitalize_after_two(remove_excess_spaces(capitalize_after_period(remove_excess_spaces(line.text))))) for line in text]
