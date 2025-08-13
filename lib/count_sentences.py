#!/usr/bin/env python3
import re

class MyString:
    
    def __init__(self, value=""):
        self.value = value  # This will call the setter

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if isinstance(new_value, str):
            self._value = new_value
        else:
            print("The value must be a string.")

    def is_sentence(self):
        return self._value.endswith(".")

    def is_question(self):
        return self._value.endswith("?")

    def is_exclamation(self):
        return self._value.endswith("!")

    def count_sentences(self):
        # Match sequences ending with ., ?, or !
        sentences = re.split(r'[.!?]', self._value)
        # Remove empty strings and whitespace-only strings
        sentences = [s.strip() for s in sentences if s.strip()]
        return len(sentences)

