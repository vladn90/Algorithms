""" Problem statement:
https://leetcode.com/problems/text-justification/description/
"""


class Solution:
    def full_justify(self, words, width):
        """ Time complexity: O(n). Space complexity: O(n), n is len(words).
        """
        n = len(words)
        i = 0
        result = []
        while i < n:
            line = []
            char_count = 0
            # while we haven't reached the end of the words list
            # and total number of characters + spaces <= width
            while i < n and char_count + (len(line)) + len(words[i]) <= width:
                line.append(words[i])  # append word to current line
                char_count += len(words[i])  # increase current character count
                i += 1  # move to the next word

            if len(line) > 1:  # line has more than one word
                # length of each space between words in line
                space = (width - char_count) // (len(line) - 1)
                # space remainder to spread between words starting from the left
                space_rem = (width - char_count) % (len(line) - 1)
            else:  # line has got only one word, no spaces needed
                space = 0
                space_rem = 0

            # assemble current line array into a single string
            if i == n:  # last line
                line_string = " ".join(line)
            else:  # any other line
                line_string = [line[0]]
                for j in range(1, len(line)):
                    if space_rem:
                        line_string.append(" " * (space + 1))
                        space_rem -= 1
                    else:
                        line_string.append(" " * space)
                    line_string.append(line[j])
                line_string = "".join(line_string)
            # add space to the end if needed
            line_string += (" " * (width - len(line_string)))

            # add assembled string to the result
            result.append(line_string)
        return result

    def full_justify_fast(self, words, width):
        """ Optimized version of the algorithm from above.
        Time complexity: O(n). Space complexity: O(n), n is len(words).
        """
        n = len(words)
        i = 0
        result = []
        while i < n:
            line = []
            char_count = 0
            # while we haven't reached the end of the words list
            # and total number of characters + spaces <= width
            line_app = line.append  # optimization
            while i < n and char_count + (len(line)) + len(words[i]) <= width:
                line_app(words[i])  # append word to current line
                char_count += len(words[i])  # increase current character count
                i += 1  # move to the next word

            if len(line) > 1:  # line has more than one word
                # length of each space between words in line
                space = (width - char_count) // (len(line) - 1)
                # space remainder to spread between words starting from the left
                space_rem = (width - char_count) % (len(line) - 1)
            else:  # line has got only one word, no spaces needed
                space = 0
                space_rem = 0

            # assemble current line array into a single string
            if i == n:  # last line
                line = " ".join(line)
            else:  # any other line
                # spread remainder spaces between words, starting from the left
                j = 0
                while space_rem:
                    line[j] += " "
                    j += 1
                    space_rem -= 1
                line = (" " * space).join(line)
            # add space to the end if needed
            if len(line) < width:
                line += (" " * (width - len(line)))
            # add assembled string to the result
            result.append(line)
        return result


if __name__ == "__main__":
    sol = Solution()
    func = sol.full_justify_fast

    words = ["This", "is", "an", "example", "of", "text", "justification."]
    width = 16
    assert func(words, width) == [
        'This    is    an', 'example  of text', 'justification.  ']

    words = ["aa", "bb", "cc", "d"]
    width = 3
    assert func(words, width) == ['aa ', 'bb ', 'cc ', 'd  ']

    words = ["aa", "bb", "cc", "d"]
    width = 2
    assert func(words, width) == ['aa', 'bb', 'cc', 'd ']

    words = ["one", "two", "three"]
    width = 20
    assert func(words, width) == ['one two three       ']
