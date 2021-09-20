class Main:
    def index_of(self, text, _str):
        compare_test_len = len(_str)
        if len(text) < compare_test_len:  # text too small compared to comparison string
            return -1
        else:
            if text[:compare_test_len] == _str:
                return 0
            else:
                return self.index_of(text[1:compare_test_len], _str)

    def index_of_helper(self, text, _str, index=0):
        compare_test_len = len(_str)
        return self.index_of_helper(text[1:1 + compare_test_len], _str, 1)

    def square_root_guess(self, x, g):
        return